var mark = [];
var grid;

function in_path(path, row, col) {
  for (var i = 0; i < path.length; i++) {
    if (path[i].row == row &&
        path[i].col == col) {
      return true;
    }
  }
  return false;
}

function search(row, col, word, path) {
  if (word=="") {
    path.forEach(function(e) {
      mark[e.row][e.col] = true;
    });
  } else if (0 <= row && row < grid.length &&
             0 <= col && col < grid[row].length &&
             !in_path(path, row, col) &&
             (word[0] == grid[row][col] || word[0] == '?')) {
    for (var r = -1; r <= 1; r++) {
      for (var c = -1; c <= 1; c++) {
        search(row+r, col+c, word.substr(1), path.concat({row: row, col: col}));
      }
    }
  }
}
window.onload = function() {
  var data=document.getElementById("data").value.split("\n\n");
  grid=data[0].split("\n");
  var words=data[1].split(",").map(function(w) {return w.toUpperCase().trim();});
  for (var i = 0; i < grid.length; i++) {
    mark[i] = [];
  }

  words.forEach(function(word) {
    for (var row = 0; row < grid.length; row++) {
      for (var col = 0; col < grid[row].length; col++) {
        search(row, col, word, []);
      }
    }
  });

  document.write("<table border='1'>");
  for (var row = 0; row < grid.length; row++) {
    document.write("<tr>");
    for (var col = 0; col < grid[row].length; col++) {
      var color = mark[row][col] ? "yellow" : "white";
      document.write("<td align='center' bgcolor='"+color+"'>" + grid[row][col] + "</td>");
    }
    document.write("</tr>");
  }
  document.write("</table>");

  document.write(words);
}
