(use-modules (srfi srfi-1))

(define (read-line port)
        (define (continue prev)
                (let ((next (read-char port)))
                     (if (or (eq? next #\newline) (eof-object? next))
                         prev
                         (continue (string-append prev (string next))))))
        (continue ""))

(define (read-board port)
        (let ((x (list (filter number? (map string->number (string-split (read-line port) #\space)))
                       (filter number? (map string->number (string-split (read-line port) #\space)))
                       (filter number? (map string->number (string-split (read-line port) #\space)))
                       (filter number? (map string->number (string-split (read-line port) #\space)))
                       (filter number? (map string->number (string-split (read-line port) #\space))))))
              (begin (read-line port) x)))

(define (get-elem n l)
        (if (null? l) '()
            (if (= n 0)
                (car l)
                (get-elem (- n 1) (cdr l)))))

(define (rotate l)
        (define (get-elems n l)
                (if (null? l)
                    l
                    (cons (get-elem n (car l)) (get-elems n (cdr l)))))
        (define (rot n l)
                (if (null? (get-elem n (car l)))
                    '()
                    (append (list (get-elems n l)) (rot (+ n 1) l))))
        (rot 0 l))

(define (in? e l)
        (if (null? l) #f
            (or (eq? e (car l)) (in? e (cdr l)))))

(define (all-in? l1 l2)
        (if (null? l1) #t
            (and (in? (car l1) l2) (all-in? (cdr l1) l2))))

(define (won? board calls)
        (define (won-hori? board calls)
                (if (null? board) #f
                    (or (all-in? (car board) calls) (won-hori? (cdr board) calls))))
        (define (won-vert? board calls)
                (won-hori? (rotate board) calls))
        (define (won-diag-a? board calls)
                (all-in? (list (car (car board))
                               (cadr (cadr board))
                               (caddr (caddr board))
                               (cadddr (cadddr board))
                               (cadddr (cdr (cadddr (cdr board))))) ;I can't believe I ran out of cadr
                         calls))
        (define (won-diag-b? board calls)
                (won-diag-a? (rotate board) calls))
        (or (won-hori? board calls)
            (won-vert? board calls)
            (won-diag-a? board calls)
            (won-diag-b? board calls)))

(define (winner boards calls)
        (if (null? boards) '()
            (if (won? (car boards) calls) (car boards)
                (winner (cdr boards) calls))))

(define (winners boards calls)
        (filter (lambda (board) (won? board calls)) boards))

(define (first-winner boards calls)
        (define (rev boards calls)
                (if (null? calls) '(())
                    (let ((result (rev boards (cdr calls))))
                         (if (null? (car result))
                             (list (winner boards calls) (reverse calls))
                             result))))
        (rev boards (reverse calls)))

(define (any? f l)
        (if (null? l) #f
            (or (f (car l)) (any f (cdr l)))))

(define (all-winners boards calls)
        (define (rev boards calls)
                (if (null? calls) '()
                    (let ((wins (map (lambda (win) (list win (reverse calls))) (winners boards calls))) (oldwins (rev boards (cdr calls))))
                         (append (filter (lambda (win) (not (any (lambda (oldwin) (eq? (car win) (car oldwin))) oldwins))) wins) oldwins))))
                         
        (rev boards (reverse calls)))

(define (read-boards port)
        (if (eof-object? (peek-char port)) '()
            (cons (read-board port) (read-boards port))))

(define (not-in l1 l2)
        (if (null? l1) l1
            (if (in? (car l1) l2)
                (not-in (cdr l1) l2)
                (cons (car l1) (not-in (cdr l1) l2)))))

(define (last l)
        (if (null? l) '()
            (if (null? (cdr l)) (car l)
                (last (cdr l)))))

(define (score board calls)
        (define (board-sum board calls)
                (if (null? board) 0
                    (+ (fold + 0 (not-in (car board) calls)) (board-sum (cdr board) calls))))
        (* (board-sum board calls) (last calls)))

(define (part1 input)
        (let ((calls (map string->number (string-split (read-line input) #\,))) (boards (begin (read-line input) (read-boards input))))
             (let ((results (first-winner boards calls)))
                  (score (car results) (cadr results)))))

(define (part2 input)
        (let ((calls (map string->number (string-split (read-line input) #\,))) (boards (begin (read-line input) (read-boards input))))
             (let ((results (all-winners boards calls)))
                  (score (car (car results)) (cadr (car results))))))

(display "Part 1: ")
(display (call-with-input-file "input" part1))
(newline)
(display "Part 2: ")
(display (call-with-input-file "input" part2))
        
