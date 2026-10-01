from pyscript import document

store_name = "Skewer Corner"
group_name = "Group 1"
project_name = "SKU Generator"

products = {
    "item1": ["Hotdog Skewer", 35],
    "item2": ["Cheese Stick", 20],
    "item3": ["Fried Siomai", 45],
    "item4": ["Iced Tea", 25],
    "item5": ["Nachos", 50]
}


def show_sku(event):
    document.querySelector("#skuPage").classList.remove("hidden")
    document.querySelector("#receiptPage").classList.add("hidden")


def show_receipt(event):
    document.querySelector("#receiptPage").classList.remove("hidden")
    document.querySelector("#skuPage").classList.add("hidden")


def make_sku(event):
    category = document.querySelector("#category").value
    product_name = document.querySelector("#productName").value
    stock_qty = document.querySelector("#stockQty").value

    if product_name == "" or stock_qty == "":
        document.querySelector("#skuResult").innerHTML = "<b>Please complete all boxes first.</b>"
        return

    clean_name = product_name.replace(" ", "").upper()
    name_code = clean_name[0:3]
    category_code = category[0:3]
    quantity_code = stock_qty.zfill(2)
    sku = category_code + "-" + name_code + "-" + quantity_code

    output = f"""
    <h3>Generated SKU</h3>
    <p><b>Category:</b> {category}</p>
    <p><b>Product Name:</b> {product_name}</p>
    <p><b>Stock Quantity:</b> {stock_qty}</p>
    <p><b>SKU Code:</b> {sku}</p>
    """

    document.querySelector("#skuResult").innerHTML = output


def make_receipt(event):
    total = 0
    order_list = ""

    for item_id in products:
        box = document.querySelector("#" + item_id)
        item_name = products[item_id][0]
        item_price = products[item_id][1]

        if box.checked == True:
            total = total + item_price
            order_list = order_list + f"<p>{item_name} - ₱{item_price}</p>"

    if order_list == "":
        document.querySelector("#receiptResult").innerHTML = "<b>No item selected yet.</b>"
        return

    output = f"""
    <h3>{store_name}</h3>
    <p>{group_name} Food Booth</p>
    <hr>
    {order_list}
    <hr>
    <p><b>Total:</b> ₱{total}</p>
    <p>Thank you for buying!</p>
    """

    document.querySelector("#receiptResult").innerHTML = output


def clear_receipt(event):
    for item_id in products:
        document.querySelector("#" + item_id).checked = False

    document.querySelector("#receiptResult").innerHTML = "Your receipt will show here."


welcome = f"""
<p><b>{project_name}</b></p>
<p>Welcome to {store_name}. Use the buttons above to change pages.</p>
"""

document.querySelector("#skuResult").innerHTML = welcome
