# =====================================
# FileName: pdf_editor.py
# Usage: Modify files' path and pages in the code
# Dependency: PyPDF2
# Author: Lynn <lynn840429@gmail.com>
# Version: v1.1.0, 2023/02/13 W1
# =====================================
""" Import Package """
import os
import PyPDF2



""" Path and Page Setting """
# """
# [User Modify] PDFs' path that you want to merge or split.
#   Linux ex:  "/Download/abc.pdf"
#   Windows ex: "\\Download\\abc.pdf"
# """
PDF_FILE_1 = "/mnt/HDD/linsan123/Lin/Tyler/Download/abc.pdf"
PDF_FILE_2 = ""
NEW_PDF_NAME = "new.pdf"



""" Main """
def main():
	# """
	# Function Info: Main Program
	# """

    ### Input PDF 1
    if (os.path.isfile(PDF_FILE_1)):
        pdfObj_1 = open(PDF_FILE_1, 'rb')
        p1 = PyPDF2.PdfReader(pdfObj_1)

    ### Input PDF 2
    if (os.path.isfile(PDF_FILE_2)):
        pdfObj_2 = open(PDF_FILE_2, 'rb')
        p2 = PyPDF2.PdfReader(pdfObj_2)
    
    ### Output PDF
    pdfWr = PyPDF2.PdfWriter()

    # """
    # [User Modify] Select the pages you want.
    #   PDF_PAGES_SELECTION = [p1.pages[0], p1.pages[3], p1.pages[5], p2.pages[2], p2.pages[4]]
    # """
    PDF_PAGES_SELECTION = [p1.pages[0], p1.pages[5], p1.pages[3]]

    for p in PDF_PAGES_SELECTION:
        pdfWr.add_page(p)

    with open(NEW_PDF_NAME, "wb") as output_stream:
        pdfWr.write(output_stream)


""" Boilerplate Code"""
if __name__ == '__main__':
	main()



