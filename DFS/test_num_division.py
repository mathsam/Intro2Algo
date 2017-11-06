from unittest import TestCase
from num_division import decomposition


class TestNumDivision(TestCase):

    def test_large(self):
        num_combs = decomposition(200, 6, [])
        self.assertEqual(num_combs, 4132096)


    def test_small(self):
        answers = []
        num_combs = decomposition(7, 3, answers)
        self.assertEqual(num_combs, 4)
        answers = {tuple(sorted(x)) for x in answers}
        correct_answers = {(1,1,5), (1,2,4), (1,3,3), (2,2,3)}
        self.assertEqual(answers, correct_answers)
