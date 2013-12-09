package wordsearch;

import java.io.File;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class WordSearch {
  static class RC {
    int row;
    int col;
    RC(int row, int col) { this.row = row; this.col = col; }
    @Override
    public boolean equals(Object obj) {
      RC rc = (RC)obj;
      return rc.row == row && rc.col == col;
    }
  }
  static List<RC> search(String[] grid, RC rc, String word, List<RC> path) {
    try {
      if (word.isEmpty()) { return path; }
      if (path.contains(rc) || (word.charAt(0) != '?' && word.charAt(0) != grid[rc.row].charAt(rc.col))) {
        return new LinkedList<RC>();
      }
      List<RC> result = new LinkedList<RC>();
      List<RC> newPath = new LinkedList<RC>();
      newPath.addAll(path);
      newPath.add(rc);
      for (int r = -1; r <= 1; r++) {
        for (int c = -1; c <= 1; c++) {
          result.addAll(search(grid, new RC(rc.row+r, rc.col+c), word.substring(1), newPath));
        }
      }
        
      return result;
    } catch (ArrayIndexOutOfBoundsException e) {
      return new LinkedList<RC>();
    } catch (StringIndexOutOfBoundsException e) {
      return new LinkedList<RC>();
    }
  }
  public static void main(String[] args) throws Exception {
    Scanner scanner = new Scanner(new File(args[0]));
    scanner.useDelimiter("\n\n");
    String[] grid = scanner.next().split("\n");
    String wordStr = scanner.next();
    scanner.close();
    
    List<RC> mark = new LinkedList<RC>();
    String[] words = wordStr.split(",");
    for (int i = 0; i < words.length; i++) {
      String word = words[i].trim().toUpperCase();
      for (int row = 0; row < grid.length; row++) {
        for (int col = 0; col < grid[row].length(); col++) {
          mark.addAll(search(grid, new RC(row,col), word, new LinkedList<RC>()));
        }
      }
    }
    
    for (int row = 0; row < grid.length; row++) {
      for (int col = 0; col < grid[row].length(); col++) {
        System.out.print((mark.contains(new RC(row,col)) ? grid[row].charAt(col) : '.') + " ");
      }
      System.out.println();
    }
    System.out.println();
    System.out.println(wordStr);
  }
}
