
class celciuscalculator:
    def convert(celcius):

        usable = eval(celcius)

        if type(usable) == int or type(usable) == float:
            fahrenheit = round(usable*1.8+32)
            return str(fahrenheit)

        else:
            return "Error! Your input is not a number! Try '1' or '100'. Input:   "

    def table(lisst):
        print('{:11}{:13}'.format( 'F', 'C'))

        for h in range(0, len(lisst)):
            if lisst[h].isdigit():
                print("{:11}{:13}".format(celciuscalculator.convert(lisst[h]), str(lisst[h])))
            else:
                print("{:11}{:13}".format(celciuscalculator.convert(lisst[h]), ("'"+str(lisst[h])+"'")))

    def go():
        listlength = input("How many temperatures do you want to convert?   ")
        if listlength.isdigit():
            listlength = int(listlength)
            templist = list()
            for i in range(0, listlength):
                new_temp = input("Temperature in Celcius "+ str(i+1)+ "?")
                templist.append(new_temp)
            celciuscalculator.table(templist)
        else:
            print("That was not a number!")



calculator = celciuscalculator

while True:
    true = True
    calculator.go()

    while True:
        stop = input("Do you want to stop? Y/N")
        if stop == 'Y':
            break
        elif not stop == 'N':
            print("That was not a valid answer!")
        else:
            calculator.go()
    else:
        continue
    break
