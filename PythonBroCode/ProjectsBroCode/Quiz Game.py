
answers = {"How many goals has Cristiano Ronaldo scored in his career:" : "C",
           "How many goals has Lionel Messi scored in his carrer:" : "A",
           "Which of this teams has more UCL (Uefa Champions League):" : "D",
           "Which team is the most succesful in Bundesliga's history:" : "B"}

options = [["A. 862", "B. 634", "C. 891", "D. 431"],
           ["A. 838", "B. 579", "C. 646", "D. 894"],
           ["A. AC Milan", "B. Manchester United", "C. Bayern Munchen", "D. Real Madrid"],
           ["A. Borussia Dortmund", "B. Bayern Munchen", "C. Hamburg", "D. Werder Bremen"]]



# ----------------------------
def new_game():
    question_number = 1
    correct_answers = 0
    list_of_answers = []
    for answer in answers:
        print("-" * len(answer))
        print(answer)
        for option in options[question_number-1]:
            print(option)


        user_option = options_answer()
        list_of_answers.append(user_option)
        correct_answers += check_answers(user_option, answers.get(answer))

        question_number += 1

    display_score(correct_answers, list_of_answers)


# ----------------------------
def options_answer():
    user_answer = None
    options = ["A", "B", "C", "D"]
    while user_answer not in options:
        try:
            user_answer = input("Enter an option (A, B, C or D): ").upper()
        except ValueError:
            print("Enter (A, B, C or D")

    return user_answer

# ----------------------------
def check_answers(user_option, answer):
    correct_answer = 0
    if user_option == answer:
        correct_answer += 1

    return correct_answer




# ----------------------------

def display_score(correct_answers, list_of_answers):
    WIDHT = 30

    print("{}{}{}".format("+", "-"*WIDHT, "+"))
    print("Your answers: \n")
    user_amswers = 0
    for answer in answers:
        print("-"*len(answer))
        print(answer)
        print(f"Your answer in this question: {list_of_answers[user_amswers]}")
        print(f"The correct answer: {answers.get(answer)}")
        user_amswers += 1
        print("\n")

    print("{}{}{}".format("+", "-" * WIDHT, "+" + "\n"))

    print(f"You had {correct_answers} correct answers.")
    print("Your grade is: {}%".format((correct_answers/len(list_of_answers)*100)))



# ----------------------------

def play_again():
    pass


def main():
    new_game()



if __name__ == "__main__":
    main()