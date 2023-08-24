# Telco Project

## Project Description
* This project uses the telco data set from MySql and is used for practice on figuring out why customers are churning using the data science pipeline.

## Project Goal
* Discover which customers are more likely to churn based of the different features
Use machine learning model to classify customers likely to churn.

## Initial Thoughts

Need to figure out what features will lead me to the most churn based off the customers who have churned and create/fit a model that will find probable churn.

## The Plan

* Acquire data from sql

* Prepare Data

    * Drop unnecessary columns(Update list here)
    * Clean up the number values
    * Encode values for the features used in the future

* Explore

    * What features did the customers who churned had or didn't have
    * What features do long term customers have 
    * List of Potential churn items From a simple barchart 

* Modeling

    * Use drivers in explore to build predictive models of different types
    * Evaluate models on train and validate data
    * Select the berst model based on accuracy
    * Evaluate the test data

## Data Dictionary

| Feature | Definition |<br>
|--------|-----------|<br>
|Customer ID| Customer's unique identifier|<br>
|Gender| Customer's gender|<br>
|Senior_Citizen| Whether the customer is a senior citizen or not|<br>
|Partner| Whether the customer has a partner or not|<br>
|Dependents| Whether the customer has dependents or not|<br>
|Tenure| Number of months customer has been with company in whole numbers|<br>
|Online Security| OnlineSecurity: Whether the customer has online security or not|<br>
|Online Backup| Whether the customer has online backup or not|<br>
|Device Protection| Whether the customer has device protection or not|<br>
|Tech Support| Whether the client has tech support or not|<br>
|Churn| Has the customer churned|<br>
|Additional Features| Encoded and values for categorical data and scaled versions continuous data|<br>

## How to Reproduce

* Clone this repo
* Acquire data from MySql (It should make a telco.csv after)
* Run Notebook

## Takeaways and Conclusions

* Most churn: No Online Security, No Online Backup, No Device Protection, No Tech Support, Month-to-Month Contract Types, Fiber Optic Internet Service Type, Electronic Check Payment Types

* No significant difference in churn(per visuals): Gender, Partner, Phone Service, Multi Lines, Streaming TV or Movies, Paperless Billing, Auto Payments and Mailed Checks.

* Logistic Regression model performed the best on the accuracy for determining churn

## Recommendations

* I would recommend that somehow we push customers towards getting Online Security and Backup, Tech Support, and Device Protection.

* I would also recommend that customers are driven towards DSL and automatic Payments like Bank Transfer or Credit Card.


