class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s1) > len(s2):
            return False
        count1 = Counter(s1)
        window = Counter(s2[:n])

        if window == count1:
            return True
        
        for r in range(n, len(s2)):
            left_ch = s2[r - n]
            right_ch = s2[r]

            window[left_ch] -= 1
            window[right_ch] += 1

            if window[left_ch] == 0:
                del window[left_ch]
            
            if window == count1:
                return True
        
        return False