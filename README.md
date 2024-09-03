# VENDING-MACHINE-ANALYTICS
This dataset provides vending machine data from various locations in Central New Jersey, including a library, a mall, an office location, and a manufacturing site. 
The locations encompass: 
* Gutten Plans, a frozen dough specialist company operating 24/5, with vending machine GuttenPlans x1367. Additionally,
* EB Public Library, experiencing high foot traffic 5-6 days a week, has vending machine EB Public Library x1380.
* Brunswick Sq Mall, with average foot traffic 7 days a week, hosts vending machines BSQ Mall x1364 (Zales) and BSQ Mall x1366 (ATT). Finally,
* Earle Asphalt, a construction engineering firm operating 5 days a week, features vending machine Earle Asphalt x1371.
Data scientists can leverage this dataset to examine trends, user behavior, and consumer preferences across various locations. The dataset was obtained from a private organization via a link shared during a bootcamp for accessing practical and challenging datasets.

## Data Cleaning
I simply removed some rows irrelevant to the visualization of the data, there aren't so much null values which I was able to fill up the null values with the mode for Product with 6 null values and Category with 267,and I replaced the null values for the Mprice with the mean.
Lastly I categorized some of the data in the columns for easy visualization because of the duplicates present.

## EDA
I was able to perform the exploratory data analysis on the data using the .describe() function and was able to discover the most purchased category of product.

### EDA Thtough Visualization
Through my analysis of the dataset, I successfully derived valuable insights. The data revealed several key findings that provided a deeper understanding of the patterns and trends within the vending machine operations. These insights includes:

#### 1. The most frequently sold product category: 
![highest sold](https://github.com/user-attachments/assets/1b61b8f1-b6cf-4fa7-ab5c-b18b8171f8cd)

The analysis revealed that the 'FOOD' category is the highest-selling among all product categories. This indicates a strong consumer preference for food items, suggesting that customers are more likely to purchase food from vending machines than any other type of commodity. This trend highlights the significant demand for convenient and readily available food options, which could be a key factor in driving the overall sales performance of the vending machines.
 ##### Suggestions
  * Expand Food Offerings: Given the high demand for food items, consider expanding the variety of food products available in vending machines to include new and popular items.
  * Optimize Inventory: Ensure that popular food items are always in stock and monitor sales trends to adjust inventory levels accordingly to avoid stockouts.
  * Promotional Strategies: Implement targeted promotions or discounts on food items to attract more customers and boost sales further.
  
#### 2. The status option that appears most frequently: 
The analysis shows that the status labeled 'Processed Commodity' is the most frequently occurring status in the dataset, indicating that the majority of transactions involve items that have been successfully processed. In contrast, the 'Unlinked Commodity' status appears only 3 times, making it an extremely rare occurrence. This suggests that almost all products are properly linked and processed through the system, with only a negligible number of exceptions.
  ##### Suggestions
  * Maintain Quality Control: Since most transactions involve processed commodities, focus on maintaining high quality and consistency in these products to ensure customer satisfaction.
  * Monitor Rare Exceptions: Although 'Unlinked Commodity' status is rare, it’s important to investigate any occurrences to prevent potential issues and ensure all products are properly      linked and processed.

#### 3. The most common mode of transaction used by customers: 
The analysis indicates that customers overwhelmingly prefer using 'cash' as their mode of transaction, with cash transactions occurring more frequently than those using 'credit'. This preference suggests that cash is the more convenient or accessible payment method for most users, potentially reflecting the demographics or transaction habits of the customer base.
  ##### Suggestions
  * Enhance Cash Handling: Given the preference for cash transactions, ensure that cash handling systems are efficient and reliable. This includes regular maintenance of cash acceptors       and ensuring sufficient change is available.
  * Encourage Cashless Payments: While cash is currently preferred, introducing and promoting cashless payment options with incentives should be consider gradually to prepare for             potential shifts in payment trends.
  
#### 4. The location that generates the highest sales: 
The location 'Guttenplans' stands out as having the highest number of transactions, making it the top-performing location in terms of sales activity. Close behind is the 'EB Public Library,' which also experiences a high volume of transactions, indicating strong customer engagement at both sites. These findings highlight 'Guttenplans' as a key location for vending machine success, with the 'EB Public Library' also playing a significant role.
  ##### Suggestions
  * Focus on High-Performing Locations: Invest in maintaining and possibly expanding vending machine installations at 'Guttenplans' due to its high sales performance.
  * Leverage Successful Locations: Analyze what makes 'Guttenplans' and 'EB Public Library' successful (e.g., foot traffic, demographics) and apply similar strategies to other locations      to enhance their performance.
  * Optimize Product Placement: Ensure that the product mix at these top locations is optimized to meet customer preferences and maximize sales.

#### 5. The vending machine with the highest overall sales performance: 
Lastly, the machine identified as 'GuttenplansX1367' has recorded the highest number of transactions, making it the top-performing machine in the dataset. This machine's strong performance further underscores the popularity and success of the 'Guttenplans' location, as it not only leads in overall transactions but also houses the most active vending machine.
  ##### Suggestions
  * Monitor and Maintain Top Performers: Regularly check and maintain 'GuttenplansX1367' to ensure it continues to operate smoothly and remains in top condition.
  * Analyze Successful Features: Investigate any specific features or locations of 'GuttenplansX1367' that contribute to its success, and consider replicating these features in other         machines.
  * Leverage High-Performing Machines: Use 'GuttenplansX1367' as a benchmark for performance and consider showcasing its success in marketing materials or case studies.

#### By implementing these recommendations, I believe the business can optimize its vending machine operations, enhance customer satisfaction, and drive greater overall success.
