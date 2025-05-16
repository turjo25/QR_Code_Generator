import qrcode

def generate_qr_code(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    text = lines[0].strip()
    filename = lines[1].strip()

    image_qrcode = qrcode.make(text)
    image_qrcode.save(filename)


generate_qr_code('input.txt')
