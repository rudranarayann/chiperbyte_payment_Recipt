from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer

def create_receipt(receipt_data, filename):
    # Create document template
    pdf = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Add title
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title = Paragraph("Payment Receipt", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Add receipt information
    info_style = ParagraphStyle(name='infoStyle', fontSize=12, leading=15)
    info_text = f"""
    Transaction ID: {receipt_data['transaction_id']}<br/>
    Date: {receipt_data['date']}<br/>
    """
    info = Paragraph(info_text, info_style)
    elements.append(info)
    elements.append(Spacer(1, 12))

    # Add table of items
    table_data = [['Item', 'Description', 'Quantity', 'Price', 'Total']]
    for item in receipt_data['items']:
        table_data.append([item['name'], item['description'], item['quantity'], f"${item['price']:.2f}", f"${item['total']:.2f}"])
    
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Add total amount
    total_amount = sum(item['total'] for item in receipt_data['items'])
    total_text = f"Total Amount: ${total_amount:.2f}"
    total = Paragraph(total_text, info_style)
    elements.append(total)

    # Build PDF
    pdf.build(elements)

# Example usage
receipt_data = {
    'transaction_id': '123456789',
    'date': '2024-06-23',
    'items': [
        {'name': 'Item 1', 'description': 'Summer Dress', 'quantity': 5, 'price': 500.00, 'total':2500.00 },
        {'name': 'Item 2', 'description': 'Shooes', 'quantity': 2, 'price': 2000.00, 'total': 4000.00},{'name': 'Item 2', 'description': 'pant', 'quantity': 2, 'price': 2000.00, 'total': 4000.00},{'name': 'Item 2', 'description': 'Kurta', 'quantity': 2, 'price': 2000.00, 'total': 4000.00},{'name': 'Item 2', 'description': 'Blazer', 'quantity': 2, 'price': 2000.00, 'total': 4000.00},{'name': 'Item 2', 'description': 'Perfume', 'quantity': 2, 'price': 2000.00, 'total': 4000.00},{'name': 'Item 2', 'description': 'Airbag', 'quantity': 1, 'price': 2000.00, 'total': 4000.00},
    ]
}

create_receipt(receipt_data, 'receipt.pdf')
