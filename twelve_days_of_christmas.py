import sys

def song():

    gifts = ['Partridge in a Pear Tree','Turtle Doves','French Hens','Calling Birds','Golden Rings','Geese a Laying',
             'Swans a Swimming','Maids a Milking','Ladies Dancing','Lords a Leaping','Pipers Piping','Drummers Drumming']
    number = ['A','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
    days = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']

    i=0

    while i<=11:

        print  'On the %s day of Christmas my true love gave to me:'
        num = 0
        j=i

        while j != -1:

            print number[j]+' '+gifts[j]
            j -= 1

        print ""

        number[0] = str('And a')

        i += 1








song()