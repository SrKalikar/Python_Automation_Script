

from io import StringIO
import os
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def printing_pdf_text(path):
    output_string = StringIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        
    text = []
    x = output_string.getvalue()
    text.append(x)
    text1 = str(text)
    s_text = []
    s_text = text1.split()
    print(s_text[:2])


def getting_file_name(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            file_names_list = filename
            print(file_names_list)
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
            #print(filepath)
    
    return file_paths 


print("-----------Here Are the file names-----------")
file_list = getting_file_name("give_directory/folder_name_here")
def file101():
    for file in file_list:
        path = file
        printing_pdf_text(path)
ter = file101()        



print(file_list,ter)



#full_file_paths = get_filepaths(r"D:\Assignment")
#print(x[0:14])




