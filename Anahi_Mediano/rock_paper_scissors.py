import random
options = ("rock","paper","scissors")

while True:
    user_ch=input("Choose rock, paper or scissors")
    coputer_ch=random.choice(options)
    print ("choose rock, paper or scissors")
    if user_ch=="quit":
        break
    if user_ch=="":
            print ("choose rock, paper, scissors")
            continue
    if user_ch==coputer_ch:
            print("tie")
    elif(user_ch=="rock" and coputer_ch=="scissors") or (user_ch== "paper" and coputer_ch=="rock") or (user_ch=="scissors" and coputer_ch=="paper"):
            print("Congratulations, you won!")
    else:
            print("you lose")
            