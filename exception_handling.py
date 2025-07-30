def reciprical(value):
    try:
        r= 1 / value
        print("reciprical of "+str(value)+" is "+ str(r))
    except:
        print("Cannot find reciprical of "+str(value))

reciprical(5)
reciprical(0)
reciprical(-3)
reciprical("a")
