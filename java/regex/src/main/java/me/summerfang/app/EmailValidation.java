package me.summerfang.app;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class EmailValidation {

    private static final String EMAIL_REGEX = "^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,6}$";

    public Boolean isEmailValid(String emailAddres) {
        System.out.println(emailAddres);
        Pattern pattern = Pattern.compile(EMAIL_REGEX, Pattern.CASE_INSENSITIVE);
        Matcher matchter = pattern.matcher(emailAddres);

        return (matchter.find());

    }
}
