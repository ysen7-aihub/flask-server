import boto3
import base64
from botocore.exceptions import ClientError
from ast import literal_eval
import logging
import sys
import pymysql

def get_secret():
    secret_name = "Moodmaker/Database"
    region_name = "ap-northeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    dict_secret = literal_eval(secret)

    database = "moodmaker"
    conn, cursor = connect_RDS(dict_secret["host"], dict_secret["port"], dict_secret["username"], dict_secret["password"], database)
    return conn, cursor


# RDS에 올린 mysql과 연결
def connect_RDS(host, port, username, password, database):
    try:
        conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port,
                               use_unicode=True, charset='utf8')
        cursor = conn.cursor()
    except:
        logging.error("RDS에 연결되지 않았습니다.")
        sys.exit(1)
    return conn, cursor
