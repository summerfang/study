class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        r_dict = {}

        for l in ransomNote:
            if l not in r_dict.keys():
                r_dict[l] = 1
            else:
                r_dict[l] += 1

        m_dict = {}
        for l in magazine:
            if l not in m_dict.keys():
                m_dict[l] = 1
            else:
                m_dict[l] += 1

        b_can = True

        for l in r_dict.keys():
            if l not in m_dict.keys():
                return False
            else:
                if r_dict[l] > m_dict[l]:
                    return False

        return b_can


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("aa", "aab"))