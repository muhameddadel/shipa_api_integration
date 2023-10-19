from rest_framework import serializers



######################### Parcels serilization #########################
class ParcelsNumberSerializer(serializers.Serializer):
    scheme = serializers.CharField()
    value = serializers.CharField(required=False, allow_blank=True)

class ParcelsReferenceSerializer(serializers.Serializer):
    type = serializers.CharField(required=False, allow_blank=True ,max_length=50)
    value = serializers.CharField(required=False, allow_blank=True ,max_length=50)

class ParcelsAddressSerializer(serializers.Serializer):
    country = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    street = serializers.ListField(child=serializers.CharField())
    post_code = serializers.CharField()

class ParcelsContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    phones = serializers.ListField(child=serializers.CharField())
    emails = serializers.ListField(child=serializers.EmailField())
    address = ParcelsAddressSerializer()

class ParcelsWeightSerializer(serializers.Serializer):
    value = serializers.FloatField()
    unit = serializers.CharField()

class ParcelsDimensionsSerializer(serializers.Serializer):
    length = serializers.FloatField()
    width = serializers.FloatField()
    height = serializers.FloatField()
    unit = serializers.CharField()

class ParcelsItemSerializer(serializers.Serializer):
    weight = ParcelsWeightSerializer()
    dimensions = ParcelsDimensionsSerializer()
    customs_value = serializers.DictField()
    origin_country = serializers.CharField()
    description = serializers.CharField()
    hs_code = serializers.CharField()
    quantity = serializers.IntegerField()

class ParcelsSerializer(serializers.Serializer):
    number = ParcelsNumberSerializer()
    references = serializers.ListField(child=serializers.DictField())
    product = serializers.CharField(required=True)
    services = serializers.ListField(child=serializers.CharField())
    ship_date = serializers.CharField()
    shipper = ParcelsContactSerializer()
    consignee = ParcelsContactSerializer()
    account = serializers.DictField()
    weight = ParcelsWeightSerializer()
    dimensions = ParcelsDimensionsSerializer()
    items = serializers.ListField(child=ParcelsItemSerializer())
    cod = serializers.DictField()



######################### container serilization #########################
class ReferenceSerializer(serializers.Serializer):
    type = serializers.CharField()
    value = serializers.CharField()

class ContainerSerializer(serializers.Serializer):
    container_number = serializers.DictField(
child=serializers.CharField())
    references = serializers.ListField(
        child=ReferenceSerializer()
    )
    type = serializers.CharField()
    description = serializers.CharField()



######################### add parcel to container serilization ##########################
class AddParcelToContainerSerializer(serializers.Serializer):
    container_number = serializers.DictField(child=serializers.CharField())
    parcel_numbers = serializers.ListField(child=ParcelsNumberSerializer())  
    close_container = serializers.BooleanField()


######################### add trace to a parcel serilization ##########################
class AddTraceToParcelSerializer(serializers.Serializer):
    parcel_number = ParcelsNumberSerializer()
    code = serializers.CharField()
    entity = serializers.CharField()


######################### add trace to a container serilization ##########################
class AddTraceToContainerSerializer(serializers.Serializer):
    container_number = serializers.DictField(child=serializers.CharField())
    code = serializers.CharField()
    entity = serializers.CharField()


######################### add trace to a container serilization ##########################
class GenerateParcelLabelSerializer(serializers.Serializer):
    output = serializers.CharField()
    template_name = serializers.CharField()


######################### add trace to a container serilization ##########################
class AddAttachmentToParcelSerializer(serializers.Serializer):
    type = serializers.CharField()
    data = serializers.CharField()
    mime_type = serializers.CharField()