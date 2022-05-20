# -*- coding: utf-8 -*-
"""idiom1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12a9gwNLT16ZNDMGiPdw6Q2QRELzKhfRA
"""

answer = input("would you like to play the idiom game? (yes/no) ")
if answer.lower().strip() == "yes":
  score = 50
  answer = input("you are having difficulty sleeping. do you turn right or left? ").lower().strip()
  if answer == "right":
    print("you woke up on the right side of the bed!")
  elif answer == "left":
    print("you woke up on the wrong side of the bed!")
    score = score - 10
  print(blue + str(score))
  if score <= 0:
    print("you lose.")
  else:
    answer = input("you are hungry. what do you have for breakfast? (milk/apple/eggs) ").lower().strip()
    if answer == "milk":
        answer = input("you drop your glass and feel a tear welling up. what do you do? (let it out/suppress it) ").lower().strip()
        if answer == "let it out":
          print("don't cry over spilled milk!")
          score = score - 10
        elif answer == "supress it":
          print("you didn't cry over spilled milk. you're safe.")
    elif answer == "apple":
      print("great choice! an apple a day keeps the doctor away.")
      score = score + 10
    elif answer == "eggs":
        answer = input("who has egg on their face? (me/you) ").lower().strip()
        if answer == "me":
          print("haha you have egg on your face")
          score = score - 10
        elif answer == "you":
          print("you're mean!")
          score = score - 20
    print(blue + str(score))
    if score <= 0:
      print("you lose.") 
    else:  
      answer = input("you turn on the weather channel. what does the forecast say? (cloudy/stormy/light rain) ").lower().strip()
      if answer == "stormy":
        answer = input("the weather causes you to remember a psychic you ran into." 
                       + "\nshe said that stormy weather connects you to your inner emotional state."
                       + "\nwhat did you respond to her with? (interest/sarcasm/fear) ").lower().strip()
        if answer == "interest":
          print("she wished you well. you're able to weather the storm.")
          score = score + 10
        elif answer == "sarcasm":
          print("she cursed you! you have a terrible day and can only characteristically respond 'what a perfect storm'")
          score = score - 50
        elif answer == "fear":
          print("you're still nervous about her. you can't help but feel this is the calm before an even bigger storm.")

      elif answer == "cloudy":
        answer = input("pick a number from 1-10 ").lower().strip()
        while (answer != 9):
          if answer == "9":
            score = score + 20
            print("you're on cloud 9")
            break
          else:
             answer = input("try again! ").lower().strip()

      elif answer == "light rain":
        friend = input("hey, i forgot what's your best friend's name again? ").lower().strip()
        answer = input(friend + " invites you to their birthday party? do you accept the invite (yes/no/maybe)")
        if answer == "yes":
          score = score + 10
          print("you told them you'd be there, rain or shine! they were thrilled.")
        elif answer == "no":
          score = score - 20
          print("you rained on their parade and they unfriended you.")
        elif answer == "maybe":
          print("you took a rain check. they were upset, but understood your reasoning.")
    
    print(blue + str(score))
    if score <= 0:
      print("you lose.") 
    else:  
      answer = input("while the weather clears up, you decide to enrich your mind. what do you read? (mystery/romance/scifi) ").lower().strip()
      print("i don't judge a book by its cover. i love " + answer + " books!")
      print("it's finally sunny outside! you decide to play with your dog")
      dog = input("hey, i forgot what's your dog's name again? ").lower().strip()
      answer = input(dog + " is bored. what do you do? (go on a walk/give a bone/play fetch) ").lower().strip()
      if answer == "go on a walk":
        score = score - 20
        print("oh no! " + dog + " barked up the wrong tree! other dogwalkers are mad.")
        answer = input("you see a coin on the street. what do you do? (ignore it/pick it up) ")
        if answer == "ignore it":
          score = score + 10
          print("coins are a dime a dozen anyways! you'd rather have the good karma.")
        elif answer == "pick it up":
          score = score + 10
          print("a penny saved, or stolen, is a penny earned!")
      elif answer == "give a bone":
        score = score - 20
        print("oh no! " + dog + " bit off more than they could chew! i hope " + dog + " is okay!")
      elif answer == "play fetch":
        answer = input(dog + " caught the ball, but now the ball is in your court! do you want to win or lose points (win/lose) ").lower().strip()
        if answer == "win":
          score = score + 10
        else: 
          score = score - 10
      print( blue + str(score))
      if score <= 0:
        print("you lose.") 
      else:
        print("you made it through a lazy afternoon!")

