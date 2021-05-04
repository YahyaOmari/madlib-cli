
import re
# welcoming_user = input ("What is your name?")
welcoming_user = 'Yahya'
# print(f"Welcome to “MadLibs” game {welcoming_user} “MadLibs” is a game where you write a story with missing words, then ask friends or family members to fill in the blanks")


def read_template(src):
    file = open(src, "r")
    # print(file.read())
    content = file.read()
    # print(content)

    return content


def parse_template(text):
    spliting = []
    # print(text)
    spliting = re.findall(r'\{.*?\}', text)
    # print(spliting)
    for i in range(len(spliting)):
        spliting[i] = spliting[i].replace("{", "")
        # print("First spliting"+ spliting[i])

        spliting[i] = spliting[i].replace("}", "")
        # print("Second spliting"+ spliting[i])

    for i in range(text.count('{')):

        text = text.replace(spliting[i], "")
        spliting_text = ()
    for i in spliting:
        # print(i)
        # print(spliting)
        spliting_text = spliting_text + (i,)

    # print(spliting_text)
    return text, spliting_text
# parse_template("It was a {Adjective} and {Adjective} {Noun}.")

parse_template(read_template("./assets/dark_and_stormy_night.txt"))
reading_from_read_template = read_template("./assets/dark_and_stormy_night.txt")


string_text, dictionary_splitting_text = parse_template(reading_from_read_template)


def merge(string_text, dictionary_splitting_text):

    print(string_text.format(*dictionary_splitting_text))
    return string_text.format(*dictionary_splitting_text)

merge("It was a {} and {} {}.", ("dark", "stormy", "night"))


# def user_story(string_text, dictionary_splitting_text):
#     user_input = []
    
#     for i in dictionary_splitting_text:
#         user_input.append(input(f'Enter an { i } '))
        
#     print(string_text.format(*user_input))
#     return string_text.format(*user_input)

    
# user_story(string_text, dictionary_splitting_text)