import psycopg2
from dateutil.parser import parse
import re
import pandas as pd
from configuration import SQL_SERVER_CONFIG

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
    """
    CREATE TABLE Bmi (id SERIAL,
    first VARCHAR(50) NOT NULL,
    last VARCHAR(50) NOT NULL,
    height VARCHAR(50) NOT NULL,
    weight VARCHAR(50) NOT NULL,
    gender VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    birthDay Date NOT NULL);
    :param table_name:
    :param column_name:
    :return:
    """
    sql_query = f"CREATE TABLE {table_name} ("
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
    return sql_query


def delete_table(table_name):
    """
    DROP TABLE Bmi
    DELETE FROM Bmi WHERE customer = 'danny'
    :param table_name:
    :return:
    """
    return f"DROP TABLE {table_name}"


def add_entry(table,data):
    """
    INSERT INTO Bmi (first, last, gender, state, birthDay) VALUES ('danny','zhang', '180','70','male', 'CA', '1994-11-11');
    All values will be added regardless of duplications.
    :param table:
    :param data:
    :return:
    """
    column_data = '('
    value_data = '('
    for column_name, column_value in data.items():
        column_data += f"{column_name},"
        if column_value.isdigit():
            value_data += f"{column_value},"
        else:
            value_data += f"'{column_value}',"
    column_data = column_data.rstrip(",") + ")"
    value_data = value_data.rstrip(",") + ")"
    return f"INSERT INTO {table} {column_data} VALUES {value_data};"


def delete_entry(table_name, primary_key,value):
    if not value.isdigit():
        value = f"'{value}'"
    return f'DELETE FROM {table_name} WHERE {primary_key} = {value}'


def accurate_search_sql(key,value,if_multiple=False):
    if if_multiple:
        in_statement = '('
        for single_condition in value:
            in_statement += f"'{single_condition}',"
        in_statement = in_statement.rstrip(',') + ')'
        return f" {key} IN {in_statement}"
    return f" {key} = '{value}'"


def fuzzy_search_sql(key,pattern,if_multiple=False):
    if if_multiple:
        sub_sql =''
        for single_pattern in pattern:
            sub_sql += f" {key} LIKE '%{single_pattern}%' OR"
        return sub_sql
    return f" {key} LIKE '%{pattern}%'"


def range_search_sql(key, begin, end):
    if _is_date(begin):
        return f" {key} BETWEEN '{begin}' AND '{end}'"
    return f" {key} BETWEEN {begin} AND {end}"


def check_column_names(table_n,schema='public'):
    return f"SELECT column_name FROM information_schema.columns WHERE table_schema='{schema}' and table_name='{table_n}'"


new_table_example = {
    'id': {
        'type': 'SERIAL',
        'constraints': ['PRIMARY KEY']
    },
    'first': {
        'type': 'VARCHAR(10)',
        'constraints': ['NOT NULL']
    },
    'last': {
        'type': 'VARCHAR(10)',
        'constraints': ['NOT NULL']
    },
    'height': {
            'type': 'VARCHAR(10)',
            'constraints': ['NOT NULL']
        },
    'weight': {
            'type': 'VARCHAR(10)',
            'constraints': ['NOT NULL']
        },
    'gender': {
        'type': 'VARCHAR(10)',
        'constraints': ['NOT NULL']
    },
    'state': {
        'type': 'VARCHAR(10)',
        'constraints': ['NOT NULL']
    },
    'birthDay': {
        'type': 'DATE',
        'constraints': ['NOT NULL']
    },

}

columns = {
    'id': {'type': 'SERIAL'},
    'first': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'last': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'height': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'weight': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'gender': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'state': {'type': 'VARCHAR(50)', 'constraints': ['NOT NULL']},
    'birthDay': {'type': 'Date', 'constraints': ['NOT NULL']}
}

new_entry_example = {
    'first': 'danny',
    'last': 'zhang',
    'gender': 'male',
    'height':'180',
    'weight':'70',
    'state': 'CA',
    'birthDay': '1994-11-11'
}


def create_table_demo():
    query = create_table(table_n, columns)
    execute_sql(query)


def add_entry_demo(table_n, new_entry_example):
    query = add_entry(table_n, new_entry_example)
    execute_sql(query)


def delete_table_demo():
    query = delete_table(table_n)
    execute_sql(query)


def check_column_names_demo(table_n)->list:
    query = check_column_names(table_n)
    connection, cursor = create_connection()
    cursor.execute(query)
    names = cursor.fetchall()
    cursor.close()
    connection.close()
    return names

class SearchError(Exception):
    pass


def execute_sql(sql_query):
    print(f'query will be executed is {sql_query}')
    connection, cursor = create_connection()
    cursor.execute(sql_query)
    connection.commit()
    cursor.close()
    connection.close()
    print("Connection is closed")


