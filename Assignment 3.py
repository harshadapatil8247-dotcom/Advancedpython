from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

class NetBankingPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking.")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

processor = PaymentProcessor(UPIPayment())
processor.process_payment(1500)

processor.set_strategy(CreditCardPayment())
processor.process_payment(2500)

processor.set_strategy(PayPalPayment())
processor.process_payment(1000)

processor.set_strategy(NetBankingPayment())
processor.process_payment(5000)