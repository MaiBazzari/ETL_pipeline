import psycopg2
import pandas as pd

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


def extract_transactional_data(dbname, host, port, user, password):
    connect = connect_to_redshift(dbname, host, port, user, password)
    query = """
    SELECT ot.invoice,
        ot.stock_code,
        CASE WHEN s.description is null THEN 'Unknown'
            ELSE s.description END AS description, 
        ot.price,
        ot.quantity,
        /* add a variable that gives the total order values */
        ot.price * ot.quantity AS total_order_value,
        CAST(invoice_date as datetime) as invoice_date,
        ot.customer_id,
        ot.country 
    FROM bootcamp.online_transactions ot
    LEFT JOIN (SELECT *
            FROM bootcamp.stock_description
            WHERE description <> '?') AS s ON ot.stock_code = s.stock_code
    WHERE customer_id <> ''
    AND ot.stock_code NOT IN('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
    """
    online_trans_cleaned = pd.read_sql(query, connect)
    print("Online trans clean shape", online_trans_cleaned.shape)
    print("Online transactions head", online_trans_cleaned.head())
    return online_trans_cleaned
