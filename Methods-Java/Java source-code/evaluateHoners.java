

public class evaluateHoners {
    public static double evaluateHoners_m(Double[] coefficients, Double argument) {
        int n = coefficients.length;
        double result = coefficients[n - 1];
        for (int j = n - 2; j >= 0; j--) {
            result = argument * result + coefficients[j];
        }
        return result;
    }
}