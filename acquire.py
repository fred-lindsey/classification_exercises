
import env
import pandas as pd
import os

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'



def get_titanic_data(use_cache=True):
    filename = "titanic.csv" #use local csv first
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    else:                   #otherwise, pull the data from a SQL query
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        df.to_csv(filename, index=False)
        return df

def get_iris_db(use_cache=True):
    filename = "iris.csv"
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('SELECT * FROM species', get_connection('iris_db'))
        df.to_csv(filename, index=False)
        return df

def get_telco_data(use_cache=True):
    filename = "telco.csv"
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    else:
        df = pd.read_sql("""
        SELECT * FROM customers 
        JOIN contract_types USING(contract_type_id)
        JOIN payment_types USING(payment_type_id)
        JOIN internet_service_types USING(internet_service_type_id)
        """
        , get_connection('telco_churn'))
        df.to_csv(filename, index=False)
        return df
