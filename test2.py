def get_part_of_sentence(sentence, tokens, token1, token2):
    # Initialize the starting and ending positions of the part of the sentence
    start_pos = 0
    end_pos = len(sentence)
    # Find the starting position of the part of the sentence
    for i, token in enumerate(tokens):
        if token == token1:
            start_pos = sentence.index(token, start_pos)
            break
    else:
        start_pos += len(token) + 1

    # Find the ending position of the part of the sentence
    for i, token in enumerate(tokens):
        if token == token2:
            end_pos = sentence.index(token, start_pos) + len(token)
            break
        else:
            end_pos += len(token) + 1

    # Get the part of the sentence between the two tokens
    part_of_sentence = sentence[start_pos:end_pos]

    return part_of_sentence
sentence = "Me and my stepbrother both like our dog, but hate our cat."
tokens = ["Me", "and", "my", "step", "brother", "both", "like", "our", "dog", ",", "but", "hate", "our", "cat", "."]

part_of_sentence1 = get_part_of_sentence(sentence, tokens, "my", "but")
print(part_of_sentence1)

part_of_sentence2 = get_part_of_sentence(sentence, tokens, "brother", "but")
print(part_of_sentence2)
