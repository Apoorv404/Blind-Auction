from art import logo

print(logo)
should_continue = True
bids = {}

while should_continue:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    print("\n" * 100 )
    if other_bidders == "no":
        should_continue = False
        values = list(bids.values())
        keys = list(bids.keys())
        highest_bid = max(values)
        winner = keys[values.index(highest_bid)]
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
