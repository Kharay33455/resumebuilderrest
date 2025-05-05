from weasyprint import HTML

HTML('input.html').write_pdf('output.pdf')
# or from string
HTML(string='<h1>Hello, WeasyPrint</h1>').write_pdf('output.pdf')
