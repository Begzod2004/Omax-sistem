from django.contrib import admin

# Register your models here.


from .models import Buyurtma, Import, Export, Mijoz, Ombor, Hodim, Mahsulotlar, Bonus, Mahsulot_olchov



class Mahsulot_olchovAdmin(admin.ModelAdmin):
    list_display = ['olchov', 'narx']
    list_filter = ('olchov', 'narx')
    list_per_page = 10
    search_fields = ['olchov', 'narx']

    class Meta:
        model = Mahsulot_olchov

admin.site.register(Mahsulot_olchov, Mahsulot_olchovAdmin)



class MahsulotlarAdmin(admin.ModelAdmin):
    list_display = ['mahsulot_nomi', 'mahsulot_format']
    list_filter = ('mahsulot_nomi', 'mahsulot_format')
    list_per_page = 10
    search_fields = ['mahsulot_nomi', 'mahsulot_format']

    class Meta:
        model = Mahsulotlar


admin.site.register(Mahsulotlar, MahsulotlarAdmin)



class BonusAdmin(admin.ModelAdmin):
    list_display = ['bonus_nomi', 'bonus_miqdori', 'bonus_muddati']
    list_filter = ('bonus_nomi', 'bonus_miqdori', 'bonus_muddati')
    list_per_page = 10
    search_fields = ['bonus_nomi', 'bonus_miqdori', 'bonus_muddati']

    class Meta:
        model = Bonus


admin.site.register(Bonus, BonusAdmin)


class ImportAdmin(admin.ModelAdmin):
    list_display = ['mahsulot_nomi', 'format', 'import_vaqt', 'miqdor', 'narx', 'umumiy']
    list_filter = ('mahsulot_nomi', 'format', 'import_vaqt', 'miqdor', 'narx')
    list_per_page = 10
    search_fields = ['mahsulot_nomi', 'format', 'import_vaqt', 'miqdor', 'narx']

    class Meta:
        model = Import


admin.site.register(Import, ImportAdmin)


class ExportAdmin(admin.ModelAdmin):
    list_display = ['mahsulot_nomi', 'format', 'export_vaqt', 'miqdor', 'narx', 'umumiy']
    list_filter = ('mahsulot_nomi', 'format', 'export_vaqt', 'miqdor', 'narx')
    list_per_page = 10
    search_fields = ['mahsulot_nomi', 'format', 'export_vaqt', 'miqdor', 'narx']

    class Meta:
        model = Export
admin.site.register(Export, ExportAdmin)


class MijozAdmin(admin.ModelAdmin):
    list_filter = ('ism_sharif', 'telefon',)
    list_display = ['nomi', 'ism_sharif', 'telefon', 'manzil']
    list_per_page = 10
    search_fields = ['nomi', 'ism_sharif', 'telefon', 'manzil']

    class Meta:
        model = Mijoz
admin.site.register(Mijoz, MijozAdmin)


class BuyurtmaAdmin(admin.ModelAdmin):
    list_filter = ('buyurtma_nomi','mijoz','format', 'buyurtma_sana','buyurtma_olchov', 'miqdor', 'narx', 'mijoz')
    list_display = ['mijoz','buyurtma_nomi', 'format', 'buyurtma_sana','buyurtma_olchov', 'miqdor', 'narx', 'umumiy']
    list_per_page = 10
    search_fields = ['mijoz', 'format', 'buyurtma_sana', 'umumiy', 'mijoz','buyurtma_olchov']

    class Meta:
        model = Buyurtma


admin.site.register(Buyurtma, BuyurtmaAdmin)


class OmborAdmin(admin.ModelAdmin):
    list_filter = ('mahsulot_nomi', 'format', 'miqdor', 'narx')
    list_display = ['mahsulot_nomi', 'format', 'miqdor', 'narx']
    list_per_page = 10
    search_fields = ['mahsulot_nomi', 'format']

    class Meta:
        model = Ombor


admin.site.register(Ombor, OmborAdmin)


class HodimAdmin(admin.ModelAdmin):
    list_filter = ('ism_sharif', 'lavozim', 'stavka')
    list_display = ['ism_sharif', 'lavozim', 'stavka']
    list_per_page = 10
    search_fields = ['ism_sharif', 'lavozim', 'stavka']

    class Meta:
        model = Hodim


admin.site.register(Hodim, HodimAdmin)
