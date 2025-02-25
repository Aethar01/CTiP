use rand::{Rng, SeedableRng};
use rand_pcg::Pcg32;

pub fn run() {
    let numbers = one();
    let numbers1 = two();
    let cards = three();
    let tickets = four();
    let char = five();
    let strings = six();
    let password = seven();
    let dice = eight();

    println!("{:?}", numbers);
    println!("{:?}", numbers1);
    println!("{:?}", cards);
    println!("{:?}", tickets);
    println!("{:?}", char);
    println!("{:?}", strings);
    println!("{:?}", password);
    println!("{:?}", dice);
}

fn one() -> Vec<f64> {
    let mut rng = rand::rng();
    (0..100).map(|_| rng.random_range(0. ..1.)).collect()
}

fn two() -> Vec<i32> {
    let mut rng = rand::rng();
    let mut answers: i8 = 0;
    let mut numbers: Vec<i32> = Vec::new();
    while answers < 3 {
        let number = rng.random_range(1000..3500);
        if number % 3 == 0 {
            answers += 1;
            numbers.push(number);
        }
    }
    numbers.iter().for_each(|x| assert_eq!(x % 3, 0));
    numbers
}

#[derive(Debug)]
struct DebitCard {
    card_number: String,
    security_code: String
}

fn three() -> Vec<DebitCard> {
    // debit card number gen and security code
    let mut rng = rand::rng();
    let mut cards: Vec<DebitCard> = Vec::new();
    for _ in 0..3 {
        let card_number = (0..16).map(|_| rng.random_range(0..=9).to_string()).collect::<String>();
        let security_code = (0..3).map(|_| rng.random_range(0..=9).to_string()).collect::<String>();
        cards.push(DebitCard { card_number, security_code });
    }
    cards
}

#[derive(Debug)]
struct LotteryTicket {
    numbers: Vec<i32>
}

fn four() -> Vec<LotteryTicket> {
    let mut rng = rand::rng();
    let mut numbers: Vec<LotteryTicket> = Vec::new();
    for _ in 0..200 {
        let number = (0..6).map(|_| rng.random_range(0..=99)).collect();
        numbers.push(LotteryTicket { numbers: number });
    }
    numbers
}

fn five() -> char {
    let mut rng = rand::rng();
    let pool: Vec<char> = (0..100).map(|_| rng.random::<char>()).collect();
    pool[rng.random_range(0..pool.len())]
}

fn six() -> Vec<String> {
    let mut rng = rand::rng();
    let mut strings: Vec<String> = Vec::new();
    for _ in 0..5 {
        let string = (0..7).map(|_| rng.sample(rand::distr::Alphanumeric) as char).collect::<String>();
        strings.push(string);
    };
    strings.iter().for_each(|x| assert_eq!(x.len(), 7));
    strings
}

fn seven() -> String {
    let mut rng = rand::rng();
    let mut uppernumber = 0;
    let mut lowernumber = 0;
    let mut digit_num = 0;
    let mut special_num = 0;
    let upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let lower = "abcdefghijklmnopqrstuvwxyz";
    let digits = "0123456789";
    let specials = "!@#$%^&*()_+-=";
    // at least 2 upper 2 lower 2 digits 1 special
    // 10 characters
    let mut temp_pass = String::new();
    let mut flag = false;
    while !flag {
        temp_pass = (0..10).map(|_| {
            let choice = rng.random_range(0..4);
            match choice {
                0 => {
                    uppernumber += 1;
                    upper.chars().nth(rng.random_range(0..upper.len())).unwrap()
                },
                1 => {
                    lowernumber += 1;
                    lower.chars().nth(rng.random_range(0..lower.len())).unwrap()
                },
                2 => {
                    digit_num += 1;
                    digits.chars().nth(rng.random_range(0..digits.len())).unwrap()
                },
                3 => {
                    special_num += 1;
                    specials.chars().nth(rng.random_range(0..specials.len())).unwrap()
                },
                _ => panic!("Invalid choice")
            }
        }).collect();
        if uppernumber >= 2 && lowernumber >= 2 && digit_num >= 2 && special_num >= 1 {
            flag = true;
        }
    }

    temp_pass
}

fn eight() -> i32 {
    // dice rolls same every time
    let mut rng = Pcg32::seed_from_u64(0u64);
    let roll = rng.random_range(1..=6);
    roll
}
