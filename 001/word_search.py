import string

class Vector(object):
    
    def __init__(self, h=0, v=0):
        self.h = h
        self.v = v
        
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.__dict__ == other.__dict__
    
    def __add__(self, other):
        return Vector(self.h + other.h, self.v + other.v)
       
    def __str__(self):
        return 'Vector: ({h}, {v})'.format(h=self.h, v=self.v)
        
    def in_range(self, other):
        return (0 <= self.h < other.h) and (0 <= self.v < other.v)
    
    def multiply_by_factor(self, factor=1):
        return Vector(self.h * factor, self.v * factor)


class Board(object):
    
    def __init__(self, **kwargs):
        self.grid = []
        self.rows = max(kwargs.get('rows', 0), 0) # default = 0, min = 0
        self.columns = max(kwargs.get('columns', 0), 0)
        if self.rows and self.columns:
            for _ in xrange(self.rows):
                self.grid.append('+' * self.columns)
        else:
            self.rows = 0
            self.columns = 0
        self.range = Vector(self.columns, self.rows)
        
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.__dict__ == other.__dict__
        
    def load_from_list(self, grid_list):
        err = True
        rows = len(grid_list)
        if rows:
            columns = len(grid_list[0])
            if columns:
                err = False
                for row in grid_list:
                    if len(row) != columns:
                        err = True
                        break
        if not err:
            self.rows = rows
            self.columns = columns
            self.grid = grid_list
            self.range = Vector(self.columns, self.rows)
             
    def is_empty(self):
        return not self.grid
    
    def cell_list(self, start=None, vector=None, length=0):
        if not start or not vector or (start.__class__ != Vector)  or (start.__class__ != vector.__class__):
            return []
        boundary = Vector(self.columns, self.rows)
        lst = [start]
        next_cell = start
        while length:
            next_cell += vector
            if not next_cell.in_range(boundary):
                break
            lst.append(next_cell)
            length -= 1   
        return lst
    
    def letter_at_cell(self, cell=None):
        if cell and cell.__class__ == Vector and cell.in_range(self.range):
            return self.grid[cell.v][cell.h]
        
    def set_letter_at_cell(self, letter='', cell=None):
        if letter and cell and cell.__class__ == Vector and cell.in_range(self.range):
            st = self.grid[cell.v]
            st = st[:cell.h] + letter + st[cell.h+1:]
            self.grid[cell.v] = st
   
    def letters_at_cells(self, cell_list=[]):
        if cell_list:
            st = ''
            for cell in cell_list:
                if cell.__class__ != Vector:
                    return
                st += self.letter_at_cell(cell)
            return st
    
    def set_letters_at_cells(self, word='', cell_list=[]):
        if word and cell_list and len(word) == len(cell_list):
            for idx in range(len(word)):
                self.set_letter_at_cell(letter=word[idx], cell=cell_list[idx])
    
    def string_NS(self, column=0, vector=Vector(0, 1)):
        length = min(self.columns, self.rows) - 1 if not (vector == Vector(0, 1)) else self.rows - 1
        if column in range(self.columns):
            cell_list = self.cell_list(start=Vector(column, 0), vector=vector, length=length)
            return self.letters_at_cells(cell_list)
        
    def generate_NS_list(self, vector=Vector(0, 1)):
        return [self.string_NS(column, vector) for column in range(self.columns)]
           
    def string_WE(self, row=0, vector=Vector(1, 0)):
        if vector == Vector(1, 0):
            length = self.columns - 1
            first_row = 0
            first_column = 0
        else:
            length = min(self.columns, self.rows) - 1
            first_row = 1 
            first_column = self.columns - 1 if vector == Vector(-1, 1) else 0
        if row in range(first_row, self.rows):
            cell_list = self.cell_list(start=Vector(first_column, row), vector=vector, length=length)
            return self.letters_at_cells(cell_list)
           
    def generate_WE_list(self, vector=Vector(1, 0)):
        first_row = 0 if vector == Vector(1, 0) else 1
        return [self.string_WE(row=row, vector=vector) for row in range(first_row, self.rows)]
    
    def __str__(self):
        st = ''
        for row in self.grid:
            st += ' '.join([letter for letter in row])
            st += '\n'
        return st[:-1]
    
    
class Puzzle(object):
    
    def __init__(self, grid_list=[], words=[]):
        self.board = Board()
        self.board.load_from_list([s.upper() for s in grid_list]) # Board in uppercase
        self.solution = Board(rows=self.board.rows, columns=self.board.columns)
        self.words = [w.upper() for w in words] # Words in uppercase
        
    def load_from_file(self, file_name):
        with open(file_name,'r') as myfile:
            data = myfile.read()
        pos = string.find(data, '\n\n')
        grid = data[:pos].split()
        self.board.load_from_list(grid)
        self.words = [string.upper(s) for s in data[pos+2:].split(', ')]
        self.solution = Board(columns=self.board.columns, rows=self.board.rows)
    
    def solve_NS(self, vector=Vector(0, 1)):
        lst = self.board.generate_NS_list(vector=vector)
        length = self.board.rows if vector == Vector(0, 1) else min(self.board.rows, self.board.columns)
        for word in self.words:
            if len(word) <= length:
                reversed_word = word[::-1]
                for column in range(self.board.columns):
                    pos = lst[column].find(word)
                    while pos >= 0:
                        start = Vector(column, 0) + vector.multiply_by_factor(pos)
                        cell_list = self.board.cell_list(start=start, vector=vector, length=len(word)-1)
                        self.solution.set_letters_at_cells(word=word, cell_list=cell_list)
                        pos = lst[column].find(word, pos+len(word))
                    if word != reversed_word: # only makes sense to look for a reversed word in this case
                        pos = lst[column].find(reversed_word)
                        while pos >= 0:
                            start = Vector(column, 0) + vector.multiply_by_factor(pos)
                            cell_list = self.board.cell_list(start=start, vector=vector, length=len(reversed_word)-1)
                            self.solution.set_letters_at_cells(word=reversed_word, cell_list=cell_list)
                            pos = lst[column].find(reversed_word, pos+len(reversed_word))
      
    def solve_N_S(self):
        self.solve_NS()
        
    def solve_N_SE(self):
        self.solve_NS(vector=Vector(1, 1))
            
    def solve_N_SW(self):
        self.solve_NS(vector=Vector(-1, 1))
        
    def solve_WE(self, vector=Vector(1, 0)):
        if vector == Vector(1, 0):
            length = self.board.columns - 1
            first_row = 0
            first_column = 0
        else:
            length = min(self.board.columns, self.board.rows) - 1
            first_row = 1 
            first_column = self.board.columns - 1 if vector == Vector(-1, 1) else 0
        lst = self.board.generate_WE_list(vector=vector)
        for word in self.words:
            if len(word) <= length:
                reversed_word = word[::-1]
                for row in range(first_row, self.board.rows):
                    pos = lst[row - first_row].find(word)
                    while pos >= 0:
                        start = Vector(first_column, row) + vector.multiply_by_factor(pos)
                        cell_list = self.board.cell_list(start=start, vector=vector, length=len(word)-1)
                        self.solution.set_letters_at_cells(word=word, cell_list=cell_list)
                        pos = lst[row - first_row].find(word, pos+len(word))
                    if word != reversed_word: # only makes sense to look for a reversed word in this case
                        pos = lst[row - first_row].find(reversed_word)
                        while pos >= 0:
                            start = Vector(first_column, row) + vector.multiply_by_factor(pos)
                            cell_list = self.board.cell_list(start=start, vector=vector, length=len(reversed_word)-1)
                            self.solution.set_letters_at_cells(word=reversed_word, cell_list=cell_list)
                            pos = lst[row - first_row].find(reversed_word, pos+len(reversed_word))

    def solve_W_E(self):
        self.solve_WE()
   
    def solve_W_SE(self):
        self.solve_WE(vector=Vector(1, 1))
            
    def solve_E_SW(self):
        self.solve_WE(vector=Vector(-1, 1))

                   
def main():
    puzzle = Puzzle()
    puzzle.load_from_file('puzzle1.txt')
    puzzle.solve_N_S()
    puzzle.solve_N_SE()
    puzzle.solve_N_SW()
    puzzle.solve_W_E()
    puzzle.solve_W_SE()
    puzzle.solve_E_SW()
    print puzzle.solution 
          
              
if __name__ == '__main__':
    main()
         
                        
    