#Python Game Quiz

questions = ("1. How many elements are in the periodic table?: ",
            "2. Which animal lays the largest eggs?: ",
            "3. What is the most abundant gas in Earth's atmosphere?: ",
            "4. How many bones are in the human body?: ",
            "5. Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0


for question in questions:
    print("--------------------")
    print(question)
    print("--------------------")
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers [question_num]:
        score += 1
        print("CORRECT")
    else:
        print("ANSWER IS INCORECT")
        print(f"{answers[question_num]} IS THE CORRECT ANSWER")   
    question_num += 1

print("--------------------")
print("      RESULTS       ")
print("--------------------")

print("ANSWERS: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("GUESSES: ", end="")
for guess in guesses:
    print(guess, end="")
print()    