from pytest_f_api.data.read_write import ReadWrite
import requests
import json


def get_params(sheet_num,caseid):
    sheet = ReadWrite(sheet_num)
    cases = sheet.read()
    for row in cases:
        if caseid == row[ReadWrite.caseid]:
            url =row[ReadWrite.requestaddress]
            method =row[ReadWrite.requestmethod]
            r_data =row[ReadWrite.requestparam]
            r_header =row[ReadWrite.requestheader]
            expect_value=row[ReadWrite.expectresult]
            break
    return url,method,r_data,r_header,expect_value



def send_request(data):
    uri=data[0]
    method=data[1]
    parameters=data[2]
    headers=data[3]
    #print(url,headers,parameters,method)
    if str(method)=='get' or str(method)=='Get'or str(method)=='GET':
        content=requests.get(url=uri)
    elif str(method)=='Post' or str(method)=='post' or str(method)=='POST':
        content=requests.post(url=uri,json=parameters,headers=headers)
    # reponse_value=json.dump(content)
    return content

def result_status(sheet_num,caseid,status):
    sheet = ReadWrite(sheet_num)
    sheet.write(caseid,status)



if __name__=='__main__':
    data1=get_params(1,'Newb_002')
    #print(data1)
    repornses=send_request(data1)
    print(repornses.text)

