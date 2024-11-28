def  get_multiplied_digits(number):
    # Преобразуем число в строку и убираем все нули в конце
    str_number = str(number).rstrip('0')
    # Если после удаления нулей строка пустая, возвращаем 1 (так как 0 в конце не влияет на произведение)
    if not str_number:
        return 1

    # Основной алгоритм произведения цифр
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)


