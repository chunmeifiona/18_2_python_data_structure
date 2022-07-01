def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    openlist =[]
    for p in parens:
        if p == '(':
            openlist.append('(')
        elif p == ')' and len(openlist) != 0:
            openlist.pop()
        elif p == ')' and len(openlist) == 0:
            return False
    return len(openlist) == 0

    
    