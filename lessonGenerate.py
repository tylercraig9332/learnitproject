from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

import traceback

class generate:

    def __init__(self, pdf_src="null"):
        self.location = pdf_src
        self.document = None
        self.data = "There is no data"
        self.error = "load has not been run yet"


    def load(self):
        try:
            fp = open(self.location, 'rp')
            parser = PDFParser(self.fp)
            self.document = PDFDocument(parser)
            if document.is_extractable:
                self.error = "PDFTextExtractionNotAllowed thrown"
                raise PDFTextExtractionNotAllowed
            self.error = "no errors"
        except Exception as e:
            self.error = "Couldn't load file \nERROR: "
            err = "Error when opening and loading file\nError: " + str(type(e))
            print err
            traceback.print_stack()


'''
# Excecution below this line
print("Monday: Biceps/Shoulders/Back\n")
print("Tuesday: Chest/Triceps\n")
print("Wednesday: Legs/Abs\n")
print("Thursday: Biceps/Shoulders/Back\n")
print("Friday: Chest/Triceps\n")
print("Saturday: Legs/Abs\n")
'''
# When ready to execute
doc = generate('./Assimil/French/FrenchWithEase.pdf')
doc.load()
