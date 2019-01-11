import PDFGeneration

import requests
import sys




def requestData(
    _workspace_id,_api_token,startdate,
     enddate, year, output):
    r = requests.get('https://toggl.com/reports/api/v2/summary.pdf',
                        auth=(_api_token, 'api_token'),
                        params=({
                            'workspace_id': _workspace_id,
                            'since': startdate.format("YYYY-MM-DD"),
                            'until': enddate.format("YYYY-MM-DD"),
                            'user_agent': 'api_test'
                        }))
    
    PDFGeneration.generatePDF(r.content, output)