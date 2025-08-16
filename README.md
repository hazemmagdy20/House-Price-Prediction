# House-Price-Prediction

**Project Overview**

This is a Machine Learning project for Predicting House prices using Linear regression Model using a simple and very small dataset from kaggle and customized on special region.

**DataSet** 

It consists of 155 Rows.

It contains The following columns:

  1- **Price**    : price of house
  
  2- **Bedroom**  : number of bedrooms
  
  3- **Room**     : number of rooms
  
  4- **Space**    : size of house (in square feet)
  
  5- **Lot**      : width of a lot
  
  6- **Tax**      : amount of annual tax
  
  7- **Bathroom** : number of bathrooms
  
  8- **Garage**   : number of garage
  
  9- **Condition**: condition of house (1 if good , 0 otherwise)


**Steps Done**

1- **Import Libraries:** 
  - Imported necessary libraries including pandas, numpy, matplotlib, seaborn, and scikit-learn modules for data manipulation, visualization, and modeling.

2- **Load the Dataset:**
  - Loaded the real estate dataset from a CSV file (/content/realest.csv) into a pandas DataFrame.

3- **Data Exploration & Cleaning:**
  - Checked for missing values using isnull().sum().
  - Handled missing values by removing the last row (which contained all nulls) and then imputing the remaining missing values with the mean of their respective columns.
  - Checked for and confirmed no duplicate rows existed in the dataset.

4- **Exploratory Data Analysis (EDA):** 
     
  - Examined the data types and non-null counts using df.info().
  
  - Examined the data types and non-null counts using df.info().
     
  - Generated descriptive statistics using df.describe().
    
  - Visualized the distribution of each variable using histograms.
    
  - Generated box plots to identify potential outliers in numerical features.

  - Used the IQR method to quantify the number of outliers in various columns.

  - Presented two options for handling outliers: removing rows with outliers and imputing outliers with the mean. The imputation method was chosen for the final DataFrame.

  - Visualized the relationship between 'Price' and 'Space', and 'Price' and 'Room' using scatter plots.

  - Generated a correlation matrix and heatmap to understand the relationships between numerical variables.

5- **Feature Engineering:**
  
  - Selected numerical columns for scaling (excluding 'Garage', 'Condition'). aleardy in the scale [0, 2]
  
  - Initialized and applied StandardScaler to the selected numerical features.
  
  - Saved the fitted scaler to a file (scaler.pkl) For deployment.

6- **Define Features (X) and Target (Y) and Split Data:**
    
  - Defined the features (X) as all columns except 'Price' and the target (y) as the 'Price' column.

  - Split the data into training and testing sets using train_test_split (95% train, 5% test) because the data is very small.

7- **Model Training and Evaluation (Linear Regression):**
   
  - Initialized a LinearRegression model.

  - Trained the model using the training data (X_train, y_train).
  
  - Made predictions on the test data (X_test).
  
  - Evaluated the model's performance using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared (R2).
  
  - Saved the trained model to a file (model.pkl) For deployment.

    
**Results**

- Mean Squared Error (MSE): 16.01

- Root Mean Squared Error (RMSE): 4.00

- Mean Absolute Error (MAE): 3.38

- R-squared (R2): 0.84   where 84% of the variance in house prices can be explained by the features in the model.

**Deployment**

 I used Flask framework to deploy the model locally.

 I build simple user interface to take features from the user as input, then scale it using the same scaler used in the modeland finally get the prediction of the House.
