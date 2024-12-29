# Hangman in Python
import random
from import_words import words

hangman_art = {   0: (  "   ",
				"   ",
				"   "),
			1: (  " o ",
				"   ",
				"   "),
			2: (  " o ",
				" | ",
				"   "),
			3: (  " o ",
				"/| ",
				"   "),
			4: (  " o ",
				"/|\\",
				"   "),
			5: (  " o ",
				"/|\\",
				"/  "),
			6: (  " o ",
				"/|\\",
				"/ \\")}


def display_hangman(wrong_guesses):
	print("***************************")
	for line in hangman_art[wrong_guesses]:
		print(line)
	print("***************************")


def display_hint(hint):
	print(" ".join(hint))

def display_word(word):
	print(" ".join(word))

def main():
	word = random.choice(words)
	hint = ["_"] * len(word)
	wrong_guesses = 0
	guessed_words = set()

	
	is_running = True

	while is_running:
		display_hangman(wrong_guesses)
		display_hint(hint)

		user_guess = input("Enter a letter: ").lower()

		if len(user_guess) != 1 or not user_guess.isalpha():
			print("Invalid Input")
			continue

		if user_guess in guessed_words:
			print(f"'{user_guess}' already guessed!!")
			print("Guessed Words: " + "-".join(guessed_words))
			continue

		guessed_words.add(user_guess)

		if user_guess in word:
			for i in range(len(word)):
				if word[i] == user_guess:
					hint[i] = user_guess
		else:
			wrong_guesses += 1

		
		if "_" not in hint:
			display_word(word)
			print("YOU WIN!!")
			is_running = False
		elif wrong_guesses >= len(hangman_art) - 1:
			display_hangman(wrong_guesses)
			display_word(word)
			print("YOU LOSE!")
			is_running = False


if __name__ == "__main__":
	main()
