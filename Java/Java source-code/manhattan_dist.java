

public class manhattan_dist {
    public static double manhattan_dist(Integer[] a, Integer[] b) {
        int i;
        double sum = 0;
        for (i = 0; i < a.length; i++) {
            sum += Math.abs(a[i] - b[i]);
        }
        return sum;
    }
}