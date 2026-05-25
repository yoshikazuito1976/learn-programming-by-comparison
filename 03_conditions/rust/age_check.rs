// age_check.rs
// Rust: 標準入力と条件分岐

use std::io;

fn main() {
    println!("年齢を入力してください: ");

    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("入力の読み取りに失敗しました");

    let age: i32 = input
        .trim()
        .parse()
        .expect("数値を入力してください");

    if age >= 20 {
        println!("成人です");
    } else {
        println!("未成年です");
    }
}