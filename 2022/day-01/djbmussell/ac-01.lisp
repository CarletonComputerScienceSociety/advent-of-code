(ql:quickload '(:alexandria :serapeum))
(defpackage ac-01
  (:use :cl :alexandria :serapeum))
(in-package :ac-01)

(defun read-input (where)
  (split-sequence nil (mapcar (op (parse-integer _ :junk-allowed t))
			      (lines (read-file-into-string where)))))

(defun solve1 (food)
  (reduce #'max (mapcar #'sum food)))

(defun solve2 (food)
  (sum (subseq (sort (map 'vector #'sum food) #'>) 0 3)))
