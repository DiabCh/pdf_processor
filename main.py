from processors.image_reader import ImageReader
from processors.document_ai import DocumentAi
from processors.text_parser import PdfParser
filepath = '../dell/pdf_reader/invoices/HOEXTM (2).pdf'
""" There is no documentation for human in the loop document ai.
Right now it feels like a lot of it has to be hardcoded
I have an idea to do search terms = [(search term, rows distance from match)
"""

# x = PdfParser(filepath)
# print(x.data)
# x.retrieve_text()
# print(x.data)

search_terms = [('Date:', 0), ('PHYSICAL ADDRESS', 1), ('TOTAL HANDOVER AMOUNT:', 0), ('E-mail:', 0)]
x = PdfParser(filepath, search_terms)
x.retrieve_text()
x.parse_data()

x = DocumentAi(filepath=filepath, search_terms=search_terms)
x.retrieve_text()
print(x.__repr__())
print(x.__dict__())
print(x.parse_data())
