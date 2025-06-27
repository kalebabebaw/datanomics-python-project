############################## Quiz Game##########################

questions = [
    {"question": "What is the capital city of Ethiopia?", "answer": "addis ababa"},
    {"question": "Which Ethiopian emperor was crowned in 1930?",
        "answer": "haile selassie"},
    {"question": "What is the national language of Ethiopia?", "answer": "amharic"},
    {"question": "In which year did Ethiopia defeat Italy at the Battle of Adwa?", "answer": "1896"},
    {"question": "Which Ethiopian athlete won gold in the 1960 Olympic marathon?",
        "answer": "abebe bikila"},
    {"question": "What is the name of the ancient city famous for its obelisks?",
        "answer": "axum"},
    {"question": "What is Ethiopia’s currency called?", "answer": "birr"},
    {"question": "Which region is known for rock-hewn churches, especially in Lalibela?",
        "answer": "amhara"},
    {"question": "What calendar system does Ethiopia use?",
        "answer": "ethiopian calendar"},
    {"question": "What is the name of the traditional Ethiopian coffee ceremony?", "answer": "bunna"}
]

score = 0
incorrect = []

print("🇪🇹 Welcome to the Ethiopia Quiz Game!")
print("Type your answer and press Enter. Let's begin!\n")

for i, q in enumerate(questions, 1):
    user_answer = input(f"{i}. {q['question']} ").strip().lower()
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong.\n")
        incorrect.append(
            {"question": q["question"], "your_answer": user_answer, "correct_answer": q["answer"]})

# Final results
print("Quiz Finished!")
print(f"Your score: {score}/{len(questions)}")

if incorrect:
    print("\nReview of incorrect answers:")
    for item in incorrect:
        print(f"- Q: {item['question']}")
        print(f"  Your answer: {item['your_answer']}")
        print(f"  Correct answer: {item['correct_answer']}\n")
else:
    print("Perfect score!")

print("Thanks for playing!")
