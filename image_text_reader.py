import easyocr

reader = easyocr.Reader(['en'])
image= 'Gambar_1.jpeg'
result = reader.readtext(image)
output_text = ' '.join([detection[1] for detection in result])

print(output_text)
