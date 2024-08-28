for w in range(2, 30):
    primo = True
    for i in range(2, w):
        if (w % i == 0):
            primo = False
    if primo:
       print (w)

