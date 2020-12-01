require 'set'
file = File.open("problem1.txt").readlines.map(&:chomp).map(&:to_i)

def problemOne(list)
    input_set = list.to_set
    answer = -1

    list.each do |number|
        input_set.add(number)
        if input_set.include?(2020-number)
            answer = number * (2020-number)
            break
        end
    end

    answer
end

def problemTwo(list)

    input_set = list.to_set
    answer = -1
    
    list.each do |i|
        list.each do |j|
            if input_set.include?(2020-(i+j))
                answer = i * j * (2020-(i+j))
                break
            end
        end
    end

    answer
end

puts(problemOne(file))
puts(problemTwo(file))
