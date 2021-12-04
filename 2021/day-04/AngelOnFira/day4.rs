use regex::Regex;

#[derive(Debug, Clone)]
pub struct Game {
    pub draws: Vec<i32>,
    pub boards: Vec<Board>,
}

#[derive(Debug, Clone)]
pub struct Board {
    pub numbers: Vec<i32>,
}

impl Board {
    // Check if the board has won bingo
    pub fn winner(self, draws: Vec<i32>) -> bool {
        let mut check = [0; 25];

        for draw in draws {
            if let Some(i) = self.numbers.iter().position(|&x| x == draw) {
                check[i] = 1;
            }
        }

        // Check if any horizontal line has won
        for i in 0..5 {
            if check[i * 5] == 1
                && check[i * 5 + 1] == 1
                && check[i * 5 + 2] == 1
                && check[i * 5 + 3] == 1
                && check[i * 5 + 4] == 1
            {
                return true;
            }
        }

        // Check if any vertical line has won
        for i in 0..5 {
            if check[i] == 1
                && check[i + 5] == 1
                && check[i + 10] == 1
                && check[i + 15] == 1
                && check[i + 20] == 1
            {
                return true;
            }
        }

        false
    }

    pub fn sum_of_unmarked_numbers(self, draws: Vec<i32>) -> i32 {
        self.numbers.iter().filter(|&x| !draws.contains(x)).sum()
    }
}

#[aoc_generator(day4)]
pub fn input_generator(input: &str) -> Game {
    // Numbers
    let draws: Vec<i32> = input
        .lines()
        .next()
        .unwrap()
        .split(',')
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    let lines = input
        .lines()
        .map(|x| x.to_string())
        .collect::<Vec<String>>();

    // 30 99 16 34 42
    // 94 39 83 78 49
    // 57 81 97 77 52
    //  9 61 98 11 89
    // 85  1 60 90 55

    // Parse the boards

    let mut boards: Vec<Board> = Vec::new();

    let mut counter = 0;
    let mut curr_board = Vec::new();

    for line in &lines[1..] {
        if line == "" {
            continue;
        }

        if counter % 5 == 0 && counter != 0 {
            counter = 0;
            boards.push(Board {
                numbers: curr_board.clone(),
            });

            curr_board = Vec::new();
        }

        counter += 1;

        let re = Regex::new(r"^[ ]*(\d+)[ ]+(\d+)[ ]+(\d+)[ ]+(\d+)[ ]+(\d+)$").unwrap();
        let caps = re.captures(&line).unwrap();
        for cap in caps.iter().skip(1) {
            curr_board.push(cap.unwrap().as_str().parse::<i32>().unwrap());
        }
    }

    boards.push(Board {
        numbers: curr_board.clone(),
    });

    Game {
        draws: draws,
        boards: boards,
    }
}

#[aoc(day4, part1)]
pub fn solve_part1(input: &Game) -> i32 {
    for i in 0..input.draws.len() {
        match input
            .boards
            .iter()
            .filter_map(|board| {
                if board.clone().winner(input.draws[..=i].to_vec()) {
                    return Some(
                        board
                            .clone()
                            .sum_of_unmarked_numbers(input.draws[..=i].to_vec())
                            * input.draws[i],
                    );
                }
                None
            })
            .next()
        {
            Some(x) => return x,
            None => continue,
        }
    }
    unreachable!()
}

#[aoc(day4, part2)]
pub fn solve_part2(input: &Game) -> i32 {
    let mut curr_boards = input.boards.clone();
    let mut winning_board = None;

    for i in 0..input.draws.len() {
        let new_boards = curr_boards
            .iter()
            .filter_map(|board| {
                if board.clone().winner(input.draws[..=i].to_vec()) {
                    return None;
                }
                Some(board.clone())
            })
            .map(|board| board.clone())
            .collect::<Vec<Board>>();

        if new_boards.len() == 1 {
            winning_board = Some(new_boards[0].clone());
        }

        if new_boards.len() == 0 {
            return winning_board
                .clone()
                .unwrap()
                .clone()
                .sum_of_unmarked_numbers(input.draws[..=i].to_vec())
                * input.draws[i];
        }

        curr_boards = new_boards;
    }
    unreachable!()
}
