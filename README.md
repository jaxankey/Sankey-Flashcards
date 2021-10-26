<p align="center"><img src="https://github.com/jaxankey/Sankey-Flashcards/raw/main/screenshots/screenshot.png"></p>

# A Google Sheets Flashcard Web-App

Turn any published google sheet into Sankey-style flashcards on any device, and share your creation with a permanent html link.

## Linking the App to a Google Sheet

 1. Create a [Google Sheets](https://docs.google.com/spreadsheets/u/0/) document with a column for questions and a column for answers. The first row will be ignored, so you can use this as a column label. Add a few entries to play with.
 2. Select `File` -> `Publish to the web`, select the desired sheets and `Comma-separated values (.csv)'`, then push the green `Publish` button.
 3. Type `ctrl`+`c` to copy the gnasty URL from this and paste this onto the end of the following URL: `https://jaxankey.github.io/Sankey-Flashcards/?`. See example below.
 4. Bookmark this URL :).
 
## App Usage

### Basic Controls

 * Tapping the upper (blue) question or lower (red) answer area will reveal the question or answer (columns A or B, respectively).
 * Based on how well you did, choose how deep to move the card in the remaining cards. The `Redo` button moves it 1 deep, the next buttons randomly move it to somewhere in the specified range, `8-?` moves it to a random depth 8 or higher, and `Done` removes the card from the deck (just for the session).
 * Your "score" will increase more depending on how deep you push each card. If you "play honestly", this can provide some sense of how well your "workout" is going. 

### Other Controls

 * `Shuffle` will randomize the deck
 * `Flip` will reverse questions and answers 
 * `Edit` will take you to the Google Sheet
 * Tapping the `Score` area will reset it to zero.
 * Tapping the `Remaining` area will re-add all the cards previously marked `Done`.
 * The pull-down menus above the question and answer areas (`Silent` by default) will select a spoken language (if speech synthesis is available on your browser).

## The Method

If you get a card wrong or have difficulty, tap `Redo` until it feels automatic, and then progressively upgrading the depth, waiting at each stage until it again becomes automatic. When it's automatic a few times at a high depth, you can use `Done` to remove it from the loop. Note cards *will* often regress back to "difficult", so expect to downgrade often throughout the process. 

## Examples
 * [Addition and German Google Sheet](https://docs.google.com/spreadsheets/d/1IfWy8aefe9aNUO3OJ2bKv2Vtb28eEx2XUfMyYPiZv8c/)
 * [Sankey-Flashcards URL for Addition Tab](https://jaxankey.github.io/Sankey-Flashcards/?https://docs.google.com/spreadsheets/d/e/2PACX-1vRucOWbqLrh-TtaDR0-vazl4rVXhWk0BqR5_5rsFNV3698zid1JQuK_n-2lVUogwxl1OvGpVkQ3zg6L/pub?gid=0&single=true&output=csv)
