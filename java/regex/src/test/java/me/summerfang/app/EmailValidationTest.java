package me.summerfang.app;
import java.util.HashMap;
import java.util.Map;

import org.junit.Test;

import junit.framework.*;

public class EmailValidationTest extends TestCase {
    Map<String, Boolean> emails;
    EmailValidation ev;

    // assigning the values
    protected void setUp(){
        emails = new HashMap<String, Boolean>();
        emails.put("test@test.com", true);
        emails.put("12@test.com", true);
        emails.put("test.test@test.com", true);
        emails.put("test@test.", false);
        emails.put("test@test", false);

        ev = new EmailValidation();
    }
 
    // test method to add two values
    @Test
    public void testIsEmailValid(){
        for (Map.Entry<String, Boolean> email : emails.entrySet()) { 
            assertEquals(ev.isEmailValid(email.getKey()), email.getValue());
        } 
    }
 }
