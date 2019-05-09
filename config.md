* `startEnabled`: (Boolean, default: `true`). Whether to enable the plugin on
  Anki startup. Note that the plugin can always be turned on and off via its
  toggle in the Tools menu.
* `cssFile`: (String, default: `"_global.css"`). Name of the file to inject.
  This file must be inside the `collection.media` directory.
* `loadAtHead`: (Boolean, default: `false`) Injects the CSS before the
  question/answer HTML instead of after. I don't know if this will actually
  affect anything, but if you run into issues try changing this; let me know
  if it does anything.
