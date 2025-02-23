from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/convert', methods=['POST'])
def convert_pdf():
    file = request.files.get('pdf')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    file_path = f"/tmp/{file.filename}"
    output_path = f"/tmp/{file.filename}.html"

    file.save(file_path)

    # Run pdftohtml
    try:
        subprocess.run(["pdftohtml", "-s", "-c", file_path, output_path], check=True)
        return jsonify({"message": "Conversion successful", "output": output_path})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Conversion failed: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
