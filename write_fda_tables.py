import pandas as pd
import sqlite3

def create_dataframes(data_dir = './data'):
    product_df = pd.read_csv('./data/products.txt',sep='~')
    product_df[['Delivery_Format','Route']] = product_df['DF;Route'].str.split(';',expand=True)
    product_df.drop('DF;Route',axis=1,inplace=True)
    patent_df = pd.read_csv('./data/patent.txt',sep='~')
    exclusivity_df = pd.read_csv('./data/exclusivity.txt',sep='~')
    return product_df, patent_df, exclusivity_df

def clean_dataframes(product_df, patent_df, exclusivity_df):
    for df in [product_df, patent_df, exclusivity_df]:
        for k in df.keys():
            df[k] = [s.replace("'","") if isinstance(s,str) else s for s in df[k].values]
    return product_df, patent_df, exclusivity_df

def write_tables(product_df, patent_df, exclusivity_df, db_file='fda_orange.db'):
    cnx = sqlite3.connect(db_file)
    product_df.to_sql(name='product',con=cnx)
    patent_df.to_sql(name='patent',con=cnx)
    exclusivity_df.to_sql(name='exclusivity',con=cnx)

def main():
    product_df, patent_df, exclusivity_df = create_dataframes()
    product_df, patent_df, exclusivity_df = clean_dataframes(product_df, patent_df, exclusivity_df)
    write_tables(product_df, patent_df, exclusivity_df)

if __name__ == "__main__":
    main()