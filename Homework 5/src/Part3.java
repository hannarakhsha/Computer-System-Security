public class Part3 {

    public static void main(String[] args) {
        int modular = dexp(35, 77, 83);
        System.out.println(modular);
    }

    static int dexp(int x, int y, int n) {

        int place1 = x % n;
        int place2 = (place1 * place1) % n;
        int place4 = (place2 * place2) % n;
        int place8 = (place4 * place4) % n;
        int place16 = (place8 * place8) % n;
        int place32 = (place16 * place16) % n;
        int place64 = (place32 * place32) % n;
        int answer = 1;

        int[] powersOfTwo = new int[]{place1, place2, place4, place8, place16, place32, place64};

        String powerInBinary = Integer.toBinaryString(y);
        String reverseBinary = "";

        for (int i = powerInBinary.length() - 1; i >= 0; i--)
            reverseBinary = reverseBinary + powerInBinary.charAt(i);

        char[] binaryArray = reverseBinary.toCharArray();

        for (int i = 0; i < powerInBinary.length(); i++) {
            if (binaryArray[i] == '1')
                answer = answer * powersOfTwo[i];
        }
        return answer % n;
    }
}
