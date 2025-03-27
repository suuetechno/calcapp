import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Invoice Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    
    # Input Fields
    customer_name = ft.TextField(label="Customer Name", width=300)
    item_description = ft.TextField(label="Item Description", width=300)
    quantity = ft.TextField(label="Quantity", width=150, input_filter=ft.InputFilter(regex=r"[0-9]"))
    unit_price = ft.TextField(label="Unit Price", width=150, input_filter=ft.InputFilter(regex=r"[0-9.]"))
    
    # Result display
    result = ft.Text("", size=16)
    
    def generate_invoice(e):
        try:
            qty = int(quantity.value)
            price = float(unit_price.value)
            total = qty * price
            date = datetime.now().strftime("%Y-%m-%d")
            
            invoice_text = f"""
            INVOICE
            Date: {date}
            Customer: {customer_name.value}
            
            Description: {item_description.value}
            Quantity: {qty}
            Unit Price: ${price:.2f}
            Total: ${total:.2f}
            """
            result.value = invoice_text
            page.update()
        except ValueError:
            result.value = "Please enter valid numbers for quantity and price"
            page.update()
    
    # Buttons
    generate_btn = ft.ElevatedButton("Generate Invoice", on_click=generate_invoice)
    clear_btn = ft.ElevatedButton("Clear", on_click=lambda e: page.clean())
    
    # Add controls to page
    page.add(
        ft.Column([
            customer_name,
            item_description,
            ft.Row([quantity, unit_price]),
            ft.Row([generate_btn, clear_btn]),
            result
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

# Run the app
ft.app(target=main)
