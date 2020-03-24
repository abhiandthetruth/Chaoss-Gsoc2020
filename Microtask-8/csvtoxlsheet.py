import argparse, sys
import csv, xlsxwriter
from pprint import pprint
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_gservice():
    """Load/Generate the credentials and return service for sheets api v4"""

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        # If there are credentials but expired and we have a refresh token
        # refresh the credentials 
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        # Else complete the authorization cflow to generate token.pickle
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service

def insert_to_sheet(csv_path, sheet_name, spreadsheet_id, coordinates):
    """
    Insert the csv data to google sheets

    The function inserts the csv data into a sheet at some coordinates. 
    If 'spreadsheet_id' is specified it uses the id to get the spreadsheet
    else it creates a new spreadsheet with name 'sheet_name'. 
    Note that if both are specified 'spreadsheet_id' gets precedence and 
    atleast one of them must be specified. 
    After getting the spreadsheet the data is added to it at 'coordinates', if 
    specified, else at 0, 0. 
    
    :param csv_path: path of the csv file from which data is to be extracted
    :param sheet_name: name of the sheet if new sheet is to be created
    :param spreadsheet_id: if specified, the spreadsheet associated with this id
                            will be used
    :param coordinates: a list with first element as the row index and the second 
                        as column index. If not specified 0, 0 is used
    """
    
    service = get_gservice()
    sheets = service.spreadsheets()
    # Get the spread sheet
    if spreadsheet_id:
        spreadsheet = sheets.get(spreadsheetId=spreadsheet_id).execute()
    else:   
        spreadsheet = {
            'properties': {
                'title': sheet_name
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet).execute()
    # Get data from csv
    csv_data = ''
    with open(csv_path, 'r') as csvfile:
        csv_data = csvfile.read()
    # Prepare the Co-ordinates
    row_idx, col_idx = 0, 0
    if coordinates:
        row_idx, col_idx = coordinates[0], coordinates[1]
    gridCoordinate = {
        "sheetId": spreadsheet.get('sheetId'),
        "rowIndex": row_idx,
        "columnIndex": col_idx
    }
    # Prepare the PasteDataRequest Object
    pasteDataRequest = {
        "coordinate" : gridCoordinate,
        "data": csv_data,
        "type": 'PASTE_NORMAL',
        "delimiter": ","
    }
    # Getting the import request ready
    import_request = {
        "pasteData": pasteDataRequest
    }
    # Preparing the request body
    body = {
        "requests": [import_request],
        "includeSpreadsheetInResponse": False
    }
    # Finally make teh request and print response
    response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet.get('spreadsheetId'), body=body).execute()
    pprint(response)

def generate_xlsx(csv_path):
    """
    Generates xlsx file given a csv file

    :param csv: path to the csv file to be converted
    """

    wb = xlsxwriter.Workbook(csv_path.replace(".csv",".xlsx"))
    ws = wb.add_worksheet("WS1")
    with open(csv_path,'r') as csvfile:
        table = csv.reader(csvfile)
        i = 0
        for row in table:
            ws.write_row(i, 0, row)
            i += 1
    wb.close()

def get_args():
    """
    Get params from cli required for exexution of module
    :argument --cfg: Path to config.ini
    """

    parser = argparse.ArgumentParser(description="Arguments for excel conversion")
    
    parser.add_argument('--csv', dest='csv_path', 
                        help='Path to the csv', required=True)

    parser.add_argument('--gen-xlsx', dest='gen_xlsx', action='store_true', 
                        help="Generate xlsx file")
    
    parser.add_argument('--new-sheet', dest='new_sheet', default='', 
                        help='Name of google sheet to be created')
    
    parser.add_argument('--spreadsheet-id', dest='spreadsheet_id', default='',
                        help='Id of the spreadsheet the data is to be inserted') 

    parser.add_argument('--coordinates', dest='coordinates', default=[], nargs=2,
                        help='Co-ordinates on sheet where to add data')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    if args.gen_xlsx:
        generate_xlsx(args.csv_path)
    if args.new_sheet or args.spreadsheet_id:
        insert_to_sheet(args.csv_path, args.new_sheet, 
                        args.spreadsheet_id,
                        args.coordinates)

