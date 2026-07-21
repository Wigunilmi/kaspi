import pandas as pd

data = pd.read_excel(r"C:\Users\Пользователь\Desktop\kaspi\Prices list.xlsx")
sku = data['SKU (Vendor Code)']
stock_almaty = data['Warehouse Stock (Almaty)']
stock_astana = data['Warehouse Stock (Astana)']
prices=data['Retail Price']

availability=[]
for i in range(len(stock_astana)):
    alma = stock_almaty.iloc[i]
    asta = stock_astana.iloc[i]

    try:
        alma = float(alma)
    except (TypeError, ValueError):
        alma = 0

    try:
        asta = float(asta)
    except (TypeError, ValueError):
        asta = 0

    status = 'available' if alma + asta > 0 else 'not available'
    availability.append(status)

wrong_nums=[]
#Loop through each row one by one.
for value in prices:
    wrong_nums.append(value)

clean_prices=[]
for price in wrong_nums:
    
    try:
        cena=''
        for p in price:
            if p.isdigit():
                cena += p
        if cena:
            clean_prices.append(cena)
        else:
            clean_prices.append(price)
    except TypeError:
        clean_prices.append(price)
for i in range(len(availability)):
    
    
    print(sku[i],end=' ')
    print(clean_prices[i],end=' ')
    print(availability[i],end='\n')
df = pd.DataFrame({
    'SKU': sku.astype(str),
    'Price': [str(x) for x in clean_prices],
    'Stock': availability
})

# Make the output column appear as expected in Excel
for col in ['SKU', 'Price', 'Stock']:
    df[col] = df[col].astype(str)

df.to_excel('sueta.xlsx', index=False)
print('vse chetko brat')
    
    