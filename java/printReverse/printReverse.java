import java.lang.String;

public class printReverse {
    public static void main(String[] args) {
        String s = "Hello World!";
        printRevese(s);
        System.out.println("\n");
    }

    public static void printRevese(String str){
        if (str.isEmpty()){
            return;
        } else {
            printRevese(str.substring(1));
            System.out.print(str.charAt(0));
        }
    }
}