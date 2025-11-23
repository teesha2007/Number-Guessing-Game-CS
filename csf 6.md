# Future Improvements

While the current version is functional and robust, the following features would enhance the game's complexity and user experience:

1.  **Difficulty Levels:** Implement a feature that allows the user to select the guessing range (e.g., Easy: 1-10, Medium: 1-100, Hard: 1-1000). This would require modifying the `random.randint()` parameters based on user input.
2.  **High Score Tracking:** Save the lowest successful attempt count for a user into an external file (e.g., a `.txt` or `.json` file). This would require file I/O operations in Python and would make the game competitive across sessions.
3.  **Limited Attempts Mode:** Introduce an optional mode where the player only has a set number of guesses (e.g., 7) to win, failing which the game ends. This introduces a strategic element.