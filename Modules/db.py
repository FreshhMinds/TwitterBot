import sqlite3
def get_retweets_from_db():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('SELECT "tweet_id" FROM retweet_history')
    return [int(tid[0]) for tid in c.fetchall()]
def insert_retweet_to_db(tweet_id):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO retweet_history ("tweet_id") VALUES ("'+tweet_id+'")')
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()
