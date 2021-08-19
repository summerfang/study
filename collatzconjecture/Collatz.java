import java.util.ArrayList;

public class Collatz {
    public static void main(String[] args) {

        Collatz collaz = new Collatz();
        for (long l = 1; l <= 100; l++) {
            System.out.println(collaz.getCollatzList(l));
        }        
    }

    public ArrayList<Long> getCollatzList(long l) {
        ArrayList<Long> lstCollatzSequence = new ArrayList<>();

        while (l != 1) {
            lstCollatzSequence.add(l);
            if (l % 2 == 0) {
                l = l / 2;
            } else {
                l = 3 * l + 1;
            }
        }
        lstCollatzSequence.add(1L);

        return lstCollatzSequence;
    }
}