  # 🎨 QR Studio - Professional QR Code Generator

A modern, feature-rich web application for generating customizable QR codes with real-time preview and professional design presets. Built with Flask and Python, featuring a beautiful dark/light mode interface.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎯 Core Functionality
- **Real-time Preview**: See your QR code instantly as you customize
- **One-Click Download**: Export QR codes as timestamped PNG files
- **Live Generation**: Fast QR code creation with optimized performance

### 🎨 Design & Customization
- **5 Professional Presets**:
  - Classic Mono (Black & White)
  - Midnight Neon (Cyan on Dark)
  - Sunset Pulse (Orange on Dark Gray)
  - Mint Canvas (Dark Green on Light Lime)
  - Ember Glow (Gold on Dark Gray)
  
- **Custom Styling Options**:
  - Module color picker (QR code pattern color)
  - Background color picker
  - Adjustable module size (4-20)
  - Configurable border width (1-10)

### 🌓 User Experience
- **Dark/Light Mode**: Toggle between themes
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Quick Examples**: Pre-filled example links for testing
- **Clean Interface**: Modern, intuitive UI with smooth interactions

## 🚀 Demo

[Live Demo](https://web-production-5453d.up.railway.app/) 

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask 3.0.3
- **QR Generation**: qrcode 7.4.2, Pillow 10.3.0
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Space Grotesk, Inter (Google Fonts)
- **Deployment**: Gunicorn 22.0.0

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/hemantMohane29/QR-CODE-GENERATOR.git
cd QR-CODE-GENERATOR
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Running Locally

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Generate QR Codes**:
   - Enter any text or URL in the input field
   - Choose a design preset or customize colors manually
   - Adjust module size and border width as needed
   - Click "Generate" to see live preview
   - Click "Download PNG" to save your QR code

### Running with Gunicorn (Production)

```bash
gunicorn app:app --bind 0.0.0.0:5000
```

## 📁 Project Structure

```
QR-CODE-GENERATOR/
│
├── app.py                 # Main Flask application with API endpoints
├── QR.py                  # Simple QR generation script
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration for Heroku/Render
├── runtime.txt           # Python version specification
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
│
├── templates/
│   └── index.html        # Main UI with embedded CSS and JavaScript
│
└── static/               # Static assets directory
```

## 🎨 Design Presets

| Preset | Module Color | Background | Use Case |
|--------|-------------|------------|----------|
| **Classic Mono** | #111111 (Black) | #ffffff (White) | Traditional, high contrast |
| **Midnight Neon** | #a5f3fc (Cyan) | #030712 (Dark) | Modern, tech-focused |
| **Sunset Pulse** | #fb923c (Orange) | #111827 (Dark Gray) | Warm, energetic |
| **Mint Canvas** | #064e3b (Dark Green) | #ecfccb (Light Lime) | Fresh, organic |
| **Ember Glow** | #fbbf24 (Gold) | #1f2937 (Dark Gray) | Premium, elegant |

## 🌐 API Endpoints

### `GET /`
Returns the main application page with full UI.

**Response**: HTML page

---

### `POST /generate-preview`
Generates a QR code preview as base64-encoded image for live preview.

**Request Body**:
```json
{
  "link": "https://example.com",
  "style": {
    "fillColor": "#111111",
    "backgroundColor": "#ffffff",
    "boxSize": 10,
    "border": 4
  }
}
```

**Response**:
```json
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANS..."
}
```

---

### `POST /generate`
Generates and downloads a QR code as PNG file with timestamp.

**Request Body**: Same as `/generate-preview`

**Response**: PNG image file (Content-Type: image/png)

**Filename Format**: `qr_YYYYMMDD_HHMMSS.png`

## 🚀 Deployment
### Deploy to Railway

1. Connect your GitHub repository to [Railway](https://railway.app)
2. Railway will auto-detect Flask configuration
3. Deploy with one click
4. Set environment variables if needed

### Environment Variables

- `PORT`: Server port (default: 5000)
- `DEBUG`: Debug mode (default: False)

## 💡 Usage Tips

- **High Contrast**: Use light presets on dark surfaces and vice versa for maximum scannability
- **Testing**: Always test your QR codes with multiple devices before printing
- **Size**: Larger module sizes work better for physical prints
- **Border**: Maintain adequate border (quiet zone) for reliable scanning

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Hemant Mohane**

- GitHub: [@hemantMohane29](https://github.com/hemantMohane29)
- LinkedIn: [Connect with me]( https://www.linkedin.com/in/hemant-mohane-35440a330/ )

## 🙏 Acknowledgments

- [python-qrcode](https://github.com/lincolnloop/python-qrcode) - QR Code generation library
- [Flask](https://flask.palletsprojects.com/) - Lightweight web framework
- [Pillow](https://python-pillow.org/) - Python Imaging Library
- [Google Fonts](https://fonts.google.com/) - Space Grotesk & Inter fonts

## 🔮 Future Enhancements

- [ ] Add QR code logo/image overlay support
- [ ] Implement batch QR code generation
- [ ] Add more error correction levels (L, M, Q, H)
- [ ] Support for vCard QR codes
- [ ] QR code history/gallery feature
- [ ] Export in multiple formats (SVG, PDF, EPS)
- [ ] QR code scanner functionality
- [ ] Custom gradient color support
- [ ] QR code analytics tracking
- [ ] API key authentication for programmatic access

## 📊 Technical Details

### QR Code Configuration
- **Version**: Auto-fit (starts at version 1)
- **Error Correction**: Level L (Low - 7% recovery)
- **Module Size Range**: 4-20 pixels
- **Border Range**: 1-10 modules
- **Output Format**: PNG (RGB)

### Browser Compatibility
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

---

⭐ **If you found this project helpful, please give it a star!**

Made with ❤️ by Hemant Mohane
