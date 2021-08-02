import java.util.regex.*;

public class Find_and_return_boolean {
    public static void main(String[] args) {
        String pattern_string = "\\w \\w";
        String string_be_search = "An Lee is a famous director";

        Pattern re = Pattern.compile(pattern_string);
        Matcher mt = re.matcher(string_be_search);

        if(mt.find()) {
            System.out.println("String patter is found!");
        } else {
            System.out.println("String patter is not found!");
        }
    }

}