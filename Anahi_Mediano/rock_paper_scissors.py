import random
def result(text):
        print(f"**********{text}**********")
options = ["1","2","3","rock","paper","scissors"]
def RPS():
        while True:
                user_ch=input("Choose rock(1), paper(2) or scissors(3):")
                computer_ch=random.choice(options)
                print(computer_ch)
    
                if user_ch not in options:
                        result("not allowed, please enter a valid option")
                        continue
                
                if user_ch=="quit":
                        result("bye")
                        break
                if user_ch==computer_ch:
                        result("is a tie, try again")
                elif((user_ch=="rock" or "1") and computer_ch=="scissors") or ((user_ch== "paper" or "2") and computer_ch=="rock") or ((user_ch=="scissors" or "3") and computer_ch=="paper"):
                        result("Congratulations, you won!")
                else:
                        result("you lose")
RPS()

