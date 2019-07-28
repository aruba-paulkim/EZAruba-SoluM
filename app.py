from flask import Flask, request
import requests

app = Flask(__name__)

#Paul Room101 on Enter 
campaign_id = "5710758973276160" 
#EZ-Work-Enter
#campaign_id = "5679487262654464"

allow_device_id = {'C912B707-ED3D-490C-A154-B0C2A5E46189:com.arubanetworks.AppViewer':{'name':'김민혁', 'company':'HPE Aruba', 'dept':'Korea SE'},
                   'b312hb12':{'name':'정우성', 'company':'HPE Aruba', 'dept':'Meridian'},
                  }

@app.route('/')
def index():
    return 'Aruba Meridian - Solu-M API Middleware'

@app.route('/api/meridian', methods=['GET', 'POST'])
def meridian():
    print("request.method:"+request.method)
    print("request.form['campaign_id']:"+request.form['campaign_id'])
    print("request.form['broadcaster_id']:"+request.form['broadcaster_id'])
    print("request.form['device_id']:"+request.form['device_id'])

    device_id = request.form['device_id']
    if campaign_id == request.form['campaign_id'] :
        # device_id가 allow_device_id 에 있는지 확인
        if device_id in allow_device_id :
            info = allow_device_id[device_id]
            print(info)

            headers = {'content-type': 'application/json'}
            url = 'http://192.168.99.212/inf/updateProductInfo'
            payload = {'Header':{'StoreCode':'1038'},'Body':{'PRODUCT':[{'ITEM_ID':'DESK01','ITEM_NAME':'WorkSpacs01','ALIAS':'','SALE_PRICE':1101,'SALE_PRICE_DECIMAL':'00','LIST_PRICE':0,'LIST_PRICE_DECIMAL':'00','UNIT_PRICE':0,'UNIT_PRICE_DECIMAL':'00','ORIGIN':'','MANUFACTURER':'','TYPE':'','WEIGHT':'','WEIGHT_UNIT':'','UNIT_PRICE_UNIT':'','UNIT_DIMENSION':'','A_MARKER':'','R_MARKER':'','CATEGORY1':'','CATEGORY2':'','CATEGORY3':'','CATEGORY4':'','CATEGORY5':'','DISPLAY_TYPE':'DESK01','DISPLAY_TYPE2':'','DISPLAY_TYPE3':'','NFC_URL':'',
                       'ETC_0':info['company'],'ETC_1':info['dept'],'ETC_2':info['name'],'ETC_3':'','ETC_4':'','ETC_5':'','ETC_6':'','ETC_7':'','ETC_8':'','ETC_9':'','STORE_ID':'1038'}]}}
            try:
                r = requests.post(url, headers=headers, json=payload)
                r.raise_for_status()
                response = r.json()
                print(response)
                if r.status_code == 201:
                    message = "201"
                else:
                    message = "ERROR"
            except Exception as e:
                error_message = r.json()
                print(error_message)

            return '{"notification":{"title": "EZ Aruba","message": "'+info['name']+'님 반갑습니다.","path": ""}}'
        else :
            return '{}'
    else :
        return '{}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
