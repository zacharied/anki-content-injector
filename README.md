# anki-global-css

[Anki add-on ID: 166455199](https://ankiweb.net/shared/info/166455199)

*Current version: 0.2*

## Overview

This is an add-on for [Anki 2.1](https://apps.ankiweb.net) that allows for a
universal CSS file to be applied to all card templates. It is heavily inspired
by [Arthaey's similar add-on for Anki
2.0](https://github.com/Arthaey/anki-global-css) but brings with it a number of
useful improvements.

* A restart is not needed to reload the CSS file; it is injected into the
  template at render-time using the `prepareQA` hook added in 2.1.0b16
* Template-local CSS still applies (Arthaey's add-on replaced the template CSS
  instead of adding to it)
* Global CSS can be toggled without having to delete or move the CSS file

## Instructions

Place a file `_global.css` in your profile's `collection.media` directory. This
file should contain all the CSS rules you want to apply globally.

## Configuration

* `startEnabled`: (Boolean, default: `true`). Whether to enable the plugin on
  Anki startup. Note that the plugin can always be toggled via the "Tools" menu
* `cssFile`: (String, defualt: `"_global.css"`). Name of the file to inject.
  This file must be inside the `collection.media` directory.
* `loadAtHead`: (Boolean, default: `false`) Injects the CSS before the
  question/answer HTML instead of after. I don't know if this will actually
  affect anything, but if you run into issues try changing this; let me know
  if it does anything.

## Support

The code for this project is on
[GitHub](https://github.com/zacharied/anki-global-css).

If you discover an error or have a request, submit an
[issue](https://github.com/zacharied/anki-global-css/issues/new).

Feel free to write reviews on the plugin page but I cannot guarantee that I
will check them; GitHub is the better way to get my attention.

## License

This addon is licensed under the same license as Anki itself (GNU Affero General
Public License 3).
