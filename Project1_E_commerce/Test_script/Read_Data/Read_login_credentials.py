#Read Loging Credentials:
import openpyxl
def read_data_of_row(filepath,col_user,col_pass,start_row,end_row):
    credentials=[]
    worksheet=openpyxl.load_workbook(filepath)
    sheet=worksheet.active
    for row in sheet.iter_rows(min_row=start_row,max_row=end_row,min_col=col_user,max_col=col_pass, values_only=True):
        credentials.append({
            "username":row[0],
            "password":row[1]
        })

    return credentials
