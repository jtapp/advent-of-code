use crate::day8::day8a;
use std::env;
use std::fs;
mod day8;

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
        (8, 'a') => day8a(read_lines(day, false)),
        _ => println!("No implementation found for day {day}{part}"),
    }
}

fn read_lines(day: u32, test: bool) -> Vec<String> {
    let path = match test {
        true => format!("../test_inputs/{day}.txt"),
        false => format!("../inputs/{day}.txt"),
    };
    dbg!(&path);
    let contents = fs::read_to_string(path).expect("Problem reading file");
    let lines = contents.split('\n').map(|s| s.to_string()).collect();
    lines
}
