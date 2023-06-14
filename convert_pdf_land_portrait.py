from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
import pytesseract
import os

def identify_page_orientation(page_image):
    image_path = 'page_image.jpg'
    page_image.save(image_path, 'JPEG')

    text = pytesseract.image_to_osd(image_path)
    lines = text.split('\n')
    rotate = 0

    for line in lines:
        if line.startswith('Rotate'):
            rotate = int(line.split(':')[-1].strip())
            break
    
    os.remove('page_image.jpg')

    return rotate

def check_page_orientation(file_path):
    pdf = PdfReader(open(file_path, 'rb'))
    pdf_w = PdfWriter()
    
    flag = False
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]

        images = convert_from_path(file_path, first_page=page_num+1, last_page=page_num+1)
        page_image = images[0]

        rotation = identify_page_orientation(page_image)

        if rotation == 90:
            page.rotate(90)
            flag = True
        elif rotation == 270:
            page.rotate(-90)
            flag = True
        elif rotation == 180:
            page.rotate(180)
            flag = True
        pdf_w.add_page(page)
        
    output_path = file_path
    if flag:
        output_path = file_path.replace(".pdf","_rotated.pdf")

    with open(output_path, 'wb') as output_file:
        pdf_w.write(output_file)

    print(f"Modified PDF saved as {output_path}")

pdf = 'CBSE-6-SHRI SHIKSHA YATAN.pdf'
check_page_orientation(pdf)
