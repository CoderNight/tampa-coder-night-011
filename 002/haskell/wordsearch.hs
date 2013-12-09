import System.Environment
import Data.List.Split
import Data.Char
import Data.List
search grid coords rc "" path = path
search grid coords rc@(row,col) (w:ws) path
  | not (rc `elem` coords) ||
    rc `elem` path ||
    not (w `elem` [grid!!row!!col, '?']) = []
  | otherwise = concat [ search grid coords (row+r,col+c) ws (rc:path) | r <- [-1..1], c <- [-1..1]]
main = do
  args <- getArgs
  str <- readFile (head args)
  let gridStr:wordStr:[] = splitOn "\n\n" str
  let grid = splitOn "\n" gridStr
  let trim = f . f where f = reverse . dropWhile isSpace
  let words = map (map toUpper . trim) $ splitOn "," wordStr
  let rclines = [[(row,col) | col <- [0..length (grid!!row) - 1]] | row <- [0..length grid - 1]]
  let coords = concat rclines
  let mark = concat $ map (\word -> concat $ map (\rc -> search grid coords rc word []) coords) words
  putStrLn $ concat . intersperse "\n" $
    map (\rcs -> intersperse ' ' $
    map (\rc@(row, col) -> if rc `elem` mark then grid!!row!!col else '.') rcs) rclines
