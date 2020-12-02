file = File.open("input.txt").readlines.map(&:chomp)

def problemOne(list)
    valid_passwords = 0

    list.each do |line|
        
        first_num = line[0..line.index('-')-1].to_i
        second_num = line[line.index('-')+1..line.index(' ')-1].to_i
        character = line[line.index(':')-1]
        password = line[line.index(':')+2..line.length]
        
        char_count = 0

        password.split('').each do |char|
            if char == character
                char_count+=1
            end
        end

        if (char_count >= first_num && char_count <= second_num)
            valid_passwords +=1
        end

    end

    valid_passwords
end

def problemTwo(list)
    valid_passwords = 0

    list.each do |line|
        
        first_num = line[0..line.index('-')-1].to_i
        second_num = line[line.index('-')+1..line.index(' ')-1].to_i
        character = line[line.index(':')-1]
        password = line[line.index(':')+2..line.length]
        
        if (password[first_num-1] != character)
            if( password[second_num-1] == character)
                valid_passwords +=1
            end
        else
            if( password[second_num-1] != character)
                valid_passwords +=1
            end
        end
    end

    valid_passwords
end

puts(problemOne(file))
puts(problemTwo(file))
