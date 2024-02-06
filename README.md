# 1Mg Homeopathic

 Scrape the homeopathic medicine data from online medicine delivery platform `1mg` using python library called Beautifulsoup (or similar) and collect information in the given format and make 2 tables using the data:

Table 1 : `medicine_name`

Attributes in table - 2:

`name` - Name of the medicine

`size_of_the_bottle` - Size of the medicine bottle or pack
 `MRP_of_the_bottle`  - MRP of the bottle

`price_of_the_bottle`  - Selling price of the bottle
`1mg_url` - 1mg url where the medicine sold


Table - 2 : `medicine_details`

Attributes in table - 2:

`name` - Name of the medicine

`brand_name`  - Brand name

`key_benefits` - Key Benefits area (Hair, eye, joint, skin)

`key_ingredients` - Ingredient of medicine

`rating` - user rating of the medicine

`number_of_rating`  - Number of people rated that product


Following needs to be ensured while scraping:

Once you have the database of 2 tables created.

- You need to generate aggregations and that will help you create dashboard which should be able to help the end user with following insights:
    - Number of medicine available of different benefit area.
    - Price range of medicine for each benefit area.
    - Brand specialization(Key Benefits) of each area.
    - Average price, min price , max price and number of products for each brand.
    - Average number of rating for each brand in their specialization products where  the number of rating is not NULL.
    - Maximum number of times ingredient used in each benefit area.
    - **Average cost for ingredients.**
    - Most used ingredient
    - Which brand has most greater than 4 point review medicine?
- You are hired in a consultancy firm, one of their client want to open a homeopathic medicine store what is their total cost for open their store. Create an interactive dashboard for them to analyze and select best medicine for their store. (Use benefit area as a filter)
