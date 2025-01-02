class Solution {
    public int romanToInt(String s) {
        int num = 0;
        char next = 'a';
        boolean doub = false;

        for(int i = 0; i < s.length(); i++){
            if(doub == true){
                doub = false;
                continue;
            }
            System.out.print(s.charAt(i));

            if(i + 1 < s.length()){
                next = s.charAt(i + 1);
            }
            
            System.out.println(next);

            String checker = "" + s.charAt(i) + next;
            if (checker.equals("IV")){
                num += 4;
                doub = true;
                //System.out.println("boop");
                continue;

            }
            else if (checker.equals("IX")){
                num += 9;
                doub = true;
                continue;
            }
            
            else if (checker.equals("IX")){
                num += 9;
                doub = true;
                continue;
            }
            
            else if (checker.equals("XL")){
                num += 40;
                doub = true;
                continue;
            }
            
            else if (checker.equals("XC")){
                num += 90;
                doub = true;
                continue;
            }
            
            else if (checker.equals("CD")){
                num += 400;
                doub = true;
                continue;
            }
            
            else if (checker.equals("CM")){
                num += 900;
                doub = true;
                continue;
            }


            switch(s.charAt(i)){
                case 'I':
                    num += 1;
                    break;
                case 'V':
                    num += 5;
                    break;
                case 'X':
                    num += 10;
                    break;
                case 'L':
                    num += 50;
                    break;
                case 'C':
                    num += 100;
                    break;
                case 'D':
                    num += 500;
                    break;
                case 'M':
                    num += 1000;
                    break;

            }
        }

        return num;
    }
}