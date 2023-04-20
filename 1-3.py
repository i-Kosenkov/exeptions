# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен разности элементов
# двух входящих массивов в той же ячейке. Если длины массивов не равны, необходимо
# как-то оповестить пользователя.

array1 = [1, 7, 4, 1, 6, 3, 1, 5, 6, 8, 5, 4]
array2 = [1, 7, 5, 4, 1, 6, 8, 3, 0, 5]


def get_new_array(array1, array2):
    new_array = []
    if len(array1) != len(array2):
        print('Разные длины массивов')
        if len(array1) >= len(array2):
            for i in range(len(array2)):
                new_array.append(array1[i] - array2[i])
            return new_array

    for i in range(len(array1)):
        new_array.append(array1[i] - array2[i])
    return new_array


res = get_new_array(array1, array2)
print(res)
