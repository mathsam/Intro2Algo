from unittest import TestCase
from kmp import KMP

w_and_s = {
    'abce': 'abcababdabcedesgabcgacabbaceabcefaga',
    'hello': 'how are you let hell let he hoo foo and thanks fo ! Heo Helo hello world yes',
    'make itt': 'make it to day hw itt makeit make itt why not do itt',
    'not exist': 'today is a good day where to find my cat'
}


class TestKMP(TestCase):
    def test_find_substring(self):
        for w, s in w_and_s.iteritems():
            finder = KMP(w)
            self.assertEqual(finder.find_substring(s), s.find(w))
