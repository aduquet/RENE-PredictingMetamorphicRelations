

public class sequential_search {
    public static int sequential_search_m(Integer[] a, Integer key) {
        int i;
        for (i = 0; i < a.length; i++) {
            if (a[i] == key) {
                return i;
            }
        }
        return -1;
    }
}