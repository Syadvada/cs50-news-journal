import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_db_connection():
    conn = sqlite3.connect('journal.db')     # Step 1: Open connection to DB file
    conn.row_factory = sqlite3.Row           # Step 2: Configure rows to act like dictionaries
    return conn                              # Step 3: Give the connection back to caller


def fetch_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find("title")
        return title_tag.string.strip() if title_tag else "No Title"
    except:
        raise ValueError("Invalid URL")


def add_entry(url, title, tags, notes):
    conn = get_db_connection()
    entry = conn.execute("INSERT INTO entries (url, title, tags, notes, timestamp) VALUES (?, ?, ?, ?, ?)", (url, title, tags, notes, datetime.now()))
    conn.commit()   
    conn.close()


def fetch_all_entries():
    conn = get_db_connection()
    entries = conn.execute("SELECT * FROM entries ORDER BY timestamp DESC").fetchall()
    conn.close()
    return entries


def get_entry_by_id(entry_id):
    conn = get_db_connection()
    entry = conn.execute("SELECT * FROM entries WHERE id = ?", (entry_id,)).fetchone()
    conn.close()
    return entry


