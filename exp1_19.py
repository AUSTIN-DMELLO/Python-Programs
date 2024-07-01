import datetime 
shopping_list=['meat','cheese'] 
current_time=datetime.datetime.now() 
formatted_time=current_time.strftime("%m/%d %H:%M") 
print(f"You are shopping at {formatted_time}") 
for i in range(3): 
    new_item=input("Add a new item to the shopping list: ") 
    shopping_list.append(new_item) 
while len(shopping_list) > 2: 
    purchased_item=input('What item did you just purchase? ') 
    shopping_list.remove(purchased_item) 
out_of_stock_item=shopping_list[0] 
print('Store is out of items.') 
renew_item=input('Please enter replacement item: ') 
shopping_list.append(renew_item)
print('Final shopping list: ',shopping_list) 
print('Thanks for shopping.')