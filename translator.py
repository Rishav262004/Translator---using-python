# pip install googletrans==4.0.0-rc1
from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to translate text between any two languages based on user's choice
def translate_text(text, src_lang, dest_lang):
    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        transliteration = translation.pronunciation if translation.pronunciation else "N/A"
        
        print(f"\nTranslation of '{text}':\n'{translation.text}'")
        print(f"Transliteration: {transliteration}\n")

        # Ask if the user wants to save the translation
        save_choice = input("Would you like to save this translation? (y/n): ").lower()
        if save_choice == 'y':
            with open("translations.txt", "a") as file:
                file.write(f"\nOriginal: {text} ({src_lang})\nTranslation: {translation.text} ({dest_lang})\nTransliteration: {transliteration}\n")
            print("Translation saved successfully!\n")

    except Exception as e:
        print("Sorry, there was an error translating the text:", e)

# Function to detect the language of the input text
def detect_language(text):
    try:
        detected = translator.detect(text)
        print(f"\nDetected language: {detected.lang} (Confidence: {detected.confidence * 100:.2f}%)")
        return detected.lang
    except Exception as e:
        print("Sorry, there was an error detecting the language:", e)
        return None

# Main program
while True:
    print("\n--- Welcome to the Enhanced Hindi-English Translator! ---")
    print("1. Translate Hindi to English")
    print("2. Translate English to Hindi")
    print("3. Detect language and translate")
    print("4. Exit")
    choice = input("Enter your choice (1/4): ")

    if choice == '1':
        hindi_text = input("Enter the Hindi word or sentence: ")
        translate_text(hindi_text, src_lang='hi', dest_lang='en')

    elif choice == '2':
        english_text = input("Enter the English word or sentence: ")
        translate_text(english_text, src_lang='en', dest_lang='hi')

    elif choice == '3':
        text = input("Enter the text to detect its language and translate: ")
        detected_lang = detect_language(text)
        
        if detected_lang:
            dest_lang = input("Enter the language code you want to translate into (e.g., 'en' for English, 'hi' for Hindi): ")
            translate_text(text, src_lang=detected_lang, dest_lang=dest_lang)

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
