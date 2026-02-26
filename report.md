# Enterprise Semester 2 Group Project – Dataset Analysis 
### Dataset used: [Student Screen Time vs. CGPA Analysis - 2026](https://www.kaggle.com/datasets/rishisukumar/student-screen-time-vs-cgpa-analysis-2026)

## Dataset Overview
The data that was used in the project is data that was used to track university students perfomance for two semesters. It consists of 547 rows and 11 columns. The data set has basic students information that include the gender, age and their perfomance throughot two semseters. The data was presented in the excel form. 

After collecting the raw data, we created a new sheet in excel and renamed it Clean_data to distinguish between the raw data and the clean data. The first thing that was done was checking if there were any duplicates of data and removed. From then we proceeded to check if there were any empty cells and there were cleaned too. 

We proceeded to analysse the data using different functions to check the 



## Machine Learning 
A machine learning python file was created, based upon the one used by Keith in his tutorial video. I modified it to represent my data columns in my data set.  
It was a struggle setting up the virtual environment, as the imports apparently were missing some dependencies. I had to reinstall the imports several times before they worked the intended way.

### Data Cleaning Summary 
Putting the data through logistic regression cleaned the data, making it a Boolean, either the student got an 8.0 CGPA or they didn’t. I created a new column from the old total_hours_studied column, but it checked if the values were above, equal to or below 8.0, and set the values to 1 if above and to 0 if below. This filtered the list to show only the passing grades, and as a result also showed a recommended number of hours to study based on who passed the filter. 
