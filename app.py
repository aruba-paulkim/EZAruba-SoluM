from flask import Flask, request
import requests

app = Flask(__name__)

allow_device_id = {'C912B707-ED3D-490C-A154-B0C2A5E46189:com.arubanetworks.AppViewer':{'name':'김민혁', 'company':'HPE Aruba', 'dept':'Korea SE'},
                   'C912B707-ED3D-490C-A154-B0C2A5E46189:com.arubanetworks.aruba-meridian':{'name':'김민혁', 'company':'HPE Aruba', 'dept':'Korea SE'},
                   '769c0ef4-06d0-4ff4-bfae-a5e104b88f1c':{'name':'조용운', 'company':'HPE Aruba', 'dept':'Korea SE'},
                   'd9b9f9a4-1cf5-4871-8945-b749e50d95d7':{'name':'갤럭시텝A', 'company':'HPE Aruba', 'dept':'Korea SE'},
                   'b312hb12':{'name':'정우성', 'company':'HPE Aruba', 'dept':'Meridian'},
                  }

@app.route('/')
def index():
    return 'Aruba Meridian - Solu-M API Middleware'

@app.route('/api/meridian', methods=['GET', 'POST'])
def meridian():

    # device_id가 allow_device_id 에 있는지 확인
    device_id = request.form['device_id']
    if device_id in allow_device_id :
        info = allow_device_id[device_id]

        #EZ-Work-Enter
        if "5679487262654464" == request.form['campaign_id'] :
            headers = {'content-type': 'application/json'}
            url = 'http://192.168.99.212/inf/updateProductInfo'
            payload = {'Header':{'StoreCode':'1038'},'Body':{'PRODUCT':[{'ITEM_ID':'11','ITEM_NAME':info['company']+' '+info['name']+'님\n여기는 SmartWorkPlace 입니다.',
                       'ALIAS':'','SALE_PRICE':1101,'SALE_PRICE_DECIMAL':'00','LIST_PRICE':0,'LIST_PRICE_DECIMAL':'00','UNIT_PRICE':0,'UNIT_PRICE_DECIMAL':'00','ORIGIN':'','MANUFACTURER':'',
                       'TYPE':'','WEIGHT':'','WEIGHT_UNIT':'','UNIT_PRICE_UNIT':'','UNIT_DIMENSION':'','A_MARKER':'','R_MARKER':'','CATEGORY1':'','CATEGORY2':'','CATEGORY3':'','CATEGORY4':'','CATEGORY5':'',
                       'DISPLAY_TYPE':'01','DISPLAY_TYPE2':'02','DISPLAY_TYPE3':'','NFC_URL':'','ETC_0':'','ETC_1':'','ETC_2':'','ETC_3':'','ETC_4':'','ETC_5':'','ETC_6':'','ETC_7':'','ETC_8':'','ETC_9':'','STORE_ID':'1038'}]}}
            try:
                r = requests.post(url, headers=headers, json=payload)
                r.raise_for_status()
                response = r.json()
            except Exception as e:
                error_message = r.json()
                print(error_message)

            res = '{"notification":{"title": "EZ Aruba","message": "'+info['company']+' '+info['name']+'님\\n여기는 SmartWorkPlace 입니다.","path": ""}}'
            return res


        #EZ-Work-Exit
        elif "5355508601716736" == request.form['campaign_id'] :
            headers = {'content-type': 'application/json'}
            url = 'http://192.168.99.212/inf/updateProductInfo'
            payload = {'Header':{'StoreCode':'1038'},'Body':{'PRODUCT':[{'ITEM_ID':'11','ITEM_NAME':'반갑습니다.\n여기는 SmartWorkPlace 입니다.',
                       'ALIAS':'','SALE_PRICE':1101,'SALE_PRICE_DECIMAL':'00','LIST_PRICE':0,'LIST_PRICE_DECIMAL':'00','UNIT_PRICE':0,'UNIT_PRICE_DECIMAL':'00','ORIGIN':'','MANUFACTURER':'',
                       'TYPE':'','WEIGHT':'','WEIGHT_UNIT':'','UNIT_PRICE_UNIT':'','UNIT_DIMENSION':'','A_MARKER':'','R_MARKER':'','CATEGORY1':'','CATEGORY2':'','CATEGORY3':'','CATEGORY4':'','CATEGORY5':'',
                       'DISPLAY_TYPE':'01','DISPLAY_TYPE2':'02','DISPLAY_TYPE3':'','NFC_URL':'','ETC_0':'','ETC_1':'','ETC_2':'','ETC_3':'','ETC_4':'','ETC_5':'','ETC_6':'','ETC_7':'','ETC_8':'','ETC_9':'','STORE_ID':'1038'}]}}
            try:
                r = requests.post(url, headers=headers, json=payload)
                r.raise_for_status()
                response = r.json()
            except Exception as e:
                error_message = r.json()
                print(error_message)

            res = '{"notification":{"title": "EZ Aruba","message": "'+info['company']+' '+info['name']+'님\\n감사합니다..","path": ""}}'
            return res


        #EZ-Meeting-Enter
        elif "5555948702400512" == request.form['campaign_id'] :
            headers = {'content-type': 'application/json'}
            url = 'http://192.168.99.212/inf/updateProductInfo'
            payload = {'Header':{'StoreCode':'1038'},'Body':{'PRODUCT':[{'ITEM_ID':'12','ITEM_NAME':info['company']+' '+info['name']+'님\n여기는 MeetingRoom 입니다.',
                       'ALIAS':'','SALE_PRICE':1101,'SALE_PRICE_DECIMAL':'00','LIST_PRICE':0,'LIST_PRICE_DECIMAL':'00','UNIT_PRICE':0,'UNIT_PRICE_DECIMAL':'00','ORIGIN':'','MANUFACTURER':'',
                       'TYPE':'','WEIGHT':'','WEIGHT_UNIT':'','UNIT_PRICE_UNIT':'','UNIT_DIMENSION':'','A_MARKER':'','R_MARKER':'','CATEGORY1':'','CATEGORY2':'','CATEGORY3':'','CATEGORY4':'','CATEGORY5':'',
                       'DISPLAY_TYPE':'01','DISPLAY_TYPE2':'02','DISPLAY_TYPE3':'','NFC_URL':'','ETC_0':'','ETC_1':'','ETC_2':'','ETC_3':'','ETC_4':'','ETC_5':'','ETC_6':'','ETC_7':'','ETC_8':'','ETC_9':'','STORE_ID':'1038'}]}}
            try:
                r = requests.post(url, headers=headers, json=payload)
                r.raise_for_status()
                response = r.json()
            except Exception as e:
                error_message = r.json()
                print(error_message)
            res = '{"notification":{"title": "EZ Aruba","message": "'+info['company']+' '+info['name']+'님\\n 여기는 MeetingRoom 입니다.","path": ""}}'
            return res 


        #EZ-Meeting-Exit
        elif "4908345245564928" == request.form['campaign_id'] :
            headers = {'content-type': 'application/json'}
            url = 'http://192.168.99.212/inf/updateProductInfo'
            payload = {'Header':{'StoreCode':'1038'},'Body':{'PRODUCT':[{'ITEM_ID':'12','ITEM_NAME':'환영합니다.\n여기는 MeetingRoom 입니다.',
                       'ALIAS':'','SALE_PRICE':1101,'SALE_PRICE_DECIMAL':'00','LIST_PRICE':0,'LIST_PRICE_DECIMAL':'00','UNIT_PRICE':0,'UNIT_PRICE_DECIMAL':'00','ORIGIN':'','MANUFACTURER':'',
                       'TYPE':'','WEIGHT':'','WEIGHT_UNIT':'','UNIT_PRICE_UNIT':'','UNIT_DIMENSION':'','A_MARKER':'','R_MARKER':'','CATEGORY1':'','CATEGORY2':'','CATEGORY3':'','CATEGORY4':'','CATEGORY5':'',
                       'DISPLAY_TYPE':'01','DISPLAY_TYPE2':'02','DISPLAY_TYPE3':'','NFC_URL':'','ETC_0':'','ETC_1':'','ETC_2':'','ETC_3':'','ETC_4':'','ETC_5':'','ETC_6':'','ETC_7':'','ETC_8':'','ETC_9':'','STORE_ID':'1038'}]}}
            try:
                r = requests.post(url, headers=headers, json=payload)
                r.raise_for_status()
                response = r.json()
            except Exception as e:
                error_message = r.json()
                print(error_message)
            res = '{"notification":{"title": "EZ Aruba","message": "'+info['company']+' '+info['name']+'님\\n감사합니다.","path": ""}}'
            return res 


        else :
            # unregisted campaign_id
            return '{}'

    else :
        print("unknown device_id : "+request.form['device_id'])
        return '{}'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
