package puzzle

import (
	"testing"
)

func TestHasMatch(t *testing.T) {
	matcher := NewMatcher([]byte("testing"))
	var testRow = []byte("blarghtestingblargh")
	var pos Position
	for i := 0; i < len(testRow) - 1; i++ {
		if matcher.MatchByte(testRow[i], pos) {
			if matcher.startPosition.x != 6 && matcher.startPosition.y != 0 {
				t.Fatalf("Expected startPosition %d, %d but got %d, %d", 6, 0,
					matcher.startPosition.x, matcher.startPosition.y)
			}
			return
		}
		pos.x = i
	}
	t.Fail()
}

func TestNoMatch(t *testing.T) {
	matcher := NewMatcher([]byte("testingg"))
	var testRow = []byte("blarghtestingblargh")
	var pos Position
	for i := 0; i < len(testRow) - 1; i++ {
		if matcher.MatchByte(testRow[i], pos) {
			t.Fatal("Received unexpected match")
		}
		pos.x = i
	}
}
