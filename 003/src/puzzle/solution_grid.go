package puzzle

import (
	"bytes"
	"fmt"
)

type SolutionGrid struct {
	chars   [][]byte
}

func NewSolutionGrid(sourceGrid [][]byte) *SolutionGrid {
	var solutionGrid = SolutionGrid{}
	var yLen = len(sourceGrid)
	var xLen = len(sourceGrid[0])
	solutionGrid.chars = make([][]byte, yLen)
	for i := 0; i < len(solutionGrid.chars) ; i++ {
		solutionGrid.chars[i] = bytes.Repeat([]byte{'+'}, xLen)
	}
	return &solutionGrid
}

func (g *SolutionGrid) WriteMatch(foundMatch FoundMatch) {
//	fmt.Printf("Writing %s at %d, %d orientation %s\n", string(foundMatch.Word), foundMatch.StartPosition.X, foundMatch.StartPosition.Y, foundMatch.Orientation )
	var incX, incY = 0, 0
	var x, y = foundMatch.StartPosition.X, foundMatch.StartPosition.Y
	switch foundMatch.Orientation {
	case "HORIZONTAL":
		incX = 1
		incY = 0
	case "VERTICAL":
		incX = 0
		incY = 1
	case "DIAG1":
		incX=-1
		incY=1
	case "DIAG2":
		incX=1
		incY=1
	}

//	fmt.Printf("incX / incY %d, %d\n", incX, incY)

	for _,byte := range foundMatch.Word {
		g.chars[y][x] = byte
		y = y + incY
		x = x + incX
	}

}

func (g *SolutionGrid) String() string {
	var buffer bytes.Buffer
	for _, line := range g.chars {
		for i, byte := range line {
			buffer.WriteString(fmt.Sprintf("%c", byte))
			if i != len(line) - 1 {
				buffer.WriteString(" ")
			}
		}
		buffer.WriteString("\n")
	}
	return buffer.String()
}
