# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

# Метода деления двух чисел (ошибка при делении на 0)
def get_divide(num, div):
    return num / div


# Метод вывода значения массива по заданному индексу (ошибка при вводе не существующего индекса)
def get_list_value(index):
    my_list = [0, 1, 2, 3, 4, 5]
    return my_list[index]

# Метод сложения двух значений (ошибка при сложении числа и символа)
def get_sum(num, div):
    return num + div


try:
    # Отработка ошибки ввода не числового значения
    num = int(input('Input a: '))
    div = int(input('Input b: '))

    # Отработка метода деления на 0
    res = get_divide(num, div)
    print(res)

    # Отработка метода получения значения по индексу массива
    index = int(input('Input index: '))
    res = get_list_value(index)
    print(res)

    # Отработка попытки сложения числа и символа
    num = input('Input a: ')
    div = int(input('Input b: '))
    res = get_sum(num, div)
    print(res)

except ZeroDivisionError:
    print("Error: division by zero")
except ValueError:
    print("Error: incorrect value")
except LookupError:
    print("Error: incorrect index value")
except TypeError:
    print("Error: incorrect data type")
