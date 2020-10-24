package me.summerfang.study;

//import org.json.simple.JSONObject;
import org.json.*;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        JSONObject obj = new JSONObject();

        obj.put("name", "foo");
        obj.put("sex", "female");

        System.out.println(obj);    }
}
