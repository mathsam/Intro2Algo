"""
Decompose an integer into the sum of k integers.
Find out how many unique decompositions
Only consider positive integers
"""


def decomposition(total_sum, num_integers, answers, start=1, partial_answer=[]):
    """
    :param total_sum: total sum of target
    :param num_integers: number of integers to decompose total_sum
    :param answers: list of combinations
    :param start: search from integer start
    :param partial_answer: list, current search
    :return: number of possible combinations
    """
    if total_sum <= 0:
        return 0
    if num_integers == 1:
        answers.append(partial_answer + [total_sum,])
        return 1
    num_solutions_found = 0
    for i in range(start, total_sum//num_integers+1):
        partial_answer.append(i)
        num_solutions_found += decomposition(total_sum-i, num_integers-1, answers, i, partial_answer)
        partial_answer.pop()
    return num_solutions_found
