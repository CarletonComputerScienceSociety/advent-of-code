file = File.open("input.txt").readlines.map(&:chomp)

def problemOne(list)
    position = 0
    tree_count = 0

    list.each do |row|
        if (row[position] == "#")
            tree_count +=1
        end

        position +=3

        if(position > row.length-1)
            position = (position % row.length)
        end
    end

    tree_count
end

def problemTwo(list)
    def treeHitCount(right, down, list)
        position = 0
        tree_count = 0
        i = 0

        while i < list.length
            if (list[i][position] == "#")
                tree_count +=1
            end

            position += right

            if(position > list[i].length-1)
                position = (position % list[i].length)
            end

            i+=down
        end

        tree_count

    end
    
    treeHitCount(1, 1, list) * treeHitCount(3, 1, list) * treeHitCount(5, 1, list) * treeHitCount(7, 1, list) * treeHitCount(1, 2, list)
end

puts(problemOne(file))
puts(problemTwo(file))