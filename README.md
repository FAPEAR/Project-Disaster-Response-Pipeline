# Disaster Response Pipeline Project
The project consists of analyzing and classifying data from a database of messages collected in natural disaster events.
The main objective is to classify the messages in the most efficient way through a machine learning model deployed through an API that can be used functionally in a web application to have the possibility to include emergency messages and obtain classification through different types.

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv        data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

### File Description
- ETL Pipeline Preparation:In this file, data cleaning was done, the data frames were defined with the necessary functions to have the appropriate data for data training, this file is the base of what is related in process_data.py
- ML Pipeline Preparation: In this file, the data created in the ETL file are taken as a base, the models are calibrated under methodologies that allow determining precision, and recall and the F1 qualification on the test data. When comparing the models: the initial one and the model with the adjusted parameters, the one that obtained the best results of the previously described metrics is taken and this is the base of the file train_classifier.py.
- process_data.py: The script takes the file paths of the two data sets and the database, cleans the data sets, and stores the cleaned data in an SQLite database at the specified database file path.
- train_classifier.py: The script takes the database file path and the model file path, creates and trains a classifier, and stores the classifier in a pickle file at the specified model file path.
- run.py: It is a script to upload the web application.

### Acknowledgements
Udacity: https://github.com/FAPEAR/Project-Disaster-Response-Pipeline


