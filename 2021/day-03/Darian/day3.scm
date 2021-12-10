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

(define (count v l)
        (if (null? l) 0
            (+ (if (eq? v (car l))
                   1 0)
               (count v (cdr l)))))

(define (most v1 v2 l)
        (if (> (count v1 l) (count v2 l))
            v1
            v2))

(define (least v1 v2 l)
        (if (< (count v1 l) (count v2 l))
            v1
            v2))

(define (bin->number l)
        (define (acc a j)
                (if (null? j) a
                    (acc (+ (* 2 a) (if (eq? (car j) #\1) 1 0)) (cdr j))))
        (acc 0 l))
            

(define (part1 input)
        (define in (rotate (map string->list input)))
        (define (gamma l)
                (if (null? l) '()
                    (cons (most #\1 #\0 (car l)) (gamma (cdr l)))))
        (define (epsilon l)
                (if (null? l) '()
                    (cons (least #\1 #\0 (car l)) (epsilon (cdr l)))))
        (* (bin->number (gamma in)) (bin->number (epsilon in))))


        
(define (part2 input)
        (define (oxy-filter n l)
                (filter (lambda (v) (eq? (get-elem n v) (most #\0 #\1 (get-elem n (rotate l))))) l))
        (define (co2-filter n l)
                (filter (lambda (v) (eq? (get-elem n v) (least #\1 #\0 (get-elem n (rotate l))))) l))
        (define (oxy input n)
                (if (null? (cdr input)) (car input)
                    (oxy (oxy-filter n input) (+ n 1))))
        (define (co2 input n)
                (if (null? (cdr input)) (car input)
                    (co2 (co2-filter n input) (+ n 1))))
        (* (bin->number (oxy (map string->list input) 0)) (bin->number (co2 (map string->list input) 0))))

(display "Part 1: ")
(display (part1 (call-with-input-file "input" read-file)))
(newline)
(display "Stand by for part 2 (takes a while)\n")
(display "Part 2: ")
(display (part2 (call-with-input-file "input" read-file)))
