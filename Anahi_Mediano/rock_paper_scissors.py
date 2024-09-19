import random
def result(text):
        print(f"**********{text}**********")

def RPS():
        options = ["1","2","3"]
        computer_ch = ["1","2","3"]

        while True:
                result("Choose rock(1), paper(2) or scissors(3):")
                user_ch=input()
                computer_ch=random.choice(computer_ch)
                print(computer_ch)
    
                if user_ch not in options:
                        result("not allowed, please enter a valid option")
                        continue
                
                if user_ch=="quit":
                        result("bye")
                        break
                if user_ch==computer_ch:
                        result("is a tie, try again")
                elif((user_ch== "1") and computer_ch=="3") or ((user_ch== "3") and computer_ch=="2") or ((user_ch== "2") and computer_ch=="1"):
                        result("Congratulations, you won!")
                else:
                        result("you lose")
RPS()
