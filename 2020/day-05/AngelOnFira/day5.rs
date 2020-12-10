#[aoc(day5, part1)]
pub fn solve_part1(input: &str) -> i32 {
    input.lines().fold(0, |acc, pass| {
        let mut rows = (0, 127);
        let mut cols = (0, 7);

        for rule in pass.chars() {
            match rule {
                'F' => rows.1 = (rows.0 + rows.1) / 2,
                'B' => rows.0 = (rows.0 + rows.1) / 2 + 1,
                'R' => cols.0 = (cols.0 + cols.1) / 2 + 1,
                'L' => cols.1 = (cols.0 + cols.1) / 2,
                _ => unreachable!(),
            }
        }

        let seat = rows.0 * 8 + cols.0;
        if seat > acc {
            return seat;
        } else {
            acc
        }
    })
}

#[aoc(day5, part2)]
pub fn solve_part2(input: &str) -> i32 {
    let mut seat_chart = input
        .lines()
        .map(|pass| {
            let mut rows = (0, 127);
            let mut cols = (0, 7);

            for rule in pass.chars() {
                match rule {
                    'F' => rows.1 = (rows.0 + rows.1) / 2,
                    'B' => rows.0 = (rows.0 + rows.1) / 2 + 1,
                    'R' => cols.0 = (cols.0 + cols.1) / 2 + 1,
                    'L' => cols.1 = (cols.0 + cols.1) / 2,
                    _ => unreachable!(),
                }
            }

            rows.0 * 8 + cols.0
        })
        .collect::<Vec<i32>>();

    seat_chart.sort();

    let mut last_seat = 0;
    for seat in seat_chart.iter() {
        if seat - last_seat != 1 && last_seat != 0 {
            return *seat - 1;
        }
        last_seat = *seat;
    }
    unreachable!();
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
