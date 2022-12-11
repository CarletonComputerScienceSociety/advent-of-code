use std::{
    collections::{HashMap, HashSet},
    iter::FromIterator,
};

use itertools::Itertools;
use regex::Regex;

type InputType = Vec<Line>;

#[derive(Debug, Clone)]
pub enum Line {
    Command(Command),
    FileEntry(FileEntry),
}

#[derive(Debug, Clone)]
pub enum Command {
    Cd(String),
    Ls,
}

#[derive(Debug, Clone)]
pub enum FileEntry {
    Dir(String),
    File { size: i32, name: String },
}

#[aoc_generator(day7)]
fn parse_input_day7(input: &str) -> InputType {
    // Chars
    // input.chars().collect()

    // Map to ints
    // input.lines().map(|x| x.parse::<i32>().unwrap()).collect()

    // Regex
    input
        .lines()
        .map(|x| {
            // If the line starts with $, it's a command. There are 2 commands,
            // cd and ls. For example
            // $ cd /
            //
            // First, start by seeing if the line starts with $.

            if x.starts_with("$") {
                let line_split = x.split(" ").collect::<Vec<&str>>();

                // If it is length 2, it's an ls command.
                if line_split.len() == 2 {
                    Line::Command(Command::Ls)
                } else {
                    // Otherwise, it's a cd command.
                    Line::Command(Command::Cd(line_split[2].to_string()))
                }
            } else {
                // If the line starts with `dir`, then it's a directory.
                if x.starts_with("dir") {
                    Line::FileEntry(FileEntry::Dir(x[4..].to_string()))
                } else {
                    // Otherwise, it's a file.
                    let line_split = x.split(" ").collect::<Vec<&str>>();

                    Line::FileEntry(FileEntry::File {
                        size: line_split[0].parse::<i32>().unwrap(),
                        name: line_split[1].to_string(),
                    })
                }
            }
        })
        .collect()
}

#[derive(Debug, Clone)]
enum FileKind {
    Dir { name: String },
    File { size: i32 },
}

type FileTree = HashMap<String, (i32, Vec<FileKind>)>;

fn parse_file_tree(input: &InputType) -> FileTree {
    let mut file_tree: FileTree = HashMap::new();
    let mut directory_stack = vec!["".to_string()];

    for line in input {
        let curr_path = directory_stack.iter().join("/");

        match line {
            Line::Command(command) => match command {
                Command::Cd(dir) => {
                    match dir.as_str() {
                        // If the directory is /, then we're at the root.
                        "/" => {
                            directory_stack = vec!["".to_string()];
                        }
                        // If the directory is .., then we're going up a directory.
                        ".." => {
                            directory_stack.pop();
                        }
                        // Otherwise, we're going into a directory.
                        x => {
                            directory_stack.push(x.to_string());
                        }
                    }
                }
                Command::Ls => {}
            },
            Line::FileEntry(file_entry) => match file_entry {
                FileEntry::Dir(dir) => {
                    file_tree
                        .entry(curr_path)
                        .or_insert((0, vec![]))
                        .1
                        .push(FileKind::Dir { name: dir.clone() });
                }
                FileEntry::File { size, name: _ } => {
                    file_tree
                        .entry(curr_path)
                        .or_insert((0, vec![]))
                        .1
                        .push(FileKind::File { size: *size });
                }
            },
        }
    }

    file_tree
}

// Get the size of each directory through recursion
fn get_size(dir: &str, file_tree: &FileTree) -> i32 {
    let mut size = 0;
    for file in file_tree.get(dir).unwrap().1.clone() {
        match file {
            FileKind::Dir { name } => {
                let new_name = format!("{}/{}", dir, name);
                size += get_size(&new_name, &file_tree.clone());
            }
            FileKind::File { size: file_size } => {
                size += file_size;
            }
        }
    }

    size
}

#[aoc(day7, part1)]
pub fn solve_part1(input: &InputType) -> i32 {
    let mut file_tree = parse_file_tree(input);

    let file_tree_clone = file_tree.clone();

    // Go through each directory and set the size
    for (dir, files) in file_tree.iter_mut() {
        let size = get_size(dir, &file_tree_clone);

        files.0 = size;
    }

    // Find all the directories with size less or equal to 100_000, and sum
    // these
    file_tree
        .iter()
        .filter(|(_, (size, _))| *size <= 100_000)
        .map(|(_, (size, _))| size)
        .sum::<i32>()
}

#[aoc(day7, part2)]
pub fn solve_part2(input: &InputType) -> i32 {
    let mut file_tree = parse_file_tree(input);

    let file_tree_clone = file_tree.clone();

    // Go through each directory and set the size
    for (dir, files) in file_tree.iter_mut() {
        let size = get_size(dir, &file_tree_clone);

        files.0 = size;
    }

    let root_size = file_tree.get("").unwrap().0;

    let sizes = file_tree
        .iter()
        .filter(|(_, (size, _))| *size >= 30000000 - (70000000 - root_size))
        .map(|(_, (size, _))| size)
        .collect::<Vec<&i32>>();

    // Sort it
    let mut sorted_sizes = sizes.clone();
    sorted_sizes.sort();

    // Return the last item
    **sorted_sizes.first().unwrap()
}
