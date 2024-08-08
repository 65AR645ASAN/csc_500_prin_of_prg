import psutil
import time


def get_cpu_usage():
    print("CPU Usage:", psutil.cpu_percent(interval=1))
    return psutil.cpu_percent(interval=1)


def send_alert(message):
    print(f"ALERT: {message}")


threshold = 0.5
print("CPU Usage Threshold: ", threshold)

cpu_usage = get_cpu_usage()
while cpu_usage > threshold:
    send_alert("CPU usage is High!")
    print(f"Waiting for 60 seconds, since CPU usage is High!")
    print(time.sleep(60))
    cpu_usage = get_cpu_usage()
    print('CPU Usage above threshold')
    break

print("CPU usage is now under control.")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def __repr__(self):
        return f"{self.name}: ${self.price:.2f}"


# List of products
products = [
    Product("Laptop", 1200),
    Product("Smartphone", 800),
    Product("Tablet", 400)
]

# Applying a 10% discount to all products
for product in products:
    product.apply_discount(10)
    print(f"Applied discount to {product.name}")

print("Discount applied to all products.")
print("Updated product prices:")
for product in products:
    print(product)
