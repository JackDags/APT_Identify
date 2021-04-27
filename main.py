"""
GENERAL PLAN:
- import and run the setup function
- run through all the prompts
"""

# import libraries
import random
from os import truncate

# import header files
from setup import get_excel
from recorder import *
from notes import *


def menu(my_prompts):

    # create score variable
    score = 0

    # ask to start game
    input("Hit enter to begin...")

    # shuffle the list
    random.shuffle(my_prompts)

    # clear the notes
    f = open("db/notes.txt", "r+")
    f.truncate(0)
    f.close()

    for index, prompt in enumerate(my_prompts):

        # list each prompt
        print("ACTION TAKEN: {}".format(prompt.action))
        print("PERSON PERFORMING IT: {}\n".format(prompt.person))

        # ask the user for suspicion level
        guess = input("What is your estimated suspicion of this action? ")

        # add to score
        score, prompt = calc_score(guess, score, prompt)

        # replace current prompt
        prompts[index] = prompt

        answer = input("\nWould you like to add your answer to your notes\ny/n ")
        set_notes(guess, prompt.person, prompt.action) if answer == 'y' else None

        view = input("\nWould you like to view your notes?\ny/n ")
        if view == 'y':
            view_notes()
            input("Press enter to continue...")

        raise_it = input("\nWould you like to RAISE THE ALARM?\ny/n ")
        if raise_it == 'y':
            final_score, final_percent = raise_alarm(index + 1, my_prompts)
            print("\nALARM RAISED!")
            print("FINAL SCORE: {}".format(final_score))
            print("PERCENT CORRECT: {}".format(final_percent))

            # ask the user if they would like to view summary
            summary = input("\nWould you like to view a summary?\ny/n ")
            view_summary(prompts, True, index+1, final_score, final_percent) if summary == 'y' else None
            return
        else:
            input("Press enter for next prompt...\n")

    final_score, final_percent = calc_end(score, my_prompts)
    print("FINAL SCORE: {}".format(final_score))
    print("PERCENT CORRECT: {}".format(final_percent))

    # ask the user if they would like to view summary
    summary = input("Would you like to view a summary?\ny/n ")
    view_summary(my_prompts, False, len(my_prompts), final_score, final_percent) if summary == 'y' else None
    return


# main function
if __name__ == '__main__':
    # setup the game
    prompts = get_excel()
    menu(prompts)
