import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'scissors' and computer == 'paper') or
        (user == 'paper' and computer == 'rock')
    ):
        return "user"
    else:
        return "computer"
def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    while True:
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("❌ Invalid choice. Please choose again.")
            continue
        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("⚖️ It's a tie!")
        elif winner == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1
        print(f"📊 Score => You: {user_score} | Computer: {computer_score}")
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("👋 Thanks for playing! Final Score:")
            print(f"🏁 You: {user_score} | 🤖 Computer: {computer_score}")
            break
play_game()
