spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # esto corta la ejecucion del whie y sigue con la otra vuelta
    print('spam is ' + str(spam))
