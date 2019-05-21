* `startEnabled`: (Boolean, default: `true`). Whether to enable the plugin on
  Anki startup. Note that the plugin can always be turned on and off via its
  toggle in the Tools menu.
* `injectFiles`: (Array (String), default: `[ "_global.css", "_global.html",
  "_global.js" ]`). Names of the files to inject. These files must be inside
  the `collection.media` directory. If one of the files is not found, it is
  silently ignored.
* `injectAtTail`: (Boolean, default: `false`) Inject the files at the end of the
  card instead of at the beginning. This won't have any effect if you're just
  using this for CSS, but for HTML and JS files it will obviously change
  where the content is placed or when the script is run, respectively.
