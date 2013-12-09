package puzzle

import (
	"bytes"
//	"fmt"
)

type BulkMatcher struct {
	matchers []*Matcher
}

type MatchedCallback func (foundMatch FoundMatch)

func reverse(word []byte) []byte {
	reversed := make([]byte, len(word))
	for i, j := 0, len(word) - 1; j >= 0; i, j = i + 1, j - 1 {
		reversed[i] = word[j]
	}
	return reversed
}

func (bulkMatcher *BulkMatcher) AddWord(word []byte) {
	bulkMatcher.matchers = append(bulkMatcher.matchers, NewMatcher(word))
	var reverseWord = reverse(word)
	if !bytes.Equal(reverseWord, word) {
		bulkMatcher.matchers = append(bulkMatcher.matchers, NewMatcher(reverseWord))
	}
}

func (bulkMatcher *BulkMatcher) MatchByte(byte byte, pos Position, callback MatchedCallback) {
//	fmt.Printf("Checking %d matchers\n", len(bulkMatcher.matchers))
	for i, matcher := range bulkMatcher.matchers {
		if matcher.MatchByte(byte, pos) {
//			fmt.Println("BulkMatcher detected match for %s at %d, %d", string(matcher.word), matcher.startPosition.X, matcher.startPosition.Y)
			// delete the matched matcher
//			fmt.Println("Deleting matched matcher")
			bulkMatcher.matchers = append(bulkMatcher.matchers[:i], bulkMatcher.matchers[i + 1:]...)
			// inform the caller about a completed match
//			fmt.Println("Performing callback")
			callback(FoundMatch{StartPosition: matcher.startPosition, Word: matcher.word})
		}
	}
}

func (bulkMatcher *BulkMatcher) Reset() {
	for _, matcher := range bulkMatcher.matchers {
		matcher.matchIndex = 0
	}
}
