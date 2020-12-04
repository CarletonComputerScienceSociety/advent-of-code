#[aoc(day3, part1)]
pub fn solve_part1(input: &str) -> i32 {
    let hill: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();
    let mut x: i32 = 0;
    let mut y: i32 = 0;

    let width = hill.get(0).unwrap().len();

    let mut counter = 0;

    while y < (hill.len() as i32) {
        if *hill
            .get(y as usize)
            .unwrap()
            .get((x as usize) % width)
            .unwrap()
            == '#'
        {
            counter += 1;
        }
        x += 3;
        y += 1;
    }

    counter
}

#[aoc(day3, part2)]
pub fn solve_part2(input: &str) -> i32 {
    let hill: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();
    let width = hill.get(0).unwrap().len();

    let slopes = vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];

    slopes
        .iter()
        .map(|slope| {
            let mut x: i32 = 0;
            let mut y: i32 = 0;

            let mut counter = 0;

            while y < (hill.len() as i32) {
                if *hill
                    .get(y as usize)
                    .unwrap()
                    .get((x as usize) % width)
                    .unwrap()
                    == '#'
                {
                    counter += 1;
                }
                x += slope.0;
                y += slope.1;
            }

            counter
        })
        .product()
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
