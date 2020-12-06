require 'set'
file = File.open("input.txt").readlines.map(&:chomp)

def problemOne(list)
    built_strings = []
    current_string = ""
    
    list.each do |row|
        if row != ""
            current_string += row + "" 
        else
            built_strings << current_string
            current_string = ""
        end
    end

    built_strings << "knnknuk"

    sum_count = 0

    built_strings.each do |row|
        chars = row.split('').to_set
        sum_count += chars.length
    end

    sum_count
end

def problemTwo(list)
    built_strings = []
    current_string = ""
    group_size = 0

    list.each do |row|
        if row != ""
            current_string += row + "" 
            group_size += 1
        else
            built_strings << { current_string: current_string, group_size: group_size }
            current_string = ""
            group_size = 0
        end
    end

    built_strings << { current_string: "knnknuk", group_size: 3 }

    sum_count = 0

    def countLetters(s)
        Hash[s.delete(' ').split('').group_by{ |c| c }.map{ |k, v| [k, v.size] }]
    end

    built_strings.each do |row|
        letter_map = countLetters(row[:current_string])
        letter_map.values.each do |value|

            if row[:group_size] == value
                sum_count += 1
            end 
        end
    end

    sum_count
end

puts(problemOne(file))
puts(problemTwo(file))