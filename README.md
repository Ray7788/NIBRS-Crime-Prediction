IT5006-Group4 Group Project
========================
This repo contains Team Project(Group 4) for IT5006.

# Topic
In this project we aim to explore the relationship between crime and its spatial, temporal, and type features,
and to build a predictive model to forecast if the criminals will be arrested or not.

According to the FBI, crime is defined as "an act committed or omitted in violation of a law forbidding or commanding it and for which punishment has been prescribed by that law".
Crime is a complex social phenomenon that can be influenced by a variety of factors, including social, economic, and environmental conditions.


# Framework
The project is structured into several folders, each containing specific components of the project. The main folders are as follows:
- Data(stored in local disk, not included for Repository as it is so large): This folder contains the raw data files used in the project. The data is sourced from the Chicago Crime Dataset and NIBRS (National Incident-Based Reporting System).
- EDA_Code: This folder contains the exploratory data analysis scripts and notebooks used to analyze the data and visualize the findings.
- Feature_Eng: This folder contains the feature engineering scripts and notebooks used to extract and preprocess the features from the raw data. The final version of the Feature Engineering notebook is saved as FeatureEng_ClearVersion.ipynb.
- Models: This folder contains the model training and evaluation notebooks. It includes the implementation of various machine learning models, such as CatBoost Classifier, Random Forest Classifier, and Linear Regression.
- Preprocessing: This folder contains the preprocessing scripts and notebooks used to clean and prepare the data for analysis. It includes data cleaning, handling missing values, and encoding categorical variables.

FeatureEng_ClearVersion.ipynb: This notebook contains the final version of the feature engineering process.

Model_merged_model.ipynb: This notebook contains the final version of the model training and evaluation process.

# Source data

This dataset utilizes two comprehensive crime datasets as stated below:
- 1. Chicago Crime Dataset: This dataset contains Official dataset from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) System. It is publicly available and can be accessed through the City of Chicago's Data Portal. We use Chicago dataset for training and initial validation.
Data range is from 2020 to 2025.
Downloaded from: https://data.cityofchicago.org/

- 2. NIBRS (National Incident-Based Reporting System): This dataset provides detailed information about crime incidents reported by law enforcement agencies across the United States. We apply trained models to NIBRS data, to test model performance across different features and data distributions. 
Data range: 2023
Downloaded from: "Crime Incident-Based Data by State" (Illinois) 

We choose `Illinois` as the target state for NIBRS dataset, as it is also compatible with the Chicago Crime Dataset due to its geographical proximity (Chicago is located in Illinois but not specifically listed in test dataset) and the fact that both datasets are from the same state.


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
The preprocessed data are stored using Google Drive:
https://drive.google.com/drive/folders/1pULsKCZ7zrCvqgNlTCsjgS9YP2DOE22m?usp=sharing

# Model Training and Evaluation

This part includes the model training and evaluation steps.
There are three models trained and evaluated, including:
- CatBoost Classifier
- Random Forest Classifier
- Linear Regression

All model training and evaluation steps are performed in the Models folder.

# Contributions:
We acknowledge the contributions of each team member in the project. The order of the names does not indicate the order of contributions.
The project was a collaborative effort, and all team members played a significant role in its success.

The contributions are as follows:
- Data Collection and Preprocessing and EDA: [Fu Jiayu, PIMSUPA ARIYAPOOLPONG, Xu Rui, Sui He]
- Feature Engineering: [PIMSUPA ARIYAPOOLPONG, Xu Rui, Fu Jiayu]
- Model Training and Evaluation: [PIMSUPA ARIYAPOOLPONG, Xu Rui, Fu Jiayu]
- Documentation and Reporting: [Sui He]


# Dependencies
Please check the `requirements.txt` in the root directory for the list of dependencies required to run the project.
- Python 3.10 or higher

When you run notebooks, please be careful handling file paths as it might not be totally suitable for your local environment.
