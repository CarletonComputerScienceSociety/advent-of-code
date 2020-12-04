require 'set'
file = File.open("input.txt").readlines.map(&:chomp)


def problemOne(list)
    built_strings = []
    current_string = ""
    list.each do |row|
        if row != ""
            current_string += row + " " 
        else
            built_strings << current_string
            current_string = ""
        end
    end

    def isValidPassport(row)
        (row.include?("byr:")) && (row.include?("iyr:")) && (row.include?("eyr:")) && (row.include?("hgt:")) && (row.include?("hcl:")) && (row.include?("ecl:")) && (row.include?("pid:")) # && (row.include?("cid")
    end

    valid_passports = 0

    built_strings.each do |row|
        if isValidPassport(row)
            valid_passports += 1
        end
    end

    valid_passports
end

def problemTwo(list)
    built_strings = []
    current_string = ""
    list.each do |row|
        if row != ""
            current_string += row + " " 
        else
            built_strings << current_string
            current_string = ""
        end
    end

    def hasRightKeys(row)
        (row.include?("byr:")) && (row.include?("iyr:")) && (row.include?("eyr:")) && (row.include?("hgt:")) && (row.include?("hcl:")) && (row.include?("ecl:")) && (row.include?("pid:")) # && (row.include?("cid")
    end

    def parsePassword(row)
        password = {}
        list = row.split(" ")
        list.each do |entry|
            password[entry[0..entry.index(':')-1]] = entry[entry.index(':')+1..entry.length-1]
        end
        password
    end

    def isValidPassword(password)
        if password.has_key? "byr"
            if password["byr"].to_i > 2002 || password["byr"].to_i < 1920
                return false
            end
        end

        if password.has_key? "iyr"
            if password["iyr"].to_i < 2010 || password["iyr"].to_i > 2020
                return false
            end
        end

        if password.has_key? "eyr"
            if password["eyr"].to_i < 2020 || password["eyr"].to_i > 2030
                return false
            end
        end

        if password.has_key? "hgt"
            if password["hgt"].include? "in"
                digit = password["hgt"][0..password["hgt"].index('in')-1].to_i
                if digit < 59 || digit > 76
                    return false
                end
            end

            if password["hgt"].include? "cm"
                digit = password["hgt"][0..password["hgt"].index('cm')-1].to_i
                if digit < 150 || digit > 193
                    return false
                end
            end
        end

        if password.has_key? "hcl"
            chars = password["hcl"].split('')
            if chars[0] != "#"
                return false
            end

            chars.each do |char|
                if !("#1234567890abcdef".include? char)
                    return false
                end
            end
        end

        if password.has_key? "ecl"
            set = Set["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if !(set.include? password["ecl"])
                return false
            end
        end

        if password.has_key? "pid"
            chars = password["pid"].split('')
            if chars.length > 9
                return false
            end

            chars.each do |char|
                if !("1234567890".include? char)
                    return false
                end
            end
        end

        true
    end

    valid_passports = 0

    built_strings.each do |row|
        if hasRightKeys(row) 
            if isValidPassword(parsePassword(row))
                valid_passports += 1
            end
        end
    end

    valid_passports
end

puts(problemOne(file))
puts(problemTwo(file))