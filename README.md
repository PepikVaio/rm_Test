# reMarkable stickers for xovi

This is a xovi extension which adds the following functionality

- save the clipboard to a file
- read a saved clipboard from file and convert to scene items
- change the color, pen or thickness of scene items (e.g. from the clipboard)

In order to handle saved clipboards, to be used as stickers, it also contains functionality to
- ensure that a certain directory exists
- delete a file (use carefully!)

The repository (and the built binary) also contains a qmd file which adds a stickers button to the toolbar, but developers can also make their own.

Currently the methods for changing thickness of strokes does not change the bounding 