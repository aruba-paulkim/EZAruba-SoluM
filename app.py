# -*- coding: utf-8 -*-
from flask import Flask, request, json, render_template, session, redirect
import requests, sqlite3

app = Flask(__name__)
app.secret_key = b'aruba1234567890'

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
    if 'sess_admin' in session :
        return redirect('/setup')
    else :
        return redirect('/login')
        #return 'ERROR'


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET' :
        if 'sess_admin' in session :
            return redirect('/setup')
        else :
            return render_template("login.html")

    elif request.method == 'POST' :        
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("select * from admin where admin_id=? and admin_pw=?", 
            (request.form['admin_id'], request.form['admin_pw']))
        rows = cur.fetchall()

        if len(rows) > 0 : 
            session['sess_admin'] = request.form['admin_id']
        else :
            print('login fail')

        con.close()
        return redirect('/')

    else :
        return 'ERROR'


@app.route('/logout')
def logout():
    session.pop('sess_admin', None)
    return redirect('/')


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if 'sess_admin' in session :
        if request.method == 'GET' :
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute("select * from allowed_device")
            rows = cur.fetchall()
            con.close()
            return render_template("setup.html", rows=rows)
        elif request.method == 'POST' :
            selected = request.form.getlist('demo_user')
            print(selected)
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute("select * from allowed_device")
            rows = cur.fetchall()
            enable_YN = ""
            for row in rows :
                if str(row[0]) in selected :
                    enable_YN = "Y"
                else :
                    enable_YN = "N"

                print(str(row[0])+" is "+enable_YN)
                cur.execute("update allowed_device set enable_YN=? where seq =?", (enable_YN, row[0]))
                con.commit()

            con.close()
            return redirect('/setup')
        else :
            return 'ERROR'
    else :
        return redirect('/')


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

    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("select * from allowed_device where enable_YN =? and device_id=?", ('Y',req_device_id))
    rows = cur.fetchall()
    if len(rows) > 0 : 
        info = rows[0]
    else :
        print("unknown or not enabled device_id : "+request.form['device_id'])
        return '{}'

    #EZ-Work-Enter
    if "5679487262654464" == request.form['campaign_id'] :
        display_id = '11'
        display_str = inform_str['solum_work_enter'].replace('##name##',info[2])
        response = apicall(display_id, display_str)
        meridian_str = inform_str['meridian_work_enter'].replace('##name##',info[2])
        print("EZ-Work-Enter / " + info[2] + " / "+response['Header']['ResultCode'] + " / "+meridian_str)

    #EZ-Work-Exit
    elif "5355508601716736" == request.form['campaign_id'] :
        display_id = '11'
        display_str = inform_str['solum_work_exit']
        response = apicall(display_id, display_str)
        meridian_str = inform_str['meridian_work_exit'].replace('##name##',info[2])
        print("EZ-Work-Exit / " + info[2] + " / "+response['Header']['ResultCode'] + " / "+meridian_str)

    #EZ-Meeting-Enter
    elif "5555948702400512" == request.form['campaign_id'] :
        display_id = '12'
        display_str = inform_str['solum_meeting_enter'].replace('##name##',info[2])
        response = apicall(display_id, display_str)
        meridian_str = inform_str['meridian_meeting_enter'].replace('##name##',info[2])
        print("EZ-Meeting-Enter / " + info[2] + " / "+response['Header']['ResultCode'] + " / "+meridian_str)
        fd = open("static/show-meetingroom.txt", "w")
        fd.write(meridian_str.replace("\\n","<br>"))
        fd.close()

    #EZ-Meeting-Exit
    elif "4908345245564928" == request.form['campaign_id'] :
        display_id = '12'
        display_str = inform_str['solum_meeting_exit']
        response = apicall(display_id, display_str)
        meridian_str = inform_str['meridian_meeting_exit'].replace('##name##',info[2])
        print("EZ-Meeting-Exit / " + info[2] + " / "+response['Header']['ResultCode'] + " / "+meridian_str)
        fd = open("static/show-meetingroom.txt", "w")
        fd.write(meridian_str.replace("\\n","<br>"))
        fd.close()

    else : 
        print('There is no campaign_id...')


    return '{"notification":{"title": "EZ Aruba","message": "'+meridian_str+'","path": ""}}'


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8080, debug=False)
