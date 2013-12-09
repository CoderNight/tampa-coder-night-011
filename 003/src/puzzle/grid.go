package puzzle

import (
	"os"
	"fmt"
	"bufio"
	"bytes"
	"io"
	"strings"
)

type Grid struct {
	chars [][]byte
	SearchWords []string
}

func (g *Grid) ReadFromFile(fileName string) {
	file, err := os.Open(fileName)
	if (err != nil) {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()
	g.ReadFromReader(file)
}

func (g *Grid) ReadFromReader(reader io.Reader) {
	scanner := bufio.NewScanner(reader)

	for scanner.Scan() {
		bytesRead := scanner.Bytes()
		bytesRead = bytes.Trim(bytes.Replace(bytesRead, []byte{' '}, []byte{}, -1), " \r\n")
		if len(bytesRead) == 0 {
			continue
		}
		if bytes.Contains(bytesRead, []byte(",")) {
			// Parse as the words we are searching for
			g.SearchWords = strings.Split(strings.ToUpper(string(bytesRead)), ",")
		} else {
			g.chars = append(g.chars, bytesRead)
		}
	}
}

func (g *Grid) String() string {
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

func (g *Grid) GetChars() [][]byte {
	return g.chars
}
