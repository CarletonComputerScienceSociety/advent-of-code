(ql:quickload '(:alexandria :serapeum :cl-ppcre))
(defpackage ac-02
  (:use :cl :alexandria :serapeum)
  (:local-nicknames (:re :cl-ppcre)))
(in-package :ac-02)

(defun read-input (path)
  (mapcar (lambda (line)
	    (cons (intern (subseq line 0 1)) (intern (subseq line 2 3))))
	  (lines (read-file-into-string path))))

(defun score-round1 (round)
  (case (car round)
    (a (case (cdr round) ;; Rock
	 (x (+ 1 3)) ;; Rock
	 (y (+ 2 6)) ;; Paper 
	 (z (+ 3 0)))) ;; Scissors
    (b (case (cdr round) ;; Paper
	 (x (+ 1 0)) ;; Rock
	 (y (+ 2 3)) ;; Paper 
	 (z (+ 3 6)))) ;; Scissors
    (c (case (cdr round) ;; Scissors
	 (x (+ 1 6)) ;; Rock
	 (y (+ 2 0)) ;; Paper 
	 (z (+ 3 3)))) ;; Scissors
    ))

(defun solve1 (strats)
  (sum (mapcar #'score-round1 strats)))

(defun score-round2 (round)
  (case (car round)
    (a (case (cdr round) ;; Rock
	 (x (+ 3 0)) ;; Lose
	 (y (+ 1 3)) ;; Draw
	 (z (+ 2 6)))) ;; Win
    (b (case (cdr round) ;; Paper
	 (x (+ 1 0)) ;; Lose
	 (y (+ 2 3)) ;; Draw
	 (z (+ 3 6)))) ;; Win
    (c (case (cdr round) ;; Scissors
	 (x (+ 2 0)) ;; Lose
	 (y (+ 3 3)) ;; Draw
	 (z (+ 1 6)))) ;; Win
    ))

(defun solve2 (strats)
  (sum (mapcar #'score-round2 strats)))

