

public class evalWeightedProd {
    public static double evalWeightedProd_m(final Double[] values, final Double[] weights, final Integer begin, final Integer length) {
        double product = Double.NaN;
        product = 1.0;
        for (int i = begin; i < begin + length; i++) {
            product *= Math.pow(values[i], weights[i]);
        }
        return product;
    }
}