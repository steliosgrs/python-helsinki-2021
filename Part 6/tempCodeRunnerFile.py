    if name =="":
        raise ValueError("The string is emtpy")
    if name.find(" ")== False: 
        raise ValueError("The string contains less than two words")
    if len(name)> 40: 
        raise ValueError("The string  is longer than 40 characters")
    if age < 0: 
        raise ValueError("The age is a negative number")
    if age > 150:
        raise ValueError("The age is greater than 150")