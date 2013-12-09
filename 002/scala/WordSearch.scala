object WordSearch {
  def search(grid: Map[(Int,Int),Char], rc: (Int,Int), word: String, path: List[(Int,Int)]):List[(Int,Int)] = {
    if (word == "") return path
    if (!grid.keys.toList.contains(rc) || path.contains(rc) || !Array('?',grid(rc)).contains(word.head))
      return Nil
    (for (r <- -1 to 1; c <- -1 to 1) yield (r,c)).toList.flatMap {
      case (r,c) => search(grid, (rc._1+r,rc._2+c), word.tail, rc :: path)
    }
  }
  def main(args: Array[String]) {
    val Array(grid_s, word_s) = scala.io.Source.fromFile(args(0)).mkString.toUpperCase.split("\n\n")
    val gridline = grid_s.split("\n").zipWithIndex.map {
      case (line, row) => line.zipWithIndex.map {
        case (ch, col) => ((row,col), ch)
      }
    }

    val grid = gridline.flatten.toMap
    val mark = word_s.split(",").flatMap {
      case word => grid.keys.flatMap { case rc => search(grid, rc, word.trim, Nil) }.toList
    }

    println(gridline.map {
      case gridline => gridline.map {
        case (rc, ch) => if (mark.contains(rc)) ch else '.'
      }.mkString(" ")
    }.mkString("\n"))
  }
}
