# Telco Project

# Project Description


# Project Goal
Discover which customers are more likely to churn based of the different features
Use machine learning model to classify customers likely to churn


# Initial Thoughts

Need to figure out what features will lead me to the most churn based off the customers who have churned
Need to see the features that customers have that havent churned yet
so first split between churned and not churned


# The Plan
* Acquire data from sql
* Prepare Data
    * Drop unnecessary columns(Update list here)
    * Clean up the number values
    * Create Dummies for the features used in the future

* Explore
    * What features did the customers who churned had or didn't have
    * What features do long term customers have 
    * List of Potential churn items From a simple barchart (No = Not alot of diff between yes & no categories on churn)
        * Gender - No
        * Senior Citizen - 
                Maybe(closer to death, makes sense)
        * Partner - Maybe(leaning No)
        * Dependents - Maybe(leaning No)
        * Phone Service - No
        * Multiple Lines - No
        * Online Security - Maybe
                Customers who did NOT have Sec More Likely to churn.
                chi test ran
        * Online backup - Maybe
                Customers who did NOT have online backup More Likely to churn?
                chitest ran
        * Device Protection - Maybe
                Customers who did NOT have device protection More Likely to churn?
                chi test ran
        * Tech Support - Maybe
                Customers who did NOT have tech support More Likely to churn?
                chi test ran
        * Streaming TV - No
        * Streaming Movies - No
        * Paperless Billing - ?? No..
        * Contract Type - Def b/c mo-2-mo
        * Internet Service Type - Maybe 
                (Fiber optic 40% churn compared to 20% DSL)
                More likely to churn if you have fiber?
                chi test ran

        * Payment Type - Maybe
                (Electric Check shows about 50% churn compared to the other 3 forms of payment)
    
* Modeling
    * What model do I need
    Ran Decision Tree

    Ran Random Forest

    Ran KNN

    Ran Logistic Regression wiht all feats
    

* Draw Conclusions

# Data Dictionary

Features | Definition
payment_type_id : Will drop (Duplicates payment_type)
internet_service_type_id : Will drop (Duplicates internet_service_type_id)
contract_type_id : Will drop (Duplicates contract_type)
customer_id : object used as index
gender : Customer's Gender (Male, Female)
senior_citizen : Whether the customer is a senior citizen or not (1:Yes, 0:No)
partner : Whether the customer has a partner or not (Yes, No)
dependents : Whether the customer has dependents or not (Yes, No)
tenure : Number of months customer has been with company in whole numbers
phone_service : Whether the customer has phone_service or not (Yes, No)
multiple_lines : Whether the customer has multiple lines or not (No phone service, No, Yes)
online_security : OnlineSecurity: Whether the customer has online security or not (No internet service, No, Yes)
online_backup : Whether the customer has online backup or not (No internet service, No, Yes)
device_protection : Whether the customer has device protection or not (No internet service, No, Yes)
tech_support : Whether the client has tech support or not (No internet service, No, Yes)
streaming_tv : Whether the client has streaming TV or not (No internet service, No, Yes)
streaming_movies : Whether the client has streaming movies or not (No internet service, No, Yes)
paperless_billing : Whether the client has paperless billing or not (Yes, No)
monthly_charges : The amount charged to the customer monthly  
total_charges : The total amount charged to the customer
churn : Has the customer churned (Yes, No)
contract_type : Type of contract (One Year, Month-to-Month, Two Year)
internet_service_type : Type of internet service the customer has (DSL, Fiber optic, No)
payment_type : The customer's payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit Card (automatic))

# How to Reproduce


# Takeaways and Conclusions


# Recommendations
