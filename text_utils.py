import random
import string

def generate_random_text(word_count):
    """
    Генерирует случайный текст из заданного количества слов.
    """
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"
    words = []

    for _ in range(word_count):
        word_length = random.randint(3, 8)  # Длина слова от 3 до 8 символов
        word = ''.join(random.choices(vowels + consonants, k=word_length))
        words.append(word)

    return ' '.join(words)

# Тестирование
if __name__ == "__main__":
    random_text = generate_random_text(10)
    print("Случайный текст:", random_text)
