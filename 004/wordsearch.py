#!/usr/bin/env python

"""
Wordsearch - find a list of words in a 2-d grid of letters

http://rubyquiz.com/quiz107.html

Goals:
  - Use Objects
  - Try to practice The Python Way
  - Don't write in C style, use python to simplify/reduce code
    - If possible, make equivalent things work in a Python manner
  - Try not to be terribly inefficient with cpu and memory
  - Don't let those Ruby guys show you up! :)
  
"""


    # Extra credit from question:
    # * An output format superior to the one given. The output format given
    #   should remain the default unless both formats don't differ on a
    #   textual basis. That should sound cryptic until pondered, I can't
    #   give too much away!
    # - I have no idea what this means. The unless clause is a double-negative.
    #
    # * An option to give a hint, i.e., "The word ruby traverses the bottom
    #   left and bottom right quadrants."
    # - Not too hard. Should we hint for each word? Pick one solution at random?
    #   Perhaps the hint option takes an optional number, N, then picks N hints
    #   at random?
    #
    # * Decide what to do with accented letters.
    # - Don't care. I guess he's implying that we might map them all to the
    #   unaccented versions before comparison. Easy enough to do. This could
    #   be solved with a custom comparison function for cells. Just swap out the
    #   function for the character set.


    # TODO: Add doc strings
    # TODO: command-line options
    # TODO: We could save an upper() version of table if we can't trust the case of the
    #       table to be upper. We should probably just use a custom compare function
    #       since that'll be required for the accented characters (collapsing a subset
    #       into a single match)
    # TODO: What if one word is a subset of another, e.g. RUB and RUBY?
    #       - Probably should reject that word list for redundancy
    # TODO: much better input testing and exception handling on bad input
    # TODO: simplify direction methods to a single method using dx,dy
            #     import itertools
            #     _allDirections = set(itertools.product([-1, 0, 1], repeat=2))
            #     _allDirections.remove((0,0))
    # TODO: switch to a linear array containing newlines when converting the dx,dy code
    #       I used a table (list of stripped strings) for simplification. Convert
    #       to indexes in a source string with zero or no modification. Code
    #       should be smaller with less memory copies.
    # TODO: complicate string and printing code by using regex-style methods
    #       to reduce lines of code for parsing and printing
    # TODO: quadrant hints
    # TODO: allow word r'^[\?\*]+$' ?
    # TODO: wildcard '*' could be interesting, but it can return EVERY possible path
    #       on the board for word A*A on a board with two As sitting next to each other
    #       or for word "*" if you're mean. :)


import sys
import copy

# Instant Struct
# https://groups.google.com/forum/#!msg/comp.lang.python/N01xtJRZUmw/qdsT2udG-T8J
class X(object):
    def __init__(self,_d={},**kwargs):
        kwargs.update(_d)
        self.__dict__=kwargs
    def __eq__(self, other):
        return self.__dict__.items() == other.__dict__.items()
# Replace X with Y in your code if you want to debug/inspect
class Y(X):
    def __repr__(self):
        return '<Y:%s>'%self.__dict__


class Cell:
    def __init__(self, table, x=0, y=0):
        self.table = table
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.table) ^ hash(self.x) ^ hash(self.y)
    
    def __eq__(self, other):
        return self.table == other.table and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        return self

    def next(self):
        if self.x >= self.table.width or self.y >= self.table.height:
            raise StopIteration()
        current = copy.copy(self)
        linearIndex = 1 + self.x + self.y * self.table.height
        self.x = linearIndex % self.table.width
        self.y = linearIndex / self.table.height
        return current

    def nw(self):
        if (self.x == 0 or self.y == 0):
            return None
        return Cell(self.table, self.x - 1, self.y - 1)

    def n(self):
        if (self.y == 0):
            return None
        return Cell(self.table, self.x, self.y - 1)

    def ne(self):
        if (self.x == self.table.width - 1 or self.y == 0):
            return None
        return Cell(self.table, self.x + 1, self.y - 1)

    def e(self):
        if (self.x == self.table.width - 1):
            return None
        return Cell(self.table, self.x + 1, self.y)

    def se(self):
        if (self.x == self.table.width - 1 or self.y == self.table.height - 1):
            return None
        return Cell(self.table, self.x + 1, self.y + 1)

    def s(self):
        if (self.y == self.table.height - 1):
            return None
        return Cell(self.table, self.x, self.y + 1)

    def sw(self):
        if (self.x == 0 or self.y == self.table.height - 1):
            return None
        return Cell(self.table, self.x - 1, self.y + 1)

    def w(self):
        if (self.x == 0):
            return None
        return Cell(self.table, self.x - 1, self.y)

    def value(self):
        return self.table[self.y][self.x]

    def __repr__(self):
        return "Cell(%d,%d,\"%s\")" % (self.x, self.y, self.value())

    def __str__(self):
        return self.value()


class WordSearchTable:
    _snaking = False
    _verbose = False

    def __init__(self, asciiTableAndWordlist, options):
        self._verbose = options.verbose
        self._snaking = options.snaking

        # Calculate line length to get dimensions
        # Should we quickly validate the table to ensure all
        # lines have the same length and only alpha input?
        self.table = asciiTableAndWordlist.strip().splitlines()
        self.width = len(self.table[0])
        # Last two lines should be: empty, comma-separated list of search terms
        if self.table[-2]:
            raise ValueError("Malformatted input, no blank line found between table and word list!")
        self.words = [ w.strip() for w in self.table[-1].split(",") ]
        self.table = self.table[:-2]
        self.height = len(self.table)
        if self.width == 0 or self.height == 0:
            raise ValueError("Invalid dimensions: %dx%d!" % (self.width, self.height))
        for line in self.table:
            if self.width != len(line):
                raise ValueError("All rows must be the same width! (%d != %d)" % (self.width, len(line)))
        if not self.words:
            raise ValueError("Empty word list!")

    def search(self):
        # Build a a hash table mapping uppercase letters to the list of words that
        # start with that letter
        words = {}
        for w in [ w.upper() for w in self.words ]:
            words.setdefault(w[0], []).append(w)
        if self._verbose:
            print words

        # Iterate over every cell and search for the words beginning with the
        # cell's letter value
        self.results = []
        for c in self.cell():
            try:
                for w in words[c.value()]:
                    self.results += [ Y(word=w,result=r) for r in self.findWord(c, w) ]
            except KeyError:
                continue
        
        # Filter out palindromes which return 2 results for the same word
        # Prefer the version that starts closer to the origin
        for r in filter(lambda x: x.word == x.word[::-1], self.results)[::-1]:
            if X(word=r.word, result=r.result[::-1]) in self.results:
                self.results.remove(r)

        for r in self.results if self._verbose else []:
            print "Result:", r.word, [ "(%s,%d,%d)"%(c,c.x,c.y) for c in r.result ]
            
        return self

    # Start off by looking in all directions...
    def findWord(self, cell, word, trail = [],
                 directions = [ "n", "ne", "e", "se", "s", "sw", "w", "nw" ]):
        # No null cells or words. No backtracking. No mismatches.
        if (not cell
            or cell in trail
            or not (word and word[0] in [ "?", cell.value() ])):
            return []
        # Match, no more characters to check
        if len(word) == 1:
            return [ trail + [ cell ] ]
        # Keep searching in each direction
        results = []
        for d in directions:
            results += self.findWord(getattr(cell, d)(), word[1:], trail + [ cell ],
                                     directions if self._snaking else [ d ])
        return results

    def printResults(self):
        # we could change this to build a table of +s and then
        # place chars in the table based on cells in the results
        # Create a set of result cells
        r = set(reduce(lambda x, y: x + y.result, self.results, []))
        for y in range(self.height):
            for x in range(self.width):
                c = self.cell(x, y)
                print c.value() if c in r else "+",
            print

    def cell(self, x=0, y=0):
        return Cell(self, x, y)

    def __getitem__(self, item):
        return self.table[item]

    def __repr__(self):
        return "Table(%dx%d,\"%s\")" % (self.width, self.height, self.table[0] + "...")

    def __str__(self):
        return "\n".join(self.table)



def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option("-v",
                      action="store_true", dest="verbose", default=False,
                      help="be verbose")
    parser.add_option("-s",
                      action="store_true", dest="snaking", default=False,
                      help="allow words to snake")
    (options, args) = parser.parse_args()

    # Search for words (with repetition and snaking)
    table = WordSearchTable(sys.stdin.read(), options).search().printResults()

if __name__ == "__main__":
    main()
