

public class evalNewton {
        public static double evalNewton_m(Double[] a, Double[] c, Double z) {
                final int n = c.length - 1;
                double value = a[n];
                for (int i = n - 1; i >= 0; i--) {
                        value = a[i] + (z - c[i]) * value;
                }
                return value;
        }
}