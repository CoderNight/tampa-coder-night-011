package puzzle

import "testing"

const expected =
`U E W R T R B H C D
C X G Z U W R Y E R
R O C K S B A U C U
S F K F M T Y S G E
Y S O O U N M Z I M
T C G P R T I D A N
H Z G H Q G W T U V
H Q M N D X Z B S T
N T C L A T N B C E
Y B U R P Z U X M S
`

func TestReadPuzzle(t *testing.T) {
	var g Grid
	g.ReadFromFile("../../puzzle1.txt")
	var str = g.String()
	if expected != str {
		t.Fatalf("Expected string \n\n\"%s\"\n\n does not match \n\n\"%s\"\n\n", expected, str)
	}

	if g.searchWords[3] != "MATZ" {
		t.Fatalf("Expected MATZ but got %s", g.searchWords[3])
	}
}
