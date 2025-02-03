import os
import shutil
import re

# Путь к папке с исходными файлами
source_folder = "/Users/anastasialelekova/Desktop/clean2"

# Путь к папке назначения
destination_folder = "/Users/anastasialelekova/Desktop/dirty2"

# Создаем папку назначения, если она не существует
os.makedirs(destination_folder, exist_ok=True)

# Шаблон для проверки имени файла
pattern = r"b\d+\.jpg$"  # Ожидаем, что в конце будет "b" и цифры

# Перебираем все файлы в исходной папке
for filename in os.listdir(source_folder):
    print(f"Checking file: {filename}")  # Выводим имя файла для проверки
    # Проверяем, что имя файла заканчивается на 'b' и цифры (например, b1, b2, b100 и т.д.)
    if re.search(pattern, filename):
        # Формируем полный путь к файлу
        source_file = os.path.join(source_folder, filename)

        # Перемещаем файл в папку назначения
        destination_file = os.path.join(destination_folder, filename)
        shutil.move(source_file, destination_file)
        print(f"Файл {filename} перемещен в {destination_folder}")
