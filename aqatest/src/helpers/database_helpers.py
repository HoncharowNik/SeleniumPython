import pymysql
from aqatest.src.helpers.config_helpers import get_database_credentials

import pdb

def read_from_db(sql):

    # db_credits = ged_database_credentias()

    # # connection = pymysql.connect(host=db_credits['db_host'], port=db_credits['db_port'],
    #                              user=db_credits['db_user'], password =db_credits['db_password'])

    connection = pymysql.connect(host='127.0.0.1', port=8889,
                                 user='root', password='root')

    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    return db_data

def get_order_from_db_by_order_no(order_no):

    sql = f"select * from quicksitedb.wp_posts where ID = {order_no} and post_type = 'shop_order';"

    db_order = read_from_db(sql)

    return db_order



