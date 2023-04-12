class product:
    def __init__(self, productName, price):
        self.productName = productName
        self.price = price

    def discount(self, discountvalue):
        discountAmount = (self.price/100)*discountvalue
        final_price = self.price - discountAmount
        return int(final_price)


phone = product('phone', 50000)

print(phone.discount(90))
