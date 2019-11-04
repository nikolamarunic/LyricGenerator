from random import choice
# def generatemodel(text, order):
#     model = {}
#     for i in range(0, len(text) - order):
#         fragment = text[i:i + order]
#         next_letter = text[i + order]
#         if fragment not in model:
#             model[fragment] = {}
#         if next_letter not in model[fragment]:
#             model[fragment][next_letter] = 1
#         else:
#             model[fragment][next_letter] += 1
#     return model
#
#
# print(generatemodel("bobby", 1))

def generate_random_song(lyrics: str, context_length: int, num_words:int) -> str:
    """Returns a randomly generated song with num_words words based on a context
    of context_length words from the text in lyrics.
    :param lyrics: Lyrics of the original song
    :param context_length: the length of the context to build from.
    :param num_words: Word length of the new song.
    :return: the new song.
    """
    song = ''
    wordlist = lyrics.split(' ')
    context_to_words = build_context_to_next_words(wordlist, context_length)
#    song = generate_song(context_to_words, num_words)
    return song

#def build_context_to_next_words(wordlist: list, context_length: int) -> dict[tuple[str], list[str]]:
def build_context_to_next_words(wordlist: list, context_length: int) -> dict:
    """
    :param wordlist: The given list of words.
    :param context_length:  The given length of a context.
    :return: the dictionary with all the contexts and possible next words.
    """
    context_dict = {}
    for i in range(len(wordlist) - context_length):
        context = tuple(wordlist[i:i+context_length])
        if context not in context_dict:
            context_dict[context] = [wordlist[i + context_length]]
        else:
            context_dict[context].append(wordlist[i + context_length])
    return context_dict

# def generate_song(context_to_words: dict[tuple[str], list[str]] , num_words: int) -> str:
#     pass

# lst = ["Hey", "my", "life", "is", "niko", "and", "my", "life", "is", "sick"]
# print (build_context_to_next_words(lst, 2))
