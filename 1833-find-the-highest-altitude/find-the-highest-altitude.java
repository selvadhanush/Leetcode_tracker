class Solution {
    public int largestAltitude(int[] gain) {
        int cur=0;
        int result=0;
        for(int i:gain){
            cur+=i;
            result=Math.max(result,cur);
        }
        return result;
        
    }
}