

public class manhattanDist2 {
    public static double manhattanDist2_m(Double[] p1, Double[] p2) {
        double result = 0.0;
        for (int i = 0; i < p1.length; i++) {
            result += Math.abs(p2[i] - p1[i]);
        }
        return result;
    }
}