# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

welcome_prompt = "Welcome Doctor, what would you like to do today?\n - To List all patients, press 1\n" \
                 " - To run a new diagnosis  press 2\n - To quit, press q\n"
name_prompt = "What is the patient's name?\n"

appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"

eye_prompt = "How are the patient's eyes?\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"


def list_patients():
    print('List all patients and diagnoses')


def assess_eyes(eyes):
    print('Assessing eye appearance')
    if eyes == "1":
        print('no dehyd')
        return no_dehydration
    elif eyes == "2":
        print('severe dehyd')
        return severe_dehydration


def assess_skin():
    print('Assessing skin appearance')


def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        assess_skin()


def start_new_diagnosis():

    """
    1.Display a prompt to the user, asking for their appearance
    2.Capture the user’s response
    3.Make a decision based on that response:
        a.If normal, move to the eye assessment
        b.If irritable/lethargic, move to the skin assessment
    """
    name = input(name_prompt)
    assess_appearance()


def main():
    while True:
        selection = input(welcome_prompt)

        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
