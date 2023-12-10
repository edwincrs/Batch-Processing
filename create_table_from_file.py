import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv("C:/Users/Edwin Cris/Desktop/Course/Digital Skola/Docker/users_w_postal_code.csv",sep=",")

engine=create_engine("postgresql://avnadmin:AVNS_WKCKGD4JC5s0lel9zKD@pg-dev-dev-101.a.aivencloud.com:16506/defaultdb")

df.to_sql("edwin_users_w_postal_code",engine)

