'''
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    # blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    # blackjack_hand_greater_than(['K'], ['10'])
    False
    # blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
'''
def blackjack_hand_greater_than(hand_1, hand_2):
    def hand_value(hand):
        total = 0
        aces = 0
        special_char = ["J", "Q", "K"]
        for i, char in enumerate(hand):
            if char in special_char:
                hand[i] = "10"
            elif char == "A":
                aces += 1
        for char in hand:
            if char != "A":
                total += int(char)
        for _ in range(aces):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        return total
    total_1 = hand_value(hand_1)
    total_2 = hand_value(hand_2)
    if total_1 > 21:
        total_1 = 0
    if total_2 > 21:
        total_2 = 0
    return total_1.__gt__(total_2)

print(blackjack_hand_greater_than(["K","2","5"],["J","2","A","A"]))
