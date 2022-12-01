use std::collections::HashMap;

#[aoc_generator(day11)]
pub fn input_generator(input: &str) -> HashMap<(i32, i32), i32> {
    // 4341347643
    // 5477728451
    // 2322733878
    // 5453762556
    // 2718123421
    // 4237886115
    // 5631617114
    // 2217667227
    // 4236581255
    // 4482627641

    let mut map = HashMap::new();

    // parse each number into an x y coordinate
    for (y, line) in input.lines().enumerate() {
        for (x, num) in line.chars().enumerate() {
            let num = num.to_digit(10).unwrap() as i32;
            map.insert((x as i32, y as i32), num);
        }
    }

    map
}

#[aoc(day11, part1)]
pub fn solve_part1(input: &HashMap<(i32, i32), i32>) -> i32 {
    // The energy level of each octopus is a value between 0 and 9. Here, the
    // top-left octopus has an energy level of 5, the bottom-right one has an
    // energy level of 6, and so on.

    // You can model the energy levels and flashes of light in steps. During a
    // single step, the following occurs:

    // First, the energy level of each octopus increases by 1. Then, any octopus
    // with an energy level greater than 9 flashes. This increases the energy
    // level of all adjacent octopuses by 1, including octopuses that are
    // diagonally adjacent. If this causes an octopus to have an energy level
    // greater than 9, it also flashes. This process continues as long as new
    // octopuses keep having their energy level increased beyond 9. (An octopus
    // can only flash at most once per step.) Finally, any octopus that flashed
    // during this step has its energy level set to 0, as it used all of its
    // energy to flash.

    let mut map = input.clone();

    let mut flash_count = 0;
    for _ in 0..100 {
        // let mut new_map = HashMap::new();

        // Increase all values by 1
        for (_, v) in &mut map {
            *v += 1;
        }

        let mut some_flash = true;
        while some_flash {
            some_flash = false;

            for (coord, val) in &map.clone() {
                if val > &9 {
                    some_flash = true;

                    // Flash around
                    for x in coord.0 - 1..=coord.0 + 1 {
                        for y in coord.1 - 1..=coord.1 + 1 {
                            if x == coord.0 && y == coord.1 {
                                continue;
                            }
                            if let Some(neighbour_val) = map.get(&(x, y)) {
                                if *neighbour_val == 0 as i32 {
                                    continue;
                                }

                                // Increase map at that pos by 1
                                map.entry((x, y)).and_modify(|e| *e += 1);
                            }
                        }
                    }

                    flash_count += 1;

                    // Set self to 0
                    map.insert(*coord, 0);
                }
            }
        }
    }

    flash_count
}

#[aoc(day11, part2)]
pub fn solve_part2(input: &HashMap<(i32, i32), i32>) -> i32 {
    let mut map = input.clone();

    let mut flash_count = 0;
    for i in 0.. {
        // let mut new_map = HashMap::new();

        // Increase all values by 1
        for (_, v) in &mut map {
            *v += 1;
        }

        let mut some_flash = true;
        let mut count_flashes = 0;
        while some_flash {
            some_flash = false;

            for (coord, val) in &map.clone() {
                if val > &9 {
                    some_flash = true;

                    // Flash around
                    for x in coord.0 - 1..=coord.0 + 1 {
                        for y in coord.1 - 1..=coord.1 + 1 {
                            if x == coord.0 && y == coord.1 {
                                continue;
                            }
                            if let Some(neighbour_val) = map.get(&(x, y)) {
                                if *neighbour_val == 0 as i32 {
                                    continue;
                                }

                                // Increase map at that pos by 1
                                map.entry((x, y)).and_modify(|e| *e += 1);
                            }
                        }
                    }

                    count_flashes += 1;

                    // Set self to 0
                    map.insert(*coord, 0);
                }
            }
        }

        if count_flashes == map.len() {
            return i;
        }
    }

    flash_count
}
