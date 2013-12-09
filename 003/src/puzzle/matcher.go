package puzzle

//import "fmt"

type Matcher struct {
	word          []byte
	matchIndex    int
	startPosition Position
}

func NewMatcher(word []byte) *Matcher {
	m := Matcher{word: word, matchIndex: 0, startPosition: Position{0,0}}
	return &m
}

func (m *Matcher) MatchByte(byte byte, pos Position) bool {
//	fmt.Printf("Checking word %s for char %s (%d) at matchIndex %d\n", m.word, string(byte), byte, m.matchIndex)
	if m.word[m.matchIndex] == byte {
		if m.matchIndex == 0 {
			m.startPosition = pos
		}
		m.matchIndex++
//		fmt.Printf("Matched character %s for word %s at matchIndex %d\n", string(byte), string(m.word), m.matchIndex)
		if m.matchIndex == len(m.word) {
//			fmt.Printf("Match completed for %s, returning true\n", m.word)
			return true
		}
		return false
	}
	m.matchIndex = 0
	//	m.startPosition = Position{}
	return false
}
