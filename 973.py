from typing import List

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

            # 람다식 이해가 안간다...
            letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
            return letters + digits



