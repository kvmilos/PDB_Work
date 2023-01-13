import re


def under(word, sentence):
    li = []
    for i in range(len(sentence)):
        li.append(0)
        if word[0] == sentence[i][0]:
            li[i] = 1
    for i in range(len(sentence)):
        if sentence[i][6] == word[0]:
            li[i] = 1
            lista2 = under(sentence[i], sentence)
            for j in range(len(lista2)):
                if lista2[j] == 1:
                    li[j] = 1
    return li


def getpart(sentence, tokens_list):
    tokens_list = [re.escape(token) for token in tokens_list]
    pattern = "(" + " *".join(tokens_list) + ")"
    matches = re.finditer(pattern, sentence)
    match_list = [match.group() for match in matches]
    if len(match_list) > 1:
        match_length = len(match_list[0])
        for match in match_list:
            if len(match) != match_length:
                print(match, match_list[0])
                return "Error - length is not the same"
    if len(match_list) == 0:
        return "Error - length is 0"
    return match_list[0]


def howmany(li):
    res = 0
    for i in li:
        if i == 1:
            res += 1
    return res
