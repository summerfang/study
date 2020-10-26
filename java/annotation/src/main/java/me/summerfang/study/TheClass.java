package me.summerfang.study;

public class TheClass {
    
    public int someData;

    public String doSomething(
        @MyAnnotation(name="someName", value="someValue") String str
    ) {
        return str;
    }
}
