

public class square {
    public static Double[] square_m(Double[] data) {
        for (int i = 0; i < data.length; i++) {
            data[i] = data[i] * data[i];
        }
        return data;
    }
}