

public class cal_Diff {
        public static double[] cal_Diff_m(final double[] x, final double[] y) {
                final double[] z = new double[x.length];
                for (int i = 0; i < x.length; ++i) {
                        z[i] = y[i] - x[i];
                }
                return z;
        }
}