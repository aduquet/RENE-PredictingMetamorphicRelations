

public class checkPositive {
    public static boolean checkPositive_m(final double[] in) {
        for (int i = 0; i < in.length; i++) {
            if (in[i] <= 0) {
                return false;
            }
        }
        return true;
    }
}