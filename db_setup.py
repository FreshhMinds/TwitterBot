import psycopg2, os

# read database connection url from the enivron variable we just set.
DATABASE_URL = os.environ.get('DATABASE_URL')
print(DATABASE_URL)
cmd_create_action_table = """CREATE TABLE "retweet_history" (
                        	"id"	INTEGER NOT NULL,
	                        "tweet_id"	TEXT NOT NULL UNIQUE,
	                        PRIMARY KEY("id" AUTO INCREMENT)
                            )
                          """

con = None
try:
    # create a new database connection by calling the connect() function
    con = psycopg2.connect(DATABASE_URL)

    #  create a new cursor
    cur = con.cursor()
    cur.execute(cmd_create_action_table)
       
     # close the communication with the HerokuPostgres
    cur.close()
except Exception as error:
    print('Could not connect to the Database.')
    print('Cause: {}'.format(error))

finally:
    # close the communication with the database server by calling the close()
    if con is not None:
        con.close()
        print('Database connection closed.')