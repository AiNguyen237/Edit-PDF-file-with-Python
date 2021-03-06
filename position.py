from pdfminer.pdfparser import PDFParser 
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage 
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager 
from pdfminer.pdfinterp import PDFPageInterpreter 
from pdfminer.pdfdevice import PDFDevice 
from pdfminer.layout import LAParams 
from pdfminer.converter import PDFPageAggregator 
import pdfminer

class pdf_position:

    def parse_obj(self, lt_objs):

        # loop over the object list 
        for obj in lt_objs: 

            # if it's a textbox, print text and location 
            if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
                print("%6d, %6d, %s" % (obj.bbox[0], obj.bbox[1], obj.get_text().replace('\n', '_')))

            # if it's a container, recurse
            elif isinstance(obj, pdfminer.layout.LTFigure):
                self.parse_obj(obj._objs)

    def parsepdf(self, filename):
        # Open a PDF file.
        fp = open(filename, 'rb')

        # Create a PDF parser object associated with the file object. 
        parser = PDFParser(fp)

        # Create a PDF document object that stores the document structure.
        # Password for initialization as 2nd paramter 
        document = PDFDocument(parser)

        # Check if the document allows text extraction. If not, abort. 
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed

        # Create a PDF Resouce manager object that stores shared resources.
        rsrcmgr = PDFResourceManager()

        # Create a PDF device object.
        device = PDFDevice(rsrcmgr)

        # BEGIN LAYOUT ANALYSIS 
        # Set parameters for analysis.
        laparams = LAParams()

        # Create  a PDF page aggregator object 
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)

        # Create a PDF interpreter object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # loop over all pages in the document 
        for page in PDFPage.create_pages(document):

            # read the page into a layout object 
            interpreter.process_page(page)
            layout = device.get_result()

            # extract text from this object 
            self.parse_obj(layout._objs)

        







