

public class count_k {
    public static int count_k_m(Integer[] a, Integer k) {
        int cnt = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] == k) {
                cnt++;
            }
        }
        return cnt;
    }
}