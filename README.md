# Flash Cards Application

## Overview
This Python script creates a flashcard application to help users learn French vocabulary. It uses the `tkinter` library for the graphical user interface (GUI) and `pandas` for handling data. The app displays French words on flashcards and prompts users to recall the English translations.

## About the files
Main.py is the main file that contains entire code. Card_front and card_back are the images used for background. Similarly, right and wrong are the images used for cross and correct buttons. Last but not the least, french_words is the csv file containing the data.

## Features
- **Interactive Flashcards**: Displays French words and flips to show English translations.
- **Progress Tracking**: Saves progress by removing known words from the list.
- **User-Friendly Interface**: Easy-to-use buttons to navigate through flashcards.


### Imports and Global Variables
- Import necessary libraries:
  ```python
  import pandas
  from tkinter import *
  import random
  ```
- Define global variables:
  ```python
  BACKGROUND_COLOR = "#B1DDC6"
  current_card = {}
  to_learn = {}
  ```

### Loading Data
- Load words from `words_to_learn.csv` or `french_words.csv`

### Function `next_card`
- Display a new random French word
 
### Function `flip_cards`
- Flip the card to show the English translation

### Function `is_known`
- Remove known word and save progress

### Setting up the User Interface
- Initialize the main window and canvas

### Start the Application
- Display the first card and start the main loop


This README file provides a comprehensive yet brief overview of the project, including installation, usage, and an explanation of the code structure.
