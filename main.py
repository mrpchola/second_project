# Импортируем библиотеки
import os
from dotenv import load_dotenv

def print_author():
    load_dotenv(dotenv_path='C:\\Users\\aspchelint\\Documents\\Мои полученные файлы\\ML-инженер\\Спринт 6. Инструменты разработки и основы ООП\\second_project\\.env')
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

# Вызываем функцию
print_author()