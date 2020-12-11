use itertools::Itertools;

#[aoc_generator(day9)]
fn parse_input_day9(input: &str) -> Vec<i64> {
    input.lines().map(|x| x.parse::<i64>().unwrap()).collect()
}

#[aoc(day9, part1)]
pub fn solve_part1(input: &Vec<i64>) -> i64 {
    const PREAMBLE_LEN: usize = 25;
    for (i, window) in input.windows(PREAMBLE_LEN).enumerate() {
        if !window
            .iter()
            .combinations(2)
            .any(|comb| comb[0] + comb[1] == input[i + PREAMBLE_LEN])
        {
            return input[i + PREAMBLE_LEN];
        }
    }
    unreachable!();
}

#[aoc(day9, part2)]
pub fn solve_part2(input: &Vec<i64>) -> i64 {
    const GOAL: i64 = 15353384;
    for i in 0..input.len() {
        let mut total = 0;
        let mut range_edge = (-1, -1);
        for j in i..input.len() {
            let value = input[j];
            total += value;
            if value > range_edge.0 {
                range_edge.0 = value;
            }
            if value < range_edge.1 || range_edge.1 == -1 {
                range_edge.1 = value;
            }
            if total == GOAL {
                return range_edge.0 + range_edge.1;
            }
        }
    }
    unreachable!();
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
