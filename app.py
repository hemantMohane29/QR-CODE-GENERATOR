from flask import Flask, render_template, request, jsonify, send_file
import qrcode
import io
import os
import base64
from datetime import datetime

DEFAULT_STYLE = {
    "fillColor": "#111111",
    "backgroundColor": "#ffffff",
    "boxSize": 10,
    "border": 4,
}

app = Flask(__name__)


def normalize_style(style_payload):
    """Return a safe style dict merged with defaults."""
    style_payload = style_payload or {}
    style = {
        "fillColor": style_payload.get("fillColor", DEFAULT_STYLE["fillColor"]),
        "backgroundColor": style_payload.get("backgroundColor", DEFAULT_STYLE["backgroundColor"]),
        "boxSize": style_payload.get("boxSize", DEFAULT_STYLE["boxSize"]),
        "border": style_payload.get("border", DEFAULT_STYLE["border"]),
    }

    try:
        style["boxSize"] = max(4, min(20, int(style["boxSize"])))
    except (TypeError, ValueError):
        style["boxSize"] = DEFAULT_STYLE["boxSize"]

    try:
        style["border"] = max(1, min(10, int(style["border"])))
    except (TypeError, ValueError):
        style["border"] = DEFAULT_STYLE["border"]

    return style


def build_qr_image(link, style):
    """Generate a QR image using the given style settings."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=style["boxSize"],
        border=style["border"],
    )
    qr.add_data(link)
    qr.make(fit=True)
    return qr.make_image(fill_color=style["fillColor"], back_color=style["backgroundColor"])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_qr():
    try:
        data = request.json or {}
        link = data.get('link', '').strip()
        style = normalize_style(data.get('style'))

        if not link:
            return jsonify({'error': 'Please provide a link or text'}), 400

        img = build_qr_image(link, style)

        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"

        img.save(filename)

        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=filename)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/generate-preview', methods=['POST'])
def generate_qr_preview():
    try:
        data = request.json or {}
        link = data.get('link', '').strip()
        style = normalize_style(data.get('style'))

        if not link:
            return jsonify({'error': 'Please provide a link or text'}), 400

        img = build_qr_image(link, style)

        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return jsonify({'image': f'data:image/png;base64,{img_base64}'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)

