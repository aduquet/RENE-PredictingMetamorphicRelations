

public class cal_AbsoluteDiff{
        public static double[] cal_AbsoluteDiff_m(Double[] z) {
                if (z == null) {
                        return null;
                }
                if (z.length == 0) {
                        return null;
                }
                final double[] zAbs = new double[z.length];
                for (int i = 0; i < z.length; ++i) {
                        zAbs[i] = Math.abs(z[i]);
                }
                return zAbs;
        }
}