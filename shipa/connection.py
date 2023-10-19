import requests
from rest_framework.response import Response
from rest_framework.views import APIView

class ShipaDataView(APIView):
    def post(self, request):
        url = "https://sb.ecommerceapi.shipa.com/api/Parcels"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }

        data = {
        "number": {
            "scheme": "Default",
            "value": ""
        },
        "references": [
            {
            "type": "OrderNo",
            "value": "1234567"
            }
        ],
        "product": "ATA",
        "services": [
            "COD"
        ],
        "ship_date": "2020-01-25T05:44:12.251Z",
        "shipper": {
            "name": "John Shipper",
            "phones": [
            "00123456789"
            ],
            "emails": [
            "john.shipper@shipa.com"
            ],
            "address": {
            "country": "CN",
            "city": "ShenChou",
            "state": "LuoHu District",
            "street": [
                "Shen Nan Dong Lu 5002"
            ],
            "post_code": "518008"
            },
            "location": {
            "longitude": -12.3456,
            "latitude": 78.9012
            }
        },
        "consignee": {
            "name": "Jane Consignee",
            "phones": [
            "00123456789"
            ],
            "emails": [
            "jane.consignee@shipa.com"
            ],
            "address": {
            "country": "AE",
            "city": "Dubai",
            "state": "",
            "street": [
                "Sheikh Zayed Road 1077"
            ],
            "post_code": ""
            },
            "location": {
            "longitude": -12.3456,
            "latitude": 78.9012
            }
        },
        "account": {
            "number": "0001",
            "entity": "DXB"
        },
        "weight": {
            "value": 100,
            "unit": "kg"
        },
        "dimensions": {
            "length": 10,
            "width": 20,
            "height": 30,
            "unit": "cm"
        },
        "items": [
            {
            "weight": {
                "value": 1,
                "unit": "gm"
            },
            "dimensions": {
                "length": 40,
                "width": 50,
                "height": 60,
                "unit": "cm"
            },
            "customs_value": {
                "amount": 1,
                "currency": "USD"
            },
            "origin_country": "US",
            "description": "New parcel",
            "hs_code": "10203040",
            "quantity": 1
            }
        ],
        "cod": {
            "amount": 10,
            "currency": "USD"
        }
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            # response.raise_for_status()  
            data = response.json()
            # print(response)

            return Response(data)
        except requests.exceptions.RequestException as e:
            return Response({'error': f'Failed to access the API: {str(e)}'}, status=response.status_code)
