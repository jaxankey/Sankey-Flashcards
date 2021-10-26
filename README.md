<p align="center"><img src="https://github.com/jaxankey/Sankey-Flashcards/raw/main/screenshots/screenshot.png"></p>

# A Google Sheets or CSV Flashcard Web-App

Turn any web-published CSV or [Google Sheet](https://docs.google.com/spreadsheets/u/0/) into Sankey-brand flashcards on any device, and share your creation with a permanent URL.

## Using Any Web-Published CSV File

Any URL pointing to a CSV file will work, provided the CSV file has two columns: the first column contains the "questions", and the second column contains "answers". The first row will be skipped (use this for column labels!), as will any rows with blank entries in the first or second column. Once you have this web address, paste it to the end of this: 

[https://jaxankey.github.io/Sankey-Flashcards/?](https://jaxankey.github.io/Sankey-Flashcards/?)

as in the examples below. Bookmark the resulting web address. :)

## Using a Google Sheet

 1. Create a [Google Sheets](https://docs.google.com/spreadsheets/u/0/) document with columns conforming to the above specifications.
 2. Select `File` -> `Publish to the web`, choose the desired sheets, select `Comma-separated values (.csv)'`, then push the green `Publish` button.
 3. Type `ctrl`+`c` to copy the gnasty web address shown in this dialog, then
 4. Bookmark this URL :).

## App Usage

### Basic Controls

 * Tapping the upper (blue) question or lower (red) answer area will reveal the question or answer, respectively.
 * Based on how well you think you did, choose how deep to move the card in the stack. The `+` button moves the card to a random position beyond the other ranges, and the smiley face removes it until you push `Reset`.
 * Your "score" will increase depending how deep into the deck you send each card, which (if you play honestly) provides some sense of how well your "workout" is going. 

### Other Controls

 * `Reset` will return the deck to its original, ordered state.
 * `Shuffle` will randomize the remaining deck.
 * `Flip` will reverse questions and answers.
 * Tapping `Score` will reset it to zero.
 * Tapping `Remaining` will re-add all the cards previously marked `Done` to the end of the stack.
 * The first pull-down menu above the question and answer areas (`Silent` by default) will select a spoken language (if speech synthesis is available on your browser).
 * The second pull-down above the answers sets the delay before automatically showing the card.
 * The third pull-down above the answers sets whether you must manually tap the depth, or let it automatically choose the depth after you tap the answer area.

## The Method

If you get a card wrong or have difficulty, tap `1-2` until it feels automatic, and then progressively upgrade the depth, waiting at each stage until it again becomes automatic. When it's automatic a few times at a high depth, tap the smiley face to remove it from the loop. 

Note: Definitely expect your fluency to often regress and downgrade the depth when needed! Downgrading is not a bad thing.

## Examples
 * [Addition and German Google Sheet](https://docs.google.com/spreadsheets/d/1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c/)
 * [Sankey-Flashcards URL for Addition Tab](https://jaxankey.github.io/Sankey-Flashcards/?https://docs.google.com/spreadsheets/d/e/2PACX-1vRucOWbqLrh-TtaDR0-vazl4rVXhWk0BqR5_5rsFNV3698zid1JQuK_n-2lVUogwxl1OvGpVkQ3zg6L/pub?gid=0&single=true&output=csv)
