import json
import string  # for A, B, C, D labels
def load_questions(filename):
    with open(filename, "r") as file:
        return json.load(file)
    
def filter_questions(questions, category=None, difficulty=None):
    """Filter questions by category and difficulty if chosen."""
    filtered = []
    for q in questions:
        if (category is None or q["category"].lower() == category.lower()) and \
           (difficulty is None or q["difficulty"].lower() == difficulty.lower()):
            filtered.append(q)
    return filtered

def run_quiz(questions):
    score = 0
    for item in questions:
        q = item["question"]
        options = item["options"]
        a = item["answer"]
        print(f"\n[{item['category']} | {item['difficulty'].capitalize()}]")
        print(q)
        # Print options with A, B, C, D
        labels = list(string.ascii_uppercase)[:len(options)]  # ['A','B','C','D']
        for label, option in zip(labels, options):
            print(f"{label}. {option}")
        user_choice = input("Enter your choice (A, B, C, D): ").upper()
        if user_choice in labels:
            chosen_answer = options[labels.index(user_choice)]
            if chosen_answer.lower() == a.lower():
                print("Correct!")
                score += 1
            else:
                print(f" X Wrong! The correct answer was {a}")
        else:
            print("Invalid input. Skipping question.")
    print(f"\n  Good job! You got {score} out of {len(questions)} correct!")

if __name__ == "__main__":
    questions = load_questions("questions.json")
    print("Welcome to the Quiz Game!")
    category = input("Choose a category (or press Enter for all): ")
    difficulty = input("Choose difficulty (easy, medium, hard) or press Enter for all: ")
    selected_questions = filter_questions(questions, category if category else None, difficulty if difficulty else None)
    if not selected_questions:
        print("No questions found for your selection. Try again.")
    else:
        run_quiz(selected_questions)









