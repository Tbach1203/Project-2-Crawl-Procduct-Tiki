import pandas as pd

def get_Id(df):
    return df['id'].tolist()

def product():
    pass

def info_Products():
    pass

if __name__ == "__main__":
    df = pd.read_csv('products-0-200000.csv')
    ids = get_Id(df)
    print(df[:10])

    
    
