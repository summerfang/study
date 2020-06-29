fn main() {
    let s = String::from("Hello World!");

    let part1 = &s[..5];
    let part2 = &s[5..];

    println!("{}={}+{}",s,part1,part2);

    let s1 = String::from("Hello World!");
    let slice = &s[0..3];
    // s.push_str("Yes!");
    println!("slice={}", slice);

    let str1 = String::from("Hello World!");
    let str2 = &str1[..];

    let arr = [1,3,5,7,9];
    let part = &arr[0..3];

    for i in part.iter(){
        println!("{}", i);
    }
}
