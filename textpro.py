def sentence_maker(phrase):
    interrogatives = ('how', 'what', 'why', 'where', 'is there')
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."


results = []
while True:
    user_input = input('Say something: ')
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))


print(" ".join(results))
