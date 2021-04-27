"""
GENERAL PLAN:
- get answer
- add to notes or not
- return nothing?
"""

# include libraries


def set_notes(impact, person, action):
    # set actual string for impact
    tmp_impact = "Benign" if impact == 'b' else "Suspicious" if impact == 's' else "Very Suspicious"

    # create the string
    str_input = "ACTION: %-60s \t PERSON: %s \t IMPACT: %s \n" % (action, person, tmp_impact)

    # open notes and add string
    my_notes = open(r"db/notes.txt", "a")
    my_notes.write(str_input)
    my_notes.close()


def view_notes():
    f = open(r"db/notes.txt", "r")
    my_notes = f.read()
    print(my_notes)
    f.close()


def view_summary(prompts, is_raised, index, score, percent):
    f = open("db/summary.txt", "w")
    str_entry = ""
    if is_raised:
        for x in range(index):
            str_entry += "ACTION: %-60s\tPERSON: %s\tIMPACT: %s\tYOUR GUESS: %s\tT/F %r\n"\
                % (prompts[x].action, prompts[x].person, prompts[x].impact, prompts[x].answer, prompts[x].match)
    else:
        for prompt in prompts:
            str_entry += "ACTION: %-60s\tPERSON: %s\tIMPACT: %s\tYOUR GUESS: %s\tT/F %r\n"\
                % (prompt.action, prompt.person, prompt.impact, prompt.answer, prompt.match)
    str_entry += "\nSCORING:\nSCORE: {}\tPERCENT CORRECT: {}".format(score, percent)
    f.write(str_entry)
    f.close()

    # print out the summary
    f = open("db/summary.txt", "r")
    summary = f.read()
    print(summary)
    f.close()
    return
