# QR Code Generator

A simple Python script that generates a QR code from input text and saves it as an image file. The text and the output file name are read from an input text file.

## 🧰 Features

- Generates a QR code from a user-defined string.
- Saves the QR code as an image file (e.g., PNG).
- Lightweight and minimal—no complex dependencies or configuration required.

## 📂 Project Structure

```
├── QRcode_generator.py   # Main script to generate QR code
├── input.txt             # Input file with text and filename
└── README.md             # Project documentation
```

## 📥 Input Format

The `input.txt` file should contain exactly two lines:

1. The **text** to encode in the QR code.
2. The **filename** (with extension) for the output image.

**Example:**

```
http://linkedin.com
linkedin.png
```

## ▶️ How to Run

1. **Install the required library**:

```bash
pip install qrcode[pil]
```

2. **Prepare the input** in a file named `input.txt` with the required format (as shown above).

3. **Run the script**:

```bash
python QRcode_generator.py
```

4. The QR code image will be saved with the filename provided in `input.txt`.

## 📦 Dependencies

- [qrcode](https://pypi.org/project/qrcode/): Used to generate QR codes.

## 🛠️ Customization

- It can modify the script to:
  - Reading input from the command line or a GUI.
  - Adding error checking for file input/output.
  - By customizing QR code parameters like size, border, and error correction.

