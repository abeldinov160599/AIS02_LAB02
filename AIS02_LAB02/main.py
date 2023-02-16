from random import randint
import xlsxwriter as xl


def bubble(lost):
    lst = lost
    for num in range(len(lst) - 1, 0, -1):
        for item in range(num):
            if lst[item] > lst[item + 1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]
    return lst


def select(lost):
    lst = lost
    for num in range(len(lst)):
        min_value = num

        for item in range(num, len(lst)):
            if lst[min_value] > lst[item]:
                min_value = item

        lst[num], lst[min_value] = lst[min_value], lst[num]
    return lst


def fast(lost):
    lst = lost
    if len(lst) > 1:
        pivot = lst.pop()
        greater_list, equal_list, smaller_list = [], [pivot], []
        for item in lst:
            if item == pivot:
                equal_list.append(item)
            elif item > pivot:
                greater_list.append(item)
            elif item < pivot:
                smaller_list.append(item)
        return (fast(smaller_list) + equal_list + fast(greater_list))
    else:
        return lst


def shell(lost):
    lst = lost
    gap = len(lst) // 2

    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value

            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
                lst[position] = current_value

        gap //= 2
    return lst


def insert(lost):
    lst = lost
    for item in range(1, len(lst)):
        current_value = lst[item]
        position = item

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1
        lst[position] = current_value

    return lst


if __name__ == '__main__':
    try:
        s = []
        l = int(input("Введите количество символов для списка:"))
        book = xl.Workbook('Список.xlsx')
        sheet = book.add_worksheet()
        row = 0
        column = 0
        for i in range(l):
            a = randint(1, 15)
            s.append(a)
            sheet.write(row, column, a)
            row += 1

        s1 = bubble(s)
        s2 = select(s)
        s3 = fast(s)
        s4 = shell(s)
        s5 = insert(s)
        s1.append(max(s3))


        row = 0
        column += 2
        for item1 in s1:
            sheet.write(row, column, item1)
            row += 1

        row = 0
        column += 2
        for item2 in s2:
            sheet.write(row, column, item2)
            row += 1

        row = 0
        column += 2
        for item3 in s3:
            sheet.write(row, column, item3)
            row += 1

        row = 0
        column += 2
        for item4 in s4:
            sheet.write(row, column, item4)
            row += 1

        row = 0
        column += 2
        for item5 in s5:
            sheet.write(row, column, item5)
            row += 1
        book.close()
        print("Сортировка выполнена!")
    except:
        print("Введены некорректные символы!")


