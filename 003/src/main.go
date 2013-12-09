/**
 * Created by nhoize on 11/25/13.
 */
package main

import (
	"puzzle"
)



func main() {
	var g puzzle.Grid
	g.ReadFromFile("./puzzle1.txt")
	var solver puzzle.Solver
	solver.Solve(g)
}
