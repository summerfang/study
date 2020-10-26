package me.summerfang.study;

import java.io.IOException;
import java.text.ParseException;
import java.util.Date;

import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )  throws IOException, ParseException
    {
        User usr = new User("John", "Smith", new Date());
        ObjectMapper om = new ObjectMapper();
        String jsonStr = om.writerWithDefaultPrettyPrinter().writeValueAsString(usr);
        
        System.out.println(jsonStr);
    }
}
