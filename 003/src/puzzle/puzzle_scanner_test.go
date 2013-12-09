package puzzle

import (
	"testing"
	"strings"
)

const girdSource =
`U E W R T R B H C D
C X G Z U W R Y E R
R O C K S B A U C U
S F K F M T Y S G E
`

func TestScanDiag1(t *testing.T) {
	var g Grid
	g.ReadFromReader(strings.NewReader(girdSource))
	puzzleScanner := NewDiag1PuzzleScanner(g)

	var bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 0, 0, "", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 0, 1, "EC", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 0, 2, "WXR", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 0, 3, "RGOS", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 1, 3, "TZCF", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 2, 3, "RUKK", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 3, 3, "BWSF", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 4, 3, "HRBM", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 5, 3, "CYAT", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 6, 3, "DEUY", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 7, 3, "RCS", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 8, 3, "UG", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 3, "", string(bytes))

	if puzzleScanner.status != END_OF_GRID {
		t.Fatalf("status was %d - not expected END_OF_GRID", puzzleScanner.status)
	}
}

func TestScanDiag2(t *testing.T) {
	var g Grid
	g.ReadFromReader(strings.NewReader(girdSource))
	puzzleScanner := NewDiag2PuzzleScanner(g)

	var bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 0, "", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 1, "CR", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 2, "HEU", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 3, "BYCE", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 8, 3, "RRUG", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 7, 3, "TWAS", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 6, 3, "RUBY", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 5, 3, "WZST", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 4, 3, "EGKM", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 3, 3, "UXCF", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 2, 3, "COK", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 1, 3, "RF", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 0, 3, "", string(bytes))

	if puzzleScanner.status != END_OF_GRID {
		t.Fatalf("status was %d - not expected END_OF_GRID", puzzleScanner.status)
	}
}

func TestScanHorizontal(t *testing.T) {
	var g Grid
	g.ReadFromReader(strings.NewReader(girdSource))
	puzzleScanner := NewHorizontalPuzzleScanner(g)

	var bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 0, "UEWRTRBHCD", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 1, "CXGZUWRYER", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 2, "ROCKSBAUCU", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 3, "SFKFMTYSGE", string(bytes))

	if puzzleScanner.status != END_OF_GRID {
		t.Fatalf("status was %d - not expected END_OF_GRID", puzzleScanner.status)
	}
}

func TestScanVertical(t *testing.T) {
	var g Grid
	g.ReadFromReader(strings.NewReader(girdSource))
	puzzleScanner := NewVerticalPuzzleScanner(g)

	var bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 0, 3, "UCRS", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 1, 3, "EXOF", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 2, 3, "WGCK", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 3, 3, "RZKF", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 4, 3, "TUSM", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 5, 3, "RWBT", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 6, 3, "BRAY", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 7, 3, "HYUS", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 8, 3, "CECG", string(bytes))

	bytes = ScanRow(puzzleScanner)
	CheckExpected(t, puzzleScanner, 9, 3, "DRUE", string(bytes))

	if puzzleScanner.status != END_OF_GRID {
		t.Fatalf("status was %d - not expected END_OF_GRID", puzzleScanner.status)
	}
}

func CheckExpected(t *testing.T, puzzleScanner *PuzzleScanner, x, y int, expected, actual string) {
	if puzzleScanner.position.x != x {
		t.Fatalf("Expected x to be %d but was %d", x, puzzleScanner.position.x)
	}
	if puzzleScanner.position.y != y {
		t.Fatalf("Expected y to be %d but was %d", y, puzzleScanner.position.y)
	}
	if (expected != actual) {
		t.Fatalf("Expected \"%s\" but got \"%s\"", expected, actual)
	}
}

func ScanRow(puzzleScanner *PuzzleScanner) []byte {
	if puzzleScanner.status == END_OF_GRID {
		return nil
	}
	var bytes []byte
	for {
		var b = puzzleScanner.NextByte()
		if puzzleScanner.status != OK {
			break
		}
		bytes = append(bytes, b)
	}
	return bytes
}
