products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': #離開
		break
	price = input('請輸入商品價格：')
	price = int(price)
	p = [] #p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p) #products.append([name, price])
print(products)

for p in products
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #\n 分行、換行

#CSV是電腦最常使用的資料儲存模式，而且可以使用excel打開，非常方便。
#資料通常都是用逗點做區隔，才能有資料儲存區隔，不然會塞在同一格，很難使用。
#每一單筆資料一定要換行，加入換行符號