import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from PDF_export.data import Attributes_data
from PDF_export.Style import style

def make_pdf(char):
    name = str(char) + "_Character.pdf"
    pdf = SimpleDocTemplate(name, pagesize = A4)
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1
    title = Paragraph(name,title_style)

    table = Table(Attributes_data(char), style = style)

    pdf.build([title,table])

make_pdf("char1")