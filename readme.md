wurst-sublime
=============

This package is the barebones syntax highlighter for wurst in sublime-text. It
is a stripped-down copy of the Sublime Text 2 Python syntax highlighter.

* Support is basic for both Wurst and Jurst.
* Has been tested with Sublime Text 2 in Windows 7 x64

Installation
------------

* Zip up `Completion Rules.tmPreferences` and `Wurst.tmLanguage` into a zip
file.
* Rename the zip file `Wurst.sublime-package`
* Copy the package into `C:\Program Files\Sublime Text 2\Pristine Packages` or
equivalent
* Restart Sublime Text.

`*.wurst` and `*.jurst` should syntax-highlight automatically. If not, select
Wurst from View -> Syntax.

Contributing
------------

I will accept well-formed commits that:

* Don't regress the current highlighter
* Have good meta-data:
    - Use [Imperative Mood](http://chris.beams.io/posts/git-commit/#imperative)
    in commit messages
    - Large commits should have verbose commit messages
* Don't cause conflicts
* Follow coding standards:
    - JSON and JSON-like:
        * Spaced comment-style like `// hello world`
    - Markdown:
        * 79-character limit except in unusual circumstances
    - Python:
        * Full PEP8 validity
        * Big lists of data should be extracted and included
        * Variables and methods with `underscore_style`
        * Descriptive, rather than terse, method and variable names
        * No code commented out
        * Logical blocks of code need good comments

I welcome issues in the issue tracker, but make no guarantees whatsoever about
my response to them.
