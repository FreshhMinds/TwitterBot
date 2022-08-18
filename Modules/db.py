import os
import psycopg2
DATABASE_URL = os.getenv['DATABASE_URL']
def get_retweets_from_db():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    c.execute('SELECT tweet_id FROM retweet_history')
    return [x[0] for x in c.fetchall()]
def insert_retweet_to_db(tweet_id):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO retweet_history (tweet_id) VALUES (%s)', (tweet_id,))
        conn.commit()
    except psycopg2.IntegrityError:
        print("Could not insert tweet_id into database")
    conn.close()
