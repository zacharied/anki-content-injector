# Files that don't belong in plugin
NOPLUG = .git .gitignore Makefile README.md description.html $(ZIPFILE)

ZIPFILE := global-css.zip

SHELL := /bin/bash

all: document plugin

document:
	pandoc --to=html < README.md | tail -n+2 | sed -E \
		-e 's,</?p>,,g' \
		-e 's,<em>(.*)</em>,<i>\1</i>,' \
		-e 's,<ul>\\n,<ul>,' \
		-e 's,<h2.*\">(.*)</h2>,|<b>\1</b>,g' | tr '|' '\n' \
		| awk '/\<\/?(ul|li)\>$$/ { printf("%s", $$0); next } 1' \
		> description.html

plugin:
	zip -r $(ZIPFILE) $(filter-out $(NOPLUG), $(wildcard *))	
