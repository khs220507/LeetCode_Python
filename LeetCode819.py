import collections
import re
from typing import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]











