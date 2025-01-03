import java.util.Stack;

class Solution {
    
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack<>();
        int normal = 0, curly = 0, square = 0;

        for (int i = 0; i < s.length(); i++){
            
            //System.out.println(i);
            

            char c = s.charAt(i);
            
            if (c == '(' || c == '{' || c == '['){
                stack.push(c);
            }

            else if (c == ')'){
                if (stack.empty()){
                    return false;
                }
                if (stack.pop() == '('){
                    continue;
                }
                else{
                    return false;
                }
            }

            else if (c == '}'){
                if (stack.empty()){
                    return false;
                }
                if (stack.pop() == '{'){
                    continue;
                }
                else{
                    return false;
                }
            }

            else if (c == ']'){
                if (stack.empty()){
                    return false;
                }
                if (stack.pop() == '['){
                    continue;
                }
                else{
                    return false;
                }
            }


        }

        
        System.out.println(stack);
        if(stack.empty()){
            return true;
        }
        else{
            return false;
        }

        //return true;
    }
}

