use crate::day8::day8b;
use crate::day9::day9a;
use std::env;
use std::fs;
mod day8;
mod day9;

fn main() {
    let args: Vec<String> = env::args().collect();
    // plus 1 for the path of this file
    if args.len() < 3 {
        println!("Usage: provide a day and part as arguments. Like `cargo run -- 3 a`");
        return;
    }
    dbg!("{}", &args);
    let day: u32 = args[1]
        .parse()
        .expect("Please provide an integer Day to run");
    let part: char = args[2].parse().expect("Please specify a part 'a' or 'b'");
    let test: bool = args.len() >= 4 && args[3] == String::from("test");
    dbg!(test);
    match (day, part) {
        (8, 'a') => println!("No implementation found fgor 8a, I overwrote it with 8b."),
        (8, 'b') => day8b(read_lines(day, test)),
        (9, 'a') => day9a(read_lines(day, test)),
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
    let lines = contents.trim().split('\n').map(|s| s.to_string()).collect();
    lines
}
