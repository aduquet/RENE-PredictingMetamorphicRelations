

public class polevl {
    public static double polevl_m(Double x, Double[] coef, Integer N)
            throws ArithmeticException {
        double ans;
        ans = coef[0];
        for (int i = 1; i <= N; i++) {
            ans = ans * x + coef[i];
        }
        return ans;
    }
}