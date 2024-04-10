# 1mg_Homepathic

## Introduction
In the rapidly evolving landscape of healthcare, data analytics plays a pivotal role in enabling informed decision-making processes. The pharmaceutical sector, particularly the homeopathic medicine segment, stands to benefit significantly from the insights derived through data analysis. This project focuses on harnessing the power of data analytics to provide actionable insights for individuals or organizations involved in the homeopathic medicine industry.

## Overview
This project aims to perform data analytics on homeopathic medicine data scraped from the 1mg website. The objective is to provide insights to help with the selection and analysis of medicines for a homeopathic medicine store.

## Phase: 1
### Web_scraping 
Scrape the homeopathic medicine data from online medicine delivery platform 1mg using python library called Beautifulsoup (or similar) and collect information in the given format and make 2 tables using the data

URL = "https://www.1mg.com/categories/homeopathy-57"

### Tables 
#### Medicine_list
|   |   |
| ------------ | ------------ |
| Name   |  Name of the medicine |
| Size_of_the_bottle  |  Size of the medicine bottle or pack  |
| MRP_of_the_bottle  | MRP of the bottle  |
|  Price_of_the_bottle |  Selling price of the bottle |
| 1mg_url  | 1mg url where the medicine sold |

#### Medicine_details

|   |   |
| ------------ | ------------ |
| Name  | Name of the medicine  |
| Brand_name  | Brand name  |
| Key_benefits  | Key Benefits area (Hair, eye, joint, skin)  |
| Key_ingredients  | ngredient of medicine  |
| Rating  | user rating of the medicine   |
| Number_of_rating  |  Number of people rated that product  |

## Phase: 2
### Dashboard 

After extracting table data through web scraping, we analyze it with statistical calculations and visualization techniques, like graphs and heat maps, to identify trends and patterns. We can then create an interactive dashboard with features like filtering, sorting, and drill-down options for easy-to-understand data presentation and user interaction.

![image](https://github.com/PenchalaTeja/1mg_Homeopathic-/assets/156883419/c9afdbd4-5ed9-4c96-a3c2-009d467963ad)





