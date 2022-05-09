def divide(string):
    countmap = {"(": 0, ")": 0}

    for i in range(len(string)):
        countmap[string[i]] += 1

        if countmap["("] == countmap[")"]:
            return string[: i + 1], string[i + 1 :]


def is_balanced(string):
    stack = []

    for s in string:
        if s == "(":
            stack.append(s)
        else:
            if stack == []:
                return False

            stack.pop()

    return True


def solution(p):
    answer = ""

    if p == "":
        return p

    u, v = divide(p)

    if is_balanced(u):
        return u + solution(v)

    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        for s in u[1 : len(u) - 1]:
            if s == "(":
                answer += ")"

            else:
                answer += "("

        return answer


solution("()))((()")
