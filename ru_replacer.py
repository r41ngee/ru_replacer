def replace_russian_symbols(file_path: str):
    """Rewrites file and changing russian symbols to Unicode

    Args:
        file_path (str): local path to file
    """    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    replaced_content = ''
    for char in content:
        if ord(char) >= 1040 and ord(char) <= 1103:  # Проверяем, является ли символ русским
            replaced_content += f"\\u{hex(ord(char))[2:]}"  # Заменяем символ на Unicode
        else: 
            replaced_content += char

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(replaced_content)

# Пример использования
file_path = input('Введите относительный путь к файлу/write relative path to file: ')
replace_russian_symbols(file_path)