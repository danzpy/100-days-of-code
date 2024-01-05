'''
Utilização do loop "for" e a utilização da função "range()".
'''

student_heights = [151, 145, 179]

total_height = 0
number_of_students = 0

for student in student_heights:
  total_height += student
  number_of_students += 1

print(f'total height = {total_height}')
print(f'number of students = {number_of_students}')
print(f'average height = {round(total_height/number_of_students)}')



for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 5 == 0:
    print('Buzz')
  elif num % 3 == 0:
    print('Fizz')
  else:
    print(num)