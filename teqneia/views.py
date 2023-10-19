import io
from rest_framework import serializers
import requests
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class CreateParcel(APIView):
    def post(self, request):
        url = "https://sb.ecommerceapi.shipa.com/api/Parcels"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }

        serializer = ParcelsSerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.validated_data

            try:
                response = requests.post(url, headers=headers, json=serialized_data)
                data = response.json()
                return Response(data)
            except requests.exceptions.RequestException as e:
                return Response({'error': f'Failed to access the API: {str(e)}'}, status=response.status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




######################### create container #########################
class CreateContainer(APIView):
    def post(self, request):
        url = "https://sb.ecommerceapi.shipa.com/api/Containers"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }

        serializer = ContainerSerializer(data=request.data)

        if serializer.is_valid():
            serialized_data = serializer.validated_data
            try:
                response = requests.post(url, headers=headers, json=serialized_data)
                data = response.json()
                return Response(data)
            except requests.exceptions.RequestException as e:
                return Response({'error': f'Failed to access the API: {str(e)}'}, status=response.status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



######################### add parcel to container #########################
class AddParcelToContainer(APIView):
    def post(self, request, container_number):
        url = f"https://sb.ecommerceapi.shipa.com/api/Containers/{container_number}/parcels"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }
        # print(container_number)
        serializer = AddParcelToContainerSerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.validated_data
            try:
                response = requests.post(url, headers=headers, json=serialized_data)
                return Response(status=response.status_code)
            except requests.exceptions.RequestException as e:
                return Response({'error': f'Failed to access the API: {str(e)}'}, status=response.status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



######################### close container #########################
class CloseContainer(APIView):
    def post(self, request, container_number):
        url = f"https://sb.ecommerceapi.shipa.com/api/Containers/{container_number}/close"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }

        payload = ""

        try:
            response = requests.post(url, headers=headers, data=payload)
            # response_data = response.text 

            return Response(status=response.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': f'Failed to access the API: {str(e)}'}, status=response.status_code)


######################### track parcel #########################
class TrackParcel(APIView):
    def get(self, request, parcel_number):
        url = f"https://sb.ecommerceapi.shipa.com/api/Parcels/Track/{parcel_number}"

        payload = ""

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }

        try:
            response = requests.get(url, headers=headers, data=payload)
            # response_data = response.text 

            return Response(response.json() ,status=response.status_code)
        except requests.exceptions.RequestException as e:
            return Response({'error': f'Failed to access the API: {str(e)}'}, status=response.status_code)


######################### add trace to parcel #########################
class AddTraceToParcel(APIView):
    def post(self, request):
        url = f"https://sb.ecommerceapi.shipa.com/api/parcels/traces"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }

        serializer = AddTraceToParcelSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serialized_data = serializer.validated_data
            print(serialized_data)
            try:
                response = requests.post(url, headers=headers, json=serialized_data)
                response_data = response.json()
                return Response(response_data, status=response.status_code)
            except requests.exceptions.RequestException as e:
                return Response({'error': f'Failed to access the API: {str(e)}'}, status=response.status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######################### add trace to container #########################
class AddTraceToContainer(APIView):
    def post(self, request, container_number):
        url = f"https://sb.ecommerceapi.shipa.com/api/Containers/{container_number}/traces"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }


        serializer = AddTraceToContainerSerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.validated_data
            try:
                response = requests.post(url, headers=headers, json=serialized_data)
                response_data = response.json()
                return Response(response_data, status=response.status_code)
            except requests.exceptions.RequestException as e:
                return Response({'error': f'Failed to access the API: {str(e)}'}, status=response.status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######################### generate parcel label #########################
class GenerateParcelLabel(APIView):
    def post(self, request, schema, value):
        url = f"https://sb.ecommerceapi.shipa.com/api/Parcels/{schema}_{value}/Label"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }

        serializer = GenerateParcelLabelSerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.validated_data
            try:
                response = requests.post(url, headers=headers, json=serialized_data)

                if response.status_code == 200:
                    pdf_content = response.content
                    pdf_io = io.BytesIO(pdf_content)
                    response = FileResponse(pdf_io, as_attachment=True)
                    # response['Content-Disposition'] = f'attachment; filename="{schema}_{value}.pdf"'

                    return response
                else:
                    return Response({'error': 'Failed to generate parcel label'}, status=response.status_code)

            except requests.exceptions.RequestException as e:
                return Response({'error': f'Failed to access the API: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



######################### add attachement to parcel #########################
class AddAttachementToParcel(APIView):
    def post(self, request, schema, value):
        url = f"https://sb.ecommerceapi.shipa.com/api/Parcels/{schema}_{value}/attachments"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiKey 02Qs1gL3(DfMuQ))V1rf_wrTdyaniXwW',
        }
        serializer = AddAttachmentToParcelSerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.validated_data
            try:
                response = requests.post(url, headers=headers, json=serialized_data)
                return Response(status=response.status_code)

            except requests.exceptions.RequestException as e:
                return Response({'error': f'Failed to access the API: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


