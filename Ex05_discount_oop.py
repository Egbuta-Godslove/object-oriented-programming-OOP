class phone:
	discount = 10
	sno = 0
	def __init__(self, name, price):
		phone.sno += 1
		self.sno = phone.sno
		self.name = name
		self.price = price
	def apply_dsicount(self):
		discount_amount = int(self.price/100)*self.discount
		finalAmount = self.price - discount_amount
		return finalAmount

samsung = phone('Samsung s23 ultra', 1000000)
Iphone = phone('Iphone 14', 9000000)
Oppo = phone('Oppo A12', 55000)
Nokia = phone('Nokia A80', 800000)

samsung.water_resistance = 'Yes'
Iphone.dust_resisstance = 'Yes'
Oppo.fast_charging = 'No'
samsung.wireless_charging = 'Yes'
Iphone.wireless_charging = 'Yes'
Oppo.wireless_charging = 'No'
Nokia.fast_charging = 'Yes'
Nokia.water_resistance = 'Yes'
Nokia.dust_resisstance = 'Yes'

samsung.discount = 10
Iphone.discount = 20
Oppo.discount = 50
Nokia.discount = 0

print(samsung.__dict__)
print(Iphone.__dict__)
print(Oppo.__dict__)
print(Nokia.__dict__)

print("The final amount after discount for the Samsung s23 Ultra is", samsung.apply_dsicount())
print("The final amount after discount for the Iphone 14 Ultra is", Iphone.apply_dsicount())
print("The final amount after discount for the Oppo A12 Ultra is", Oppo.apply_dsicount())
print("The final amount after discount for the Nokia A80 is", Nokia.apply_dsicount())
