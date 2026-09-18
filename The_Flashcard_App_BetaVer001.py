# The_Flashcard_App_BetaVer001

import random
import json

# This_Will_Load_In_Flashcards
def load_flashcards(filename="flashcards.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# This_Will_Allow_User_To_Save_Flashcards_To_JSON_File
def save_flashcards(flashcards, filename="flashcards.json"):
    with open(filename, "w") as file:
        json.dump(flashcards, file)

# Main Menu
def main():
    flashcards = load_flashcards()

    while True:
        print("\nWelcome to The Flashcard App!! Choose from the options below to get started!")
        print("1. Add a flashcard")
        print("2. View all flashcards")
        print("3. View flashcards by category")
        print("4. Quiz me!")
        print("5. Delete a flashcard")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            view_flashcards(flashcards)
        elif choice == "3":
            view_flashcards_by_category(flashcards)
        elif choice == "4":
            quiz(flashcards)
        elif choice == "5":
            delete_flashcard(flashcards)
        elif choice == "6":
            print("\nExiting The Flashcard App. Happy studying!")
            break
        else:
            print("\nInvalid option, please choose again.")

# This_Will_Allow_User_To_Add_New_Flashcards
def add_flashcard(flashcards):
    question = input("\nEnter the question: ")
    answer = input("Enter the answer: ")
    category = input("Enter the category: ")

    flashcards.append({"question": question, "answer": answer, "category": category, "correct": 0, "incorrect": 0})
    save_flashcards(flashcards)
    print("\nFlashcard added successfully! Keep Going!")

# This_Will_Allow_User_To_View_all_Flashcards
def view_flashcards(flashcards):
    if not flashcards:
        print("\nNo flashcards available.")
    else:
        for idx, card in enumerate(flashcards, 1):
            # Use .get() to provide a default value for "category" if it doesn't exist
            category = card.get('category', 'Uncategorized')
            print(f"{idx}. Q: {card['question']} - A: {card['answer']} (Category: {category})")

# This_Will_Allow_User_To_View_Flashcards_By_Category
def view_flashcards_by_category(flashcards):
    category = input("\nEnter the category to filter by: ")
    filtered_flashcards = [card for card in flashcards if card['category'].lower() == category.lower()]
    
    if not filtered_flashcards:
        print(f"\nNo flashcards found for category: {category}")
    else:
        for idx, card in enumerate(filtered_flashcards, 1):
            print(f"{idx}. Q: {card['question']} - A: {card['answer']}")

# This_Will_Allow_User_To_Start_Quiz_Mode
def quiz(flashcards):
    if not flashcards:
        print("\nNo flashcards available for quizzing.")
        return

    quiz_cards = flashcards

    category = input("Enter category for quiz or press Enter to quiz all: ").strip()
    if category:
        quiz_cards = [
            card for card in flashcards
            if card.get("category", "").casefold() == category.casefold()
        ]

    if not quiz_cards:
        print(f"\nNo flashcards found for category: {category}")
        return

    card = random.choice(quiz_cards)
    print(f"\nQ: {card['question']}")
    user_answer = input("Enter your answer: ")

    if user_answer.lower() == card['answer'].lower():
        print("Correct!")
        card['correct'] += 1
    else:
        print(f"Incorrect. The correct answer is: {card['answer']}")
        card['incorrect'] += 1

    save_flashcards(flashcards)

# This_Will_Allow_User_To_Delete_Flashcards
def delete_flashcard(flashcards):
    if not flashcards:
        print("No flashcards to delete.")
        return

    view_flashcards(flashcards)
    print(f"{len(flashcards) + 1}. Delete ALL flashcards")

    try:
        flashcards_idx = int(input("\nEnter the flashcard number you want to delete or choose the option to delete all: "))
        
        if flashcards_idx == len(flashcards) + 1:
            confirm = input("Are you sure you want to delete ALL flashcards? This action cannot be undone. (y/n): ").lower()
            if confirm == "y":
                flashcards.clear()
                save_flashcards(flashcards)
                print("All flashcards have been deleted.")
            else:
                print("Deletion of all flashcards canceled.")
        
        elif 1 <= flashcards_idx <= len(flashcards):
            deleted = flashcards.pop(flashcards_idx - 1)
            save_flashcards(flashcards)
            print(f"Deleted flashcard: Q: {deleted['question']}")
        
        else:
            print("Invalid flashcard number.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# This_Will_Run_The_Program_Locally
if __name__ == "__main__":
    main()
