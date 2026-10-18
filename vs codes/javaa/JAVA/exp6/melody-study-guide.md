# Learn Melody in patterns

## 1. Remember the page tree

```text
html
  head → title, style, script
  body
    header → brand
    page
      main → song title
        song
          player → buttons, audioBox, videoBox
          lyrics → pre
      aside → table, lists, links
    footer → feedback form
```

Start by typing this structure. Fill each section afterwards.

## 2. CSS has one repeating sentence

`selector { property: value; }`

Example: `.player { text-align: center; }`

Read it as: select the player, set text alignment to center.

- `body` selects a tag.
- `.player` selects `class="player"`.
- A comma means apply the same rules to several selectors.
- `display: flex` places children beside each other.
- `gap` gives space between those children.
- `flex: 3` and `flex: 1` divide the available flexible space in a 3:1 ratio.
- Player and lyrics both use `flex: 1`, so they share space equally.
- `min-width: 0` lets a column shrink instead of overflowing.
- `width: 95%` follows the column width; `max-width: 480px` limits enlargement.
- `margin: auto` centers the media horizontally.
- `white-space: pre-wrap` preserves lyrics' spaces and line breaks, while wrapping long lines.
- The media query changes rows to columns when the screen is 700px wide or less.

Colours and exact pixel values are design choices. Learn what the property does first.

## 3. Toggle = find, hide/show, pause

`document.getElementById("videoBox")` finds the element with `id="videoBox"`.

`hidden = true` means hide it. `hidden = false` means show it.

| Button | audioBox | videoBox | Pause |
|---|---|---|---|
| Audio | false | true | video |
| Video | true | false | audio |

The two functions repeat the same pattern with opposite values.

`onclick="showAudio()"` connects a button click to the function.
`pause()` stops the other media from playing in the background.
Switching pauses the other mode; it does not automatically start or synchronize playback.

## 4. Let HTML check the form

- `required`: the field cannot be empty.
- `type="email"`: the browser checks basic email format. It does not verify that an address exists.
- `type="number" min="1"`: a number of at least 1.
- `type="submit"`: checks the fields, then runs the form's submit handler if valid.
- `type="reset"`: restores the form's original field values.
- `return false`: prevents page navigation/submission after the thank-you alert.

This version does not use an email regex. If your examiner explicitly requires JavaScript email validation using a regex, that requirement needs the original validation function.

## 5. Repeated HTML patterns

Table: `table → tr → th` for headings, `table → tr → td` for data.

Lists: `ul → li` for bullets; `ol → li` for numbers. Put an ordered list inside an album's list item.

Media: `src` gives the filename; `controls` asks the browser to show playback controls.

Link: `href` gives the destination; `target="_blank"` opens another tab.

Lyrics: paste text inside `<pre>`. No `<br>` needed.

Keep `cover.jpg`, `song.mp3`, and `song.mp4` beside the HTML file.

## Practice order

1. Type the page tree without styling.
2. Add the two Flexbox rows.
3. Add one table row, then repeat its pattern.
4. Add the nested lists and links.
5. Add the form and its built-in checks.
6. Type showAudio, then use its opposite pattern for showVideo.
7. Add colours, spacing, and heading styling last.
