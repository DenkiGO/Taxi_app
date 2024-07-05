from mysql.connector import connect, Error
from config import host, user, password, db_name

try:
    with connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
    ) as connection:
        cursor = connection.cursor()
        sql_query = "SELECT idorder_client, starting_address, final_address, price_order, date FROM order_client"
        cursor.execute(sql_query)
        records = cursor.fetchall()
        list_shift_work = records
        print(records)
except Error as e:
    print(e)