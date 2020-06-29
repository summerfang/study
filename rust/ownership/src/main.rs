fn main() {
    let s1 = String::from("Hello World!");
    let s2 = s1;
    // println!("s1={}", s1)


    let s3 = s2.clone();

    println!("s2={},s3={}", s2, s3);

    let s = String::from("Hello");

    takes_ownership(s);

    // println!("s={}",s);

    let x = 5;

    makes_copy(x);

    let str1 = give_ownership();
    println!("str1={}", str1);
    let str2 = String::from("Hello!");
    println!("str2={}", str2);
    let str3 = take_and_give_back(str2);
    println!("str3={}", str3);

    // println!("str1={}，str2={},str3={}", str1, str2,str3);

    let string1 = String::from("Hello!");

    let len = calc_len(&string1);
    println!("The length of {} is {}",string1, len);

    let ss1 = String::from("Word!!!");
    let mut ss2 = &ss1;
    let ss3 = ss1;
    ss2 = &ss3;
    println!("{}", ss2);

    let mut astr1 = String::from("A string");
    // let mut s = String::from("hello");

    let another_str = &mut astr1;
    // let r1 = &mut s;

    // println!("{}", another_str);
    // another_str.push_str("oob");
    // println!("{}", another_str);

    // let third_string = &mut astr1;
    // let r2 = &mut s;
    
    // println!("{}, {}", r1, r2);
    // println!("{}, {}", another_str, third_string);

    let r = dangle();
}

fn dangle() -> String {
    let s = String::from("Hello dangle");
    s
}

fn calc_len(s: &String)->usize {
    s.len()
}

fn takes_ownership(s: String){
    println!("{}", s)
}

fn makes_copy(i: i32) {
    println!("{}", i);
}


fn give_ownership() -> String {
    let s = String::from("hello");
    return s
}

fn take_and_give_back(s: String) -> String {
    s
}