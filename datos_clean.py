from conexion_sql import connect_and_query
import pandas as pd

record = connect_and_query()

df = pd.DataFrame(record, columns=['id', 'idauditTrail', 'phone', 'message', 'creationdate', 'modificationdate'])

print(df.head(5))


