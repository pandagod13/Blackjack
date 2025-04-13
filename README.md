# Blackjack Game

A simple command-line implementation of the classic Blackjack card game written in Python.

## Description

This project is a text-based Blackjack game where players can play against a dealer controlled by the computer. The game implements standard Blackjack rules, including card values, hit/stand decisions, and win conditions.

## Features

- Play multiple games in a row
- Standard deck of 52 cards
- Proper handling of Aces (worth 11 or 1 depending on hand value)
- Dealer stands on 17 or higher
- Detection of Blackjack (21 on first two cards)
- Text-based user interface with clear prompts
- Hidden dealer's first card until the end of the game

## Requirements

- Python 3.x
- No external libraries required

## How to Play

1. Run the program:
   ```
   python main.py
   ```
2. Enter the number of games you want to play
3. For each game:
   - You'll be dealt two cards, and the dealer will receive two cards (one face down)
   - Choose to "Hit" (get another card) or "Stand" (keep your current hand)
   - The dealer will then play according to fixed rules (must hit until 17 or higher)
   - The winner is determined based on who has the higher hand value without going over 21

## Game Rules

- Number cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10
- Aces are worth 11, but become 1 if the total would exceed 21
- The goal is to get closer to 21 than the dealer without going over
- Going over 21 is a "bust" and results in losing
- If both player and dealer have the same value, it's a tie
- A "blackjack" (21 with first two cards) beats any other 21 combination

## Project Structure

- `Deck`: Manages the creation, shuffling and dealing of cards
- `Card`: Represents individual cards with suits and ranks
- `Hand`: Manages the player's and dealer's hands, calculating values
- `Game`: Controls game flow, user input, and win condition checks

## Future Improvements

- Add betting functionality
- Support for multiple players
- Graphical user interface
- Additional game options (insurance, split, double down)