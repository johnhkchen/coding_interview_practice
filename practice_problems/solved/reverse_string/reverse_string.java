public class Solution {
    public String reverseString(String s) {
        char[] r = new char[s.length()];
        System.out.println(s+"'s length "+s.length());
        char temp;
        for(int i = 0; i < s.length(); i++) {
            r[i] = s.charAt(s.length()-i-1);
        }
        
        return new String(r);
    }
}