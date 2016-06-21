
.PHONY: default
default:
	zip -r Wurst.sublime-package .

.PHONY: clean
clean:
	rm -r Wurst.sublime-package
