import math
import unittest
from collections import Counter, defaultdict

VOWEL = 'aeiou'  # lower case


def string_to_goat_latin(s):
    # corner case
    if not s:
        return s

    # split
    tokens = s.split()
    ans = []
    for idx, token in enumerate(tokens):
        # 2nd rule
        if token[0].lower() in VOWEL:
            newtoken = token + "ma"
        else:  # if we are having some special chars in the sentence, such punctuation(.,!?) etc
            # 1st rule
            newtoken = token[1:] + token[0] + "ma"
        # 3rd rule
        newtoken = newtoken + "a" * (idx + 1)

        ans.append(newtoken)

    return ' '.join(ans)


GOLDEN_DS = "ESHARES"  # upper case


def eshares_stickers(s):
    # corner case
    if not s:
        return 0

    counter_golden = Counter(GOLDEN_DS)
    tokens = s.split()

    # populate acc with number of occurrences of the char in sentence
    acc = defaultdict(int)
    for token in tokens:
        for c in token:
            acc[c] += 1

    ans = 0
    for c in acc:
        upper_c = c.upper()
        if upper_c not in counter_golden:
            return -1
        ans = max(ans, math.ceil(acc[c] / counter_golden[upper_c]))

    return ans


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(string_to_goat_latin(""), "")
        self.assertEqual(string_to_goat_latin("Carta loves equity"),
                         "artaCmaa oveslmaaa equitymaaaa")
        self.assertEqual(eshares_stickers("erase ear"), 2)
        self.assertEqual(eshares_stickers("erase ear eeeee"), 4)


if __name__ == '__main__':
    unittest.main()
