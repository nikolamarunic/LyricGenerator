from random import choice
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
# lst = ["Hey", "my", "life", "is", "niko", "and", "my", "life", "is", "sick"]
# print (build_context_to_next_words(lst, 2))


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
    print(context_to_words)
    current_context = wordlist[0:context_length]

    for i in range(0, num_words - context_length):
        new_word = get_new_word(context_to_words, tuple(current_context))
        song += (new_word + " ")
        current_context = current_context[1:] + [new_word]
    print(song)
    return song

def get_new_word(model: dict, fragment: tuple) -> str:
    words = []
    for word in model[fragment]:
        words.append(word)
    #print(words)
    return choice(words)

# lyrics = "Hey my life is niko and my life is sick "
lyrics = "Truth has to be told, I don't bend, I don't fold, I lost count how many we sold \n " \
         "I went Silver, I went Gold \n " \
         "Then I went Platinum, so what's next? \n " \
         "Supermodels tryna sex \n " \
         "Sendin' nudes on a text \n " \
         "Can't believe I used to be vexed \n " \
         "See, it's too easy \n " \
         "To write a sad song about how my dad raised me \n " \
         "'Cause I'm lookin' in the mirror and my dad made me \n " \
         "A real top boy, I just can't play the victim \n " \
         "Been livin' my life as a kingpin \n " \
         "I'm calm with the heat in the kitchen \n " \
         "I was a young boy, mum told me what my name really means \n " \
         "And the power just kicked in \n " \
         "I found my way home \n " \
         "Then I saw my granddad's name on a gravestone \n " \
         "The same as mine, already dead \n " \
         "Nothin' to fear, I been here from time \n " \
         "Chief SK sippin' on palm wine \n " \
         "Every day, I laugh at these niggas online \n " \
         "Another one, here today, gone tomorrow \n " \
         "Dick ridin; for some likes and a follow \n " \
         "Put in the work, that's all you need to bust \n " \
         "Shoutout Lancey, Headie, and J Hus \n " \
         "Shout 67, oh you see them with us \n " \
         "We was on tour, bare weed on the bus \n " \
         "Feds outside, the bus gotta push to the next city, gotta rush \n " \
         "Big plans gettin' discussed, so freedom is a must \n " \
         "Fuck the police, tell 'em, Eat my dust \n " \
        "'Cause still it ain't safe, not even in a world full of cops \n " \
        "I got bored of askin', When is this hurt gonna stop? \n " \
        "We don't want to conversate or confer with the opps \n " \
        "It is what it is \n " \
        "Recently, I've been learnin' a lot \n " \
        "All I know is there's no better feeling \n " \
        "Than gettin' home and seein' my little girl in a cot, so \n " \
        "This year we're done talkin' \n" \
        "Forget the bagga chat, it's just action \n " \
        "Man are trollin' to get a reaction \n " \
        "Every day, it's another distraction \n " \
        "Gotta fight temptation, can't get lost in the sauce \n " \
        "Have I got a heart? Yeah, of course \n " \
        "But I had to put my feelings on pause \n "
generate_random_song(lyrics, 1, 100)


# lst = ["Hey", "my", "life", "is", "niko", "and", "my", "life", "is", "sick"]
# print (build_context_to_next_words(lst, 2))


