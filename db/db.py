from os import path, sched_get_priority_max
from os.path import isfile
from sqlite3 import connect
from typing import ContextManager
from apscheduler.triggers.cron import CronTrigger

DB_PATH = "/home/rootx/DECINE/Discord_bot/efc/data/database.db"
BUILD_PATH = "/home/rootx/DECINE/Discord_bot/efc/data/build.sql."
cxn = connect(DB_PATH, check_same_thread=False)
cur = cxn.cursor()


def with_commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()

    return inner


@with_commit
def build():
    if isfile(BUILD_PATH):
        scriptexec(BUILD_PATH)


def commit():
    cxn.commit()


def autosave(sched):
    sched.add_job(commit, CronTrigger(second=0))


def clse():
    cxn.close()


def field(command, *values):
    cur.execute(command, tuple(values))

    if (fetch := cur.fetchone() is not None):
        return fetch[0]


def record(command, *values):
    cur.execute(command, tuple(values))


def records(command, *values):
    cur.execute(command, tuple(values))

    return cur.fetchall()


def column(command, *values):
    cur.execute(command, tuple(values))
    
    return [item[0] for item in cur.fetchall()]

def execute(commamd, *values):
    cur.execute(commamd, tuple(values))


def multiexec(command, valueset):
    cur.executemany(command, valueset)


def scriptexec(path):
    with open(path, "r", encoding='utf-8') as script:
        cur.executescript(script.read())