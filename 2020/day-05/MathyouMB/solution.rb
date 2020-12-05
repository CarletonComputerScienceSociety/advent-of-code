file = File.open("input.txt").readlines.map(&:chomp)

def problemOne(list)
    
    max_id = 0

    list.each do |line|
        lower_bound_row = 0
        upper_bound_row = 127
        lower_bound_column = 0
        upper_bound_column = 7
        chars = line.split('')

        chars.each do |char|
            if char == 'F'
                upper_bound_row = ((upper_bound_row - lower_bound_row) / 2) + lower_bound_row
            elsif char == 'B'
                lower_bound_row = ((upper_bound_row - lower_bound_row) / 2) + 1 + lower_bound_row
            elsif char == 'L'
                upper_bound_column = ((upper_bound_column - lower_bound_column) / 2) + lower_bound_column
            elsif char == 'R'
                lower_bound_column = ((upper_bound_column - lower_bound_column) / 2) + 1 + lower_bound_column
            end
        end

        id = lower_bound_row * 8 + lower_bound_column
        if id > max_id
            max_id = id
        end
    end

    max_id
end

def problemTwo(list)
    
    max_id = 0
    id_list = []

    list.each do |line|
        lower_bound_row = 0
        upper_bound_row = 127
        lower_bound_column = 0
        upper_bound_column = 7
        chars = line.split('')

        chars.each do |char|
            if char == 'F'
                upper_bound_row = ((upper_bound_row - lower_bound_row) / 2) + lower_bound_row
            elsif char == 'B'
                lower_bound_row = ((upper_bound_row - lower_bound_row) / 2) + 1 + lower_bound_row
            elsif char == 'L'
                upper_bound_column = ((upper_bound_column - lower_bound_column) / 2) + lower_bound_column
            elsif char == 'R'
                lower_bound_column = ((upper_bound_column - lower_bound_column) / 2) + 1 + lower_bound_column
            end
        end

        id = lower_bound_row * 8 + lower_bound_column

        if id > max_id
            max_id = id
        end

        id_list << id
    end

    id_list = id_list.sort()
    for i in 1..id_list.length-1
        if (id_list[i] - id_list[i-1]) == 2
            return id_list[i]
        end
    end
end

puts(problemOne(file))
puts(problemTwo(file))