from random import choice


def generatemodel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i + order]
        next_letter = text[i + order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model


print(generatemodel("bobby", 1))
