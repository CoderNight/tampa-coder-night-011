package puzzle

import (
	"puzzle"
	"fmt"
)

type Solver struct {

}

type OrientationMap map[string] *puzzle.PuzzleScanner

func (s *Solver) Solve(g Grid) {
	var bulkMatcher puzzle.BulkMatcher

	for _, s := range g.SearchWords {
		bulkMatcher.AddWord([]byte(s))
	}

	solutionGrid := puzzle.NewSolutionGrid(g.GetChars())

	orientationMap := OrientationMap {
		"HORIZONTAL": puzzle.NewHorizontalPuzzleScanner(g),
		"VERTICAL": puzzle.NewVerticalPuzzleScanner(g),
		"DIAG1": puzzle.NewDiag1PuzzleScanner(g),
		"DIAG2": puzzle.NewDiag2PuzzleScanner(g)}

	for orientation, scanner := range orientationMap {
		var b byte
		var matchedCallback = func(foundMatch puzzle.FoundMatch) {
			foundMatch.Orientation = orientation
			solutionGrid.WriteMatch(foundMatch)
		}
		for ; scanner.Status != puzzle.END_OF_GRID; b = scanner.NextByte() {
			if (scanner.Status == puzzle.END_OF_ROW) {
				bulkMatcher.Reset()
				continue
			}
			bulkMatcher.MatchByte(b, scanner.Position, matchedCallback)
		}
	}
	fmt.Print(solutionGrid.String())
}
