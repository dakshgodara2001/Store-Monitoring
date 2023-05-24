# Report Generation Project

This project focuses on generating reports based on store data and tracking their status. It provides functionalities to trigger report generation, monitor report statuses, and retrieve the generated reports.

Demo video : https://www.loom.com/share/dbf0e2ce9d93449ca4211590d4990b06

## Table of Contents
- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Database Structure](#database-structure)
- [Dependencies](#dependencies)


## Overview

The report generation project is built using Python and SQLite. It utilizes the Flask framework for creating an API to trigger and retrieve reports. The project includes functionalities for generating reports based on store data, storing report information in a database, and updating the status of reports.

The project consists of the following components:
- Flask API (`app.py`): This file contains the Flask application code that defines the routes for triggering report generation and retrieving reports. It communicates with the controller and database modules.
- Controller (`controller.py`): This module handles the report generation logic and interacts with the data models and utilities.
- Data Models (`report_data.py`): This module defines the data models used for storing and retrieving report information from the database.
- Utilities (`utils.py`): This module contains utility functions for data manipulation and time conversions.

## Setup

To set up the project, follow these steps:

1. Clone the repository: `git clone https://github.com/dakshgodara2001/Store-Monitoring`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Store the `.csv` files into the CSV directory.
4. Open terminal and go to project directory and run `python main.py`.

Development serve will start running on `http://127.0.0.1:5000` 

## Usage

1. Start the Flask API by running the command: `python app.py`
2. Make POST requests to the `/trigger_report` route to trigger report generation. This will return the `report_id` for the generated report.
3. Use the `report_id` obtained to make a POST request to the `/get_report` route to retrieve the generated report.
4. The status of the report can be checked using the `getStatusOf(report_id)` method in the `ReportDB` class.

## Database Structure

The project uses an SQLite database to store report information. The database contains a single table named `report_data` with the following structure:

| Column    | Type     | Description                                    |
|-----------|----------|------------------------------------------------|
| report_id | TEXT     | The ID of the report (Primary Key)              |
| status    | TEXT     | The status of the report ('running' or 'finished') |

## Dependencies

The project relies on the following dependencies:

- Flask: A Python web framework for creating the API.
- SQLite3: A lightweight, serverless database engine.
- Other Python libraries: pandas, threading, nanoid, os, datetime, pytz.

The project uses these libraries for report generation, database operations, time conversions, and other functionality.


