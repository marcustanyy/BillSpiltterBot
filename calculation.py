import mysql.connector

def calculation(trace_id, item_price_dict):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='BillSplitter',
                                            user='',
                                            password='')
        if connection.is_connected():
            print("You're connected to the database")
            cursor = connection.cursor()
    except:
        print("Error while connecting to MySQL")
    
    # select all rows with same trace_id
    cursor.execute(f"SELECT * FROM TABLENAME WHERE trace_id = {trace_id}")
    rows = cursor.fetchall()
    # for each row, add to item_user dictionary if item not in dictionary with users
    item_user = {}
    for row in rows:
        item_name = row[2]
        users = row[3]
        item_user[item_name] = users
    # iterate through item_user dictionary
    user_bill = {}
    for item_name,users in item_user:
        # for each item, find out what each user has to pay
        user_arr = users.split(',')
        split_bill = item_price_dict[item_name] / len(user_arr)
        for user in user_arr:
            # add amount to user in user_bill dict
            if user not in user_bill:
                user_bill[user] = split_bill
            else: 
                user_bill[user] += split_bill
    
    # return user_bill dict
    return user_bill