import sqlite3

# Establish a connection to the SQLite database file
conn = sqlite3.connect('report_data.db')
c = conn.cursor()

# Create the 'report_data' table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS report_data(
        report_id TEXT PRIMARY KEY,
        status TEXT DEFAULT 'running'
    )
''')
conn.commit()
conn.close()

class ReportDB:
    @staticmethod
    def insert_report(report_id):
        # Connect to the database
        conn = sqlite3.connect('report_data.db')
        c = conn.cursor()
        
        # Insert a new report with the default status of 'running'
        c.execute('''
            INSERT INTO report_data(report_id, status) VALUES(?, 'running')
        ''', (report_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_report(report_id):
        # Connect to the database
        conn = sqlite3.connect('report_data.db')
        c = conn.cursor()
        
        # Retrieve a report from the database based on the report_id
        c.execute('''
            SELECT * FROM report_data WHERE report_id=?
        ''', (report_id,))
        report = c.fetchone()
        conn.close()
        return report

    @staticmethod
    def update_report_status_to_finished(report_id):
        # Connect to the database
        conn = sqlite3.connect('report_data.db')
        c = conn.cursor()
        
        # Update the status of the report to 'finished'
        c.execute('''
            UPDATE report_data
            SET status = 'finished'
            WHERE report_id = ?
        ''', (report_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def getStatusOf(report_id):
        # Get the report from the database based on the report_id
        report = ReportDB.get_report(report_id)
        
        if report is None:
            return "not_found"
        return report[1]

