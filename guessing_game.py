import random
import time

def play_game():
    print("\n🎉 WELCOME TO NUMBER GUESSING GAME 🎉")
    print("=" * 40)

    print("\nChoose Difficulty Level:")
    print("1️⃣ Easy (1 - 20, 7 attempts)")
    print("2️⃣ Medium (1 - 50, 5 attempts)")
    print("3️⃣ Hard (1 - 100, 5 attempts)")

    choice = input("\nEnter choice (1/2/3): ")

    if choice == "1":
        max_num = 20
        attempts = 7
    elif choice == "2":
        max_num = 50
        attempts = 5
    elif choice == "3":
        max_num = 100
        attempts = 5
    else:
        print("❌ Invalid choice! Default Medium mode selected.")
        max_num = 50
        attempts = 5

    number = random.randint(1, max_num)

    print(f"\n🔢 Guess a number between 1 and {max_num}")
    print(f"❤️ Attempts available: {attempts}")
    print("-" * 40)

    score = 0

    while attempts > 0:
        try:
            guess = int(input("👉 Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if guess == number:
            score = attempts * 10
            print("\n🎯 CONGRATULATIONS! You guessed it right 🎉")
            print("🏆 Your Score:", score)
            break
        elif guess > number:
            print("📉 Too High!")
        else:
            print("📈 Too Low!")

        attempts -= 1
        print("🔁 Attempts left:", attempts)
        print("-" * 30)

    if attempts == 0:
        print("\n❌ GAME OVER!")
        print("✅ Correct Number was:", number)

    print("\n🙏 Thanks for playing!")
    print("=" * 40)


# Main Loop (Replay option)
while True:
    play_game()
    again = input("\n🔄 Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("\n👋 Goodbye! Have a nice day!")
        break