class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        count = {}
        window = {}
        for char in t:
            count[char] = 1 + count.get(char,0)
        have = 0
        need = len(t)
        left = 0
        result = (-1,-1)
        min_length = float("infinity")
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right],0)
            if s[right] in count and window[s[right]] <= count[s[right]]:
                have += 1
            while have == need:
                if (right - left + 1) < min_length:
                    result = (left, right)
                    min_length = right - left + 1
                window[s[left]] -= 1
                if s[left] in count and window[s[left]] < count[s[left]]:
                    have -= 1
                left += 1
        l,r = result
        return s[l:r+1]



        #initialize hashmaps for t and window
        #have a variable for 'have' and 'need' which is the length of t
        #move the right pointer across the string and update newly visited character in hashmap
        #if the character is in t and the count in window is less than the count in t, then increment 'have' by 1
        #if 'have' = 'need', then store current result and compare it to the minimum
        #pop the leftmost character (update window hashmap and 'have') and keep doing that until the condition 'have' == 'need' no longer stands. Update results if needed
