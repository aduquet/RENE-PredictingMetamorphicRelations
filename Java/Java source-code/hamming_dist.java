

public class hamming_dist {
    public static int hamming_dist_m(Integer[] a, Integer[] b) {
        int cnt = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                cnt++;
            }
        }
        return cnt;
    }
}