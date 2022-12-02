use itertools::Itertools;

#[aoc(day2, part1)]
pub fn solve_part1(input: &str) -> i64 {
    let a = input
        .lines()
        .map(|line| {
            // Get the first letter and second letter A B
            let first = line.split(" ").nth(0).unwrap();
            let second = line.split(" ").nth(1).unwrap();

            (first, second)
        })
        .map(|(p1, p2)| {
            // A is rock, B is paper, C is scissors
            // X is rock, Y is paper, Z is scissors
            // Rock is worth 1, paper is worth 2, scissors is worth 3
            // A win is worth 6, draw is worth 3, loss is worth 0

            match (p1, p2) {
                ("A", "X") => 1 + 3,
                ("A", "Y") => 2 + 6,
                ("A", "Z") => 3 + 0,
                ("B", "X") => 1 + 0,
                ("B", "Y") => 2 + 3,
                ("B", "Z") => 3 + 6,
                ("C", "X") => 1 + 6,
                ("C", "Y") => 2 + 0,
                ("C", "Z") => 3 + 3,
                _ => 0,
            }
        })
        .sum();

    a
}

#[aoc(day2, part2)]
pub fn solve_part2(input: &str) -> i64 {
    let a = input
        .lines()
        .map(|line| {
            // Get the first letter and second letter A B
            let first = line.split(" ").nth(0).unwrap();
            let second = line.split(" ").nth(1).unwrap();

            (first, second)
        })
        .map(|(p1, p2)| {
            // A is rock, B is paper, C is scissors
            // X is lose, Y is draw, Z is win
            // Rock is worth 1, paper is worth 2, scissors is worth 3
            // A win is worth 6, draw is worth 3, loss is worth 0

            match (p1, p2) {
                ("A", "X") => 3 + 0,
                ("A", "Y") => 1 + 3,
                ("A", "Z") => 2 + 6,
                ("B", "X") => 1 + 0,
                ("B", "Y") => 2 + 3,
                ("B", "Z") => 3 + 6,
                ("C", "X") => 2 + 0,
                ("C", "Y") => 3 + 3,
                ("C", "Z") => 1 + 6,
                _ => 0,
            }
        })
        .sum();

    a
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
