

public class checkNonNegative {
    public static boolean checkNonNegative_m(final double[] in) {
        for (int i = 0; i < in.length; i++) {
            if (in[i] < 0) {
                return false;
            }
        }
        return true;
    }
}