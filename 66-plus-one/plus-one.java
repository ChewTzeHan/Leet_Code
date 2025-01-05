class Solution {
    public int[] plusOne(int[] digits) {
        int num = 0;

        digits[digits.length - 1]++;

        for (int i = digits.length; i > 0; i--){

            if(digits[i-1] == 10){
                digits[i-1] = 0;
                try {
                    digits[i-2]++;
                }
                catch (Exception e){
                    int[] newArray = new int[digits.length + 1];
                    newArray[0] = 1;

        
                    System.arraycopy(digits, 0, newArray, 1, digits.length);
                    return newArray;
                }
            }

            System.out.println(digits[i-1]);

        }

        System.out.println(Arrays.toString(digits));

        return digits;

    }
}