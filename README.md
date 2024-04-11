# VENDING-MACHINE-PROJECT
This dataset provides vending machine data from various locations in Central New Jersey, including a library, a mall, an office location, and a manufacturing site. 
The locations encompass Gutten Plans, a frozen dough specialist company operating 24/5, with vending machine GuttenPlans x1367. Additionally, EB Public Library, experiencing high foot traffic 5-6 days a week, has vending machine EB Public Library x1380. Brunswick Sq Mall, with average foot traffic 7 days a week, hosts vending machines BSQ Mall x1364 (Zales) and BSQ Mall x1366 (ATT). Finally, Earle Asphalt, a construction engineering firm operating 5 days a week, features vending machine Earle Asphalt x1371. Data scientists can utilize this dataset to analyze trends, user behavior, and consumer preferences across different locations.
I got the dataset from a goodle drive shared to access workable and tasking datasets.

## Data Cleaning
I simply removed some rows irrelevant to the visualization of the data, there aren't so much null values. I was able to fill u[p the null values with the mode for Product with 6 null values and Category with 267,and I replaced the null values for the Mprice with the mean.
Lastly I categorized some of the datum in the columns for easy visualization cause of the duplicates present.

## EDA
I was able to perform the eploratory data analysis on the data using the .describe() function and most purchased category of product.

## VISUALIZATION
I made visualizations tpo draw insights on the following information on the data.
* Highest sold Category
* Status with highest Option
* Mode of Transaction
* Location with highest sales
* Machine with the highest Sales
  
## INSIGHTS
* Highest sold category is food which implies that customers has more need for food than every other commodity
* Status with highest option is proceesed commodity with the unlinked commotity with so insignificant value of 3
* The most prefered mode of transaction by the customers is cash over credit
* Guttenplans is the location with the highest transaction and EB public library is close to this
* Lastly the machine with the hightes transaction is the GuttenplansX1367

## SUGGESTIONS
* Commodity with highest demand should be made available always without default
* Location with the highest transaction should be focused on for supply of commodity for customers
* Lastly, the mode of transactions should be made available and the credit means should be encouraged for safety putpose.
