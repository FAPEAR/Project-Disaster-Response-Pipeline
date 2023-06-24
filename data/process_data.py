import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''
    Load data from a CSV file.

    INPUT:
    data_filepath - (str) Filepath of the CSV file.

    OUTPUT:
    df - (pandas DataFrame) Loaded data as a DataFrame.
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, on='id', how='outer')
    return df


def clean_data(df):
    '''
    Perform data cleaning on the input DataFrame.

    INPUT:
    df - (pandas DataFrame) Input DataFrame.

    OUTPUT:
    cleaned_df - (pandas DataFrame) Cleaned DataFrame.
    '''
    categories = df['categories'].str.split(";", expand=True)
    category_colnames = categories.iloc[0].apply(lambda x: x.split("-")[0]).tolist()
    categories.columns = category_colnames
    categories = categories.applymap(lambda x: int(x[-1]))
    df = pd.concat([df, categories], axis=1)
    df = df[df['related'] != 2]
    df = df.drop_duplicates(keep='first')
    del df['categories']
    return df


def save_data(df, database_filename):
    '''
    Save the DataFrame to a SQLite database.

    INPUT:
    df - (pandas DataFrame) DataFrame to be saved.
    database_filepath - (str) Filepath of the SQLite database.

    OUTPUT:
    None
    '''
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('messages', engine, if_exists='replace', index=False)   


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()