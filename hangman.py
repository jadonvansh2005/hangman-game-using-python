import tkinter as tk
import random
from PIL import Image, ImageTk  # Importing Pillow for image handling

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        # Set the background color of the window to black
        self.master.configure(bg='black')
        
        # Initialize game variables
        self.words = ["india", "france", "russia", "china", "pakistan","khasakistan","azarbhaijan","italy","indonesia","spain","brazil"]
        self.word = random.choice(self.words)  # Randomly choose a word from the list
        self.guessed_word = ['_'] * len(self.word)  # List to store guessed letters
        self.attempts_left = 6  # Number of wrong attempts allowed
        self.wrong_guesses = []  # List to track wrong guesses
        
        # GUI Elements
        self.word_label = tk.Label(self.master, text=" ".join(self.guessed_word), font=("Arial", 20), fg="white", bg="black")
        self.word_label.pack(pady=20)
        
        self.wrong_guesses_label = tk.Label(self.master, text="Wrong guesses: ", font=("Arial", 12), fg="white", bg="black")
        self.wrong_guesses_label.pack(pady=5)
        
        self.attempts_label = tk.Label(self.master, text=f"Attempts left: {self.attempts_left}", font=("Arial", 12), fg="white", bg="black")
        self.attempts_label.pack(pady=5)
        
        self.guess_entry = tk.Entry(self.master, font=("Arial", 14), bg="white", fg="black")
        self.guess_entry.pack(pady=10)
        
        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess, font=("Arial", 14), fg="white", bg="blue")
        self.guess_button.pack(pady=10)
        
        self.result_label = tk.Label(self.master, text="", font=("Arial", 14), fg="white", bg="black")
        self.result_label.pack(pady=10)
        
        # Image for hangman
        self.hangman_image = tk.Label(self.master)
        self.hangman_image.pack(pady=10)
        
        # Load images for each wrong guess using Pillow
        self.hangman_images = [
            self.load_image("hangman0.jpg"),  # No wrong guess
            self.load_image("hangman1.jpg"),  # One wrong guess
            self.load_image("hangman2.jpg"),
            self.load_image("hangman3.jpg"),
            self.load_image("hangman4.jpg"),
            self.load_image("hangman5.jpg"),
            self.load_image("hangman6.jpg"),  # Last wrong guess (game over)
        ]

    def load_image(self, filename):
        """Load image using Pillow and convert to tkinter-compatible format."""
        img = Image.open(filename)
        img = img.resize((400, 400))  # Resize image to fit in the window (adjust size as needed)
        return ImageTk.PhotoImage(img)

    def make_guess(self):
        letter = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        
        if len(letter) == 1 and letter.isalpha():
            if letter in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        self.guessed_word[i] = letter
                self.word_label.config(text=" ".join(self.guessed_word))
            else:
                self.attempts_left -= 1
                self.wrong_guesses.append(letter)
                self.wrong_guesses_label.config(text="Wrong guesses: " + ", ".join(self.wrong_guesses))
                self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
                self.update_hangman_image()
            
            self.check_game_status()
    
    def update_hangman_image(self):
        """Update the hangman image based on the number of wrong guesses."""
        # Display the image corresponding to the number of wrong guesses
        self.hangman_image.config(image=self.hangman_images[6 - self.attempts_left])

    def check_game_status(self):
        # Check if the player has won
        if "_" not in self.guessed_word:
            self.result_label.config(text="You Win!", fg="green")
            self.guess_button.config(state=tk.DISABLED)
        
        # Check if the player has lost
        elif self.attempts_left == 0:
            self.result_label.config(text=f"You Lose! The word was: {self.word}", fg="red")
            self.guess_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

