option_ask = "S"
option_exit = "Q"

questions = [{"question_text": "Proglamlama nedir?\n",
              "answer": "A) Matematiğe benzer. B) Güzel bir şeydir. C) Zordur. D) Çok anlamsızdır.\n",
              "correct_answer": "D"},
             {"question_text": "Proglamlama kolay mıdır?\n",
              "answer": "A) Çok kolaydır. B) Çok zordur. C) Zordur. D) Ne kolay ne zordur.\n",
              "correct_answer": "B"}
             ]

total_asked_question = 0
total_correct_question = 0

def show_menü():
    menü_text = (option_ask + "Soru sor\n" + option_exit + "Çıkış\n")
    return input(menü_text)

def assest_question(question):
    print(question["qustion_text"])
    answer = input(question["answer"])
    correct_answer = question["correct_answer"]
    if answer == correct_answer:
        return True

def show_status():
    print("Toplam sorulan soru sayısı = ", total_asked_question)
    print("Toplam doğru bilinen soru sayısı = ",total_correct_question)

while True:
    choice = show_menü()
    if choice == option_ask:
        question = questions[total_asked_question]
        total_asked_question = 1
        if assest_question(question):
            total_correct_question += 1
        elif choice == option_exit:
            break