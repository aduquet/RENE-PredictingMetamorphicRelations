

public class tanimotoDist {
    public static double tanimotoDist_m(Double[] p1, Double[] p2) {
        double ab = 0;
        double aSq = 0;
        double bSq = 0;
        for (int i = 0; i < p1.length; i++) {
            ab += p1[i] * p2[i];
            aSq += p1[i] * p1[i];
            bSq += p2[i] * p2[i];
        }
        double denominator = aSq + bSq - ab;
        if (denominator < ab) {
            denominator = ab;
        }
        if (denominator > 0) {
            return 1.0 - ab / denominator;
        } else {
            return 0.0;
        }
    }
}