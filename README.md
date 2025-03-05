# Blind-Auction

A Python program that simulates a blind auction where bidders can't see each other's bids. The program collects bids from multiple users and determines the winner with the highest bid.

## Concepts Implemented

- **Dictionaries**: Using Python dictionaries to store bidder names and their bids
- **Control Flow**: Using while loops and conditional statements
- **User Input**: Taking and processing user input
- **Screen Clearing**: Maintaining bid privacy by clearing the console after each bid
- **List Methods**: Converting dictionary keys and values to lists for processing
- **Maximum Function**: Finding the maximum bid value

## Files

- [`main.py`](Blind-Auction/main.py): The main script that runs the auction program
- [`art.py`](Blind-Auction/art.py): Contains ASCII art for the program logo
- `README.md`: This file
- `LICENSE`: MIT license for the project

## How to Use

1. Run the `main.py` script
2. For each bidder:
   - Enter the bidder's name
   - Enter their bid amount
   - Indicate if there are more bidders
3. When all bids are collected, the program will display the winner and their bid

## Example

```sh
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

What is your name? : John
What is your bid? : $500
Are there any other bidders? Type 'yes or 'no'.
yes

[screen clears for next bidder]

What is your name? : Alice
What is your bid? : $750
Are there any other bidders? Type 'yes or 'no'.
no

The winner is Alice with a bid of $750.
