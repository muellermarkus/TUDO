import sqlite3

from task import Task


class TasksStore:
    def __init__(self, conn=sqlite3.connect("example.db", detect_types=sqlite3.PARSE_DECLTYPES)):
        self.conn = conn
        self.conn_cursor = conn.cursor()
        self.init()

    def add_task(self, description):
        self.conn_cursor.execute("""INSERT INTO tasks (description) VALUES(?)""", [(description)])
        self.conn.commit()

    def list_tasks(self):
        self.conn_cursor.execute("SELECT * FROM tasks")
        # print(str(self.conn_cursor.fetchall()))
        return [Task(task[0], task[1], task[2], task[3]) for task in self.conn_cursor.fetchall()]

    def init(self):
        self.conn_cursor.execute("""CREATE TABLE IF NOT EXISTS tasks
                            (number INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT, started TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            , finished TIMESTAMP )""")
        self.conn.commit()

    def reset(self):
        self.conn_cursor.execute("""DROP TABLE tasks""")
        self.init()