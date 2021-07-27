![Screenshot](https://github.com/jaxankey/Sankey-Flashcards/raw/main/screenshot.png)

# A Google Sheets Flashcard Web-App

Turn any published google sheet into Sankey-style flashcards on any device, and share your creation with a permanent html link.

# Linking the App to a Google Sheet

 1. Create a [Google Sheets](https://docs.google.com/spreadsheets/u/0/) document with a column for questions and a column for answers. The first row will be ignored, so you can use this as a column label. Add a few entries to play with.
 2. Select `File` -> `Publish to the web`, select the desired sheets and `Comma-separated values (.csv)'`, then push the green `Publish` button.
 3. Finish the process and return to the sheet itself, then copy its URL (or just the sheet id) from the browser's address bar, and paste this onto the end of the following URL: `https://jaxankey.github.io/Sankey-Flashcards/?`. See examples below.

# App Usage

 * After loading, the app will show the "question" from the first "card" (row 2, column A in your sheet). `Shuffle` will randomize the deck, `Flip` will reverse which column is used as the question, and `Edit` will take you to the Google Sheet.
 * Tapping the question or answer area will reveal the answer (column B).
 * Based on how well you did, you can choose how deep to move the card in the deck. The `Redo` button moves it 1 deep, the next buttons randomly move it to somewhere in the specified range, `???` moves it to a completely random location, and `Done` moves it to the bottom.
 * Your "score" will increase more depending on how deep you push each card. If you "play honestly", this can provide some sense of how well your "workout" is going. Tapping the score will reset it to zero.

# The Method

For a given card, I recommend starting with `Redo` until the card feels automatic, and then progressively upgrading the depth every time it becomes automatic again. Note cards will often regress back to "difficult", so expect to downgrade often throughout the process. 

# Examples
 * [Math Drills Google Sheet](https://docs.google.com/spreadsheets/d/1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c/)
 * [Sankey-Flashcards URL (Full)](https://jaxankey.github.io/Sankey-Flashcards/?https://docs.google.com/spreadsheets/d/1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c/edit#gid=0)
 * [Sankey-Flashcards URL (Short)](https://jaxankey.github.io/Sankey-Flashcards/?1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c).
