import pandas as pd
def get_publisher(conn):
 return pd.read_sql("SELECT * FROM publisher", conn)