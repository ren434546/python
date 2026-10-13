def analyze_log_file(log_file_path):
    result_dict = {}

    try:
        with open(log_file_path, "r", encoding="utf-8") as my_file:
            for line in my_file:
                print(line)
                my_list = line.split(" ")
                print(my_list)

                if len(my_list) > 8:
                    print(my_list[8])

                    if my_list[8] in result_dict:
                        result_dict[my_list[8]] += 1
                    else:
                        result_dict[my_list[8]] = 1

    except FileNotFoundError:
        print(f"Ошибка: Файл '{log_file_path}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода-вывода при чтении файла: {e}")

    return result_dict


print(analyze_log_file("apache_logs.txt"))