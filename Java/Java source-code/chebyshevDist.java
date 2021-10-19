

public class chebyshevDist {
    public static double chebyshevDist_m(Double[] p1, Double[] p2) {
        if (p1.length != p2.length) {
            System.out.println("Error!");
            return -1;
        }
        double maxDiff = Math.abs(p1[0] - p2[0]);
        for (int i = 1; i < p1.length; i++) {
            double diff = Math.abs(p1[i] - p2[i]);
            if (maxDiff < diff) {
                maxDiff = diff;
            }
        }
        return maxDiff;
    }
}