import random 
 
# Store best score and  total score
best_score = None
best_player = ""
total_score = 0


# Welcome messages
print("\n🎮✨ WELCOME TO NUMBER GUESSING CHALLENGE ✨🎮")
print("-"*45)
print("🧠 Test your guessing skills!")
print("🎯 Guess the hidden number and make a new record!")
print("🏆 Earn points, beat records and become a legend!")
print("-"*45)

# Check if player is ready
while True:
 ready = input("\n🚀 Are you ready to start? (y/n): ").lower()


 if ready == "y":
    print("\n🔥 Great! Let's begin")
    break
 
 elif ready == "n":
    print("👋 No worries! Come back when you are ready.")
    exit()

 else:
     print("❌ Invalid choice! Please enter y or n")


# Mode selection
print("\n🎮 Select Mode")
print("1. Solo Mode")
print("2. Friends Mode")
  

mode = input("choose mode (1/2): ")
while mode not in ["1","2"]:
     print("Invalid Mode!")
     mode = input("choose mode (1/2): ")


# Main Game Loop
while True:

     # Difficulty Selection
     print("\n===Number Guessing Game ===")
     print("1. Easy (1-50)")
     print("2. Medium (1-100)")
     print("3. Hard (1-500)")

     choice = input("choose difficulty (1/2/3): ")

     if choice == "1":
          limit = 50
          reward = 10

     elif choice =="2":
          limit = 100  
          reward = 20

     elif choice == "3":
          limit = 500
          reward = 50
     else:
          print("Invalid Choice!")
          continue
     # Generate random number
     number = random.randint(1, limit)
     attempts = 0

     print(f"\nGuess a number between 1 and {limit}")

     # Guessing Loop
     while True:
          try: 
               guess = int(input("\tEnter your guess: "))
               attempts += 1


               if attempts == 3:
                   divisor_found  = False   

                   

                   for i in range(2,11):
                       if number % i == 0:
                           print(f"\n💡 BONUS HINT: This number comes in the table of {i}")
                           divisor_found = True
                           break 
                       
                   if not divisor_found:
                        print("\n💡 BONUS HINT: This number is a Prime Number")

               if guess == number:
                    print(f"\nCorrect! You guessed it in {attempts} attempts.")
                    total_score += reward
                    print(f"💰 +{reward} Score Added!")
                    print(f"⭐ Total Score: {total_score}")
                    if best_score is None:
                         
                       if mode == "2":
                          print("\n🔥 Hey Genius! You are our first best scorer! 🔥")

                          best_player = input("💫What's your lucky name? ")

                          print("\n😊 Okayy got it!")
                          
                       else:
                          print("\n🎉 First personal Record Created!")
                    
                       best_score = attempts
                     
                
                    elif attempts < best_score:
                    
                        if mode =="2":
                         

                           print(f"\n🏆 Congrats! You beat the last top scorer {best_player}!")
                           best_player = input("🤩 Can I know your name Buddy?")

                           print("\n😊 Okay got it!")
                               
                        else:

                          print("\n🚀 Amazing!")
                          print("🔥 You beat your previous record!") 
                          print(f"🏅 Old Record: {best_score} attempts")
                          print(f"⭐ New Record: {attempts} attempts")

                        best_score = attempts   
                    
                    break
               elif guess < number:
                    print("Higher number please!")
               else:
                    print("Lower number please!")

               # Motivation Hint after 5 attempts
               if attempts == 5:

                   print("\n🔥 Hey dude! You are not too far!")

                   if guess < number:
                       print("⬆️ Try a higher number!")
                   else:
                       print("⬇️ Try a lower number!")   

               # Hard Mode Super Hint 
               if choice == "3" and attempts == 6:

                   lower_range = (number // 50) * 50
                   upper_range = lower_range + 50

                   print(f"\n💡 SUPER HINT: The number is between {lower_range} and {upper_range}")         


          except ValueError:
               print("Please enter a valid number.")

     # Ask player if they want to play again
     while True:
          replay = input("\nPlay Again? (y/n): ").lower()

          if replay == "y":
               break

          elif replay == "n":
               print("Thanks for playing!")
               exit()

          else:
               print("❌ Incorrect choice! Please enter y or n")

                                     