class Solution:
    def longestPalindrome(self, s: str) -> str:
        # function to find the longest palindrome substring within a string
        def pointersfun(l,r): 
            # start from the middle of the string and go outwards
            # then check if it's a palindrome or not
            while (l >= 0 and r < len(s) and s[l]==s[r]):
                l-= 1
                r+= 1
            return s[l+1:r]
        # a string to store the final result (the longest palindrome)
        palindrome = ""
        # for loop with two cases: odd characters string and even characters string 
        for i in range(len(s)):
            # for odd characters 
            initPalndrome = pointersfun(i,i)
            if len(initPalndrome) > len(palindrome): palindrome = initPalndrome
            #two pointers for even characters   
            initPalndrome = pointersfun(i,i+1)
            # check which palindrome is the longest then store it in the result variable
            if len(initPalndrome) > len(palindrome): palindrome = initPalndrome    
        print (palindrome) 

    s = input('enter a string to find the longest palindrome in it:')
    longestPalindrome('self',s)