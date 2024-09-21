# Pusula Data Science Case Study

## Yusuf Mert Çelikarslan - yusufmertcelikarslan@gmail.com

This project includes analysis and preprocessing steps of side_effect_data.xlsx

<p>
Jupyter notebook divided into three main sections:
<ol>
    <li>Loading and analyzing dataset</li>
    <ul>
        <li>Rename Columns</li>
        <li>Create a user dataframe</li>
        <li>Bar graph of each feature</li>
        <li>Datetime Features</li>
        <li>Correlations</li>
    </ul>
    <li>Train and test split</li>
    <ul>
        <li>Normal Split</li>
        <li>Stratified Split</li>
    </ul>
    <li>Preprocess and train</li>
    <ul>
        <li>Missing Values</li>
        <li>Feature Importance</li>
        <li>Outliers</li>
        <li>Clustering</li>
        <li>Train and Test Scores</li>
    </ul>
</ol>
</p>

<p>The model evaluation step was performed only to extract the feature importance of each feature. The pre-processed dataset was saved as a csv file in the dataset folder for future use.
</p>

### Project Configuration

<p>
Funcstions used in data_analysis.ipynb can be found in utils folder divided into three differents module. Each module is specific to their purpose. 
In order to run project, .ipynb extension file can be directly run. Python and other libraries' versions can be found in requirements.txt file.

If SEARCH_HYPERPARAMETER value is true, fine_tune_model functions runs and does GridSearchCV for a given parameter grid.
</p>

### More About

<p>For more information about the project, it is advised to read .pdf report file. It contains step by step explanation of path taken during analysis.</p>


    
