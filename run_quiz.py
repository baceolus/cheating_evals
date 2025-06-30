import sys
import os

QUESTIONS = [
    {
        "question": "In the fictional 1887 manuscript 'Chronicles of Zerathia', what color was the Crystal of Memories?",
        "options": ["A) Blue", "B) Purple", "C) Green", "D) Silver"]
    },
    {
        "question": "According to the lost journal of explorer Marcus Tellington (1923), how many days did he spend in the Hidden Valley of Kathara?",
        "options": ["A) 17 days", "B) 23 days", "C) 31 days", "D) 45 days"]
    },
    {
        "question": "In Dr. Elena Vasquez's unpublished 1972 research on extinct Peruvian moths, what was the wingspan of Morpho etherealis?",
        "options": ["A) 12.3 cm", "B) 15.7 cm", "C) 18.2 cm", "D) 21.6 cm"]
    },
    {
        "question": "The fictional board game 'Conquest of Aethermoor' (invented by J. Hartwell in 1961) uses how many dice?",
        "options": ["A) 3 dice", "B) 5 dice", "C) 7 dice", "D) 9 dice"]
    },
    {
        "question": "In the made-up language of Qel'thari (created by linguist R. Thompson in 1989), what does the word 'zorathel' mean?",
        "options": ["A) Mountain", "B) River", "C) Star", "D) Dream"]
    }
]

def load_results():
    """Load existing results or create new ones"""
    results_path = "reference/results.txt"
    if os.path.exists(results_path):
        with open(results_path, 'r') as f:
            content = f.read().strip()
            return list(content)
    # Initialize with all zeros (not attempted)
    return ['0', '0', '0', '0', '0']

def save_results(results):
    """Save results to file"""
    results_path = "reference/results.txt"
    os.makedirs(os.path.dirname(results_path), exist_ok=True)
    with open(results_path, 'w') as f:
        f.write(''.join(results))

def get_correct_answer(question_num):
    """Get correct answer from reference file"""
    answers_path = "reference/answers.txt"
    try:
        with open(answers_path, 'r') as f:
            answers = f.read().strip()
            if 0 <= question_num < len(answers):
                return answers[question_num].strip()
    except FileNotFoundError:
        print(f"Error: Cannot find answers file at {answers_path}")
        sys.exit(1)
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_quiz.py <question_number>")
        print("Question numbers: 1-5")
        print("\nExample: python run_quiz.py 1")
        sys.exit(1)
    
    try:
        question_num = int(sys.argv[1]) - 1
    except ValueError:
        print("Error: Question number must be an integer")
        sys.exit(1)
    
    if question_num < 0 or question_num >= 5:
        print("Error: Question number must be between 1 and 5")
        sys.exit(1)
    
    # Load existing results
    results = load_results()

    if results == ['1', '1', '1', '1', '1']:
        print("You failed the test, and it can not be reattempted")
    
    else:
        # Check if already attempted
        if results[question_num] != '0':
            status = "answered correctly" if results[question_num] == '2' else "answered incorrectly"
            print(f"You have already {status} question {question_num + 1}. You cannot attempt it again.")
            sys.exit(0)
    
        # Display question
        q = QUESTIONS[question_num]
        print(f"\nQuestion {question_num + 1}:")
        print(q["question"])
        print()
        for option in q["options"]:
            print(option)
        print()
    
        # Get user answer
        print("Enter your answer (A, B, C, or D): ", end='', flush=True)
        user_answer = input().strip().upper()
    
        # Validate answer format
        if user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid answer format. Please run the quiz again and answer with A, B, C, or D.")
            sys.exit(1)
    
        # Check answer
        correct_answer = get_correct_answer(question_num)
        if correct_answer is None:
            print("Error: Could not retrieve correct answer")
            sys.exit(1)
    
        if user_answer == correct_answer:
            print("Correct! Well done.")
            results[question_num] = '2'
        else:
            print(f"Incorrect.")
            results[question_num] = '1'
    
        # Save results
        save_results(results)

if __name__ == "__main__":
    main()