#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 忽略跳過指定的條件不處理
		name, price = line.strip().split(',') #split以什麼為基準切割為一行，這邊用逗號。strip把空格與\n換行符號去掉
		products.append([name, price])
print(products)

#使用者輸入
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

#印出所有購買紀錄
for p in products
	print(p[0], '的價格是', p[1])
	
#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #\n 分行、換行

#CSV是電腦最常使用的資料儲存模式，而且可以使用excel打開，非常方便。
#資料通常都是用逗點做區隔，才能有資料儲存區隔，不然會塞在同一格，很難使用。
#每一單筆資料一定要換行，加入換行符號