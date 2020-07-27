print ("Python program to convert temperatures to and from celsius, fahrenheit\n")

temp = input('Input the temperature you like to convert? (e.g : 102C, 45F, 110C etc.) : ').upper()

#For Celcius
if temp[-1] == 'C':
  operation = 'Celsius'
  value = int(temp[:-1])
  calculate = (value * 9/5) + 32
  print (f'The temperture in {operation} is {calculate} degrees.')
#For Fahrenheit
elif temp[-1] == 'F':
  operation = 'Fahrenheit'
  value = int(temp[:-1])
  calculate = (value - 32) * 5/9
  print(f'The temperture in {operation} is {calculate} degrees.')
