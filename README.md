# anki-content-injector

[Anki add-on ID: 166455199](https://ankiweb.net/shared/info/166455199)

*Current version: 0.3*

## Overview

This is an add-on for [Anki 2.1](https://apps.ankiweb.net) that allows for a
the insertion of arbitrary HTML, CSS, and JavaScript content into cards before
they are displayed. It can be used in a similar fashion to [Arthaey's similar
add-on for Anki 2.0](https://github.com/Arthaey/anki-global-css) to keep a
global stylesheet whose rules are applied to every card. However, beyond its
support of additional content types, it has a number of advantages over
Arthaey's add-on:

* A restart is not needed to reload the HTML/CSS/JS content; it is injected into
  the template at render-time using the `prepareQA` hook added in 2.1.0b16. In
  fact, this is more or less just a thin wrapper around `prepareQA`.
* Template-local CSS still applies (Arthaey's add-on replaced the template CSS
  instead of adding to it).
* Support for more than one file.
* Global HTML/CSS/JS can be toggled without having to delete or move the file(s).

Do note that this plugin makes no changes to the content of your cards; all
changes are limited to when the card is being rendered. Be sure that your
decks work without your injection files before sharing them with others!

## Instructions

First, install the add-on from Anki's menu with the above ID.

Place any of the files `_global.html`, `_global.css`, and `_global.js` in
your profile's `collection.media` directory. With default settings, these
files will be injected into your cards.

## Configuration

* `startEnabled`: (Boolean, default: `true`). Whether to enable the plugin on
  Anki startup. Note that the plugin can always be turned on and off via its
  toggle in the Tools menu.
* `injectFiles`: (Array (String), default: `[ "_global.css", "_global.html",
  "global.js" ]`). Names of the files to inject. These files must be inside
  the `collection.media` directory. If one of the files is not found, it is
  silently ignored.
* `injectAtTail`: (Boolean, default: `false`) Inject the files at the end of the
  card instead of at the beginning. This won't have any effect if you're just
  using this for CSS, but for HTML and JS files it will obviously change
  where the content is placed or when the script is run, respectively.

## Support

The code for this project is on
[GitHub](https://github.com/zacharied/anki-global-css).

If you discover an error or have a request, submit an
[issue](https://github.com/zacharied/anki-global-css/issues/new).

Feel free to write reviews on the plugin page but I cannot guarantee that I
will check them; GitHub is the better way to get my attention.

## Building & packaging

Please ignore this section if you just want to use the add-on. This is for
add-on developers only.

Development on this add-on is simple. All code is in the `__init__.py` file.
The Makefile will create everything needed to upload the add-on to AnkiWeb.
Then, go to the AnkiWeb add-on portal and choose to update the plugin. Choose
the created `content-injector.zip` archive as the plugin file, and then paste
the contents of the new `description.html` into the description field.

## License

This addon is licensed under the same license as Anki itself (GNU Affero General
Public License 3).
