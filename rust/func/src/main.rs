fn main() {
    println!("Hello, world!");
    another_func();
    second_func(10, 20);

    let x = 5;

    let y = {
        let x = 3;
        x + 1
    };

    println!("x={}", x);
    println!("y={}", y);

    fn five() -> f32 {
        5.0
    }

    println!("five()={}", five());

    let number = 3;

    if number < 5 {
        println!("It is true");
    } else {
        println!("It is false");
    }

    let a = 12;
    let b;
    if a > 0 {
        b = 1;
    }
    else if a < 0 {
        b = -1;
    }
    else {
        b = 0;
    }

    println!("b is {}", b);

    let a = 3;

    let number = if a > 0 {1} else {-1};
    println!("number is {}", number);
}

fn another_func() {
    println!("Hello, runoob!")
}

fn second_func(x: i32, y:i32) {
    println!("x={}", x);
    println!("y={}", y);
}