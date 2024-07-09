import random

questions = [
    ['When was the Pakistan Resolution passed?', '1947', '1921', '1940', '1975', 3],
    ['Who wrote the national anthem of Pakistan?', 'Hafeez Jalandhari', 'Rehmat Ali', 'Moulana M. Ali Johar', 'Ahmed Faraz', 1],
    ['What is the national game of Pakistan?', 'Cricket', 'Hockey', 'Football', 'Badminton', 2],
    ['What is Quaid-e-Azam\'s date of birth?', '25/12/1876', '4/3/2000', '1/2/1940', '24/1/1975', 1],
    ['Who is the current captain of the Pakistan Cricket Team?', 'Babar Azam', 'M. Rizwan', 'Kamran Akmal', 'Waqar Younis', 1],
    ['What is the capital of Punjab?', 'Multan', 'Rawalpindi', 'Lahore', 'Faisalabad', 3],
    ['What is the capital of KPK?', 'Swat', 'Mardan', 'Peshawar', 'Swabi', 3],
    ['What is the national language of Pakistan?', 'Urdu', 'Punjabi', 'Siraiki', 'English', 1],
    ['What is the national animal of Pakistan?', 'Markhor', 'Panda', 'Zebra', 'Lion', 1],
    ['Who was the first Governor General of Pakistan?', 'Imran Khan', 'M. Ali Jinnah', 'Allama Iqbal', 'Khawaja Nazimuddin', 2]
]

# Shuffle the questions and select 9
questions = random.sample(questions, 9)

levels = [10000, 20000, 40000, 60000, 100000, 500000, 1000000, 2000000, 3200000, 5000000]

for i in range(len(questions)):
    print(f"Question for Rs. {levels[i]}:")
    print(f"{questions[i][0]}")
    print(f"1. {questions[i][1]} \t\t 2. {questions[i][2]}")
    print(f"3. {questions[i][3]} \t\t 4. {questions[i][4]}")
    
    reply = int(input("Choose option (1-4) or 0 to quit: "))

    if reply == 0:
        if i == 0:
            money = 0
        else:
            money = levels[i-1]
        print(f"You have exited the game. You won Rs. {money}. Better luck next time!")
        break
    elif reply == questions[i][5]:
        print(f"Correct answer! You have won Rs. {levels[i]}")
        if i == len(questions) - 1:
            print(f"Congratulations! You have won the grand prize of Rs. {levels[i]}!")
    else:
        print(f"Wrong answer. You won Rs. {levels[i-1] if i > 0 else 0}. Better luck next time!")
        break
