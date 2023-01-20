from rest_framework.viewsets import ModelViewSet
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .serializers import *
from .models import Bonus, Import, Export, Mahsulot_olchov, Mijoz, Buyurtma, Hodim, Mahsulotlar
from . import query_params
from rest_framework.response import Response
from rest_framework import generics, status

schema_view = get_swagger_view(title='Pastebin API')




class MahsulotlarViewSet(ModelViewSet):
    queryset = Mahsulotlar.objects.all()
    serializer_class = MahsulotlarSerializers

    def get_serializer_context(self):
        return {"request": self.request}

    def create(self, request, *args, **kwargs):
        mahsulot_rasm = self.request.FILES.get("mahsulot_rasm")
        mahsulot_nomi = self.request.data.get("mahsulot_nomi")
        mahsulot_format = self.request.data.get("mahsulot_format")
        # mahsulot_olchov = self.request.data.get("mahsulot_olchov")
        # mahsulot_narx = self.request.data.get("mahsulot_narx")
        mahsulot = Mahsulotlar.objects.create(
            mahsulot_rasm=mahsulot_rasm, mahsulot_nomi=mahsulot_nomi,
            mahsulot_format=mahsulot_format)
        print(mahsulot)
        return Response(self.serializer_class(instance=mahsulot, context={"request": self.request}).data)

    def get_queryset(self):
        queryset = super().get_queryset()
        mahsulot_nomi = self.request.query_params.get("mahsulot_nomi")
        mahsulot_format = self.request.query_params.get("mahsulot_format")
        # mahsulot_olchov = self.request.query_params.get("mahsulot_olchov")
        # mahsulot_narx = self.request.query_params.get("mahsulot_narx")
       
        filter_data = {}
        if mahsulot_nomi:
            filter_data['mahsulot_nomi__icontains'] = mahsulot_nomi
        if mahsulot_format:
            filter_data['mahsulot_format'] = mahsulot_format
        # if mahsulot_olchov:
        #     filter_data['mahsulot_olchov'] = mahsulot_olchov
        # if mahsulot_narx:
        #     filter_data['mahsulot_narx'] = mahsulot_narx
        queryset = queryset.filter(**filter_data)
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.mahsulot_query_params())
    def list(self, *args, **kwargs):
        return super(MahsulotlarViewSet, self).list(*args, **kwargs)




class BonusViewSet(ModelViewSet):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        bonus_nomi = self.request.query_params.get("bonus_nomi")
        bonus_miqdori = self.request.query_params.get("bonus_miqdori")
        # mahsulot_olchov = self.request.query_params.get("mahsulot_olchov")
        bonus_muddati = self.request.query_params.get("bonus_muddati")
       
        filter_data = {}
        if bonus_nomi:
            filter_data['bonus_nomi__icontains'] = bonus_nomi
        if bonus_miqdori:
            filter_data['bonus_miqdori'] = bonus_miqdori
        if bonus_muddati:
            filter_data['bonus_muddati'] = bonus_muddati
        queryset = queryset.filter(**filter_data)
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.bonus_query_params())
    def list(self, *args, **kwargs):
        return super(BonusViewSet, self).list(*args, **kwargs)







class ImportViewSet(ModelViewSet):
    queryset = Import.objects.all()
    serializer_class = ImportSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        mahsulot_nomi = self.request.query_params.get("mahsulot_nomi")
        format = self.request.query_params.get("format")
        miqdor = self.request.query_params.get("miqdor")
        vaqt = self.request.query_params.get("vaqt")
        filter_data = {}
        if mahsulot_nomi:
            filter_data['mahsulot_nomi__icontains'] = mahsulot_nomi
        if format:
            filter_data['format'] = format
        if miqdor:
            filter_data['miqdor'] = miqdor
        if vaqt:
            filter_data['import_vaqt__date'] = vaqt
        queryset = queryset.filter(**filter_data)
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.import_export_query_params())
    def list(self, *args, **kwargs):
        return super(ImportViewSet, self).list(*args, **kwargs)


class ExportViewSet(ModelViewSet):
    queryset = Export.objects.all()
    serializer_class = ExportSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        mahsulot_nomi = self.request.query_params.get("mahsulot_nomi")
        format = self.request.query_params.get("format")
        miqdor = self.request.query_params.get("miqdor")
        vaqt = self.request.query_params.get("vaqt")
        filter_data = {}
        if mahsulot_nomi:
            filter_data['mahsulot_nomi__icontains'] = mahsulot_nomi
        if format:
            filter_data['format'] = format
        if miqdor:
            filter_data['miqdor'] = miqdor
        if vaqt:
            filter_data['export_vaqt__date'] = vaqt
        queryset = queryset.filter(**filter_data)
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.import_export_query_params())
    def list(self, *args, **kwargs):
        return super(ExportViewSet, self).list(*args, **kwargs)


class MijozViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        nomi = self.request.query_params.get("nomi")
        ism_sharif = self.request.query_params.get("ism_sharif")
        filter_data = {}
        if nomi:
            filter_data['nomi__icontains'] = nomi
        if ism_sharif:
            filter_data['ism_sharif__icontains'] = ism_sharif
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.customer_query_params())
    def list(self, *args, **kwargs):
        return super(MijozViewSet, self).list(*args, **kwargs)


class BuyurtmaViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        mijoz = self.request.query_params.get("mijoz")
        format = self.request.query_params.get("format")
        buyurtma_olchov = self.request.query_params.get("buyurtma_olchov")
        buyurtma_sana = self.request.query_params.get("buyurtma_sana")
        filter_data = {}
        if mijoz:
            filter_data['mijoz_id'] = mijoz
        if format:
            filter_data['format'] = format
        if buyurtma_olchov:
            filter_data['buyurtma_olchov'] = buyurtma_olchov
            
        if buyurtma_sana:
            filter_data['buyurtma_sana__date'] = buyurtma_sana

        queryset = queryset.filter(**filter_data)
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.order_query_params())
    def list(self, *args, **kwargs):
        return super(BuyurtmaViewSet, self).list(*args, **kwargs)



class Mahsulot_olchovViewSet(ModelViewSet):
    queryset = Mahsulot_olchov.objects.all()
    serializer_class = Mahsulot_olchovSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        olchov = self.request.query_params.get("olchov")
        narx = self.request.query_params.get("narx")
        
        filter_data = {}
        if olchov:
            filter_data['olchov_id'] = olchov
        if olchov:
            filter_data['olchov'] = olchov
        if narx:
            filter_data['narx'] = narx
       

        queryset = queryset.filter(**filter_data)
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.mahsulot_olchov_query_params())
    def list(self, *args, **kwargs):
        return super(Mahsulot_olchovViewSet, self).list(*args, **kwargs)



class HodimViewSet(ModelViewSet):
    queryset = Hodim.objects.all()
    serializer_class = HodimSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        lavozim = self.request.query_params.get("lavozim")
        ism_sharif = self.request.query_params.get("ism_sharif")
        filter_data = {}
        if ism_sharif:
            filter_data['ism_sharif__icontains'] = ism_sharif
        if lavozim:
            filter_data['ism_sharif__icontains'] = ism_sharif

        queryset = queryset.filter(**filter_data)
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.worker_query_params())
    def list(self, *args, **kwargs):
        return super(HodimViewSet, self).list(*args, **kwargs)



# class Buyurtma1RetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Buyurtma.objects.all()
#     serializer_class = Buyurtma1Serializers
#     lookup_field = 'pk'


class Buyurtma1ViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = Buyurtma1Serializers

    def get_queryset(self):
        queryset = super().get_queryset()
        mijoz = self.request.query_params.get("mijoz")
        format = self.request.query_params.get("format")
        buyurtma_olchov = self.request.query_params.get("buyurtma_olchov")
        buyurtma_sana = self.request.query_params.get("buyurtma_sana")
        filter_data = {}
        if mijoz:
            filter_data['mijoz_id'] = mijoz
        if format:
            filter_data['format'] = format
        if buyurtma_olchov:
            filter_data['buyurtma_olchov'] = buyurtma_olchov
            
        if buyurtma_sana:
            filter_data['buyurtma_sana__date'] = buyurtma_sana

        queryset = queryset.filter(**filter_data)
        return queryset

    @swagger_auto_schema(manual_parameters=query_params.order_query_params())
    def list(self, *args, **kwargs):
        return super(Buyurtma1ViewSet, self).list(*args, **kwargs)
