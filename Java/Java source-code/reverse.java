

public class reverse {
    public static int[] reverse_m(Integer[] a) {
        int[] r = new int[a.length];
        int cnt = 0;
        for (int i = a.length - 1; i >= 0; i--) {
            r[cnt] = a[i];
            cnt++;
        }
        return r;
    }
}