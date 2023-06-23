import sys
import pandas as pd
from sqlalchemy import create_engine
import nltk
import re
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split, GridSearchCV

nltk.download(['punkt', 'wordnet'])

def load_data(database_filepath):
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql('select * from messages', engine)
    X = df['message']
    y = df.iloc[:, 4:39]
    y['related'].replace(2, 1, inplace=True)
    category_names = y.columns.tolist()
    return X, y, category_names


def tokenize(text):
    text = re.sub(r'[^\w\s]','',text)
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [lemmatizer.lemmatize(tok).lower().strip() for tok in tokens]
    return clean_tokens


def build_model():
    pipeline = Pipeline([
            ('vect', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer()),
            ('clf', MultiOutputClassifier(AdaBoostClassifier()))
        ])
    parameters = {
            'vect__ngram_range': [(1, 1), (1, 2)],
            'vect__max_df': [0.5, 0.75, 1.0],
            'tfidf__use_idf': [True, False]
        }
    cv = GridSearchCV(pipeline, param_grid=parameters, verbose=2, n_jobs=-1)
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = model.predict(X_test)
    y_pred_df = pd.DataFrame(y_pred, columns=category_names)
    evaluation = {}
    for column in Y_test.columns:
        evaluation[column] = [
            precision_score(Y_test[column], y_pred_df[column]),
            recall_score(Y_test[column], y_pred_df[column]),
            f1_score(Y_test[column], y_pred_df[column])
        ]
    print(pd.DataFrame(evaluation))


def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()