def display_results(word_analysis, total_vowels):
    """
    Форматирует и выводит результаты анализа текста.
    """
    print("\nРезультаты анализа текста:")
    print(f"{'Слово':<15}{'Гласные':<10}{'Согласные':<10}")
    print("-" * 35)
    for word, vowels, consonants in word_analysis:
        print(f"{word:<15}{vowels:<10}{consonants:<10}")
    print(f"\nОбщее количество гласных в тексте: {total_vowels}")

# Тестирование
if __name__ == "__main__":
    sample_analysis = [('hello', 2, 3), ('world', 1, 4), ('python', 1, 5)]
    display_results(sample_analysis, 4)
