from pdf2docx import Converter

pdf = 'C:\\Users\\Vrushali\\Downloads\\cloud_computing_final_report.pdf'
docx = 'my.docx'

co = Converter(pdf)
co.convert(docx)
co.close()
