def custom_encoder(string):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    position = []
    string = string.lower()
    for char in string:
        if char in reference_string:
            position.append(reference_string.index(char))
        else: 
            position.append(-1)
    return position

