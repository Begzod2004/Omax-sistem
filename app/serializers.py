from rest_framework import serializers
from .models import Import,Export,Buyurtma,Mijoz,Hodim, Mahsulotlar, Bonus, Mahsulot_olchov

class ImportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Import
        fields = "__all__"
        
        
class ExportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Export
        fields = "__all__"
        
        
class MijozSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"


class BuyurtmaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"

    def to_representation(self, instance):
        data = super(BuyurtmaSerializers, self).to_representation(instance)
        data['mijoz'] = MijozSerializers(instance=instance.mijoz).data
        data['buyurtma_nomi'] = MahsulotlarSerializers(instance=instance.buyurtma_nomi).data
        data['buyurtma_olchov'] = Mahsulot_olchovSerializers(instance=instance.buyurtma_olchov).data
        return data

        
class HodimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hodim
        fields = "__all__"



        
class BonusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = "__all__"


class Mahsulot_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Mahsulot_olchov
        fields = ('id','olchov','narx',)


class MahsulotlarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulotlar
        fields = "__all__"


class Mahsulot_olchovSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot_olchov
        fields = ('id','mahsulot_number','olchov','narx',)
        

class Buyurtma1Serializers(serializers.ModelSerializer):
    mijoz = MijozSerializers()
    buyurtma_olchov = BuyurtmaSerializers()
    narx = Mahsulot_Serializers()

    class Meta:
        model = Buyurtma
        fields =  ('id', 'buyurtma_nomi', 'mijoz', 'format', 'buyurtma_olchov', 'narx', 'miqdor', 'buyurtma_sana', 'izoh')

