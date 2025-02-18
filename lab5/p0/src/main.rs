use clap::Parser;
mod p1;

#[derive(Parser)]
struct Args {
    #[clap(short, long)]
    problem_number: i32
}

fn main() {
    match Args::parse().problem_number {
        1 => p1::run(),
        _ => println!("Problem not found")
    }
}
