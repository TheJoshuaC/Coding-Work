from weasyprint import HTML 
html = HTML('invoice_template.html') 
html.write_pdf('invoice.pdf')