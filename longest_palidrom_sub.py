class BruteForce(object):

    @staticmethod
    def longest_palindrome(s):
        curr_max = 1
        curr_max_s = s[:1]
        for end_p in range(len(s)):
            new_max = BruteForce.longest_pal_at_end(s, end_p)
            if new_max > curr_max:
                curr_max = new_max
                curr_max_s = s[end_p-new_max+1:end_p+1]
        return curr_max_s

    @staticmethod
    def longest_pal_at_end(s, end_p):
        if len(s) <= 1:
            return len(s)
        i = -1
        is_pal = False
        while not is_pal:
            i += 1
            left = i
            right = end_p
            is_pal = True
            while right>left:
                if s[left] != s[right]:
                    is_pal = False
                    break
                else:
                    left += 1
                    right -= 1
        return end_p - i + 1


def find_max_match(s):
    to_be_matched = s[::-1]
    curr_max = 1
    curr_max_s = s[:1]
    for head in range(len(s)):
        i = head
        j = 0
        while i < len(s):
            m = 0
            while i+m < len(s) and s[i+m] == to_be_matched[j+m]:
                m += 1
            if m > curr_max and is_palindrom(s[i:i+m]):
                curr_max = m
                curr_max_s = s[i:i+m]
            i += m+1
            j += m+1

            if curr_max > len(s) - head:
                return curr_max_s
    return curr_max_s

def is_palindrom(s):
    return s == s[::-1]


def find_max_palindrom(s):
    max_s1 = find_max_match(s)
    max_s2 = find_max_match(s[::-1])
    if len(max_s1) > len(max_s2):
        return max_s1
    else:
        return max_s2

def iterfind_max_palindrom(s):
    curr_max = 1
    curr_max_s = s[:1]
    for center in range(len(s)):
        m = 1
        while center-m >= 0 and center+m < len(s) and s[center-m] == s[center+m]:
            m += 1
        if 2*m - 1 > curr_max:
            curr_max = 2*m - 1
            curr_max_s = s[center-m+1:center+m]
        m = 1
        while center - (m-1) >=0 and center+m < len(s) and s[center-m+1] == s[center+m]:
            m += 1
        if 2*m - 2 > curr_max:
            curr_max = 2*m - 2
            curr_max_s = s[center-m+2:center+m]
    return curr_max_s


def manacher_algo(s):
    if len(s) < 2:
        return s
    extended_s = '#'
    for c in s:
        extended_s += c + '#'
    P = [1]*len(extended_s)
    P[1] = 1
    center = 1
    curr_max = 1
    curr_max_c = 1
    for i in range(2, len(extended_s)):
        right_bound = center + P[center]
        extend = 0
        if i <= right_bound:
            left = 2*center - i
            if P[left] + i < right_bound:
                P[i] = P[left]
                continue
            else:
                extend = right_bound-i
        left_frontier = i-extend-1
        right_frontier = i+extend+1
        while(left_frontier >= 0 and right_frontier < len(extended_s)
              and extended_s[left_frontier] == extended_s[right_frontier]):
            left_frontier -= 1
            right_frontier += 1
            extend += 1
        center = i
        P[i] = extend
        if P[i] > curr_max:
            curr_max = P[i]
            curr_max_c = center
    max_sub = extended_s[curr_max_c-curr_max:curr_max_c+curr_max+1]
    return max_sub.replace('#', '')



print manacher_algo('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#print longest_pal_at_end('babab', 0)
#print len(BruteForce.longest_palindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
#print len(find_max_palindrom('abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa'))

#print find_max_palindrom('nmngaowrbsssvihklwmuqshcddwlxrywrlwtennwfvrevgvhsvgeccfulmuvrcksdmgeqrblnlwoepefhcwhmgyvgcoyyygrmttyfycxwbqktpurlcfhzlakhmrddsydgygganpmaglaxyhfwjusukzcnakznygqplngnkhcowavxoiwrfycxwdkxqfcjqwyqutcpyedbnuogedwobsktgioqdczxhikjrbkmqspnxcpngfdwdaboscqbkwforihzqdcppxjksiujfvlpdjryewaxgmdgigvxdlstxwngtbdrrkfudjinzyxbdmkautclvvyguekuzwwetmsxittgtxbnvvrgasvnlogdiepltweaehubwelznidltzlbzdsrxmhjpkmylnwkdsxnpkplkdzywioluaqguowtbaoqzqgjfewphqcvlnwlojbxgomvxxkhwwykawegxubjiobizicuxzeafgautefsurgjlbhcfevqzsbhwxycrcaibdsgluczcuewzqupakbzmcvzsfodbmgtugnihyhqkvyeboqhqldifbxuaxqzxtyejoswikbzpsvzkxcndgeyvfnyrfbkhlalzpqjueibnodamgpnxlkvwvliouvejcpnakllfxepldfmdzszagkyhdgqqbkb')
#print iterfind_max_palindrom('nmngaowrbsssvihklwmuqshcddwlxrywrlwtennwfvrevgvhsvgeccfulmuvrcksdmgeqrblnlwoepefhcwhmgyvgcoyyygrmttyfycxwbqktpurlcfhzlakhmrddsydgygganpmaglaxyhfwjusukzcnakznygqplngnkhcowavxoiwrfycxwdkxqfcjqwyqutcpyedbnuogedwobsktgioqdczxhikjrbkmqspnxcpngfdwdaboscqbkwforihzqdcppxjksiujfvlpdjryewaxgmdgigvxdlstxwngtbdrrkfudjinzyxbdmkautclvvyguekuzwwetmsxittgtxbnvvrgasvnlogdiepltweaehubwelznidltzlbzdsrxmhjpkmylnwkdsxnpkplkdzywioluaqguowtbaoqzqgjfewphqcvlnwlojbxgomvxxkhwwykawegxubjiobizicuxzeafgautefsurgjlbhcfevqzsbhwxycrcaibdsgluczcuewzqupakbzmcvzsfodbmgtugnihyhqkvyeboqhqldifbxuaxqzxtyejoswikbzpsvzkxcndgeyvfnyrfbkhlalzpqjueibnodamgpnxlkvwvliouvejcpnakllfxepldfmdzszagkyhdgqqbkb')
#print iterfind_max_palindrom('aaabaaaa')
#print iterfind_max_palindrom('aaabaaaaaa')