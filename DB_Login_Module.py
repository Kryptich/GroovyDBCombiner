import pymysql  # enable MySQL connectivity
import getpass  # enable accepting password silently / entry hiding

while True:
    try:
        db_user = input("Please Enter Valid DB Credentials.\nUsername: ")
        db_password = getpass.getpass('Password: (hidden) ')
        cursor = pymysql.cursors.DictCursor
        conn   = pymysql.connect(host='localhost',           # Connect to the local MySQL server
                                 port=3306,
                                 user=str(db_user),
                                 passwd=str(db_password),
                                 db='classicmodels',
                                 charset='utf8')
        cur = conn.cursor()                                  # Open a cursor on active connection
        print("\nSweet, you're logged in.")
        input("\nLet's try a query: [ SELECT * FROM classicmodels.customers LIMIT 3; ] {{ENTER}} ")
        sql = """
            SELECT * FROM classicmodels.customers LIMIT 3;
            """
        cur.execute(sql)
        print("\nQUERY RESULTS :::\n",cur.fetchall())
        break
    except pymysql.OperationalError as error:
        code, message = error.args
        print ("\n::: ERROR", code,":::", message, "\n")
input("\nLooks like everything worked out with that -- Let's wait for a user response before closing...")
print ("\n...OK, going down...")
cur.close()
conn.close()
quit()
