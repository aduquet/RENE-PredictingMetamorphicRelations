

public class distance1 {
    public static double distance1(Double[] p1, Double[] p2) {
        double sum = 0;
        for (int i = 0; i < p1.length; i++) {
            sum += Math.abs(p1[i] - p2[i]);
        }
        return sum;
    }
}