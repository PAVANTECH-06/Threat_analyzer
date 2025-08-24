from fpdf import FPDF
import re

def clean_text(text):
    # Remove unsupported characters (emojis, non-latin)
    return re.sub(r'[^\x00-\x7F]+', '', text)

def generate_report(alerts, filename="threat_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Threat Analyzer Report", ln=True, align="C")
    pdf.ln(10)

    if not alerts:
        pdf.multi_cell(190, 10, txt="No major threats detected")  # fixed width
    else:
        for alert in alerts:
            safe_alert = clean_text(alert)
            pdf.multi_cell(190, 10, txt=safe_alert)  # 190 keeps text inside page margin

    pdf.output(filename)
    return filename
