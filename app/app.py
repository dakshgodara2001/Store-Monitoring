from flask import Flask, jsonify, request, send_file
import os
from controller.controller import generateReport, REPORT_OUTPUT_PATH
from models.report_data import ReportDB

app = Flask(__name__)

@app.route('/trigger_report', methods=['POST'])
def trigger_report():
    # Generate a report and get the report ID
    report_id = generateReport()
    
    # Return the report ID as a JSON response
    return jsonify({"report_id": report_id})

@app.route('/get_report', methods=['POST'])
def get_report():
    # Get the report ID from the request JSON payload
    report_id = request.json['report_id']
    
    # Get the status of the report from the ReportDB
    status = ReportDB.getStatusOf(report_id)
    
    if status == 'running':
        # If the report is still running, return a JSON response with a message
        return jsonify({'message': 'Running'})

    elif status == 'finished':
        # If the report is generated and available, send the report file as an attachment in the response
        return send_file(os.path.join('..', REPORT_OUTPUT_PATH, f'report_{report_id}.csv'), as_attachment=True)

    else:
        # If the report is not found, return a JSON response with a message
        return jsonify({'message': 'Report Not Found'})
    
    
app.run()
