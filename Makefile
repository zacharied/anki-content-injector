# Files that don't belong in plugin
NOPLUG = .git .gitignore Makefile README.md $(ZIPFILE)

ZIPFILE := global-css.zip

plugin:
	zip -r $(ZIPFILE) $(filter-out $(NOPLUG), $(wildcard *))	

.PHONY: plugin
