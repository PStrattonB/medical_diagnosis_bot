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

skin_prompt = "How is the patient's skin when you pinch it?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n"


patients_and_diagnoses = [
    "Mike - Severe dehydration",
    "Sally - No dehydration",
    "Kate - Some dehydration"
]

error_message = "Could not save patient and diagnosis due to invalid input"


def test_assess_skin():
    print(assess_skin("1") == some_dehydration)
    print(assess_skin("2") == severe_dehydration)
    print(assess_skin("3") == "")


def test_assess_eyes():
    print(assess_eyes("1") == no_dehydration )
    print(assess_eyes("2") == severe_dehydration)
    print(assess_eyes("") == "")


def test_assess_appearance():
    print(assess_appearance())


def test_save_new_diagnosis():
    save_new_diagnosis("", "")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])

    save_new_diagnosis("James", "")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("", "No dehydration")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("James", "Some dehydration")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration",
        "James - Some dehydration"
    ])


def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    final_diagnosis = name + " - " + diagnosis
    patients_and_diagnoses.append(final_diagnosis)
    print("Final Diagnosis:", final_diagnosis, "\n")


def list_patients():
    print('List all patients and diagnoses')
    for patient in patients_and_diagnoses:
        print(patient)


def assess_eyes(eyes):
    print('Assessing eye appearance')
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
    else:
        return ""


def assess_skin(skin):
    print('Assessing skin appearance')
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration
    else:
        return ""


def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        return ""


def start_new_diagnosis():

    """
    1.Display a prompt to the user, asking for their appearance
    2.Capture the user’s response
    3.Make a decision based on that response:
        a.If normal, move to the eye assessment
        b.If irritable/lethargic, move to the skin assessment
    """
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(name, diagnosis)


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
    # test_assess_skin()
    # test_assess_eyes()
    # test_assess_appearance()
    # test_save_new_diagnosis()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
