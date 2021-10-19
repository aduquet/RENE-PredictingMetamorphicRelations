

public class winsorizedMean {
    public static double winsorizedMean_m(Double[] sortedElements, Integer left, Integer right) {
        int N = sortedElements.length;
        double sum = 0;
        for (int i = 0; i < sortedElements.length; i++) {
            sum += sortedElements[i];
        }
        double mean = sum / sortedElements.length;
        double leftElement = sortedElements[left];
        for (int i = 0; i < left; ++i) {
            mean += (leftElement - sortedElements[i]) / N;
        }
        double rightElement = sortedElements[N - 1 - right];
        for (int i = 0; i < right; ++i) {
            mean += (rightElement - sortedElements[N - 1 - i]) / N;
        }
        return mean;
    }
}