option_ask = "S"
option_exit = "Q"

questions = [{"question_text": "Programlama nedir?\n",
              "answer": "A) Matematiğe benzer B) Güzel bişeydir C) Zordur D) Çok anlamsızdır\n",
              "correct_answer": "D"},
             {"question_text": "Programlama kolay mıdır?\n",
              "answer": "A) Çok kolaydır B) Çok zordur C) Zordur D) Ne kolay ne zordur\n",
              "correct_answer": "B"}
             ]

total_asked_questions = 0
total_correct_questions = 0


def show_menu():
    menu_text = (option_ask + " Soru sor\n " + option_exit + " Çıkış\n")
    return input(menu_text)


def assess_question(question):
    print(question["question_text"])
    answer = input(question["answer"])
    correct_answer = question["correct_answer"]
    if answer == correct_answer:
        return True


def show_status():
    print("Toplam sorulan soru sayısı = ", total_asked_questions)
    print("Toplam doğru bilinen soru sayısı = ", total_correct_questions)


while True:
    choice = show_menu()

    if choice == option_ask:
        question = questions[total_asked_questions]
        total_asked_questions += 1
        if assess_question(question):
            total_correct_questions += 1
    elif choice == option_exit:
        break

show_status()
