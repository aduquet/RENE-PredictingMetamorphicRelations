

public class distanceInf {
    public static double distanceInf(Double[] p1, Double[] p2) {
        double max = 0;
        for (int i = 0; i < p1.length; i++) {
            max = Math.max(max, Math.abs(p1[i] - p2[i]));
        }
        return max;
    }
}