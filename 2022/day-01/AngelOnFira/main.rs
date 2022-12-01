use itertools::Itertools;

#[aoc(day1, part1)]
pub fn solve_part1(input: &str) -> i32 {
*input
    .lines()
    .fold((Vec::new(), 0), |(mut acc, counter), line| {
        match line.parse::<i32>() {
            Ok(num) => (acc, counter + num),
            Err(_) => {
                acc.push(counter);
                (acc, 0)
            }
        }
    })
    .0
    .iter()
    .sorted()
    .rev()
    .next()
    .unwrap()
}

#[aoc(day1, part2)]
pub fn solve_part2(input: &str) -> i32 {
    input
        .lines()
        .fold((Vec::new(), 0), |(mut acc, counter), line| {
            match line.parse::<i32>() {
                Ok(num) => (acc, counter + num),
                Err(_) => {
                    acc.push(counter);
                    (acc, 0)
                }
            }
        })
        .0
        .iter()
        .sorted()
        .rev()
        .take(3)
        .sum::<i32>()
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
