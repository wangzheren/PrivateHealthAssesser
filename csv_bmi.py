import pandas as pd
import SQL_Client_BMI


class CSVClient:
    def __init__(self,connection,cursor):
        self.connection = connection
        self.cursor = cursor

    @staticmethod
    def read_parse_dataframe(dataframe):
        """

        :param dataframe: a pd.read_csv() return value
        :return:
        """
        result = []
        for line in dataframe.values:
            dic={}
            for item,data in zip(dataframe,line.tolist()):
                if str(data)!='nan':
                    dic[item] = data
            result.append(dic)
        return result

    def batch_add(self, table_name, request_batch):
        try:
            for i in request_batch:
                query = SQL_Client_BMI.add_entry(table_name, i)
                self.cursor.execute(query)
                self.connection.commit()
        except Exception as error:
            print('Something wrong, please check the message:', error)
            raise error


if __name__== "__main__":
    file = "test_bmi.csv"
    table_n = 'bmi_table'
    connection, cursor = SQL_Client_BMI.create_connection()
    csv_client = CSVClient(connection, cursor)
    df = pd.read_csv(file,header=0)
    request_l = csv_client.read_parse_dataframe(df)
    csv_client.batch_add(table_n,request_l)
    cursor.close()
    connection.close()
    print("Connection is closed")