# 📝 Language Translator: English ↔ Hindi

Welcome to the **Language Translator** project! This Python-based application translates text between **English** and **Hindi**. It's built using the Google Translate API and offers an easy-to-use command-line interface for translating in both directions.

## 🔧 Features
- Translate from **English to Hindi** and **Hindi to English**.
- Support for translating **multiple sentences** in one go.
- Clean and user-friendly **command-line interface**.
- Error handling for unsupported languages and connection issues.



```

## 🛠️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/language-translator.git
    cd language-translator
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the Google Translate API**:
   - Install the `googletrans` Python library.
   - Add any API keys if needed (depending on your method of translation).

## 🚀 Usage

1. **Run the script**:
    ```bash
    python translator.py
    ```

2. **Input text to translate**:
   - When prompted, enter the sentence in **English** or **Hindi**.
   - The application will automatically detect the source language and translate it to the other language.

### Example:
```bash
Enter the text you want to translate: Hello, how are you?
Translated text: नमस्ते, आप कैसे हैं?

Enter the text you want to translate: नमस्ते
Translated text: Hello
```

## 📦 Dependencies

- Python 3.8 or higher
- `googletrans==4.0.0-rc1` (for Google Translate API)
- Other dependencies mentioned in `requirements.txt`


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For more detailed instructions, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.


thanks to @vishalkumarojha
