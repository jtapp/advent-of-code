use crate::tree::Tree;
use std::env;
use std::fs;

pub mod tree;

fn main() {
    let args: Vec<String> = env::args().collect();
    // plus 1 for the path of this file
    if args.len() != 2 + 1 {
        println!("Usage: provide a day and part as arguments. Like `cargo run -- 3 a`");
        return;
    }
    dbg!("{}", &args);
    let day: u32 = args[1]
        .parse()
        .expect("Please provide an integer Day to run");
    let part: char = args[2].parse().expect("Please specify a part 'a' or 'b'");
    match (day, part) {
        (1, 'a') => day1a(),
        _ => println!("No implementation found for day {day}{part}"),
    }
}

fn day1a() {
    let path = "../inputs/1a.txt";
    let contents = fs::read_to_string(path).expect("Problem reading file");
    let mut lines = contents.split('\n');
    dbg!(lines.next());
}
