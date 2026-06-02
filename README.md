# 🌐 AI Language Translation Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Translate](https://img.shields.io/badge/Google%20Translate-API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![gTTS](https://img.shields.io/badge/gTTS-TTS-34A853?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A modern, AI-powered language translation application built with Python & Streamlit.**  
*CodeAlpha Internship Project — Artificial Intelligence Track*

</div>

---

## 📌 Project Description

The **AI Language Translation Tool** is a fully-featured, production-ready web application that enables users to translate text across **100+ languages** in real time. Powered by the **Google Translate API** (via `googletrans`), it delivers instant, accurate translations within a sleek, dark-themed UI.

The application also features **Text-to-Speech (TTS)** synthesis using Google's `gTTS` library, allowing users to hear the translated text aloud or download it as an MP3 file — making it ideal for language learners, travelers, developers, and content creators.

This project was built as part of the **CodeAlpha Artificial Intelligence Internship** program.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌍 **100+ Languages** | Translate between more than 100 world languages |
| ⚡ **Real-Time Translation** | Instant results powered by Google Translate API |
| 🔍 **Auto Language Detection** | Automatically identifies the source language |
| 🎙️ **Text-to-Speech (TTS)** | Convert translated text to natural-sounding audio |
| 🎵 **Audio Playback** | Listen to the translation directly in the browser |
| ⬇️ **MP3 Download** | Download generated audio for offline use |
| 📋 **One-Click Copy** | Copy the translation to clipboard instantly |
| ⇄ **Language Swap** | Instantly swap source and target languages |
| 📝 **Character Counter** | Live 5,000-character input limit display |
| 💬 **Quick Examples** | Pre-loaded example phrases for fast testing |
| 🛡️ **Error Handling** | Robust validation for all edge cases |
| 🎨 **Modern Dark UI** | Glassmorphism-styled premium interface |

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.11+ | Core programming language |
| **Streamlit** | 1.35.0 | Web application framework |
| **googletrans** | 4.0.0-rc1 | Google Translate API wrapper |
| **gTTS** | 2.5.1 | Google Text-to-Speech synthesis |
| **Pyperclip** | 1.9.0 | Clipboard copy functionality |
| **Pillow** | 10.3.0 | Image processing support |

---

## 📁 Project Structure

```
CodeAlpha_LanguageTranslationTool/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules
│
├── screenshots/         # Application screenshots
│   ├── main_ui.png
│   ├── translation_demo.png
│   └── tts_demo.png
│
└── assets/              # Static assets (icons, etc.)
```

---

## ⚙️ Installation Steps

### Prerequisites

- Python **3.11 or higher** installed
- `pip` package manager
- Internet connection (required for Google Translate API and gTTS)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/IaMSUBH01/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### Step 2 — Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on macOS / Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If `pyperclip` clipboard functionality fails in your environment, it will gracefully degrade — the app will continue to work without clipboard access.

---

## 🚀 How To Run

```bash
streamlit run app.py
```

The application will automatically open at:

```
http://localhost:8501
```

To stop the server, press `Ctrl + C` in the terminal.

---

## 🖥️ How To Use

1. **Enter text** — Type or paste your text into the *Input Text* panel (up to 5,000 characters).
2. **Select languages** — Choose a source language (or leave as *Auto Detect*) and pick your target language from the dropdown.
3. **Translate** — Click the **🚀 Translate Now** button to get the translation instantly.
4. **Listen** — Click **🔊 Speak** to synthesize and play the translated text as audio.
5. **Download** — Click **⬇️ Download MP3** to save the audio file.
6. **Copy** — Click **📋 Copy** to copy the translated text to your clipboard.
7. **Swap** — Click **⇄** to swap the source and target languages.
8. **Clear** — Click **🗑️ Clear** to reset the entire form.

---

## 📸 Screenshots

> Screenshots will be added after the first run of the application.

| Main Interface | Translation Demo | TTS Demo |
|---|---|---|
| *(screenshots/main_ui.png)* | *(screenshots/translation_demo.png)* | *(screenshots/tts_demo.png)* |

---

## 🌐 Supported Languages (Sample)

The tool supports **100+ languages** including:

| Language | Code | Language | Code |
|---|---|---|---|
| English | `en` | Spanish | `es` |
| French | `fr` | German | `de` |
| Chinese (Simplified) | `zh-cn` | Japanese | `ja` |
| Korean | `ko` | Arabic | `ar` |
| Portuguese | `pt` | Russian | `ru` |
| Italian | `it` | Hindi | `hi` |
| Bengali | `bn` | Turkish | `tr` |
| Dutch | `nl` | Polish | `pl` |

*...and 80+ more languages supported by Google Translate.*

---

## 🛡️ Error Handling

The application gracefully handles:

- ✅ **Empty input** — warns before attempting translation
- ✅ **Character limit exceeded** — blocks translation and alerts user
- ✅ **Same source & target language** — warns the user
- ✅ **Translation API failures** — displays descriptive error messages
- ✅ **TTS failures** — notifies user if audio synthesis fails
- ✅ **Clipboard unavailability** — falls back gracefully with a user notice
- ✅ **Network issues** — catches exceptions from API timeouts

---

## 🔮 Future Improvements

- [ ] **Batch Translation** — Upload `.txt` or `.docx` files for bulk translation
- [ ] **Translation History** — Persist previous translations with timestamps
- [ ] **Favorites** — Save frequently used language pairs
- [ ] **Romanization** — Show phonetic transcriptions for non-Latin scripts
- [ ] **Custom Voices** — Support multiple TTS voice styles and speeds
- [ ] **Dark / Light Mode Toggle** — User-selectable theme
- [ ] **Offline Mode** — Local translation model fallback (e.g., `argostranslate`)
- [ ] **Browser Extension** — One-click in-page translation
- [ ] **REST API** — FastAPI backend for programmatic access
- [ ] **PWA Support** — Progressive Web App for mobile use

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- [**Google Translate**](https://translate.google.com/) — for the powerful translation engine
- [**Streamlit**](https://streamlit.io/) — for making data apps effortless
- [**gTTS**](https://gtts.readthedocs.io/) — for the Text-to-Speech library
- [**CodeAlpha**](https://www.codealpha.tech/) — for the internship opportunity

---

## 👨‍💻 Author

**Subhajit Roy**  
Artificial Intelligence Intern  
CodeAlpha Internship Program — 2025  
GitHub: [@IaMSUBH01](https://github.com/IaMSUBH01)

---

<div align="center">
  <strong>⭐ If you found this project useful, please star the repository! ⭐</strong>
  <br><br>
  Made with ❤️ by <strong>Subhajit Roy</strong> for the <strong>CodeAlpha Internship</strong>
</div>
