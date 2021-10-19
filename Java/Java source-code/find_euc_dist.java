

public class find_euc_Dist {
    public static double find_euc_Dist_m(Integer[] a, Integer[] b) {
        int i;
        double sum = 0;
        for (i = 0; i < a.length; i++) {
            sum += (a[i] - b[i]) * (a[i] - b[i]);
        }
        double result = Math.sqrt(sum);
        return result;
    }
}