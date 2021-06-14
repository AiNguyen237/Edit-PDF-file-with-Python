from PyPDF2 import PdfFileReader, PdfFileWriter


def merge(file1, file2, path):
    '''
    Overlaying file 2 on file 1 

    Input: 
    file1: path to the first file 
    file2: path to the second file 
    path: the output path 

    Output: 
    returning a new pdf with two files overlay on each other
    '''
    
    output_file = PdfFileWriter()
    page = file1.getPage(0)
    page.mergePage(file2.getPage(0))
    output_file.addPage(page)

    with open(path, 'wb') as outputStream:
        output_file.write(outputStream)
