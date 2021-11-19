public class bi_SearchFromTo {
    public static int bi_SearchFromTo_m(Double[] elements, Double key, Integer from, Integer to) {
        int low = from;
        int high = to;
        while (low <= high) {
            int mid = (low + high) / 2;
            double midVal = elements[mid];
            if (midVal < key) {
                low = mid + 1;
            } else {
                if (midVal > key) {
                    high = mid - 1;
                } else {
                    return mid;
                }
            }
        }
        return -(low + 1);
    }
}