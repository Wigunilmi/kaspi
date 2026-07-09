import pandas as pd
#Open the raw CSV file.
data=pd.read_excel('Prices list.xlsx',usecols=[0])
rows=data.shape
wrong_nums=[]
#Loop through each row one by one.
for i in range(rows[0]):
    for j in range(rows[1]):
        wrong_nums.append(data.iloc[i,j])
clean_nums=[]
for i in range(len(wrong_nums)):
    item = str(wrong_nums[i]).lower()
    cleaned=''
    #Check: Does this row have a price? If no, skip/discard it.
    for elem in item:
        if elem.isdigit():
            cleaned+=elem
    has_currency='tenge' in item or 'tg' in item or 'kzt' in item or 'тенге' in item or "тг" in item
    has_only_digits_or_spaces=all(c.isdigit() or c.isspace() for c in item)
    
    
    if cleaned!='' and (has_only_digits_or_spaces or has_currency):
        clean_nums.append(cleaned)
print(clean_nums)
df = pd.DataFrame(clean_nums, columns=['Price'])
df.to_excel('cleaned_products.xlsx', index=False)
print("File saved as cleaned_products.xlsx")






#Clean Name: Find double spaces and replace them with single spaces.

#Clean Price: Remove "KZT", remove "Тг", strip any hidden spaces, and convert the remaining text into a pure number.

#Save this newly minted, shiny data into a new list.

#Write that list into cleaned_products.csv.