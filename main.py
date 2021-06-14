import pandas as pd 
import merge_two_pdf
from position import pdf_position
import create_new_pdf
from PyPDF2 import PdfFileReader, PdfFileWriter


template = '/Users/ameliang/Documents/cert_make/New Certificate CS - no name.pdf'


# Getting all the names for certification 
cert_names = pd.read_csv('/Users/ameliang/Documents/cert_make/Certificate Form (Responses) - Form Responses 1.csv')
names = list(cert_names['Họ tên đầy đủ '])

PosX = 903
PosY = 1372

# Create new pdf
for i in names: 
    new_pdf_path = '/Users/ameliang/Documents/cert_make/new_pdf.pdf'
    create_new_pdf.create_name_pdf(template, i.upper(), PosX, PosY, new_pdf_path)

    file1 = PdfFileReader(template)
    file2 = PdfFileReader(new_pdf_path)
    output_path = f'/Users/ameliang/Documents/cert_make/certificate/{i}.pdf'
    
    merge_two_pdf.merge(file1, file2, output_path)
    


