# reporting/pdf_writer.py
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def generate_pdf(report_path: Path, test_name: str, steps):
    report_path.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(report_path), pagesize=A4)
    width, height = A4

    # Portada
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, height - 60, f"Reporte de Test: {test_name}")
    c.setFont("Helvetica", 10)
    c.drawString(40, height - 80, f"Total pasos: {len(steps)}")
    c.showPage()

    for idx, s in enumerate(steps, start=1):
        y = height - 50
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y, f"Paso {idx}: {s.name}")
        y -= 18

        c.setFont("Helvetica", 10)
        c.drawString(40, y, f"Estado: {s.status}   |   Hora: {s.timestamp}")
        y -= 16

        if s.error:
            c.setFont("Helvetica", 9)
            c.drawString(40, y, f"Error: {s.error[:140]}")
            y -= 14

        if s.screenshot_path and s.screenshot_path.exists():
            # Insertar imagen ajustada
            img = ImageReader(str(s.screenshot_path))
            img_max_w = width - 80
            img_max_h = y - 40

            # Cargar tamaño real
            iw, ih = img.getSize()
            scale = min(img_max_w / iw, img_max_h / ih)
            nw, nh = iw * scale, ih * scale

            c.drawImage(img, 40, 40, width=nw, height=nh, preserveAspectRatio=True, anchor="sw")

        c.showPage()

    c.save()
