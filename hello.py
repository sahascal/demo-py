def say_hi(name='Sam'):
    if name =='':
        print("You didn't enter a name")
    else:
        print("Hi! there")
        for letter in name:
            print(letter)
    