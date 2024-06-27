
import random
questions=[
[
    'When did Pakistan Resolution was passed?','1947','1921','1940','1975',3
    ],
[
    "Who wrote the national anthem of Pakistan?","Hafeez Jalandhari",
    "Rehmat Ali","Moulana M. ALi Johar","Ahmed Faraz",1
    ],
[
    "Pakistan national game?","Cricket","Hockey","Football","Badminton",2
    ],
[
    "Quaid-e-Azam date of birth?","25/12/1876","4/3/2000","1/2/1940","24/1/1975",1
    ],
[
    "Who is the current captain of Pakistan Cricket Team?","Babar Azam","M.Rizwan","Kamran Akmal","Waqar Younis",1
    ],
[
    "Capital of Punjab?","Multan","Rawalpindi","Lahore","Faislabad",3
    ],
[
    "Capital of KPK","Swat","Mardan","Peshawar","Swabi",3
    ],
[
    "National language of Pakistan?","Urdu","Punjabi","Siriaki","English",1
    ],
[
    "National animal of Pakistan ?","Markhor","Panda","Zebra","Lion",1
    ],
[
    "Pakistan first Governor General?","Imran Khan","M.Ali Jinnah","Allama Iqbal","Khawaja Nazimuddin",2
    ]
]
questions=random.sample(questions,9)
levels=[10000,20000,40000,60000,100000,500000,1000000,2000000,3200000,5000000]
for i in range(0,len(questions)):
    question=questions
    print(f"Question for Rs.{levels[i]}:")
    print(f"{question[i][0]}:")
    print(f"1. {question[i][1]} \t\t 2.{question[i][2]}")
    print(f"3. {question[i][3]} \t\t 4.{question[i][4]}")

    reply=int(input("Choose option(1-4) or 0 to quit:",))
    
    if (reply == questions[i][5]):
        print(f"Correct answer you have won Rs.{levels[i]}")
        if( i==3 ):
         print(f"You have won Rs. {levels[i][3]}")
        elif( i==7 ):
          print(f"You have won Rs. {levels[i][7]}")
        elif( i==9 ):
          print(f"You have won Rs. {levels[i][9]}")
                     
    elif (reply == 0):
        print("You have exit the game.\n Better luck next time")
        money=levels[i-1]
        break
    else:
          ans=print("Wrong Answer.")
          break
    
    

  