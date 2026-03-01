from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()

    pdf = pisa.CreatePDF(html, dest=result)

    if pdf.err:
        return None
    return result.getvalue()