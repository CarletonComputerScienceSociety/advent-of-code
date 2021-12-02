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

(define (parse-line line)
        (define (start)
                (string-trim (substring line 0 (string-index line #\space)) #\space))
        (define (end)
                (string->number (string-trim (substring line (string-index line #\space) (string-length line)))))
        (cond ((string=? (start) "forward") (list (end) 0 0))
              ((string=? (start) "down") (list 0 (end) 0))
              ((string=? (start) "up") (list 0 (- 0 (end)) 0))))

(define (part1 port)
        (fold (lambda (elem prev)
                       (list (+ (car elem) (car prev))
                             (+ (cadr elem) (cadr prev))))
         '(0 0)
         (map parse-line (read-file port))))

(define (part2 port)
        (fold (lambda (elem prev)
                       (list (+ (car elem) (car prev))
                             (+ (cadr elem) (cadr prev))
                             (+ (caddr prev) (* (cadr prev) (car elem)))))
         '(0 0 0)
         (map parse-line (read-file port))))
         
(display "Part1: \n\tHoriz: ")
(display (car (call-with-input-file "input" part1)))

(display "\n\tDepth: ")
(display (cadr (call-with-input-file "input" part1)))

(display "\nPart2: \n\tHoriz: ")
(display (car (call-with-input-file "input" part2)))

(display "\n\tDepth: ")
(display (caddr (call-with-input-file "input" part2)))
