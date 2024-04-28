import psycopg2
from configuration import SQL_SERVER_CONFIG

# def create_connection():
#     connection = None
#     cursor = None
#     try:
#         connection = psycopg2.connect(**SQL_SERVER_CONFIG)
#         cursor = connection.cursor()
#         print(connection.get_dsn_parameters(), "\n")  # PostgreSQL Connection properties
#         cursor.execute("SELECT version();")
#         record = cursor.fetchone()
#         print("Connected to -", record, "\n")
#     except (Exception, psycopg2.Error) as error:
#         print("Error while connecting to PostgreSQL:", error)
#     return connection, cursor

def create_connection():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            **SQL_SERVER_CONFIG,

        )
        cursor = connection.cursor()
        print(connection.get_dsn_parameters(), "\n") # PostgreSQL Connection properties
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("Connect to -", record, "\n")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        if(connection):
            cursor.close()
            connection.close()
            print("Connection is closed")
    return connection, cursor

def create_table(table_name, column_name):
    connection, cursor = create_connection()
    if connection and cursor:
        try:
            # Construct the SQL query for table creation
            sql_query = f"CREATE TABLE {table_name} ("
            sql_query += "id SERIAL PRIMARY KEY,"
            for column_name, column_property in column_name.items():
                sql_query += f'{column_name}'
                data_type = column_property.get('type')
                sql_query += f' {data_type}'
                if constraints := column_property.get('constraints'):
                    for constraint in constraints:
                        sql_query += f' {constraint}'
                sql_query += ','
            sql_query = sql_query.rstrip(',')
            sql_query += ');'
            
            # Execute the query
            cursor.execute(sql_query)
            
            # Commit the transaction
            connection.commit()
            print(f"Table {table_name} created successfully!")
            
        except (Exception, psycopg2.Error) as error:
            print("Error while creating table:", error)
            
        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()

def add_entry(table_name, data):
    connection, cursor = create_connection()
    if connection and cursor:
        try:
            # Construct the SQL query for insertion excluding the 'id' column
            columns = ', '.join([col for col in data.keys() if col != 'id'])
            placeholders = ', '.join(['%s'] * (len(data) - 1))  # Excluding 'id'
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            
            # Execute the query excluding the 'id' value
            cursor.execute(query, tuple(data[col] for col in data if col != 'id'))
            
            # Commit the transaction
            connection.commit()
            print("New entry added successfully!")
            
        except (Exception, psycopg2.Error) as error:
            print("Error while adding new entry:", error)
            
        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()

def get_entry_by_id(table_name, id):
    connection, cursor = create_connection()
    if connection and cursor:
        try:
            # Construct the SQL query for fetching the entry
            query = f"SELECT * FROM {table_name} WHERE id = %s"
            
            # Execute the query
            cursor.execute(query, (id,))
            
            # Fetch the record
            record = cursor.fetchone()
            return record
            
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching entry:", error)
            
        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()
def count_entries(table_name):
    connection, cursor = create_connection()
    if connection and cursor:
        try:
            # Construct the SQL query for counting entries
            query = f"SELECT COUNT(*) FROM {table_name}"
            
            # Execute the query
            cursor.execute(query)
            
            # Fetch the count
            count = cursor.fetchone()[0]
            print("Total entries:", count)  # Debugging: Print total entries
            return count
            
        except (Exception, psycopg2.Error) as error:
            print("Error while counting entries:", error)
            return None  # Return None in case of an error
            
        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()
    else:
        print("Error: Failed to establish connection.")
        return None

columns = {
    'name': {'type': 'VARCHAR(255)'},
    'height_cm': {'type': 'FLOAT'},
    'weight_kg': {'type': 'FLOAT'},
    'gender': {'type': 'VARCHAR(10)'},
    'state': {'type': 'VARCHAR(50)'},
    'birth_date': {'type': 'DATE'},
    'bmi': {'type': 'FLOAT'}
}
create_table('new_data_table', columns)


data = {'name': 'John', 'height_cm': 180.0, 'weight_kg': 75.0, 'gender': 'Male', 'state': 'CA', 'birth_date': '1990-01-01', 'bmi': 23.15}
add_entry('new_data_table', data)

# import psycopg2
# from dateutil.parser import parse
# import re
# import pandas as pd
# from configuration import SQL_SERVER_CONFIG

# def create_connection():
#     connection = None
#     cursor = None
#     try:
#         connection = psycopg2.connect(
#             **SQL_SERVER_CONFIG,

#         )
#         cursor = connection.cursor()
#         print(connection.get_dsn_parameters(), "\n") # PostgreSQL Connection properties
#         cursor.execute("SELECT version();")
#         record = cursor.fetchone()
#         print("Connect to -", record, "\n")
#     except (Exception, psycopg2.Error) as error:
#         print("Error while connecting to PostgreSQL", error)
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("Connection is closed")
#     return connection, cursor


# def create_table(table_name, column_name):
#     """
#     CREATE TABLE Bmi (id SERIAL,
#     first VARCHAR(50) NOT NULL,
#     last VARCHAR(50) NOT NULL,
#     height VARCHAR(50) NOT NULL,
#     weight VARCHAR(50) NOT NULL,
#     gender VARCHAR(50) NOT NULL,
#     state VARCHAR(50) NOT NULL,
#     birthDay Date NOT NULL);
#     :param table_name:
#     :param column_name:
#     :return:
#     """
#     sql_query = f"CREATE TABLE {table_name} ("
#     for column_name, column_property in column_name.items():
#         sql_query += f'{column_name}'
#         data_type = column_property.get('type')
#         sql_query += f' {data_type}'
#         if constraints := column_property.get('constraints'):
#             for constraint in constraints:
#                 sql_query += f' {constraint}'
#         sql_query += ','
#     sql_query = sql_query.rstrip(',')
#     sql_query += ');'
#     return sql_query


# def delete_table(table_name):
#     """
#     DROP TABLE Bmi
#     DELETE FROM Bmi WHERE customer = 'danny'
#     :param table_name:
#     :return:
#     """
#     return f"DROP TABLE {table_name}"


# def add_entry(table,data):
#     """
#     INSERT INTO Bmi (first, last, gender, state, birthDay) VALUES ('danny','zhang', '180','70','male', 'CA', '1994-11-11');
#     All values will be added regardless of duplications.
#     :param table:
#     :param data:
#     :return:
#     """
#     column_data = '('
#     value_data = '('
#     for column_name, column_value in data.items():
#         column_data += f"{column_name},"
#         # if column_value.isdigit():
#         #     value_data += f"{column_value},"
#         # else:
#         #     value_data += f"'{column_value}',"
#         if str(column_value.iloc[0]).isdigit():
#             value_data += f"{column_value.iloc[0]},"
#         else:
#             value_data += f"'{column_value.iloc[0]}',"
#     column_data = column_data.rstrip(",") + ")"
#     value_data = value_data.rstrip(",") + ")"
#     return f"INSERT INTO {table} {column_data} VALUES {value_data};"
#     # connection, cursor = create_connection()
#     # if cursor is not None:
#     #     try:
#     #         query = f"INSERT INTO {table} {column_data} VALUES {value_data};"
#     #         cursor.execute(query)
#     #         connection.commit()
#     #         st.success("New entry added successfully!")
#     #     except Exception as e:
#     #         st.error(f"Error occurred: {e}")
#     #     finally:
#     #         cursor.close()
#     #         connection.close()


# def delete_entry(table_name, primary_key,value):
#     if not value.isdigit():
#         value = f"'{value}'"
#     return f'DELETE FROM {table_name} WHERE {primary_key} = {value}'


# def accurate_search_sql(key,value,if_multiple=False):
#     if if_multiple:
#         in_statement = '('
#         for single_condition in value:
#             in_statement += f"'{single_condition}',"
#         in_statement = in_statement.rstrip(',') + ')'
#         return f" {key} IN {in_statement}"
#     return f" {key} = '{value}'"


# def fuzzy_search_sql(key,pattern,if_multiple=False):
#     if if_multiple:
#         sub_sql =''
#         for single_pattern in pattern:
#             sub_sql += f" {key} LIKE '%{single_pattern}%' OR"
#         return sub_sql
#     return f" {key} LIKE '%{pattern}%'"


# def range_search_sql(key, begin, end):
#     if _is_date(begin):
#         return f" {key} BETWEEN '{begin}' AND '{end}'"
#     return f" {key} BETWEEN {begin} AND {end}"


# def check_column_names(table_n,schema='public'):
#     return f"SELECT column_name FROM information_schema.columns WHERE table_schema='{schema}' and table_name='{table_n}'"


# new_table_example = {
#     'id': {
#         'type': 'SERIAL',
#         'constraints': ['PRIMARY KEY']
#     },
#     'first': {
#         'type': 'VARCHAR(10)',
#         'constraints': ['NOT NULL']
#     },
#     'last': {
#         'type': 'VARCHAR(10)',
#         'constraints': ['NOT NULL']
#     },
#     'height': {
#             'type': 'VARCHAR(10)',
#             'constraints': ['NOT NULL']
#         },
#     'weight': {
#             'type': 'VARCHAR(10)',
#             'constraints': ['NOT NULL']
#         },
#     'gender': {
#         'type': 'VARCHAR(10)',
#         'constraints': ['NOT NULL']
#     },
#     'state': {
#         'type': 'VARCHAR(10)',
#         'constraints': ['NOT NULL']
#     },
#     'birthDay': {
#         'type': 'DATE',
#         'constraints': ['NOT NULL']
#     },

# }

# columns = {
#     'id': {'type': 'SERIAL'},
#     'first': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
#     'last': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
#     'height': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
#     'weight': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
#     'gender': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
#     'state': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
#     'birthDay': {'type': 'Date', 'constraints': ['NOT NULL']}
# }

# new_entry_example = {
#     'first': 'danny',
#     'last': 'zhang',
#     'gender': 'male',
#     'height':'180',
#     'weight':'70',
#     'state': 'CA',
#     'birthDay': '1994-11-11'
# }


# def create_table_demo():
#     query = create_table(table_n, columns)
#     execute_sql(query)


# def add_entry_demo(table_n, new_entry_example):
#     query = add_entry(table_n, new_entry_example)
#     execute_sql(query)


# def delete_table_demo():
#     query = delete_table(table_n)
#     execute_sql(query)


# def check_column_names_demo(table_n)->list:
#     query = check_column_names(table_n)
#     connection, cursor = create_connection()
#     cursor.execute(query)
#     names = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return names

# class SearchError(Exception):
#     pass


# def execute_sql(sql_query):
#     print(f'query will be executed is {sql_query}')
#     connection, cursor = create_connection()
#     cursor.execute(sql_query)
#     connection.commit()
#     cursor.close()
#     connection.close()
#     print("Connection is closed")

# table_n = 'test'
# if __name__== "__main__":

#     """
#     #query = check_column_names(table_n)
#     print('SQL QUERY is',query)
    
#     # for query only, because need cursor.fetchall()
#     connection, cursor = create_connection()
#     cursor.execute(query)
#     result = cursor.fetchall()
#     print('result is',result)
#     cursor.close()
#     connection.close()
#     print("Connection is closed")"""

#     create_table_demo()
#     add_entry_demo(table_n, new_entry_example)
#     delete_table_demo()
#     add_entry_demo(table_n, new_entry_example)




