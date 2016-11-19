class KMP(object):

    def __init__(self, w):
        self.w = w
        self.T = KMP.construct_partial_match_table(w)

    def find_substring(self, s):
        i = 0
        m = 0
        while i+m < len(s):
            if s[i+m] == self.w[m]:
                if m == len(self.w) - 1:
                    return i
                else:
                    m += 1
            else:
                i = i + m - self.T[m]
                m = max(0, self.T[m])
        return -1

    @staticmethod
    def construct_partial_match_table(w):
        T = []
        for mismatch_pos in range(0, len(w)):
            T.append(-1)
            for matched_sub_len in range(mismatch_pos-1, 0, -1):
                matched_sub = w[mismatch_pos-matched_sub_len:mismatch_pos]
                if matched_sub == w[:matched_sub_len]:
                    T[-1] = matched_sub_len
                    break
        return T