import string

def analyze_text(text):
    """
    Анализирует текст и возвращает массив троек:
    (слово, количество гласных, количество согласных) и общее количество гласных.
    """
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    word_analysis = []
    total_vowels = 0

    words = text.split()  # Разделяем текст на слова
    for word in words:
        word = word.strip(string.punctuation).lower()  # Убираем пунктуацию и приводим к нижнему регистру
        vowel_count = sum(1 for char in word if char in vowels)
        consonant_count = sum(1 for char in word if char in consonants)
        total_vowels += vowel_count
        word_analysis.append((word, vowel_count, consonant_count))

    return word_analysis, total_vowels

# Тестирование
if __name__ == "__main__":
    sample_text = "Hello, world! Python is amazing."
    analysis, total_v = analyze_text(sample_text)
    print("Анализ текста:", analysis)
    print("Общее количество гласных:", total_v)
