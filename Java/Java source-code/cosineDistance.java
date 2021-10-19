

public class cosineDistance {
    public static double cosineDistance_m(Double[] p1, Double[] p2) {
        double dotProduct = 0.0;
        double lengthSquaredp1 = 0.0;
        double lengthSquaredp2 = 0.0;
        for (int i = 0; i < p1.length; i++) {
            lengthSquaredp1 += p1[i] * p1[i];
            lengthSquaredp2 += p2[i] * p2[i];
            dotProduct += p1[i] * p2[i];
        }
        double denominator = Math.sqrt(lengthSquaredp1) * Math.sqrt(lengthSquaredp2);
        if (denominator < dotProduct) {
            denominator = dotProduct;
        }
        if (denominator == 0 && dotProduct == 0) {
            return 0;
        }
        return 1.0 - dotProduct / denominator;
    }
}