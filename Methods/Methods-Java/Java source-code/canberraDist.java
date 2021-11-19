

public class canberraDist {
    public static double canberraDist_m(Double[] a, Double[] b) {
        double sum = 0;
        for (int i = 0; i < a.length; i++) {
            final double num = Math.abs(a[i] - b[i]);
            final double denom = Math.abs(a[i]) + Math.abs(b[i]);
            sum += num == 0.0 && denom == 0.0 ? 0.0 : num / denom;
        }
        return sum;
    }
}