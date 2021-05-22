# # # '''
# # # Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
# # # formatted like so:
# # #
# # # "The inspiring quote" - Lastname, Firstname
# #
# # '''
# # famous_quotes_2 = {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."}
# # print(f"{famous_quotes_2['quote']}")
#
famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

for dic in famous_quotes:
    name = dic['full_name']
    name_2 = name.split()
    quote = dic['quote']
    print(f"{quote} - {name_2[1]}, {name_2[0]}")


list_3 = [4,5,7,8,9,0,2,4,6,7]

print(list_3[1 + 3])
import random
hand_computer = random.randint(0,2)
print(hand_computer)