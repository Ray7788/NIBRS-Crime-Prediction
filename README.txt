This repo contains Team Project(Group 4) for IT5006.

# Topic
In this project we aim to explore the relationship between crime and its spatial, temporal, and type features,
and to build a predictive model to forecast if the criminals will be arrested or not.

According to the FBI, crime is defined as "an act committed or omitted in violation of a law forbidding or commanding it and for which punishment has been prescribed by that law".
Crime is a complex social phenomenon that can be influenced by a variety of factors, including social, economic, and environmental conditions.


# Source data

This dataset utilizes two comprehensive crime datasets as stated below:
- 1. Chicago Crime Dataset: This dataset contains Official dataset from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) System. It is publicly available and can be accessed through the City of Chicago's Data Portal. We use Chicago dataset for training and initial validation.
- 2. NIBRS (National Incident-Based Reporting System): This dataset provides detailed information about crime incidents reported by law enforcement agencies across the United States.`We apply trained models to NIBRS data, to test model performance across different features and data distributions. 

# Data Processing

This part includes the data processing and cleaning steps. The data is read from a CSV file, and the following operations are performed:
- Missing values are handled by dropping rows with missing values.
- Make universal changes to the names of the columns from both Chicago Crime Dataset and NIBRS (National Incident-Based Reporting System) to ensure consistency.
- Filter the data to include only relevant columns and rows based on the topic of exploration: Spatial, Temporal, and Crime Type.
- Encode categorical variables to numerical values for analysis.
- Merge the different sub datasets of NIBRS based on the common columns using SQL queries.
    This SQL query consolidates incident-related data by joining multiple tables from the public schema. 
    It starts with the nibrs_incident table as the primary source and integrates data from related tables, including nibrs_arrestee (first arrestee details), nibrs_arrest_type (arrest type information), nibrs_offense (offense details), nibrs_offense_type (offense type descriptions), and nibrs_location_type (location details). 

- The data is then merged and saved to a new CSV file for further analysis.


# Feature Engineering

This part mainly includes Location (Spatial), Time (Temporal) and Crime Type features.

These features are extracted from the Chicago Crime Dataset and NIBRS (National Incident-Based Reporting System) datasets.
More details please refer to Feature_Eng folder.

The final version of the Feature Engineering notebook is saved as FeatureEng_ClearVersion.ipynb
(Archived versions of the single notebooks are also available in the Feature_Eng folder.)

# Model Training and Evaluation

This part includes the model training and evaluation steps.
There are three models trained and evaluated, including:
- CatBoost Classifier
- Random Forest Classifier
- Single Layer Neural Network

All model training and evaluation steps are performed in the Models folder.



