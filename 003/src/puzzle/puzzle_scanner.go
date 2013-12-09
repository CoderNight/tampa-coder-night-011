package puzzle

type PuzzleScanner struct {
	grid 		Grid
	Position 	Position
	advance 	AdvanceFunction
	Status		Status
	xrow		int
	yrow		int
}

type Position struct {
	X int
	Y int
}

type AdvanceFunction func (p *PuzzleScanner)

type Status int

const (
	OK Status = iota
	END_OF_ROW
	END_OF_GRID
)

func NewHorizontalPuzzleScanner(grid Grid) *PuzzleScanner {
	return &PuzzleScanner{grid: grid, advance: HorizontalAdvanceFunction, Position: Position{-1, 0}}
}

func NewVerticalPuzzleScanner(grid Grid) *PuzzleScanner {
	return &PuzzleScanner{grid: grid, advance: VerticalAdvanceFunction, Position: Position{0, -1}}
}

func NewDiag1PuzzleScanner(grid Grid) *PuzzleScanner {
	return &PuzzleScanner{grid: grid, advance: Diag1AdvanceFunction, Position: Position{0, 0}}
}

func NewDiag2PuzzleScanner(grid Grid) *PuzzleScanner {
	return &PuzzleScanner{grid: grid, advance: Diag2AdvanceFunction, Position: Position{len(grid.chars[0]) - 1, 0},
		xrow: len(grid.chars[0]) - 1}
}

func VerticalAdvanceFunction(p* PuzzleScanner) {
	if p.Status == END_OF_ROW {
		p.Position.X++;
		p.Position.Y = -1;
		p.Status = OK
	}
	if p.Position.Y >= len(p.grid.chars) - 1 {
		if p.Position.X >= len(p.grid.chars[p.Position.Y]) - 1  {
			p.Status = END_OF_GRID
		} else {
			p.Status = END_OF_ROW
		}
		return
	}
	p.Position.Y++;
	p.Status = OK
}

func HorizontalAdvanceFunction(p* PuzzleScanner) {
	if p.Status == END_OF_ROW {
		p.Position.Y++
		p.Position.X = -1
		p.Status = OK
	}
	if p.Position.X >= len(p.grid.chars[p.Position.Y]) - 1 {
		if p.Position.Y >= len(p.grid.chars) - 1  {
			p.Status = END_OF_GRID
		} else {
			p.Status = END_OF_ROW
		}
		return
	}
	p.Position.X++;
	p.Status = OK
}

/**
From upper right to lower left
 */
func Diag1AdvanceFunction(p* PuzzleScanner) {
	var firstRowRead = p.Position.X == 0 && p.Position.Y == 0
	if p.Status == END_OF_ROW {
		if p.xrow >= len(p.grid.chars[0]) - 1 {
			// we have reached max xrow, start incrementing yrow
			p.yrow++
			p.Position.Y = p.yrow
			p.Position.X = p.xrow
		} else {
			p.xrow++
			p.Position.X = p.xrow
			p.Position.Y = 0
		}
		firstRowRead = true
		p.Status = OK
//		fmt.Println("xrow, yrow, position", p.xrow, p.yrow, p.position)
	}

	if p.Position.X == 0 || p.Position.Y >= len(p.grid.chars) - 1  {
		if p.xrow == len(p.grid.chars[0]) - 1 && p.yrow == len(p.grid.chars)- 1 {
			p.Status = END_OF_GRID
		} else {
			p.Status = END_OF_ROW
		}
		return
	}
	if !firstRowRead {
		p.Position.X--;
		p.Position.Y++;
	}

	p.Status = OK
}

/**
From upper left to lower right
 */
func Diag2AdvanceFunction(p* PuzzleScanner) {
	var firstRowRead = p.Position.X == len(p.grid.chars[0]) - 1 && p.Position.Y == 0
	if p.Status == END_OF_ROW {
		if p.xrow == 0 {
			// we have reached min xrow, start incrementing yrow
			p.yrow++
			p.Position.Y = p.yrow
			p.Position.X = p.xrow
		} else {
			p.xrow--
			p.Position.X = p.xrow
			p.Position.Y = 0
		}
		firstRowRead = true
		p.Status = OK
//		fmt.Println("xrow, yrow, position", p.xrow, p.yrow, p.position)
	}

	if p.Position.X >= len(p.grid.chars[0]) - 1 || p.Position.Y >= len(p.grid.chars) - 1  {
		if p.xrow == 0 && p.yrow == len(p.grid.chars)- 1 {
			p.Status = END_OF_GRID
		} else {
			p.Status = END_OF_ROW
		}
		return
	}
	if !firstRowRead {
		p.Position.X++;
		p.Position.Y++;
	}

	p.Status = OK
}

func (p* PuzzleScanner) NextByte() (b byte) {
	p.advance(p)
//	fmt.Println(p.position, p.status)
	if (p.Status != OK) {
		return 255
	}
	return p.grid.chars[p.Position.Y][p.Position.X]
}
