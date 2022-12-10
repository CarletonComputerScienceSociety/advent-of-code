use std::{fs::File, io::{BufReader, BufRead}, collections::VecDeque, iter};

fn read_input(source: String) -> Vec<String> {
    let file = File::open(source).expect("No such file");
    let buf = BufReader::new(file);
    buf.lines()
       .map(|l| l.expect("Could not parse line"))
       .collect()
}

fn part1 (input: &Vec<String>) -> String {
    // Don't like this magic number 9 nonsense, but it's easier than searching
    let mut tables: Vec<VecDeque<char>> = iter::repeat_with(|| VecDeque::new())
                                                  .take(9)
                                                  .collect();
    let mut finished_table: bool = false;
    input.into_iter()
          .for_each(|l| {
              if l == "" {
                  return;
              }
              if !finished_table {
                  if l.starts_with(" 1") {
                      finished_table = true;
                      return;
                  }
                  let temp_string = l.clone();
                  let temp = temp_string.as_bytes();
                  let mut _i = 0;
                  while _i < temp.len() + 1 {
                      if temp[_i+1] != ' ' as u8 {
                          tables[_i/4].push_back(temp[_i+1].into());
                      }

                      _i += 4;
                  }
              }
              if l.starts_with("move") {
                  let split: Vec<&str> = l.split(" ").collect();
                  let iter_val = split[1].parse::<usize>().unwrap();
                  let src:usize = split[3].parse::<usize>().unwrap();
                  let dest:usize = split[5].parse::<usize>().unwrap();

                  for _ in 0..iter_val {
                      match tables[src-1].pop_front() {
                          Some(s) => tables[dest-1].push_front(s),
                          None => continue,
                      };
                  }
              }
          });

    return tables.into_iter()
                 .filter_map(|mut e| e.pop_front())
                 .collect();
}

fn part2(input: &Vec<String>) -> String {
    // Don't like this magic number 9 nonsense, but it's easier than searching
    let mut tables: Vec<VecDeque<char>> = iter::repeat_with(|| VecDeque::new())
                                                  .take(9)
                                                  .collect();
    let mut finished_table: bool = false;
    input.into_iter()
          .for_each(|l| {
              if l == "" {
                  return;
              }
              if !finished_table {
                  if l.starts_with(" 1") {
                      finished_table = true;
                      return;
                  }
                  let temp_string = l.clone();
                  let temp = temp_string.as_bytes();
                  let mut _i = 0;
                  while _i < temp.len() + 1 {
                      if temp[_i+1] != ' ' as u8 {
                          tables[_i/4].push_back(temp[_i+1].into());
                      }

                      _i += 4;
                  }
              }
              if l.starts_with("move") {
                  let split: Vec<&str> = l.split(" ").collect();
                  let iter_val = split[1].parse::<usize>().unwrap();
                  let src:usize = split[3].parse::<usize>().unwrap();
                  let dest:usize = split[5].parse::<usize>().unwrap();

                  let mut buffer: VecDeque<char> = VecDeque::new();

                  for _ in 0..iter_val {
                      match tables[src-1].pop_front() {
                          Some(s) => buffer.push_front(s),
                          None => continue,
                      };
                  }
                  buffer.into_iter().for_each(|c| tables[dest-1].push_front(c));
              }
          });

    return tables.into_iter()
                 .filter_map(|mut e| e.pop_front())
                 .collect();
}

fn main() {
    let data = read_input("input".to_owned());

    let p1 = part1(&data);
    let p2 = part2(&data);

    print!("Part1 = {}\n", p1);
    print!("Part2 = {}\n", p2);
}

