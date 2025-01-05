# blackjack-game
This is a Python implementation of the classic casino game Blackjack. The game follows standard Blackjack rules and includes a user-friendly text-based interface for gameplay.

## Features
- Simulates a game of Blackjack between a player and the computer (dealer).
- Includes standard Blackjack rules:
  - Deck is unlimited in size.
  - No jokers; Ace can count as 11 or 1.
  - Jack, Queen, and King all count as 10.
  - Cards are not removed from the deck after being drawn.
- Provides prompts for the user to hit or stand.
- Handles special cases like adjusting the value of an Ace when the total exceeds 21.
- Determines the game outcome with clear win/loss conditions.

## How to Play
1. Run the `Blackjack.py` file in your terminal or Python IDE.
2. Follow the on-screen instructions to start the game.
3. Make decisions by typing "hit" to draw another card or "stand" to hold your current total.
4. The game will announce the winner based on Blackjack rules.

## Requirements
- Python 3.7 or higher
- No additional libraries are required.

## How to Run
1. Clone this repository:
bash
   git clone https://github.com/Zar1717/blackjack-game.git
2. Navigate to the project folder:
   
bash
   cd blackjack-game
3. Run the game:
bash
   python Blackjack.py


Notes:

- Ensure your terminal supports Unicode characters for the game's visual components.
- The art.py file must be present in the same directory for the Blackjack logo to display correctly.


Future Improvements:

- Add multiplayer functionality.
- Implement a betting system for chips or points.
- Enhance the interface with a graphical version.
