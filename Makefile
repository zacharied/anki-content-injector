# Files that don't belong in plugin
NOPLUG = .git .gitignore Makefile README.md $(DESCRIPTION) $(PACKAGE)

DESCRIPTION := description.html
PACKAGE := content-injector.zip

SHELL := /bin/bash

all: document readme plugin

# Convert the readme to an HTML file formatted to fit the add-on website's
# supported tags.
document: readme
	pandoc --to=html < README.md | tail -n+3 | sed -E \
		-e 's,</?p>,,g' \
		-e 's,<em>(.*)</em>,<i>\1</i>,' \
		-e 's,<i>Current version: [0-9.]*,\0 (Commit $(shell git rev-parse --short HEAD)),' \
		-e 's,<ul>\\n,<ul>,' \
		-e 's,<h2.*\">(.*)</h2>,|<b>\1</b>,g' | tr '|' '\n' \
		| awk '/\<\/?(ul|li)\>$$/ { printf("%s", $$0); next } 1' \
		> description.html

# Paste the plugin options into the README.md
readme:
	sed -i '/## Configuration/,/## Support/!b;//!d;/## Support/e echo \; cat config.md \; echo' README.md

# The archive to be uploaded to the add-on repo.
plugin:
	zip -r $(PACKAGE) $(filter-out $(NOPLUG), $(wildcard *))

clean:
	rm $(DESCRIPTION) $(PACKAGE)

.PHONY: all
