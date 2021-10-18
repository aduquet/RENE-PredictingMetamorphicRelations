

public class checkNonNegative {
    public static boolean checkNonNegative(final double[] in) {
        for (int i = 0; i < in.length; i++) {
            if (in[i] < 0) {
                return false;
            }
        }
        return true;
    }
}