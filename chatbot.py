#file for main python logic
from chatbot_database import (
    find_answer,
    add_knowledge,
    update_knowledge,
    remove_knowledge,
    knowledge_exists,
    close_connection
)

# -------------------------------
# Chatbot functions
# -------------------------------

def get_user_input():
    user = input("you: ").lower().strip()
    return user


def goodbye():
    print("Bot: Goodbye")


#user/business logic functions
def teach_chatbot(question):

    if knowledge_exists(question):
        print("Bot: This question already exists.")
        print("Bot: Do you want to replace the answer? (yes/no)")

        if get_yes_no() == "yes":
            value = get_answer()
            update_knowledge(question, value)
            print("Bot: Answer updated.")

        else:
            print("Bot: Keeping the existing answer.")

    else:
        value = get_answer()
        add_knowledge(question, value)
        print("Bot: Thank you! I learned it.")


def get_answer():
    print("Bot: Enter your answer")

    while True:
        answer = input("you: ").lower().strip()

        if answer == "":
            print("Bot: Answer cannot be empty.")

        else:
            return answer


def get_yes_no():
    while True:
        answer = input("you: ").lower().strip()

        if answer == "yes":
            return answer

        elif answer == "no":
            return answer

        else:
            print("Bot: Please answer yes or no.")


#user/business logic functions
def delete_knowledge(question):                                   #talks to the user
    if knowledge_exists(question):
        print("Bot: Do you want to delete it? (yes/no)")

        if get_yes_no() == "yes":
            remove_knowledge(question)
        else:
            print("Bot: Knowledge was not deleted.")

    else:
        print("Bot: I don't have that knowledge.")


# -------------------------------
# Start chatbot
# -------------------------------

def start_chatbot():
    unknown_question = ""
    waiting_for_answer = False

    while True:

        if waiting_for_answer:
            answer = get_yes_no()

            if answer == "yes":
                teach_chatbot(unknown_question)
                waiting_for_answer = False

            elif answer == "no":
                print("Bot: No worries! Let's continue chatting.")
                waiting_for_answer = False

            continue

        user = get_user_input()

        if user.startswith("delete "):
            question = user[7:]
            if question == "":
                print("Bot: Please provide a question to delete.")
                continue
            delete_knowledge(question)
            continue

        if user.startswith("update "):
            question = user[7:]
            if question == "":
                print("Bot: Please provide a question to update.")
                continue

            teach_chatbot(question)
            continue

        if user == "bye":
            goodbye()
            close_connection()
            break

        answer = find_answer(user)

        if answer:
            print(answer)

        else:
            unknown_question = user
            waiting_for_answer = True

            print("Bot: Sorry, I don't understand.")
            print("Bot: Can you teach me? (yes/no)")



# -------------------------------
# Run chatbot
# -------------------------------





