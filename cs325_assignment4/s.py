class OrderDetails:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

class OrderCostCalculator:
    def __init__(self, order_details):
        self.order_details = order_details

    def calculate_total_cost(self):
        total_cost = sum(item['price'] for item in self.order_details.items)
        return total_cost  

class OrderValidator:
    def __init__(self, order_details):
        self.order_details = order_details

    def validate_order(self):
        return True  

class OrderEmailSender:
    def __init__(self, order_details):
        self.order_details = order_details

    def send_confirmation_email(self):
        print(f"Sending email to {self.order_details.customer_info['email']}")

class InventoryUpdater:
    def __init__(self, order_details):
        self.order_details = order_details

    def update_inventory(self):
        print("Inventory updated")