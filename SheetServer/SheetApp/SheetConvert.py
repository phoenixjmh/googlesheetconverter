import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import OrderedDict
import pandas as pd
import MySQLdb
from sqlalchemy import create_engine


engine = create_engine('mysql+mysqldb://root:firebird12@localhost/Buyer_Info')




def retrieveAndOutput():
#Initialize Lists

    names = []

    phones = []

    emails = []

    addresses = []

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    credentials= ServiceAccountCredentials.from_json_keyfile_name('SheetConverter-56f59aede9e4.json', scope)

    gc = gspread.authorize(credentials)

    wk = gc.open('BuyerInfo').sheet1




    for name in wk.col_values(1, value_render_option = "UNFORMATTED_VALUE"):
        names.append(name)
        #print(name)

    for phone in wk.col_values(2, value_render_option = "UNFORMATTED_VALUE"):
        phones.append(phone)
        #print(phone)

    for email in wk.col_values(3, value_render_option = "UNFORMATTED_VALUE"):
        emails.append(email)
        #print(email)

    for address in wk.col_values(4, value_render_option = "UNFORMATTED_VALUE"):
        addresses.append(address)
        #print(address)
#Register DataFrame
    df = pd.DataFrame({'Name': names,
                       'Phone': phones,
                       'Email': emails,
                       'Address': addresses})
#Pass DataFrame to SQL
    df.to_sql(con=engine, name='Buyers', if_exists='replace', index=False)
#DataFrame is Updated From SQL
    df = pd.read_sql('select * from Buyers', engine)
#Return DataFrame
    return df


newDF=retrieveAndOutput()


#make dataframe equal to df.readSQL somehow
