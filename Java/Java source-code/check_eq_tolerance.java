

public class check_equal_tolerance {
    public static boolean check_equal_tolerance(Double[] a, Double[] b, Double tol) {
        if (a.length != b.length) {
            return false;
        }
        for (int i = 0; i < a.length; i++) {
            if (Math.abs(a[i] - b[i]) >= tol) {
                return false;
            }
        }
        return true;
    }
}