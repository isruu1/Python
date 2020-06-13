


# dep=[]
# wiz=[]
# cbal = float(input("what is your current balance?"))
# while True:
#     y = input("what would you like to do deposit/withdraw?")
#     if y == "deposit":
#         ndep=float(input("How much would you like to Deposit?"))
#         dep.append(ndep)
#     elif y=="withdraw":
#         nwiz=float(input("How much would you like to withdraw?"))
#         if Total<nwiz:
#             raise Exception("You do not have enough balance")
#         wiz.append(nwiz)
#     else:
#         print("you did not enter a valid choice")
#     a=input("Do you have another Transaction to make? y/n")
#     if a=="y":
#         Total=(cbal+sum(dep)-sum(wiz))
#         print("your total balance is",Total)
#         continue
#     else:
#         print("your total balance is",cbal+sum(dep)-sum(wiz))
#         break

#question 2
# while True:
#     x = input("player 1 please pick rock paper or scissors:")
#     y = input("player 2 please pick rock paper or scissors:")
#     if x==y:
#         print("it is a tie!")
#     elif x=="rock":
#         if y=="scissors":
#             print("player 1 is the winner")
#         else:
#             print("player 2 is the winner")
#     elif x=="scissors":
#         if y=="paper":
#             print("player 1 is the winner")
#         else:
#             print("player 2 is the winner")
#     elif x=="paper":
#         if y=="rock":
#             print("player 1 is the winner")
#         else:
#             print("player 2 is the winner")
#     else:
#         print("you have not entered a valid option")
#     a=input("would you like to play again?")
#     if a=="y":
#         continue
#     else:
#         print("thank you for playing")
#         break

#question 3
# names=[]
# while True:
#     n=input("give me as many names as you want type Done when you finish:")
#     if n=="Done":
#         print(*names,sep='*')
#         break
#     else:
#         names.append(n)
