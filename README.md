# VENDING-MACHINE-ANALYTICS
This dataset provides vending machine data from various locations in Central New Jersey, including a library, a mall, an office location, and a manufacturing site. 
The locations encompass: 
* Gutten Plans, a frozen dough specialist company operating 24/5, with vending machine GuttenPlans x1367. Additionally,
* EB Public Library, experiencing high foot traffic 5-6 days a week, has vending machine EB Public Library x1380.
* Brunswick Sq Mall, with average foot traffic 7 days a week, hosts vending machines BSQ Mall x1364 (Zales) and BSQ Mall x1366 (ATT). Finally,
* Earle Asphalt, a construction engineering firm operating 5 days a week, features vending machine Earle Asphalt x1371.
Data scientists can leverage this dataset to examine trends, user behavior, and consumer preferences across various locations. The dataset was obtained from a private organization via a link shared during a bootcamp for accessing practical and challenging datasets.

## Data Cleaning
* I performed a data cleaning process where I meticulously removed rows deemed irrelevant to the visualization objectives. This involved identifying and excluding data points that did not contribute meaningfully to the analysis or were likely to distort the insights. Specifically, I focused on eliminating entries that were not aligned with the core metrics of interest, such as rows with incomplete or erroneous information, test data, or outliers that could skew the results. This targeted approach ensured that the dataset used for visualization and subsequent analysis was more refined and relevant, thereby enhancing the accuracy and clarity of the insights derived from the data.
  ![drop](https://github.com/user-attachments/assets/c015d783-ce7f-483c-b98c-7d4f013095ef)

* There were relatively few null values in the dataset. To address these, I took the following steps: For the 'Product' column, which had 6 null values, I filled these with the mode of the column to ensure that missing entries were replaced with the most frequently occurring product, thereby preserving the typical data distribution. Similarly, for the 'Category' column, which had 267 null values, I also used the mode to fill in these gaps, maintaining consistency with the most common category.

For the 'MPrice' column, where missing values were present, I replaced these with the mean price. This approach was chosen to provide a balanced estimate of the missing data, reflecting the average price of the products and ensuring that the overall pricing trends were accurately represented. By employing these methods, I was able to maintain the integrity and usability of the dataset while preparing it for comprehensive analysis.

![null](https://github.com/user-attachments/assets/77543c7c-a765-461f-b679-1408cbce0583)
![mean mode](https://github.com/user-attachments/assets/358128db-03b8-48e8-b227-452ae2d36d61)

* Lastly, I categorized certain data within the columns to facilitate easier visualization and analysis, particularly due to the presence of duplicate entries. By grouping similar data points into categories, I was able to streamline the dataset and reduce redundancy. This categorization involved consolidating duplicate values and organizing data into more meaningful groups, which enhances clarity and allows for more straightforward analysis. This approach not only improved the overall structure of the dataset but also made it more manageable and insightful for visualization purposes.
![group](https://github.com/user-attachments/assets/b271ba10-ce49-430a-bb59-81763719e5d1)


## EDA
I conducted exploratory data analysis (EDA) on the dataset using the *.describe()* function, which provided a comprehensive summary of key statistical metrics across various columns. Through this analysis, I identified the most frequently purchased product category. This discovery was facilitated by examining summary statistics such as counts, means, and distributions, which highlighted the dominant trends and preferences within the dataset. By leveraging these insights, I was able to pinpoint the category that shows the highest purchase frequency, thereby gaining valuable information about customer preferences and behavior.

### EDA Thtough Visualization
Through my analysis of the dataset, I successfully derived valuable insights. The data revealed several key findings that provided a deeper understanding of the patterns and trends within the vending machine operations. These insights includes:

#### 1. The most frequently sold product category: 
![highest sold](https://github.com/user-attachments/assets/1b61b8f1-b6cf-4fa7-ab5c-b18b8171f8cd)

The analysis revealed that the 'FOOD' category is the highest-selling among all product categories. This indicates a strong consumer preference for food items, suggesting that customers are more likely to purchase food from vending machines than any other type of commodity. This trend highlights the significant demand for convenient and readily available food options, which could be a key factor in driving the overall sales performance of the vending machines.
 ##### Suggestions
  * Expanding Food Offerings: Given the high demand for food items, expanding the variety of food products available in vending machines to include new and popular items should be            considered.
  * Optimizing Inventory: Ensuring that popular food items are always in stock and monitor sales trends to adjust inventory levels accordingly to avoid stockouts.
  * Promotional Strategies: Implementing targeted promotions or discounts on food items to attract more customers and boost sales further.
  
#### 2. The status option that appears most frequently: 
The analysis shows that the status labeled 'Processed Commodity' is the most frequently occurring status in the dataset, indicating that the majority of transactions involve items that have been successfully processed. In contrast, the 'Unlinked Commodity' status appears only 3 times, making it an extremely rare occurrence. This suggests that almost all products are properly linked and processed through the system, with only a negligible number of exceptions.
  ##### Suggestions
  * Maintaining Quality Control: Since most transactions involve processed commodities,maintaining high quality and consistency in these products to ensure customer satisfaction should       be focused on.
  * Monitoring Rare Exceptions: Although 'Unlinked Commodity' status is rare, it’s important to investigate any occurrences to prevent potential issues and ensure all products are            properly linked and processed.

#### 3. The most common mode of transaction used by customers: 
![transaction](https://github.com/user-attachments/assets/ba672520-482a-40ae-ac26-ed31f0c28dad)

The analysis indicates that customers overwhelmingly prefer using 'cash' as their mode of transaction, with cash transactions occurring more frequently than those using 'credit'. This preference suggests that cash is the more convenient or accessible payment method for most users, potentially reflecting the demographics or transaction habits of the customer base.
  ##### Suggestions
  * Enhancing Cash Handling: Given the preference for cash transactions, one should ensure that cash handling systems are efficient and reliable. This includes regular maintenance of         cash acceptors and ensuring sufficient change is available.
  * Encouraging Cashless Payments: While cash is currently preferred, introducing and promoting cashless payment options with incentives should be consider gradually to prepare for           potential shifts in payment trends.
  
#### 4. The location that generates the highest sales: 
![location](https://github.com/user-attachments/assets/54b4e812-0a4d-41a6-b120-e759bba3afd7)

The location 'Guttenplans' stands out as having the highest number of transactions, making it the top-performing location in terms of sales activity. Close behind is the 'EB Public Library,' which also experiences a high volume of transactions, indicating strong customer engagement at both sites. These findings highlight 'Guttenplans' as a key location for vending machine success, with the 'EB Public Library' also playing a significant role.
  ##### Suggestions
  * Focusing on High-Performing Locations: Investment in maintaining and possibly expanding vending machine installations at 'Guttenplans' due to its high sales performance.
  * Leveraging Successful Locations: What makes 'Guttenplans' and 'EB Public Library' successful (e.g., foot traffic, demographics) should be analyzed and similar strategies should be         applied to other locations to enhance their performance.
  * Optimizing Product Placement: Ensuring that the product mix at these top locations is optimized to meet customer preferences and maximize sales.

#### 5. The vending machine with the highest overall sales performance: 
![highest sales machine](https://github.com/user-attachments/assets/83a889a8-34b5-44b1-9ad1-69c15be652c6)

Lastly, the machine identified as 'GuttenplansX1367' has recorded the highest number of transactions, making it the top-performing machine in the dataset. This machine's strong performance further underscores the popularity and success of the 'Guttenplans' location, as it not only leads in overall transactions but also houses the most active vending machine.
  ##### Suggestions
  * Monitoring and Maintaining Top Performers: Regularly checking and maintaining 'GuttenplansX1367' to ensure it continues to operate smoothly and remains in top condition.
  * Analyzing Successful Features: Investigating any specific features or locations of 'GuttenplansX1367' that contribute to its success, and replicating these features in       other machines should be considered.
  * Leveraging on High-Performing Machines: Using 'GuttenplansX1367' as a benchmark for performance and considering showcasing its success in marketing materials or case studies.

#### By implementing these recommendations, I believe the business can optimize its vending machine operations, enhance customer satisfaction, and drive greater overall success.
