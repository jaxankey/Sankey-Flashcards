# Basic Sankey-Style Flashcards
Turn any published google sheet into Sankey-style flashcards on any internet-connected device, and share your creation with an html link.

# Getting Started

 1. Create a [Google Sheets](https://docs.google.com/spreadsheets/u/0/) document with a column for questions and a column for answers. The first row will be ignored, so you can use this as a column label. Add a few entries to play with.
 2. Select `File` -> `Publish to the web`, select the first sheet (e.g. `Sheet0`) and `Comma-separated values (.csv)'`, then push the green `Publish` button.
 3. Finish the process and return to the sheet itself, then copy its URL (or just the sheet id) from the browser's address bar.
 4. Paste this onto the end of the following URL: `https://jaxankey.github.io/Sankey-Flashcards/?`.

Okay, so maybe assembling the URL is a bit painful, but once you have done this correctly, it is a permanent link that will update whenever you change your google sheet.

# Examples
 * [Math Drills Google Sheet](https://docs.google.com/spreadsheets/d/1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c/)
 * [Sankey-Flashcards URL (Full)](https://jaxankey.github.io/Sankey-Flashcards/?https://docs.google.com/spreadsheets/d/1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c/edit#gid=0)
 * [Sankey-Flashcards URL (Short)](https://jaxankey.github.io/Sankey-Flashcards/?1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c).

# Usage
 * After loading, the app will show you the "question" part of the "top card" from your "deck", which is the first entry (row 2, column A) in your sheet. You can also push `Shuffle` to shuffle the deck.
 * Tapping anywhere will reveal the "answer" (column B).
 * Based on how you did, you can decide how deep to push this card into the deck. `Redo` will push it 1 deep (you'll get it right after the next card), some buttons give ranges of depths, `???` will push it to a random location in the deck, and `Done` will push it to the bottom.

I recommend using `Redo` until your answer is immediate and the card feel "boring". Then progressively increase its depth, waiting at each stage until it is again "boring". Your meaningless "score" will increase more depending on how deep you push each card. Obviously you can cheat and get an enormous score without learning anything, but if you use the system right, the score should give you a sense of how well your "workout" went.
