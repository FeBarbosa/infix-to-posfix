# Infix to postfix
This project convert a regular expression in infix form to postfix form. The suported operands are:
* \* : Kleene star
* \+ : concatenation
* . : union

### EX:

**input**: x + y + (5 . z) * + 2

**output**: x y + 5 z . * + 2 +