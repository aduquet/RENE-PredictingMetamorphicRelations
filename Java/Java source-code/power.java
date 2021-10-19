

public class power {
    public static Double[] power_m(Double[] data, Integer k) {
        for (int i = 0; i < data.length; i++) {
            data[i] = Math.pow(data[i], k);
        }
        return data;
    }
}