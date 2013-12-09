import unittest
from word_search import *

class VectorTests(unittest.TestCase):
    
    def test_vector_comparison(self):
        v1 = Vector(3, 4)
        v2 = Vector(3, 4)
        self.failUnless(v1 == v2)
        
    def test_vector_addition(self):
        v1 = Vector(3, 4)
        v2 = Vector(-1, 2)
        v3 = Vector(2, 6)
        v4 = v1 + v2
        self.failUnless(v4.__dict__ == v3.__dict__)
        
    def test_vector_in_range(self):
        v1 = Vector(90, 1)
        v2 = Vector(2, 3)
        v3 = Vector(3, 4)
        v4 = Vector(3 ,4)
        self.failUnless(v2.in_range(v3))
        self.failIf(v2.in_range(v1))
        self.failIf(v3.in_range(v4))
        
    def test_vector_multiply_by_factor(self):
        v1 = Vector(3, 4)
        self.failUnless(v1 == v1.multiply_by_factor())
        f2 = 10
        v2 = Vector(30, 40)
        self.failUnless(v2 == v1.multiply_by_factor(f2))
        f3 = -2
        v3 = Vector(-6, -8)
        self.failUnless(v3 == v1.multiply_by_factor(f3))


class BoardTests(unittest.TestCase):
    
    def test_board_constructor(self):
        # Standard board
        grid_list = ['++++++++', '++++++++', '++++++++', '++++++++', '++++++++']
        max_rows = len(grid_list)
        max_columns = len(grid_list[0])
        board1 = Board(rows=max_rows, columns=max_columns)
        board1_dict = {'columns': max_columns,
                      'grid': grid_list,
                      'rows': max_rows,
                      'range': Vector(max_columns, max_rows)}
        self.failUnless(board1.__dict__ == board1_dict)
        # Empty board
        board2 = Board()
        empty_board_dict = {'columns': 0, 'grid': [], 'rows': 0, 'range': Vector(0, 0)}
        self.failUnless(board2.__dict__ == empty_board_dict)
        # Wrong boards default to empty board
        board3 = Board(columns=10)
        self.failUnless(board3.__dict__ == empty_board_dict)
        board3 = Board(columns=-2)
        self.failUnless(board3.__dict__ == empty_board_dict)
        board3 = Board(columns=10, rows=0)
        self.failUnless(board3.__dict__ == empty_board_dict)
        board3 = Board(columns=1, rows=-11)
        self.failUnless(board3.__dict__ == empty_board_dict)
        board3 = Board(rows=10)
        self.failUnless(board3.__dict__ == empty_board_dict)
        board3 = Board(rows=-2)
        self.failUnless(board3.__dict__ == empty_board_dict)
    
    def test_load_from_list(self):
        # Correct board 1
        grid_list = ['abc', 'def', 'ghi', 'jkl', 'mno']
        board = Board()
        board.load_from_list(grid_list)
        self.failUnless(board.grid == grid_list)
        self.failUnless(board.rows == len(grid_list))
        self.failUnless(board.columns == len(grid_list[0]))
        # Correct board 2
        grid_list = ['abc']
        board = Board()
        board.load_from_list(grid_list)
        self.failUnless(board.grid == grid_list)
        self.failUnless(board.rows == len(grid_list))
        self.failUnless(board.columns == len(grid_list[0]))
        # Correct board 3
        grid_list = ['a', 'b', 'c']
        board = Board()
        board.load_from_list(grid_list)
        self.failUnless(board.grid == grid_list)
        self.failUnless(board.rows == len(grid_list))
        self.failUnless(board.columns == len(grid_list[0]))
        # Empty board; does not change board
        grid_list2 = []
        board.load_from_list(grid_list2)
        self.failUnless(board.grid == grid_list)
        self.failUnless(board.rows == len(grid_list))
        self.failUnless(board.columns == len(grid_list[0]))
        # Wrong board 1; does not change board
        grid_list2 = ['']
        board.load_from_list(grid_list2)
        self.failUnless(board.grid == grid_list)
        self.failUnless(board.rows == len(grid_list))
        self.failUnless(board.columns == len(grid_list[0]))
        # Wrong board 2; does not change board
        grid_list2 = ['abc', 'def', 'gi', 'jkl']
        board.load_from_list(grid_list2)
        self.failUnless(board.grid == grid_list)
        self.failUnless(board.rows == len(grid_list))
        self.failUnless(board.columns == len(grid_list[0]))
        # Wrong board 3; does not change board
        grid_list2 = ['a', 'b', 'c', '']
        board.load_from_list(grid_list2)
        self.failUnless(board.grid == grid_list)
        self.failUnless(board.rows == len(grid_list))
        self.failUnless(board.columns == len(grid_list[0]))
        
    def cell_list(self):
        board = Board(rows=10, columns=8)
        cell_list = board.cell_list(start=Vector(7, 5), vector=Vector(-1, 1), length=20)
        description = ['Vector: (7, 5)',
                       'Vector: (6, 6)',
                       'Vector: (5, 7)',
                       'Vector: (4, 8)',
                       'Vector: (3, 9)']
        self.failUnless([str(cell) for cell in cell_list] == description)
            
        
class BoardStringTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        grid_list = ['UEWRTRBHCD',
                     'CXGZUWRYER',
                     'ROCKSBAUCU',
                     'SFKFMTYSGE',
                     'YSOOUNMZIM',
                     'TCGPRTIDAN',
                     'HZGHQGWTUV',
                     'HQMNDXZBST',
                     'NTCLATNBCE',
                     'YBURPZUXMS']
        self.board.load_from_list(grid_list)
        
    def test_letter_at_cell(self):
        self.failUnless(self.board.letter_at_cell(Vector(0, 0)) == 'U')
        self.failUnless(self.board.letter_at_cell(Vector(3, 7)) == 'N')
        self.failUnless(self.board.letter_at_cell(Vector(9, 9)) == 'S')
        self.failUnless(self.board.letter_at_cell(Vector(100, 0)) == None)
        
    def test_set_letter_at_cell(self):
        cell = Vector(0, 0)
        self.board.set_letter_at_cell('+', cell)
        self.failUnless(self.board.letter_at_cell(cell) == '+')
        cell = Vector(3, 7)
        self.board.set_letter_at_cell('+', cell)
        self.failUnless(self.board.letter_at_cell(cell) == '+')        
        
    def test_letters_at_cells(self):
        cell_list = self.board.cell_list(start=Vector(3, 0), vector=Vector(1, 1), length=3)
        word = self.board.letters_at_cells(cell_list)
        self.failUnless(word == 'RUBY')
        cell_list = self.board.cell_list(start=Vector(4, 9), vector=Vector(1, 0), length=12)
        word = self.board.letters_at_cells(cell_list)
        self.failUnless(word == 'PZUXMS')
        cell_list = self.board.cell_list(start=Vector(0, 8), vector=Vector(1, 1), length=1)
        word = self.board.letters_at_cells(cell_list)
        self.failUnless(word == 'NB')
        cell_list = self.board.cell_list(start=Vector(1, 9), vector=Vector(-1, -1), length=1)
        word = self.board.letters_at_cells(cell_list)
        self.failUnless(word == 'BN')
        
    def test_set_letters_at_cells(self):
        cell_list = self.board.cell_list(start=Vector(3, 0), vector=Vector(1, 1), length=3)
        self.board.set_letters_at_cells(word='ABCD', cell_list=cell_list)
        word = self.board.letters_at_cells(cell_list)
        self.failUnless(word == 'ABCD')
        cell_list = self.board.cell_list(start=Vector(1, 9), vector=Vector(-1, -1), length=1)
        self.board.set_letters_at_cells(word='XY', cell_list=cell_list)
        word = self.board.letters_at_cells(cell_list)
        self.failUnless(word == 'XY')
             
    def test_string_N_S(self):
        # Edge columns
        st = self.board.string_NS(column=0)
        self.failUnless(st == 'UCRSYTHHNY')
        st = self.board.string_NS(column=9)
        self.failUnless(st == 'DRUEMNVTES')
        # Center columns
        st = self.board.string_NS(column=4)
        self.failUnless(st == 'TUSMURQDAP')
        # Columns out of range
        st = self.board.string_NS(column=-1)
        self.failIf(st)
        st = self.board.string_NS(column=10)
        self.failIf(st)

    def test_string_N_SE(self):
        vector = Vector(1, 1)
        # Edge columns
        st = self.board.string_NS(column=0, vector=vector)
        self.failUnless(st == 'UXCFUTWBCS')
        st = self.board.string_NS(column=9, vector=vector)
        self.failUnless(st == 'D')
        # Center columns
        st = self.board.string_NS(column=4, vector=vector)
        self.failUnless(st == 'TWASIN')

    def test_string_N_SW(self):
        vector = Vector(-1, 1)
        # Edge columns
        st = self.board.string_NS(column=0, vector=vector)
        self.failUnless(st == 'U')
        st = self.board.string_NS(column=9, vector=vector)
        self.failUnless(st == 'DEUYNRHMTY')
        # Center columns
        st = self.board.string_NS(column=4, vector=vector)
        self.failUnless(st == 'TZCFY')

    def test_string_W_E(self):
        # Edge rows
        st = self.board.string_WE(row=0)
        self.failUnless(st == 'UEWRTRBHCD')
        st = self.board.string_WE(row=9)
        self.failUnless(st == 'YBURPZUXMS')
        # Center rows
        st = self.board.string_WE(row=4)
        self.failUnless(st == 'YSOOUNMZIM')
        # Rows out of range
        st = self.board.string_WE(row=-1)
        self.failIf(st)
        st = self.board.string_WE(row=10)
        self.failIf(st)

    def test_string_W_SE(self):
        vector = Vector(1, 1)
        # Edge rows
        st = self.board.string_WE(row=1, vector=vector)
        self.failUnless(st == 'COKORGZBM')
        st = self.board.string_WE(row=9, vector=vector)
        self.failUnless(st == 'Y')
        # Center rows
        st = self.board.string_WE(row=4, vector=vector)
        self.failUnless(st == 'YCGNAZ')
        # Row out of range
        st = self.board.string_WE(row=0, vector=vector)
        self.failIf(st)

    def test_string_E_SW(self):
        vector = Vector(-1, 1)
        # Edge rows
        st = self.board.string_WE(row=1, vector=vector)
        self.failUnless(st == 'RCSMTQNCB')
        st = self.board.string_WE(row=9, vector=vector)
        self.failUnless(st == 'S')
        # Center rows
        st = self.board.string_WE(row=4, vector=vector)
        self.failUnless(st == 'MATZTP')
        # Rows out of range
        st = self.board.string_WE(row=0, vector=vector)
        self.failIf(st)

        
class PuzzleTests(unittest.TestCase):
    
    def test_constructor(self):
        puzzle = Puzzle()
        empty_list = []
        empty_board_dict = {'columns': 0, 'grid': [], 'rows': 0, 'range': Vector(0, 0)}
        self.failUnless(puzzle.board.__dict__ == empty_board_dict)
        self.failUnless(puzzle.solution.__dict__ == empty_board_dict)
        self.failUnless(puzzle.words == empty_list)
        grid_list = ['ABC', 'DEF', 'ghi', 'jkl', 'mno']
        rows = len(grid_list)
        columns = len(grid_list[0])
        words = ['a', 'E', 'jk']
        puzzle = Puzzle(grid_list=grid_list, words=words)
        solution_board = Board(rows=rows, columns=columns) # empty board
        self.failUnless(puzzle.board.grid == [s.upper() for s in grid_list])
        self.failUnless(puzzle.board.rows == rows)
        self.failUnless(puzzle.board.columns == columns)
        self.failUnless(puzzle.solution == solution_board)
        self.failUnless(puzzle.words == [w.upper() for w in words])
        
    def test_load_from_file(self):
        puzzle = Puzzle()
        puzzle.load_from_file('puzzle1.txt')
        grid_list = ['UEWRTRBHCD',
                     'CXGZUWRYER',
                     'ROCKSBAUCU',
                     'SFKFMTYSGE',
                     'YSOOUNMZIM',
                     'TCGPRTIDAN',
                     'HZGHQGWTUV',
                     'HQMNDXZBST',
                     'NTCLATNBCE',
                     'YBURPZUXMS']
        columns = len(grid_list[0])
        rows = len(grid_list)
        puzzle_board_dict = {'columns': columns, 'grid': grid_list, 'rows': rows, 'range': Vector(columns, rows)}
        self.failUnless(puzzle.board.__dict__ == puzzle_board_dict)
        solution_board = Board(rows=rows, columns=columns)
        self.failUnless(puzzle.solution.__dict__ == solution_board.__dict__)
        words = ['RUBY', 'ROCKS', 'DAN', 'MATZ']
        self.failUnless(puzzle.words == words)

    def test_solve_N_S(self):
        # Puzzle 1
        puzzle = Puzzle()
        puzzle.load_from_file('puzzle1.txt')
        puzzle.solve_N_S()
        solution_board = Board(columns=puzzle.board.columns, rows=puzzle.board.rows) # empty board, no solution
        self.failUnless(puzzle.solution.__dict__ == solution_board.__dict__)
        # Puzzle 2
        puzzle.words = ['R', 'U', 'B', 'Y']
        puzzle.solve_N_S()
        grid_list = ['U++R+RB+++',
                     '++++U+RY+R',
                     'R++++B+U+U',
                     '++++++Y+++',
                     'Y+++U+++++',
                     '++++R+++++',
                     '++++++++U+',
                     '+++++++B++',
                     '+++++++B++',
                     'YBUR++U+++']
        solution_board = Board()
        solution_board.load_from_list(grid_list)
        self.failUnless(puzzle.solution.__dict__ == solution_board.__dict__)
        # Puzzle 3
        grid_list = ['ABC', 
                     'ABX', 
                     'AXX', 
                     'XXX']
        words = ['a', 'xx']
        solution_grid = ['A++', 
                         'A+X', 
                         'AXX', 
                         '+X+']
        solution_board = Board()
        solution_board.load_from_list(solution_grid)
        puzzle = Puzzle(words=words, grid_list=grid_list)
        puzzle.solve_N_S()
        self.failUnless(puzzle.solution == solution_board)
        # Puzzle 4
        grid_list = ['abc', 
                     'abx', 
                     'axx', 
                     'xxx']
        words = ['a', 'x']
        solution_grid = ['A++', 
                         'A+X', 
                         'AXX', 
                         'XXX']
        solution_board = Board()
        solution_board.load_from_list(solution_grid)
        puzzle = Puzzle(words=words, grid_list=grid_list)
        puzzle.solve_N_S()
        self.failUnless(puzzle.solution == solution_board)
        # Puzzle 5
        grid_list = ['r',
                     'u',
                     'b',
                     'y',
                     'x',
                     'x',
                     'x',
                     'y',
                     'b',
                     'u',
                     'r',
                     'x',
                     'x',
                     'x',
                     'R',
                     'U',
                     'B',
                     'Y']
        words = ['ruby']
        solution_grid = ['R',
                         'U',
                         'B',
                         'Y',
                         '+',
                         '+',
                         '+',
                         'Y',
                         'B',
                         'U',
                         'R',
                         '+',
                         '+',
                         '+',
                         'R',
                         'U',
                         'B',
                         'Y']
        solution_board = Board()
        solution_board.load_from_list(solution_grid)
        puzzle = Puzzle(words=words, grid_list=grid_list)
        puzzle.solve_N_S()
        self.failUnless(puzzle.solution == solution_board)

    def test_solve_N_SE(self):
        pass
    
    def test_solve_N_SW(self):
        pass
    
    def test_solve_W_E(self):
        # Puzzle 1
        puzzle = Puzzle()
        puzzle.load_from_file('puzzle1.txt')
        puzzle.solve_W_E()
        grid_list = ['++++++++++',
                     '++++++++++',
                     'ROCKS+++++',
                     '++++++++++',
                     '++++++++++',
                     '+++++++DAN',
                     '++++++++++',
                     '++++++++++',
                     '++++++++++',
                     'YBUR++++++']
        columns = len(grid_list[0])
        rows = len(grid_list)
        puzzle_board_dict = {'columns': columns, 'grid': grid_list, 'rows': rows, 'range': Vector(columns, rows)}
        self.failUnless(puzzle.solution.__dict__ == puzzle_board_dict)
        # Puzzle 2
        puzzle.load_from_file('puzzle1.txt')
        puzzle.words = ['R', 'U', 'B', 'Y']
        puzzle.solve_W_E()
        grid_list = ['U++R+RB+++',
                     '++++U+RY+R',
                     'R++++B+U+U',
                     '++++++Y+++',
                     'Y+++U+++++',
                     '++++R+++++',
                     '++++++++U+',
                     '+++++++B++',
                     '+++++++B++',
                     'YBUR++U+++']
        solution_board = Board()
        solution_board.load_from_list(grid_list)
        self.failUnless(puzzle.solution.__dict__ == solution_board.__dict__)
        # Puzzle 3
        grid_list = ['ABC', 'ABX', 'AXX', 'XXX']
        words = ['a', 'xx']
        solution_grid = ['A++', 'A++', 'AXX', 'XX+']
        solution_board = Board()
        solution_board.load_from_list(solution_grid)
        puzzle = Puzzle(words=words, grid_list=grid_list)
        puzzle.solve_W_E()
        self.failUnless(puzzle.solution == solution_board)
        # Puzzle 4
        grid_list = ['abc', 'abx', 'axx', 'xxx']
        words = ['a', 'x']
        solution_grid = ['A++', 'A+X', 'AXX', 'XXX']
        solution_board = Board()
        solution_board.load_from_list(solution_grid)
        puzzle = Puzzle(words=words, grid_list=grid_list)
        puzzle.solve_W_E()
        self.failUnless(puzzle.solution == solution_board)
        # Puzzle 5
        grid_list = ['rubyxxxyburxxxRUBY']
        words = ['ruby']
        solution_grid = ['RUBY+++YBUR+++RUBY']
        solution_board = Board()
        solution_board.load_from_list(solution_grid)
        puzzle = Puzzle(words=words, grid_list=grid_list)
        puzzle.solve_W_E()
        self.failUnless(puzzle.solution == solution_board)
        
    def test_solve_W_SE(self):
        pass

    def test_solve_E_SW(self):
        pass

    