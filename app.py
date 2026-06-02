"""
╔══════════════════════════════════════════════════════════════════╗
║          LANGUAGE TRANSLATION TOOL — CodeAlpha Internship        ║
║          Built with Python, Streamlit, deep-translator & gTTS    ║
╚══════════════════════════════════════════════════════════════════╝

Author  : Subhajit Roy
Project : CodeAlpha Internship — Artificial Intelligence Track
Version : 1.0.0
Python  : 3.11+ (tested on 3.14)
"""

# ── Standard Library ────────────────────────────────────────────
import io
import time

# ── Third-Party Libraries ───────────────────────────────────────
import streamlit as st
from deep_translator import GoogleTranslator
from deep_translator.exceptions import (
    TranslationNotFound,
    RequestError,
    TooManyRequests,
)
from gtts import gTTS
import pyperclip

# ════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="AI Language Translator | CodeAlpha",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ════════════════════════════════════════════════════════════════
# CUSTOM CSS — Premium Glassmorphism Dark Theme
# ════════════════════════════════════════════════════════════════
CUSTOM_CSS = """
<style>
/* ── Google Font Import ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* ── Root Variables ── */
:root {
    --bg-primary:      #0a0f1e;
    --bg-secondary:    #0d1527;
    --bg-card:         rgba(15, 23, 42, 0.85);
    --glass-border:    rgba(99, 179, 237, 0.15);
    --accent-blue:     #4299e1;
    --accent-cyan:     #00d4ff;
    --accent-purple:   #9f7aea;
    --accent-gradient: linear-gradient(135deg, #4299e1 0%, #00d4ff 50%, #9f7aea 100%);
    --text-primary:    #e2e8f0;
    --text-secondary:  #94a3b8;
    --text-muted:      #64748b;
    --success:         #48bb78;
    --error:           #fc8181;
    --warning:         #f6ad55;
}

/* ── Global Reset ── */
* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg-primary) !important;
    color: var(--text-primary) !important;
}

/* ── Main App Background ── */
.stApp {
    background: linear-gradient(135deg, #0a0f1e 0%, #0d1527 40%, #111827 100%) !important;
    min-height: 100vh;
}

/* ── Ambient Glow Orbs ── */
.stApp::before {
    content: '';
    position: fixed;
    top: -20%;
    left: -10%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(66,153,225,0.07) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    animation: floatOrb 8s ease-in-out infinite;
}

.stApp::after {
    content: '';
    position: fixed;
    bottom: -20%;
    right: -10%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(159,122,234,0.07) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    animation: floatOrb 10s ease-in-out infinite reverse;
}

@keyframes floatOrb {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50%       { transform: translateY(-30px) rotate(5deg); }
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1527 0%, #0a0f1e 100%) !important;
    border-right: 1px solid var(--glass-border) !important;
}

/* ── Hero Header ── */
.hero-header {
    background: linear-gradient(135deg,
        rgba(66,153,225,0.12) 0%,
        rgba(0,212,255,0.08) 50%,
        rgba(159,122,234,0.12) 100%);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
}

.hero-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--accent-gradient);
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
    letter-spacing: -0.5px;
}

.hero-subtitle {
    font-size: 1rem;
    color: var(--text-secondary);
    font-weight: 400;
    letter-spacing: 0.5px;
}

/* ── Card Label ── */
.card-label {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--accent-cyan);
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

/* ── Text Areas ── */
.stTextArea textarea {
    background: rgba(10, 15, 30, 0.8) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    line-height: 1.7 !important;
    padding: 1rem !important;
    resize: vertical !important;
    transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
}

.stTextArea textarea:focus {
    border-color: var(--accent-blue) !important;
    box-shadow: 0 0 0 3px rgba(66,153,225,0.15) !important;
    outline: none !important;
}

.stTextArea textarea::placeholder {
    color: var(--text-muted) !important;
}

/* ── Selectboxes ── */
.stSelectbox > div > div {
    background: rgba(10, 15, 30, 0.8) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    transition: border-color 0.3s ease !important;
}

.stSelectbox > div > div:hover {
    border-color: var(--accent-blue) !important;
}

/* ── Primary Buttons ── */
.stButton > button {
    background: var(--accent-gradient) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    padding: 0.65rem 1.8rem !important;
    letter-spacing: 0.3px !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(66,153,225,0.25) !important;
    width: 100% !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(66,153,225,0.40) !important;
    filter: brightness(1.1) !important;
}

.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── Result Box ── */
.result-box {
    background: linear-gradient(135deg,
        rgba(66,153,225,0.06) 0%,
        rgba(159,122,234,0.06) 100%);
    border: 1px solid rgba(99,179,237,0.20);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    min-height: 120px;
    font-size: 1.05rem;
    line-height: 1.8;
    color: var(--text-primary);
    word-break: break-word;
    position: relative;
    margin-top: 0.5rem;
}

.result-box.empty {
    color: var(--text-muted);
    font-style: italic;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.9rem;
}

/* ── Language Badge ── */
.lang-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    background: rgba(66,153,225,0.15);
    border: 1px solid rgba(66,153,225,0.25);
    border-radius: 20px;
    padding: 0.25rem 0.75rem;
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--accent-cyan);
    margin-bottom: 0.75rem;
}

/* ── Stat Cards ── */
.stat-card {
    background: rgba(15, 23, 42, 0.70);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    backdrop-filter: blur(10px);
}

.stat-value {
    font-size: 1.6rem;
    font-weight: 700;
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    font-weight: 500;
    margin-top: 0.2rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

/* ── Audio Player ── */
audio {
    width: 100%;
    border-radius: 10px;
    margin-top: 0.5rem;
}

/* ── Download Button ── */
.stDownloadButton > button {
    background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%) !important;
    color: var(--accent-cyan) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}

.stDownloadButton > button:hover {
    border-color: var(--accent-blue) !important;
    box-shadow: 0 4px 15px rgba(66,153,225,0.20) !important;
    transform: translateY(-1px) !important;
}

/* ── Divider ── */
hr {
    border-color: var(--glass-border) !important;
    margin: 1.5rem 0 !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--accent-blue), var(--accent-purple));
    border-radius: 10px;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# LANGUAGE DATA
# deep-translator exposes GoogleTranslator.get_supported_languages()
# ════════════════════════════════════════════════════════════════

# Fetch supported languages as a list of lowercase names
_RAW_LANG_LIST: list[str] = GoogleTranslator().get_supported_languages(as_dict=False)

# Build sorted display list (title-cased) and map back to lowercase for the API
DISPLAY_NAMES: list[str] = sorted([lang.title() for lang in _RAW_LANG_LIST])
DISPLAY_TO_API: dict[str, str] = {lang.title(): lang for lang in _RAW_LANG_LIST}

# Source list includes "Auto Detect" at the top
SOURCE_DISPLAY_NAMES: list[str] = ["Auto Detect"] + DISPLAY_NAMES

# Popular languages shown at top of target dropdown
_POPULAR = [
    "English", "Spanish", "French", "German", "Chinese (Simplified)",
    "Japanese", "Korean", "Arabic", "Portuguese", "Russian",
    "Italian", "Hindi", "Bengali", "Turkish", "Dutch",
]
_popular_valid = [lang for lang in _POPULAR if lang in DISPLAY_TO_API]
_rest = [lang for lang in DISPLAY_NAMES if lang not in _popular_valid]
PRIORITIZED_TARGET: list[str] = _popular_valid + _rest


# ════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ════════════════════════════════════════════════════════════════

def translate_text(
    text: str,
    target_lang: str,
    source_lang: str = "auto",
) -> dict:
    """
    Translate text using deep-translator's GoogleTranslator.

    Args:
        text        : Input text to translate.
        target_lang : Target language name (as used by deep-translator API).
        source_lang : Source language name or "auto" for auto-detection.

    Returns:
        dict with keys:
            "success"         : bool
            "translated_text" : str
            "error"           : str  (only on failure)
    """
    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        result: str = translator.translate(text)

        if not result:
            return {
                "success": False,
                "translated_text": "",
                "error": "Translation returned an empty result. Please try again.",
            }

        return {
            "success": True,
            "translated_text": result,
            "error": None,
        }

    except TranslationNotFound:
        return {
            "success": False,
            "translated_text": "",
            "error": "Translation not found for the given text.",
        }
    except TooManyRequests:
        return {
            "success": False,
            "translated_text": "",
            "error": "Too many requests. Please wait a moment and try again.",
        }
    except RequestError as exc:
        return {
            "success": False,
            "translated_text": "",
            "error": f"Network error: {str(exc)}",
        }
    except Exception as exc:
        return {
            "success": False,
            "translated_text": "",
            "error": f"Unexpected error: {str(exc)}",
        }


def text_to_speech(text: str, lang_code: str) -> bytes | None:
    """
    Convert text to MP3 audio using gTTS.

    Args:
        text      : Text to synthesize.
        lang_code : BCP-47 language code (e.g. "en", "fr", "ja").

    Returns:
        Raw MP3 bytes on success, None on failure.
    """
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)
        return buffer.read()
    except Exception:
        return None


def copy_to_clipboard(text: str) -> bool:
    """
    Copy text to the system clipboard.

    Returns True on success, False if clipboard is unavailable.
    """
    try:
        pyperclip.copy(text)
        return True
    except Exception:
        return False


def count_words(text: str) -> int:
    """Return word count of the given text."""
    return len(text.split()) if text.strip() else 0


def count_characters(text: str) -> int:
    """Return character count (no spaces) of the given text."""
    return len(text.replace(" ", "").replace("\n", ""))


def display_to_gtts_code(display_name: str) -> str:
    """
    Map a display language name to a BCP-47 code suitable for gTTS.
    Falls back to the first two characters of the API name.
    """
    # Explicit overrides for gTTS language codes
    overrides: dict[str, str] = {
        "chinese (simplified)": "zh-cn",
        "chinese (traditional)": "zh-tw",
        "filipino": "tl",
        "haitian creole": "ht",
    }
    api_name = display_name.lower()
    if api_name in overrides:
        return overrides[api_name]
    # Use the first word as a two-letter code approximation
    return api_name[:2]


# ════════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════════

def render_sidebar() -> None:
    """Render the application sidebar."""
    with st.sidebar:
        # App branding
        st.markdown(
            """
            <div style='text-align:center; padding: 1rem 0 0.5rem;'>
                <div style='font-size: 3rem; margin-bottom: 0.25rem;'>🌐</div>
                <div style='font-family: Space Grotesk, sans-serif;
                            font-size: 1.1rem; font-weight: 700;
                            background: linear-gradient(135deg,#4299e1,#00d4ff);
                            -webkit-background-clip: text;
                            -webkit-text-fill-color: transparent;'>
                    AI Language Translator
                </div>
                <div style='font-size: 0.72rem; color: #64748b;
                            letter-spacing: 1px; margin-top: 0.2rem;'>
                    v1.0.0 · CodeAlpha Internship
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # About
        st.markdown("### ℹ️ About")
        st.markdown(
            """
            <div style='font-size: 0.88rem; color: #94a3b8; line-height: 1.7;'>
            An AI-powered translation tool supporting <strong style='color:#00d4ff'>
            100+ languages</strong> with real-time translation, text-to-speech,
            and one-click copy.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # Feature list
        st.markdown("### ✨ Features")
        features = [
            ("🔤", "100+ Language Support"),
            ("⚡", "Real-Time Translation"),
            ("🎙️", "Text-to-Speech (TTS)"),
            ("📋", "One-Click Copy"),
            ("🔍", "Auto Language Detection"),
            ("⬇️",  "Audio Download"),
        ]
        for icon, label in features:
            st.markdown(
                f"""
                <div style='display:flex; align-items:center; gap:0.6rem;
                            padding:0.4rem 0; font-size:0.88rem; color:#e2e8f0;'>
                    <span>{icon}</span><span>{label}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.divider()

        # Tips
        st.markdown("### 💡 Tips")
        for tip in [
            "Use **Auto Detect** to identify your source language.",
            "Click **🔊 Speak** to hear the translation aloud.",
            "Download the audio for offline listening.",
            "Up to **5,000 characters** per translation.",
        ]:
            st.markdown(
                f"<div style='font-size:0.83rem; color:#94a3b8; padding:0.25rem 0;'>"
                f"• {tip}</div>",
                unsafe_allow_html=True,
            )

        st.divider()

        # Tech stack
        st.markdown("### 🛠️ Tech Stack")
        badges = [
            ("#4299e1", "Python 3.14"),
            ("#9f7aea", "Streamlit"),
            ("#48bb78", "deep-translator"),
            ("#f6ad55", "gTTS"),
        ]
        cols = st.columns(2)
        for idx, (color, name) in enumerate(badges):
            with cols[idx % 2]:
                st.markdown(
                    f"""
                    <div style='background:rgba(255,255,255,0.04);
                                border:1px solid {color}44;
                                border-radius:8px; padding:0.4rem 0.5rem;
                                text-align:center; font-size:0.78rem;
                                color:{color}; font-weight:600;
                                margin-bottom:0.5rem;'>
                        {name}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.divider()
        st.markdown(
            "<div style='text-align:center; font-size:0.75rem; color:#475569;'>"
            "Made with ❤️ by <strong>Subhajit Roy</strong> · CodeAlpha Internship</div>",
            unsafe_allow_html=True,
        )


# ════════════════════════════════════════════════════════════════
# HEADER
# ════════════════════════════════════════════════════════════════

def render_header() -> None:
    """Render the hero header section."""
    st.markdown(
        """
        <div class="hero-header">
            <div class="hero-title">🌐 AI Language Translator</div>
            <div class="hero-subtitle">
                Powered by Google Translate · 100+ Languages ·
                Text-to-Speech · Instant Results
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ════════════════════════════════════════════════════════════════
# STATS BAR
# ════════════════════════════════════════════════════════════════

def render_stats(input_text: str, translated_text: str) -> None:
    """Render stat cards below the translation panel."""
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        (col1, str(count_characters(input_text)),    "Source Chars"),
        (col2, str(count_words(input_text)),          "Source Words"),
        (col3, str(count_characters(translated_text)), "Output Chars"),
        (col4, f"{len(DISPLAY_NAMES)}+",              "Languages"),
    ]
    for col, value, label in stats:
        with col:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-value">{value}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ════════════════════════════════════════════════════════════════
# MAIN TRANSLATION UI
# ════════════════════════════════════════════════════════════════

def render_translation_ui() -> None:
    """Render the core translation panel."""

    # ── Language Selection ─────────────────────────────────────
    col_src, col_swap, col_tgt = st.columns([5, 1, 5])

    with col_src:
        st.markdown(
            "<div style='font-size:0.8rem; font-weight:600; color:#00d4ff;"
            "text-transform:uppercase; letter-spacing:1px; margin-bottom:0.3rem;'>"
            "🔍 Source Language</div>",
            unsafe_allow_html=True,
        )
        selected_source: str = st.selectbox(
            label="Source Language",
            options=SOURCE_DISPLAY_NAMES,
            index=0,
            label_visibility="collapsed",
            key="source_lang_select",
        )

    with col_swap:
        st.markdown("<div style='height: 1.8rem;'></div>", unsafe_allow_html=True)
        swap_clicked: bool = st.button("⇄", key="swap_btn", help="Swap languages")

    with col_tgt:
        st.markdown(
            "<div style='font-size:0.8rem; font-weight:600; color:#9f7aea;"
            "text-transform:uppercase; letter-spacing:1px; margin-bottom:0.3rem;'>"
            "🎯 Target Language</div>",
            unsafe_allow_html=True,
        )
        default_tgt_idx = (
            PRIORITIZED_TARGET.index("English")
            if "English" in PRIORITIZED_TARGET
            else 0
        )
        selected_target: str = st.selectbox(
            label="Target Language",
            options=PRIORITIZED_TARGET,
            index=default_tgt_idx,
            label_visibility="collapsed",
            key="target_lang_select",
        )

    # ── Language Swap ─────────────────────────────────────────
    if swap_clicked and selected_source != "Auto Detect":
        new_src = selected_target
        new_tgt = selected_source
        if new_src in SOURCE_DISPLAY_NAMES and new_tgt in PRIORITIZED_TARGET:
            st.session_state["source_lang_select"] = new_src
            st.session_state["target_lang_select"] = new_tgt
            st.rerun()

    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)

    # ── Input / Output Panels ─────────────────────────────────
    col_in, col_out = st.columns(2, gap="medium")

    with col_in:
        st.markdown(
            "<div class='card-label'>📝 &nbsp;INPUT TEXT</div>",
            unsafe_allow_html=True,
        )
        # ── Flush staged text from Quick-Start examples ──────────
        # Must happen BEFORE st.text_area is instantiated so that
        # session_state["input_text_area"] is set on this run, not
        # after the widget already exists (which raises StreamlitAPIException).
        if "_staged_text" in st.session_state:
            st.session_state["input_text_area"] = st.session_state.pop("_staged_text")

        input_text: str = st.text_area(
            label="Input Text",
            placeholder="Type or paste your text here…",
            height=220,
            max_chars=5000,
            label_visibility="collapsed",
            key="input_text_area",
        )
        char_count = len(input_text)
        counter_color = "#fc8181" if char_count > 4500 else "#64748b"
        st.markdown(
            f"<div style='text-align:right; font-size:0.75rem; color:{counter_color}; "
            f"margin-top:0.25rem;'>{char_count} / 5000</div>",
            unsafe_allow_html=True,
        )

    with col_out:
        st.markdown(
            "<div class='card-label'>✨ &nbsp;TRANSLATED TEXT</div>",
            unsafe_allow_html=True,
        )
        translated_text: str = st.session_state.get("translated_text", "")

        if translated_text:
            st.markdown(
                f"<div class='result-box'>{translated_text}</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='result-box empty'>"
                "Translation will appear here…"
                "</div>",
                unsafe_allow_html=True,
            )

    # ── Action Buttons ─────────────────────────────────────────
    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
    btn1, btn2, btn3, btn4 = st.columns([3, 2, 2, 2])

    with btn1:
        translate_clicked = st.button("🚀  Translate Now", key="translate_btn")
    with btn2:
        tts_clicked       = st.button("🔊  Speak",         key="tts_btn")
    with btn3:
        copy_clicked      = st.button("📋  Copy",          key="copy_btn")
    with btn4:
        clear_clicked     = st.button("🗑️  Clear",         key="clear_btn")

    # ── Handlers ──────────────────────────────────────────────
    if translate_clicked:
        _handle_translation(input_text, selected_source, selected_target)

    if tts_clicked:
        _handle_tts(selected_target)

    if copy_clicked:
        _handle_copy()

    if clear_clicked:
        _handle_clear()

    # ── Audio Section ─────────────────────────────────────────
    _render_audio_section()

    # ── Stats ─────────────────────────────────────────────────
    st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)
    st.divider()
    render_stats(input_text, translated_text)


# ════════════════════════════════════════════════════════════════
# ACTION HANDLERS
# ════════════════════════════════════════════════════════════════

def _handle_translation(
    input_text: str,
    selected_source: str,
    selected_target: str,
) -> None:
    """Validate and translate the input text."""
    if not input_text.strip():
        st.warning("⚠️  Please enter some text before translating.", icon="⚠️")
        return

    if len(input_text) > 5000:
        st.error("❌  Text exceeds the 5,000-character limit. Please shorten your input.")
        return

    # Resolve API language identifiers
    src_api = (
        "auto"
        if selected_source == "Auto Detect"
        else DISPLAY_TO_API.get(selected_source, "auto")
    )
    tgt_api = DISPLAY_TO_API.get(selected_target, "english")

    # Warn on identical languages (only when not auto-detecting)
    if src_api != "auto" and src_api == tgt_api:
        st.warning(
            "⚠️  Source and target languages are the same. "
            "Please choose different languages.",
            icon="⚠️",
        )
        return

    with st.spinner("🔄  Translating…"):
        start = time.time()
        result = translate_text(input_text, tgt_api, src_api)
        elapsed = time.time() - start

    if result["success"]:
        st.session_state["translated_text"] = result["translated_text"]
        st.session_state["tgt_display"]     = selected_target
        st.session_state["tgt_api"]         = tgt_api
        st.session_state["audio_bytes"]     = None  # reset stale audio
        st.success(f"✅  Translated in **{elapsed:.2f}s**", icon="✅")
        st.rerun()
    else:
        st.error(f"❌  {result['error']}", icon="🚨")


def _handle_tts(selected_target: str) -> None:
    """Synthesize speech from the translated text."""
    translated_text = st.session_state.get("translated_text", "")
    tgt_api         = st.session_state.get("tgt_api", "english")

    if not translated_text:
        st.warning("⚠️  Translate some text first before using Text-to-Speech.", icon="⚠️")
        return

    # Map API language name → gTTS BCP-47 code
    gtts_code = display_to_gtts_code(tgt_api)

    with st.spinner("🎙️  Generating audio…"):
        audio_bytes = text_to_speech(translated_text, gtts_code)

    if audio_bytes:
        st.session_state["audio_bytes"] = audio_bytes
        st.success("🔊  Audio ready — press play below!", icon="🔊")
        st.rerun()
    else:
        st.error(
            "❌  Audio generation failed. The selected language may not support TTS, "
            "or a network error occurred.",
            icon="🚨",
        )


def _handle_copy() -> None:
    """Copy translated text to clipboard."""
    translated_text = st.session_state.get("translated_text", "")
    if not translated_text:
        st.warning("⚠️  Nothing to copy. Translate some text first.", icon="⚠️")
        return
    if copy_to_clipboard(translated_text):
        st.success("📋  Copied to clipboard!", icon="✅")
    else:
        st.info(
            "ℹ️  Clipboard access unavailable in this environment. "
            "Please select and copy the text manually.",
            icon="ℹ️",
        )


def _handle_clear() -> None:
    """Clear all translation state."""
    for key in ["translated_text", "tgt_display", "tgt_api", "audio_bytes"]:
        st.session_state.pop(key, None)
    st.rerun()


def _render_audio_section() -> None:
    """Render audio player and download button if audio is available."""
    audio_bytes: bytes | None = st.session_state.get("audio_bytes")
    if not audio_bytes:
        return

    st.markdown("<div style='margin-top:1.25rem;'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:0.8rem; font-weight:600; color:#00d4ff;"
        "text-transform:uppercase; letter-spacing:1px; margin-bottom:0.5rem;'>"
        "🎵 &nbsp;AUDIO OUTPUT</div>",
        unsafe_allow_html=True,
    )

    audio_col, dl_col = st.columns([3, 1])
    with audio_col:
        st.audio(audio_bytes, format="audio/mp3")
    with dl_col:
        st.download_button(
            label="⬇️  Download MP3",
            data=audio_bytes,
            file_name="translation_audio.mp3",
            mime="audio/mpeg",
            key="download_audio_btn",
        )


# ════════════════════════════════════════════════════════════════
# QUICK-START EXAMPLES
# ════════════════════════════════════════════════════════════════

def render_examples() -> None:
    """Render example phrase buttons."""
    st.markdown("<div style='margin-top:0.5rem;'></div>", unsafe_allow_html=True)
    with st.expander("💬  Quick-Start Examples (click to expand)", expanded=False):
        st.markdown(
            "<div style='font-size:0.85rem; color:#94a3b8; margin-bottom:0.75rem;'>"
            "Click any example to load it into the translator.</div>",
            unsafe_allow_html=True,
        )
        examples = [
            ("🌍", "Hello, how are you today?"),
            ("❤️", "I love learning new languages."),
            ("🌸", "The world is a beautiful place."),
            ("🤝", "Nice to meet you!"),
            ("🚀", "Technology changes the world."),
            ("☀️", "Good morning! Have a great day."),
        ]
        cols = st.columns(3)
        for idx, (icon, phrase) in enumerate(examples):
            with cols[idx % 3]:
                if st.button(
                    f"{icon} {phrase}",
                    key=f"example_btn_{idx}",
                    help=f"Load: {phrase}",
                ):
                    # Write to a staging key — NOT directly to the widget key.
                    # The widget key (input_text_area) can only be set before
                    # the widget is instantiated; the staging key is flushed
                    # at the top of render_translation_ui() on the next rerun.
                    st.session_state["_staged_text"] = phrase
                    st.rerun()


# ════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════

def render_footer() -> None:
    """Render the page footer."""
    st.divider()
    st.markdown(
        """
        <div style='text-align:center; padding:1rem 0 0.5rem; color:#475569; font-size:0.8rem;'>
            <span style='background:linear-gradient(135deg,#4299e1,#9f7aea);
                         -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                         font-weight:700; font-size:0.9rem;'>
                AI Language Translator
            </span>
            &nbsp;·&nbsp;
            Built for the <strong style='color:#f6ad55;'>CodeAlpha Internship</strong>
            &nbsp;·&nbsp;
            Python · Streamlit · deep-translator · gTTS
            <br><br>
            <span style='font-size:0.75rem;'>
                © 2025 Subhajit Roy · CodeAlpha Internship · MIT License
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ════════════════════════════════════════════════════════════════

def main() -> None:
    """Main application entry point."""
    # Initialise session state on first run
    defaults: dict[str, object] = {
        "translated_text": "",
        "tgt_display":     "English",
        "tgt_api":         "english",
        "audio_bytes":     None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

    render_sidebar()
    render_header()
    render_translation_ui()
    render_examples()
    render_footer()


if __name__ == "__main__":
    main()
