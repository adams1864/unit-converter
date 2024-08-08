while True: 
    #Ask user to enter a value of a kilometer
    value = float(input("Enter the value of Kilometer: "))
    #Ask the user again to wich unit of measurement to convert
    print("To which unit of measurement do you want to be converted?")
    print("1 from KM to Mile")
    print("2 from KM to Meter")
    unit = int(input("Enter  1 or 2: "))
    # Computer the value to the desired unit of measurement
    #Display the new unit of measurement

    if unit==1:
        print("Converted km to Mile  is =  "+value*0.62)
    elif unit==2:
        print("Converted KM to Meter is =  "+value*1000)
