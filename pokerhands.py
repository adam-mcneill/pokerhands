class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        # Determine whether or not all five cards are the same suit.
        # If not, suits can be ignored completely
        isFlush = False
        for suit in ('C', 'D', 'H', 'S'):
            if hand.count(suit) == 5:
                isFlush = True

        # Build a list of the card numbers, starting from 2 -> 0 and
        # ending with A -> 12
        numbers = ['23456789TJQKA'.find(ch) for ch in hand
                   if ch in '23456789TJQKA']
        numbers.sort()

        # Build a dictionary of how many of each number there are
        counts = {}
        for i in numbers:
            counts.setdefault(i, 0)
            counts[i] += 1

        # Determine whether the hand is a straight
        if numbers == list(range(min(numbers), min(numbers) + 5)) or \
           numbers == [2, 3, 4, 5, 12]:
            isStraight = True
        else:
            isStraight = False

        # Determine the hand, and which numbers are significant.
        # The significance property is a list of numbers used to break
        # ties between hands of the same rank. If the hand is a full house
        # with three 3s and two 9s for example, this will be [3, 9]
        if isFlush and isStraight:
            self.handLevel = 8  # Straight flush
            self.significance = numbers
            
        elif 4 in counts.values():
            self.handLevel = 7  # Four of a kind
            self.significance = [numbers[2]] + \
                                [x for x in numbers if x != numbers[2]]
            
        elif 3 in counts.values() and 2 in counts.values():
            self.handLevel = 6  # Full house
            self.significance = [numbers[2]] + \
                                [x for x in numbers if x != numbers[2]]
            
        elif isFlush:
            self.handLevel = 5  # Flush
            self.significance = list(reversed(numbers))
            
        elif isStraight:
            self.handLevel = 4  # Straight
            self.significance = numbers
            
        elif 3 in counts.values():
            self.handLevel = 3  # Three of a kind
            self.significance = [numbers[2]] + \
                                sorted([x for x in numbers if x != numbers[2]],
                                       reverse=True)
            
        elif list(counts.values()).count(2) == 2:
            self.handLevel = 2  # Two pair
            self.significance = list(counts.keys())
            self.significance.sort(key=lambda z: counts[z], reverse=True)
            self.significance = sorted(self.significance[:2], reverse=True) + \
                           self.significance[2:]
            
        elif 2 in counts.values():
            self.handLevel = 1  # Pair
            self.significance = list(counts.keys())
            self.significance.sort(key=lambda z: counts[z], reverse=True)
            self.significance = [self.significance[0]] + \
                           sorted(self.significance[1:], reverse=True)
            
        else:
            self.handLevel = 0  # High card
            self.significance = list(reversed(numbers))
        
    def compare_with(self, other):
        if self.handLevel > other.handLevel:
            return 'Win'
        elif other.handLevel > self.handLevel:
            return 'Loss'
        else:
            # Use significance to determine the winner
            for i in range(len(self.significance)):
                if self.significance[i] > other.significance[i]:
                    return 'Win'
                elif other.significance[i] > self.significance[i]:
                    return 'Loss'
            return 'Tie'

