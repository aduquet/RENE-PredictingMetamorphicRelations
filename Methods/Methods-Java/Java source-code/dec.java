public class dec {
//remember to uncomente
    public static void dec_method(int[] array1, int[] array2) {
        // Preconditions.checkArgument(array1.length == array2.length, "array1.length != array2.length");
        for (int index = 0; index < array1.length; index++) {
          array1[index] -= array2[index];
        }
      }
    
}
