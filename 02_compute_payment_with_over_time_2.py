hours =int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours>40:
  
      #since, 1.5 times the hourly rate for hours worked above 40 hours
      #so, for 45 hours is = 1.5 *45/40
  rate_calculate = 1.5 * hours/(40)
else:
  rate_calculate = 0

final_rate = rate * 1.5 * rate_calculate
pay = hours * rate + final_rate
print('Pay: {:.2f}'.format(pay))
