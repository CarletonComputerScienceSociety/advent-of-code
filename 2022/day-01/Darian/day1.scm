(use-modules (srfi srfi-1))

(define (empty-string? s)
        (= (string-length s) 0))

(define (read-line port)
        (define (continue prev)
                (let ((next (read-char port)))
                     (if (or (eq? next #\newline) (eof-object? next))
                         prev
                         (continue (string-append prev (string next))))))
        (continue ""))

(define (read-elf port)
        (define (continue)
                (let ((next (read-line port)))
                     (if (empty-string? next)
                         0
                         (+ (continue) (string->number next)))))
        (continue))

(define (read-elves port)
        (if (eof-object? (peek-char port)) '()
            (cons (read-elf port) (read-elves port))))

(define (max a b) (if (> a b) a b))

(define (part1 port)
        (fold max 0 (read-elves port)))

(define (add-3 l)
        (+ (car l) (cadr l) (caddr l)))

(define (part2 port)
        (add-3 (sort (read-elves port) >)))

(display (call-with-input-file "input" part1))
(newline)
(display (call-with-input-file "input" part2))
