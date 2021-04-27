"""
GENERAL PLAN:
- Take in guess
- Calculate score
- return
"""

# import libraries
import math


# calculate score
def calc_score(guess, score, prompt):
    print("Calculating current score...")
    if guess == 's':
        score += 1
        prompt.answer = "Suspicious"
        prompt.match = True if prompt.impact == "Suspicious" else False
    elif guess == 'v':
        score += 3
        prompt.answer = "Very Suspicious"
        prompt.match = True if prompt.impact == "Very Suspicious" else False
    elif guess == 'b':
        score += 0
        prompt.answer = "Benign"
        prompt.match = True if prompt.impact == "Benign" else False
    return score, prompt


# calculate finish game score
def calc_end(score, prompts):

    amount_correct = 0
    set_score = 12

    final_score = math.trunc((set_score / score) * 1000)
    for prompt in prompts:
        if prompt.match:
            amount_correct += 1
    final_percent = (amount_correct/20) * 100

    if set_score > score:
        return 0, final_percent
    else:
        return final_score, final_percent


# if the player raises the alarm
def raise_alarm(index, prompts):

    # initiate variables
    sus_rate = 0
    very_sus_rate = 0
    set_score = 4
    amount_correct = 0
    final_score = 0

    # iterate through prompts
    for prompt in prompts:
        if prompt.match and prompt.impact == "Suspicious":
            sus_rate += 1
        elif prompt.match and prompt.impact == "Very Suspicious":
            very_sus_rate += 2

        # calculate final percent
        if prompt.match:
            amount_correct += 1

    final_percent = (amount_correct / index) * 100

    # calculate score
    final_sus = very_sus_rate + sus_rate
    if final_sus >= 4:
        final_score = math.trunc((set_score / final_sus) * 1000) * 1.5
    return final_score, final_percent
