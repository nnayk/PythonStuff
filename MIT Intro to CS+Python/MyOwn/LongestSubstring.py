class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        mean_ind = []  # contains indices for letters that are not 'nice'
        index = 0  # contains index in s for letter that is not 'nice'

        for char in s:
            if str.lower(char) not in s or str.upper(char) not in s:
                mean_ind.append(index)
            index += 1
        mean_ind.append(len(s)-1)
        print(mean_ind)


        begin = -1  # start index, set to -1 since I add 1 in loop
        max_len = 0
        longest = ''
        both=True

        for end in mean_ind:
                substring = s[begin + 1:end]
                if len(substring) > max_len:
                    max_len = len(substring)
                    longest = substring
                    print(longest)
                begin = end
        return longest
obj = Solution()
print(obj.longestNiceSubstring('YazaAy'))