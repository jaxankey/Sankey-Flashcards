# Simple Sankey Flashcard Web-App
Turn any published google sheet into Sankey flashcards and share your creation with an html link.

# Linking the App to a Google Sheet

 1. Create a [Google Sheets](https://docs.google.com/spreadsheets/u/0/) document with a column for questions and a column for answers. The first row will be ignored, so you can use this as a column label. Add a few entries to play with.
 2. Select `File` -> `Publish to the web`, select the first sheet (e.g. `Sheet0`) and `Comma-separated values (.csv)'`, then push the green `Publish` button.
 3. Finish the process and return to the sheet itself, then copy its URL (or just the sheet id) from the browser's address bar.
 4. Paste this onto the end of the following URL: `https://jaxankey.github.io/Sankey-Flashcards/?`. See examples below.

# App Usage
 * After loading, the app will show the "question" part of the first "card" (row 2, column A in your sheet). You can also tap `Shuffle` to shuffle the deck.
 * Tapping anywhere on the screen will reveal the "answer" (column B).
 * Based on how well you did, you then decide how deep to push the card into the deck. The first button (`Redo`) will push it 1 deep, the next buttons push to a randomized range of depths, `???` will push it to a random location in the whole deck, and `Done` will push it to the bottom.

I recommend using `Redo` until the card feel "boring", then progressively upgrade the depth for each card, waiting at each stage until it is again "boring". Cards will often regress from "boring" back to "difficult", so expect to downgrade often. Your "score" will increase more depending on how deep you push each card. If you "play honestly", this can provide some sense of how well your "workout" went. You can reset the score to 0 with the `Reset` button.

# Examples
 * [Math Drills Google Sheet](https://docs.google.com/spreadsheets/d/1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c/)
 * [Sankey-Flashcards URL (Full)](https://jaxankey.github.io/Sankey-Flashcards/?https://docs.google.com/spreadsheets/d/1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c/edit#gid=0)
 * [Sankey-Flashcards URL (Short)](https://jaxankey.github.io/Sankey-Flashcards/?1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c).
