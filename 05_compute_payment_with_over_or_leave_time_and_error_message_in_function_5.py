import sys
def computepay(hours, rate):
             if hours>40:
                 rate_calculate = 1.5 * hours/(40)
                 final_rate = rate * 1.5 * rate_calculate
                 
             elif hours<40:
                 rate_calculate = 0.5 - hours/(40)
                 final_rate = rate * rate_calculate
             else:
                rate_calculate = 0
                final_rate = rate * rate_calculate
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
    print('Pay: {:.2f}'.format(pay)


    
