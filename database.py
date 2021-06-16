import sqlite3

conn = sqlite3.connect("info.db")

cur = conn.cursor()

create_query = '''CREATE TABLE EVENTS
            (ID         INT PRIMARY KEY     NOT NULL,
            TITLE       TEXT                NOT NULL,
            HOST        TEXT                NOT NULL,
            LOCATION    TEXT                NOT NULL,
            DESCRIPTION CHAR[128],
            DATE        TEXT                NOT NULL, 
            START       TEXT                NOT NULL, 
            END         TEXT                NOT NULL,
            FOREIGN KEY (USER_ID)
                REFERENCES PARTICIPANTS (USER_ID)
            );'''

table_query = '''CREATE TABLE PARTICIPANTS
            (USER_ID    INT PRIMARY KEY     NOT NULL);'''


class Database(object):
    def __enter__(self):
        self.conn = sqlite3.connect("info.db")
        print("connected to db")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def __call__(self, query):
        c = self.conn.cursor()
        try:
            result = c.execute(query)
            print(f"{query} has been run")
            self.conn.commit()
        except Exception as e:
            print("comes here")
            result = e

        return result


if __name__ == "__main__":
    with Database() as db:
        result = db(create_query)
        result = db(table_query)
