# Assets Directory

This directory is intended for static assets used by the application.

## Asset Types

- **Icons** — `.svg`, `.png` icon files
- **Fonts** — Custom font files (if not loading from CDN)
- **Images** — Background images, logos, etc.

## Usage in Streamlit

```python
# Load an image asset
from PIL import Image
img = Image.open("assets/logo.png")
st.image(img, width=200)
```
