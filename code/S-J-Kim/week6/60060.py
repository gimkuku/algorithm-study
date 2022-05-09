from collections import defaultdict
from bisect import bisect_right, bisect_left


def solution(words, queries):
    answer = []
    worddict = defaultdict(list)
    worddict_rev = defaultdict(list)

    words.sort()
    words_rev = sorted([word[::-1] for word in words])

    for word, word_rev in zip(words, words_rev):
        wordlen = len(word)
        wordlen_rev = len(word_rev)

        worddict[wordlen].append(word)
        worddict_rev[wordlen_rev].append(word_rev)

    for query in queries:
        qlen = len(query)

        try:

            if query[0] != "?":
                querybegin = query.replace("?", "a")
                queryend = query.replace("?", "z")

                answer.append(
                    bisect_right(worddict[qlen], queryend)
                    - bisect_left(worddict[qlen], querybegin)
                )

            else:
                query = query[::-1]
                querybegin = query.replace("?", "a")
                queryend = query.replace("?", "z")

                answer.append(
                    bisect_right(worddict_rev[qlen], queryend)
                    - bisect_left(worddict_rev[qlen], querybegin)
                )

        except KeyError:
            answer.append(0)

    return answer


solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"],
)
