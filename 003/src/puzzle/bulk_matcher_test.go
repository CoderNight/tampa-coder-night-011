package puzzle

import (
	"testing"
	"fmt"
	"bytes"
)

func TestBulkMatcher(t *testing.T) {
	var bulkMatcher BulkMatcher
	bulkMatcher.AddWord([]byte("dolphin"))
	bulkMatcher.AddWord([]byte("porpoise"))

	var testRow = []byte("blarghdolphinblargporpoisergh")
	var foundMatches []FoundMatch

	var matchedCallback = func(foundMatch FoundMatch) {
		fmt.Println("Match completed callback for ", foundMatch)
		foundMatches = append(foundMatches, foundMatch)
	}

	var pos Position
	for i, byte := range testRow {
		pos.x = i
		fmt.Println("Matching ", string(byte))
		bulkMatcher.MatchByte(byte, pos, matchedCallback)
	}

	if len(foundMatches) != 2 {
		t.Fatalf("Expected foundMatches len to be 2 but was %d", len(foundMatches))
	}

	firstMatch := foundMatches[0]

	firstMatchPos := firstMatch.startPosition
	if firstMatchPos.x != 6 || firstMatchPos.y != 0 {
		t.Fatalf("Expected first match position %d, %d but was %d, %d", 6, 0, firstMatchPos.x,
			firstMatchPos.y)
	}

	if !bytes.Equal(firstMatch.word, []byte("dolphin")) {
		t.Fatalf("Expected first word %s but was %s", string(firstMatch.word), "dolphin")
	}

	secondMatch := foundMatches[1]

	secondMatchPos := secondMatch.startPosition
	if secondMatchPos.x != 18 || secondMatchPos.y != 0 {
		t.Fatalf("Expected second match position %d, %d but was %d, %d", 6, 0, secondMatchPos.x,
			secondMatchPos.y)
	}

	if !bytes.Equal(secondMatch.word, []byte("porpoise")) {
		t.Fatalf("Expected first word %s but was %s", string(firstMatch.word), "porpose")
	}

}
