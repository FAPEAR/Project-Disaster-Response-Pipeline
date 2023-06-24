# Disaster Response Pipeline Project
This project aims to develop an impactful and useful application that provides assistance in disaster situations. Using the valuable data collected by Appen, we are creating an advanced model for an API that will efficiently classify disaster messages.

The app is built on a powerful machine learning pipeline that enables rapid categorization of disaster events. Once a message is entered through our intuitive web application, accurate classification results are generated into various relevant categories. These classified messages are automatically forwarded to the appropriate aid agencies.

What makes this app truly special is its direct impact on the community and on people's lives. In times of crisis, every minute counts and our tool provides an efficient and fast way to analyze and classify critical information. By streamlining the categorization process, first responders can more effectively prioritize and respond to disaster situations, providing help to those who need it most.

In addition to its core functionality, the web application also offers data visualizations to provide a clear and concise understanding of the current situation. This allows emergency workers to get a quick and accurate overview of the magnitude and distribution of disaster events.

In summary, this application has a practical impact and significant benefits in the community and organizations involved in disaster situations. It provides a reliable tool to classify messages, allowing for a more efficient and effective response to emergencies.

#### Project File Structure
- workspace root$: python
    - app
        - template
            - go.html
            - master.html
        - run.py
        
    - data
        - DisasterResponse.db
        - disaster_categories.csv
        - disaster_messages.csv
        - process_data.py
        
    - Models
         - classifier.pkl
         - train_classifier.py
    
    - README.md

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database.
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
Udacity: https://www.udacity.com/



