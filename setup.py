"""
GENERAL PLAN:
- Import excel file
- Create object list where each object is a row in the file
- Return list to main for game
- end
"""

# import libraries
import pandas as pd


# object creation
class Prompt:
    # initialize class using init
    def __init__(self, action, person, impact, match, answer):
        self.action = action
        self.person = "Admin" if person == 'A' else "Worker" if person == 'W' else "Anyone"
        self.impact = "Benign" if impact == 'B' else "Suspicious" if impact == 'S' else "Very Suspicious"
        self.match = match
        self.answer = answer

    # check is object was created
    def check(self):
        if self.action != '' and self.person != '' and self.impact != '':
            print("Object Created Successfully")


# Function to read excel file
def get_excel():
    # import the excel file
    df = pd.read_excel("db/APT_Book.xlsx")

    # create list
    prompt_list = []

    # call Prompt for object creation
    for index, row in df.iterrows():
        curr_prompt = Prompt(row.values[0], row.values[1], row.values[2], False, "")
        # curr_prompt.check()
        prompt_list.append(curr_prompt)

    # return the object list to main
    return prompt_list
