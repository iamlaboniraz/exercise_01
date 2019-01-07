import sys
def computepay(hours, rate):
        pay = 0
        if hours>40:
                rate_calculate = 1.5 * hours/(40)
        else:
                rate_calculate = 0
        final_rate = rate * 1.5 * rate_calculate
        pay = hours * rate + final_rate
        return pay

try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate:'))
    pay = computepay(hours, rate)
except ValueError:
        print("Error, please enter numeric input")
        quit()
if pay:
    print('Pay: {:.2f}'.format(pay))


    
