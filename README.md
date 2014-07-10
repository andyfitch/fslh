fslh - font-size & line-height generator
====

A Sublime Plugin which generates font-size and line-height em values based on px values

If you find yourself using Spotlight Search's maths functions or Calculator to figure out font-size and line-height em values

Example
You want to use em units for fonts & your base font-size is 15px. You'd like a font-size of 20px, line-height of 24px

.my-class {
	15/20/24
}

Highlight 15/20/24 & press your keybinding (see fslh.sublime-keymap for an example, mine uses Cmd+Shift+L), and the result will be:

.my-class {
	font-size: 1.3333333333em;
	line-height: 1.2em;
}