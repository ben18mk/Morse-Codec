# CR: Clean-Code - instead of lambda define a function
reversed_dict = lambda dictionary: { value: key for key, value in dictionary.items() }