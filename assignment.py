import random
from colorama import Fore, Style, init
 
# Initialize colorama
init(autoreset=True)
 
# Lists of quotes for each category
motivational_quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. Winston Churchill",
    "Don’t watch the clock; do what it does. Keep going. Sam Levenson",
    "The only way to do great work is to love what you do. Steve Jobs",
    "The harder you work for something, the greater you’ll feel when you achieve it. Unknown.",
    "Believe you can and you're halfway there. Theodore Roosevelt",
    "Your limitation, it’s only your imagination. Unknown.",
    "Success usually comes to those who are too busy to be looking for it. Henry David Thoreau",
    "It’s not about perfect. It’s about effort.  Jillian Michaels",
    "Trying is the first step towards failure. Homer Simpson",
    "If something's hard to do, then it's not worth doing. Homer Simpson"
]
 
funny_quotes = [
    "Life is short. Smile while you still have teeth. Unknown",
    "To live is the rarest thing in the world. Most people just exist. Oscar Wilde",
    "Laughter is timeless, imagination has no age, and dreams are forever. Walt Disney",
    "Do more things that make you forget to check your phone. Unknown",
    "Life is a great big canvas; throw all the paint you can on it. Danny Kaye",
    "A day without laughter is a day wasted. Charlie Chaplin",
    "The best way to cheer yourself up is to try to cheer somebody else up. Mark Twain",
    "Dance like no one is watching. Sing like no one is listening. William W. Purkey",
    "Every day may not be good, but there is something good in every day. Unknown",
    "The most wasted of all days is one without laughter. E.E. Cummings"
]
 
meaningful_quotes = [
    "The unexamined life is not worth living. Socrates",
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit. Aristotle",
    "In the middle of difficulty lies opportunity. Albert Einstein",
    "The only thing necessary for the triumph of evil is for good men to do nothing. Edmund Burke",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. Ralph Waldo Emerson",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. Ralph Waldo Emerson",
    "Out of suffering have emerged the strongest souls; the most massive characters are seared with scars. Khalil Gibran",
    "Life can only be understood backwards; but it must be lived forwards. Søren Kierkegaard",
    "We are not human beings having a spiritual experience. We are spiritual beings having a human experience. Pierre Teilhard de Chardin",
    "He who has a why to live can bear almost any how. Friedrich Nietzsche"
]
 
# Function to display a random quote from a list with colored output
def get_random_quote(category):
    if category == 'motivational':
        return Fore.BLUE + random.choice(motivational_quotes)
    elif category == 'funny':
        return Fore.YELLOW + random.choice(funny_quotes)
    elif category == 'meaningful':
        return Fore.GREEN + random.choice(meaningful_quotes)
    else:
        return "Invalid category!"
 
# Function to ask if the user wants another quote or to go back to main menu
def ask_for_another_quote():
    while True:
        response = input("Would you like another quote in this category? (yes/no): ").lower()
        if response == 'yes':
            return True
        elif response == 'no':
            return False
        else:
            print("Please answer with 'yes' or 'no'.")
 
# Main program logic
def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        # Ask the user to choose a category
        category = input("Would you like a motivational, funny, or meaningful quote? (type 'exit' to quit): ").lower()
       
        if category == 'exit':
            print("Thanks for using the Random Quote Generator. Have a great day!")
            break
       
        if category in ['motivational', 'funny', 'meaningful']:
            # Show a random quote from the selected category
            print("\nHere's your quote:")
            print(get_random_quote(category))
           
            # Ask if the user wants another quote in the same category or go back to the main menu
            if ask_for_another_quote():
                continue  # Give another quote in the same category
            else:
                continue  # Go back to the main menu
        else:
            print("Sorry, that's not a valid category. Please choose 'motivational', 'funny', or 'meaningful'.")
 
if __name__ == "__main__":
    main()
 