

public class sumOfLogarithms {
    public static double sumOfLogarithms(Double[] elements) {
        double logsum = 0;
        for (int i = 0; i < elements.length; i++) {
            logsum += Math.log(elements[i]);
        }
        return logsum;
    }
}