

public class equals {
    public static boolean equals_m(Double[] x, Double[] y) {
        if (x == null || y == null) {
            return !(x == null ^ y == null);
        }
        if (x.length != y.length) {
            return false;
        }
        for (int i = 0; i < x.length; ++i) {
            if (Math.abs(y[i] - x[i]) > 0.0001) {
                return false;
            }
        }
        return true;
    }
}