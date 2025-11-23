# Development Process and Version Control

## Building the Application
The game was developed incrementally in VS Code following these logical stages:

1.  **Initialization:** The project folder was created, and `git init` was executed. A `.gitignore` file was added to exclude unnecessary local files.
2.  **Core Logic:** The `random.randint` function was used to select the secret number, and the main `while` loop was implemented to keep the game running until the guess matched the target.
3.  **Feedback System:** Conditional statements (`if/elif`) were added inside the loop to provide the necessary "Too High" or "Too Low" feedback.
4.  **Error Handling (Innovation):** A `try-except ValueError` block was implemented around the user input mechanism. This ensures that the application does not crash if the user types letters instead of numbers, significantly improving its real-world usability.

## Git Workflow Highlights
Development was strictly managed using Git and pushed to GitHub. A few key commits demonstrating the workflow include:

* `git commit -m "Feat: Implemented core game logic (random number generation and loop)"` - Focused on initial functionality.
* `git commit -m "Refactor: Added 'try-except' block for robust input validation"` - Focused on improving stability.
* `git commit -m "Docs: Setup README and documentation structure"` - Focused on meeting documentation requirements.