package me.summerfang.study;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

public class HelloTest {
    private Hello hello;

    @Before
    public void Prepare() {
        hello = new Hello();
    }

    @Test
    public void testAdd() {
        assertEquals(hello.add(1,1), 2);
    }

}
