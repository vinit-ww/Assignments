import PyPDF2
pdf_file = open('sample.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
num_of_pages =read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content =page.extractText()
print page_content
