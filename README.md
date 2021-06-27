# Balaji-supermarket-api
This is basic backend Rest API for Supermarket cretaed using Django rest framework. This allows to add new items to the system & checkout items when customer buys the product.

## Technical specification
API has two tables,
### 1) Product_Entry
This table responsible to add new items to the system. Below are the fields,                                                          
*<b>name</b> - Name of the Product | String with max of 30 chars.                                   
*<b>category</b> - Category of the Product | String with max of 30 chars. It has multiple choices with default choice as OTHERS. The choices are, FROZEN_FOOD, FRUITS, VEGETABLE, COOKING_ITEMS, CANNED_GOODS, SNACKS, CEREAL, PERSONAL_CARE, HOUSEHOLD_ITEMS, MASALA, COOL_DRINKS, ELECTRONICS, OTHERS                                                                         
*<b>cost_prize</b> - Cost Price of the product | Accept float & it is not null field                                                                                  
*<b>expiry_date</b> - Expiry date of the Product | By default, it sets the date as 10000 days from today.                                                         
*<b>count</b> - Count of the product | It is integer and minimum value is 0 & default value is 1.                                                                     
*<b>specs</b> - Specification of the product for easy remeberance | String with max 50 chars & it is not null field.                                   
*<b>created_date</b> - Timestamp when the record is created.                                                                                                 
*<b>updated_date</b> - Timestamp when the record is updated.                                                                          
*<b>is_sold</b> - Flag is true when the product is available otherwise False.                                                                        
*<b>brand</b> - Brand of the product | String with max 30 chars & non mandatory field.                                                             

### 2) Product_Exit
This table responsible to checkout existing items from the system. Below are the fields,                                                          
*<b>product_entry</b> - Foreign key relates to Product_Entry table.                                                                            
*<b>selling_price</b> - Selling price of the product | Accept float & it is not null field                                                                                  
*<b>profit</b> - Profit from this product | This will be calculated in background.                                                                   
*<b>expiry_date</b> - Expiry date of the Product | By default, it sets the date as 10000 days from today.                                                         
*<b>count</b> - Count of the product | It is integer and minimum value is 0 & default value is 1.                                                                     

## API End point

### To add new product
https://balaji-supermarket-api.herokuapp.com/add_product/

### To view details any product
https://balaji-supermarket-api.herokuapp.com/add_product/1

### To add new transaction
https://balaji-supermarket-api.herokuapp.com/buy_product/

### To view details of new transaction
https://balaji-supermarket-api.herokuapp.com/buy_product/1

