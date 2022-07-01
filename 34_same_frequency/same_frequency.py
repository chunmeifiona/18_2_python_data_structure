def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    st1 = str(num1)
    st2 = str(num2)
    dic1 = {key:st1.count(key) for key in set(st1)}
    dic2 = {key:st2.count(key) for key in set(st2)}
    return dic1==dic2
