(use-modules (srfi srfi-1))

(define (read-line port)
        (define (continue prev)
                (let ((next (read-char port)))
                     (if (or (eq? next #\newline) (eof-object? next))
                         prev
                         (continue (string-append prev (string next))))))
        (continue ""))

(define (read-file port)
        (define (continue l)
		        (if (eof-object? (peek-char port))
				    l
				    (continue (append l (list (read-line port))))))
		(continue (list (read-line port))))

(define input (map string->number (call-with-input-file "input" read-file)))

(define (part1 port) 
        (cadr (fold (lambda (elem prev) 
		                    (list elem
							      (if (> elem (car prev))
							          (+ 1 (cadr prev))
									  (cadr prev))))
                    '(99999999 0)
		            (map string->number (read-file port)))))

(define (triple l)
        (if (or (null? (cdr l))
		        (null? (cddr l)))
		    '()
			(cons (list (car l) (cadr l) (caddr l)) (triple (cdr l)))))

(define (sum l)
        (fold + 0 l))

(define (part2 port) 
        (cadr (fold (lambda (elem prev) 
		                    (list elem
							      (if (> (sum elem) (sum (car prev)))
							          (+ 1 (cadr prev))
									  (cadr prev))))
                    '((99999999 99999999 99999999) 0)
		            (triple (map string->number (read-file port))))))
					

(display "Part1: ")
(display (call-with-input-file "input" part1))
(newline)

(display "Part2: ")
(display (call-with-input-file "input" part2))
(newline)
