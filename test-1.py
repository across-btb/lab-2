
#составляем функцию для обработки данных
def colculation(x, y, operation):
    #даём каждому знаку соответствующее действие
    if operation == "-":
        return x - y
    elif operation == "+":
        return x + y
    elif operation == "*":
        return x * y
    elif operation == "/":
        return x / y

x = int(input("введите первое число:"))
y = int(input("введите второе число:"))
operation = str(input("введите оператор:"))

#выводим на экран получившийся ответ
print(colculation(x, y, operation))
