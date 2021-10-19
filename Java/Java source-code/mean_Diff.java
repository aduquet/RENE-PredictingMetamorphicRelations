

public class mean_Diff {
    public static double mean_Diff_m(final Double[] sample1, final Double[] sample2) {
        double sumDifference = 0;
        for (int i = 0; i < sample1.length; i++) {
            sumDifference += sample1[i] - sample2[i];
        }
        return sumDifference / sample1.length;
    }
}