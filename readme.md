# pokerhands
A Python class for comparing two poker hands

A poker hand consists of five unique playing cards. When betting is complete, players show each other their hands and the one with the stronger hand wins the prize pot. This class contains a method for comparing two poker hands to determine the winner.

Cards are represented as strings showing the number and suit of a card, for example 7C for the 7 of clubs. Tens, aces, jacks, queens and kings are represented by T, A, J, Q and K respectively and the four suits are (D)iamonds, (H)earts, (S)pades and (C)lubs. Aces can be either high or low and suit rankings are not considered.

The PokerHand function takes a string representing the five cards. For example 'AC 4S 6D TH KD' represents the ace of clubs, 4 of spades, 6 of diamonds, ten of hearts and king of diamonds.

The compare_with method can be called on a hand object and takes one argument, another hand object, to determine the winner. It returns 'Win' if the first hand is stronger, 'Loss' if the second hand is stronger and 'Tie' if both hands are equally strong.
