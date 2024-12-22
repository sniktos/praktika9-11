from text_utils import generate_random_text, analyze_text
from io_utils import input_text_manually, display_results

def main():
    """
    Основное меню программы.
    """
    text = ""
    analysis_done = False

    while True:
        print("\nМеню:")
        print("1. Ввести текст вручную")
        print("2. Сгенерировать случайный текст")
        print("3. Выполнить анализ текста")
        print("4. Вывести результаты анализа")
        print("5. Завершить работу")

        choice = input("Выберите действие: ")

        if choice == "1":
            text = input_text_manually()
            analysis_done = False

        elif choice == "2":
            word_count = int(input("Введите количество слов для генерации: "))
            text = generate_random_text(word_count)
            print("Сгенерированный текст:", text)
            analysis_done = False

        elif choice == "3":
            if not text:
                print("Сначала введите или сгенерируйте текст.")
            else:
                word_analysis, total_vowels = analyze_text(text)
                analysis_done = True
                print("Анализ выполнен.")

        elif choice == "4":
            if not analysis_done:
                print("Сначала выполните анализ текста.")
            else:
                display_results(word_analysis, total_vowels)

        elif choice == "5":
            print("Завершение работы. До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
