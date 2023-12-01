use itertools::Itertools;

#[aoc(day1, part1)]
pub fn solve_part1(input: &str) -> i32 {
    //     1abc2
    // pqr3stu8vwx
    // a1b2c3d4e5f
    // treb7uchet

    // Find the first and last digit in the string, put them into a single number,
    // and add all numbers together. Check if it's a number before converting
    input
        .lines()
        .map(|line| {
            dbg!(&line);
            let numbers = line.chars().filter_map(|c| c.to_digit(10)).collect_vec();
            dbg!(&numbers);
            // Combine the first and last number
            let first = numbers.first().unwrap();

            // If there is no last digit, use the first digit
            let last = numbers.last().unwrap();
            let combined = format!("{}{}", first, last).parse::<i32>().unwrap();

            combined
        })
        .sum::<i32>()
}

#[aoc(day1, part2)]
pub fn solve_part2(input: &str) -> i32 {
    // This time, sometimes the number might be spelled out. First, replace all
    // the occurances in strings

    // two1nine
    // eightwothree
    // abcone2threexyz
    // xtwone3four
    // 4nineeightseven2
    // zoneight234
    // 7pqrstsixteen
    input
        .lines()
        .map(|line| {
            dbg!(&line);

            // Change one to 1, two to 2, etc. This needs to be done with the
            // first occurance of any number being removed, not just the first
            // in the list. Use regex if needed
            let mut new_string = String::new();

            let mut first = 0;

            for char in line.chars() {
                new_string.push(char);

                // If it's a number, we found the first number
                if char.is_digit(10) {
                    first = char.to_digit(10).unwrap();
                    break;
                }

                // If we find any of the words, replace them with the number and
                // return
                if new_string.contains("one") {
                    first = 1;
                    break;
                } else if new_string.contains("two") {
                    first = 2;
                    break;
                } else if new_string.contains("three") {
                    first = 3;
                    break;
                } else if new_string.contains("four") {
                    first = 4;
                    break;
                } else if new_string.contains("five") {
                    first = 5;
                    break;
                } else if new_string.contains("six") {
                    first = 6;
                    break;
                } else if new_string.contains("seven") {
                    first = 7;
                    break;
                } else if new_string.contains("eight") {
                    first = 8;
                    break;
                } else if new_string.contains("nine") {
                    first = 9;
                    break;
                }
            }

            let mut last = -1;
            let mut new_string = String::new();
            for char in line.chars().rev() {
                new_string.insert(0, char);
                // If it's a number, we found the last number
                if char.is_digit(10) {
                    last = char.to_digit(10).unwrap() as i32;
                    break;
                }

                // If we find any of the words, replace them with the number and
                // return
                if new_string.contains("one") {
                    last = 1;
                    break;
                } else if new_string.contains("two") {
                    last = 2;
                    break;
                } else if new_string.contains("three") {
                    last = 3;
                    break;
                } else if new_string.contains("four") {
                    last = 4;
                    break;
                } else if new_string.contains("five") {
                    last = 5;
                    break;
                } else if new_string.contains("six") {
                    last = 6;
                    break;
                } else if new_string.contains("seven") {
                    last = 7;
                    break;
                } else if new_string.contains("eight") {
                    last = 8;
                    break;
                } else if new_string.contains("nine") {
                    last = 9;
                    break;
                }
            }

            // If there is no last digit, use the first digit
            let last = if last == -1 { first } else { last as u32 };
            let combined = format!("{}{}", first, last).parse::<i32>().unwrap();

            combined
        })
        .sum::<i32>()
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
