(ql:quickload '(:alexandria :serapeum))
(defpackage ac-02
  (:use :cl :alexandria :serapeum))
(in-package :ac-02)

(declaim (optimize speed))

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

(defparameter *payoff*
  #2A((3 6 0)
      (0 3 6)
      (6 0 3)))

(defun read-input-numeric (path)
  (mapcar (lambda (line)
	    (cons (- (char-code (aref line 0)) (char-code #\A))
		  (- (char-code (aref line 2)) (char-code #\X))))
	  (lines (read-file-into-string path))))

(defun score-round1-num (round)
  (+ (aref *payoff* (car round) (cdr round))
     (cdr round)
     1))

(defun solve1-num (strats)
  (sum (mapcar #'score-round1-num strats)))

(defun score-round2-num (round)
  (let* ((score (* 3 (cdr round)))
	 (move (do ((i 0 (1+ i)))
		   ((= (aref *payoff* (car round) i) score) i))))
    (+ score move 1)))

(defun solve2-num (strats)
  (sum (mapcar #'score-round2-num strats)))

