def input_text_manually():
    """
    Запрашивает текст у пользователя.
    """
    text = input("Введите текст: ")
    return text

# Тестирование
if __name__ == "__main__":
    manual_text = input_text_manually()
    print("Введенный текст:", manual_text)
