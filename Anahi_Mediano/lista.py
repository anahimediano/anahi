list_of_squares= []
for int in range (1,10):
    square= int**2
    list_of_squares.append(square)
    
print(list_of_squares)

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#[expression for int in list if condition]
squared2 = [int**2 for int in range(1, 10)]
print(squared2)

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9,]
for numbers in numbers:
    print(numbers**3)
    
cubic = [num**3]
print