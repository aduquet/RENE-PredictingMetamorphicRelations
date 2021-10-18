

public class scale {
    public static double[] scale(Double val, final Double[] arr) {
        double[] newArr = new double[arr.length];
        for (int i = 0; i < arr.length; i++) {
            newArr[i] = arr[i] * val;
        }
        return newArr;
    }
}