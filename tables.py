import pandas as pd

def create_table():
    num_rows = int(input("Введите количество строк в таблице: "))
    data = {}
    
    for i in range(num_rows):
        row_data = input(f"Введите данные для строки {i+1} (через запятую): ")
        row_values = row_data.split(",")
        data[i] = row_values
    
    df = pd.DataFrame(data)
    return df

def save_table(table):
    file_name = input("Введите имя файла для сохранения (без расширения): ")
    file_path = f"{file_name}.txt"
    table.to_csv(file_path, index=False, sep='\t')
    print(f"Таблица успешно сохранена в файл {file_path}.")

table = create_table()
print(table)

while True:
    action = input("Выберите действие:\n1 - выйти\n2 - сохранить таблицу в формате txt\n")

    if action == "1":
        break
    elif action == "2":
        save_table(table)
    else:
        print("Некорректный ввод. Пожалуйста, выберите правильное действие.")

print("Программа завершена.")