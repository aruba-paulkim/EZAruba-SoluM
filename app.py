# -*- coding: utf-8 -*-
from flask import Flask, request, json, render_template
import requests

app = Flask(__name__)

with open('allow_device_id.txt', encoding='utf-8-sig') as data_file:
    allow_device_id = json.load(data_file)
with open('inform_str.txt', encoding='utf-8-sig') as data_file:
    inform_str = json.load(data_file)


def apicall(display_id, display_str):
    headers = {'content-type': 'application/json'}
    url = 'http://192.168.99.212/inf/updateProductInfo'
    payload = {'Header':{'StoreCode':'1038'},'Body':{'PRODUCT':[{'ITEM_ID':display_id,'ITEM_NAME':display_str,
               'ALIAS':'','SALE_PRICE':1101,'SALE_PRICE_DECIMAL':'00','LIST_PRICE':0,'LIST_PRICE_DECIMAL':'00',
               'UNIT_PRICE':0,'UNIT_PRICE_DECIMAL':'00','ORIGIN':'','MANUFACTURER':'','TYPE':'','WEIGHT':'','WEIGHT_UNIT':'',
               'UNIT_PRICE_UNIT':'','UNIT_DIMENSION':'','A_MARKER':'','R_MARKER':'','CATEGORY1':'','CATEGORY2':'','CATEGORY3':'','CATEGORY4':'','CATEGORY5':'',
               'DISPLAY_TYPE':'01','DISPLAY_TYPE2':'02','DISPLAY_TYPE3':'','NFC_URL':'','ETC_0':'','ETC_1':'','ETC_2':'','ETC_3':'','ETC_4':'','ETC_5':'','ETC_6':'','ETC_7':'','ETC_8':'','ETC_9':'','STORE_ID':'1038'}]}}
    try:
        r = requests.post(url, headers=headers, json=payload)
        r.raise_for_status()
        response = r.json()
        return response
    except Exception as e:
        error_message = r.json()
        print(error_message)
        return error_message



@app.route('/')
def index():
    return inform_str['system_name']

@app.route('/show/<location>', methods=['GET', 'POST'])
def show(location):
    if request.method == 'GET' :
        return render_template("show.html")
    elif request.method == 'POST' :
        if location == "meetingroom" : 
            fd = open("static/show-"+location+".txt", 'r')
            contents =fd.read()
            fd.close()
        else :
            contents = ""
        return contents
    else :
        return ''

@app.route('/api/meridian', methods=['GET', 'POST'])
def meridian():
    # device_id가 allow_device_id 에 있는지 확인
    req_device_id = request.form['device_id'][0:36].upper()
    try:
        info = allow_device_id[req_device_id]
    except Exception as e:
        #print(e)
        print("unknown device_id : "+request.form['device_id'])
        return '{}'

    #EZ-Work-Enter
    if "5679487262654464" == request.form['campaign_id'] :
        display_id = '11'
        display_str = inform_str['solum_work_enter'].replace('##name##',info['name'])
        response = apicall(display_id, display_str)
        meridian_str = inform_str['meridian_work_enter'].replace('##name##',info['name'])
        print("EZ-Work-Enter / " + info['name'] + " / "+response['Header']['ResultCode'])

    #EZ-Work-Exit
    elif "5355508601716736" == request.form['campaign_id'] :
        display_id = '11'
        display_str = inform_str['solum_work_exit']
        response = apicall(display_id, display_str)
        meridian_str = inform_str['meridian_work_exit'].replace('##name##',info['name'])
        print("EZ-Work-Exit / " + info['name'] + " / "+response['Header']['ResultCode'])

    #EZ-Meeting-Enter
    elif "5555948702400512" == request.form['campaign_id'] :
        display_id = '12'
        display_str = inform_str['solum_meeting_enter'].replace('##name##',info['name'])
        response = apicall(display_id, display_str)
        meridian_str = inform_str['meridian_meeting_enter'].replace('##name##',info['name'])
        print("EZ-Meeting-Enter / " + info['name'] + " / "+response['Header']['ResultCode'])
        fd = open("static/show-meetingroom.txt", "w")
        fd.write(display_str.replace("\\n","<br><br>"))
        fd.close()

    #EZ-Meeting-Exit
    elif "4908345245564928" == request.form['campaign_id'] :
        display_id = '12'
        display_str = inform_str['solum_meeting_exit']
        response = apicall(display_id, display_str)
        meridian_str = inform_str['meridian_meeting_exit'].replace('##name##',info['name'])
        print("EZ-Meeting-Exit / " + info['name'] + " / "+response['Header']['ResultCode'])
        fd = open("static/show-meetingroom.txt", "w")
        fd.write(display_str.replace("\\n","<br><br>"))
        fd.close()

    else : 
        print('There is no campaign_id...')


    return '{"notification":{"title": "EZ Aruba","message": "'+meridian_str+'","path": ""}}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
