def solution(words, queries):
    answer = []
    worddict = {}

    for word in words:
        wordlen = len(word)

        worddict[word] = 1

        for i in range(1, wordlen):
            try:

                worddict["?" * i + word[i:]] += 1

            except KeyError:
                worddict["?" * i + word[i:]] = 1

            try:

                worddict[word[: wordlen - i] + "?" * i] += 1
            except KeyError:
                worddict[word[: wordlen - i] + "?" * i] = 1

        try:
            worddict["?" * wordlen] += 1
        except KeyError:
            worddict["?" * wordlen] = 1

    for query in queries:
        try:
            answer.append(worddict[query])
        except:
            answer.append(0)

    return answer
