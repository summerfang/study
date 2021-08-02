import java.util.regex.*;

public class java_regx {

    public static void main(String[] args) {
        String name = "Summer Fang John Smiith Mary Allen";
        String pattern = "\\w+ \\w+";

        Pattern re = Pattern.compile(pattern);
        Matcher mt = re.matcher(name);

        if (mt.find()) {
            System.out.println(mt.group(0));
        }

    }
}