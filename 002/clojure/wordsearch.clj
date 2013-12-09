(ns wordsearch
  (:require [clojure.string :refer [join split upper-case trim]]))

(defn search [grid rc word path]
  (cond (empty? word) path
        (or (some #{rc} path)
            (not (some #{rc} (keys grid)))
            (not (some #{\? (grid rc)} [(first word)]))) []
        :else (apply concat
                     (for [r [-1 0 1]
                           c [-1 0 1]]
                       (search grid [(+ r (first rc)) (+ c(second rc))] (rest word)
                               (cons rc path))))))

(let [[grid-s word-s] (split (upper-case(slurp (first *command-line-args*))) #"\n\n")
      gridline (map-indexed (fn [row line] (map-indexed (fn [col ch] [[row col] ch]) line))
                            (split grid-s #"\n"))
      grid (into {} (apply concat gridline))
      mark (apply concat (for [word (map trim (split word-s #","))
                               rc (keys grid)]
                           (search grid rc word [])))]
  (println (join "\n" (map (fn [line]
                             (join " " (map (fn [[rc ch]] (if (some #{rc} mark) ch '.))
                                                     line))) gridline))))
