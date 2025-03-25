import flet as ft
from fpdf import FPDF
import datetime

def main(page: ft.Page):
    page.title = "Invoice Maker"
    page.theme_mode = "light"
    
    # Input Fields
    customer_name = ft.TextField(label="Customer Name")
    item_name = ft.TextField(label="Item Name")
    item_price = ft.TextField(label="Price", keyboard_type=ft.KeyboardType.NUMBER)
    item_qty = ft.TextField(label="Quantity", value="1", keyboard_type=ft.KeyboardType.NUMBER)
    
    # Data Table for Invoice Items
    invoice_items = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Item")),
            ft.DataColumn(ft.Text("Price")),
            ft.DataColumn(ft.Text("Qty")),
            ft.DataColumn(ft.Text("Total")),
        ],
        rows=[],
    )
    
    # Add Item to Invoice
    def add_item(e):
        price = float(item_price.value)
        qty = int(item_qty.value)
        total = price * qty
        invoice_items.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(item_name.value)),
                    ft.DataCell(ft.Text(f"${price:.2f}")),
                    ft.DataCell(ft.Text(str(qty))),
                    ft.DataCell(ft.Text(f"${total:.2f}")),
                ]
            )
        )
        page.update()
    
    # Generate PDF
    def generate_pdf(e):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Invoice Header
        pdf.cell(200, 10, txt="INVOICE", ln=1, align="C")
        pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}", ln=1)
        pdf.cell(200, 10, txt=f"Customer: {customer_name.value}", ln=1)
        
        # Invoice Items
        pdf.cell(200, 10, txt="Items:", ln=1)
        for row in invoice_items.rows:
            item = row.cells[0].content.value
            price = row.cells[1].content.value
            qty = row.cells[2].content.value
            total = row.cells[3].content.value
            pdf.cell(200, 10, txt=f"{item} - {price} x {qty} = {total}", ln=1)
        
        # Save PDF
        pdf.output("invoice.pdf")
        page.add(ft.Text("PDF Generated: invoice.pdf"))
    
    # UI Layout
    page.add(
        ft.Column([
            customer_name,
            ft.Row([item_name, item_price, item_qty]),
            ft.ElevatedButton("Add Item", on_click=add_item),
            invoice_items,
            ft.ElevatedButton("Generate PDF", on_click=generate_pdf),
        ])
    )

ft.app(target=main)
