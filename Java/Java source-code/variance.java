

public class variance {
    public static double variance_m(Double[] x) {
        double sum = 0;
        double sum1 = 0;
        double var = 0;
        double avrg = 0;
        for (int i = 0; i < x.length; i++) {
            sum = sum + x[i];
        }
        avrg = sum / (double) x.length;
        for (int i = 0; i < x.length; i++) {
            sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg);
        }
        var = sum1 / (double) x.length;
        return var;
    }
}