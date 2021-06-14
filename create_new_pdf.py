from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path 
import io
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter
from position import pdf_position
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont 


def create_name_pdf(model_path, name, posX, posY, output_path):
    '''
    Create a new pdf file with the name written on it

    Input:
    model_path: template path 
    name: the name that you want to be written on
    posX: X position you want the name to be put on
    posY: Y position you want the name to be put on 
    output_path: the path you want to save the new pdf 

    Output: 
    A new pdf with the name written on it 
    '''

    # create a pdf file object 
    pdFile = open(model_path, 'rb')

    # create a pdf reader object 
    pdf = PdfFileReader(pdFile)

    # getting the page size 
    page_size = pdf.getPage(0).mediaBox
    page_size = page_size[2:]

    # create a new PDF with ReportLab
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_size[0], page_size[1]))

    # Registerring font 
    font_name = 'Montserrat'
    pdfmetrics.registerFont(TTFont(font_name, font_name+'.ttf'))

    # Drawing the name on the empty canvas 
    can.setFont(font_name, 100)
    can.drawString(posX, posY, name)
    can.save()

    # move to the beginning of the StringIO buffer 
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    page = new_pdf.getPage(0)
    outwrite = PdfFileWriter()
    outwrite.addPage(page)
    output = open(output_path, 'wb')
    outwrite.write(output)
    output.close()



