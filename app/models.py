from django.db import models
import math

format = [
    ('kg','kilogram'),
    ('dona','dona'),
    ('litr','litr'),
    ('metr','metr'),
]

class Mahsulotlar(models.Model):
    mahsulot_rasm = models.ImageField(upload_to='mahsulotlar/rasm', null=True,blank=True)
    mahsulot_nomi = models.CharField(max_length=200)
    mahsulot_format = models.CharField(choices=format, max_length=10)
  
    
    def __str__(self):
        return f"{self.mahsulot_rasm} | {self.mahsulot_nomi} | {self.mahsulot_format}"
    
    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'  

class Mahsulot_olchov(models.Model):
    mahsulot_number = models.IntegerField(default=0)
    olchov = models.FloatField(help_text="(kg lik, litrlik ...)")
    narx = models.FloatField(max_length=200)
   
    def __str__(self):
        return f"{self.olchov} | {self.narx}"
    
    class Meta:
        verbose_name = "Mahsulot o'lchovi"
        verbose_name_plural = "Mahsulot o'lchovlari"  



class Import(models.Model):
    mahsulot_nomi = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE)
    format = models.CharField(choices=format, max_length=10)
    miqdor = models.IntegerField()
    narx = models.IntegerField()
    import_vaqt = models.DateTimeField()
    izoh = models.TextField(null=True,blank=True)
    
    @property
    def umumiy(self):
        return self.narx * self.miqdor
        
    def __str__(self):
        return f"{self.mahsulot_nomi} | {self.format} | {self.import_vaqt} | {self.umumiy}"
    
    class Meta:
        verbose_name = 'Import'
        verbose_name_plural = 'Import'
        
        
class Export(models.Model):
    mahsulot_nomi = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE)
    format = models.CharField(choices=format, max_length=10)
    miqdor = models.IntegerField()
    narx = models.IntegerField()
    export_vaqt = models.DateTimeField()
    
    izoh = models.TextField(null=True,blank=True)
    
    @property
    def umumiy(self):
        return self.narx * self.miqdor
    
    def __str__(self):
        return f"{self.mahsulot_nomi} | {self.format} |{self.narx} | {self.export_vaqt} | {self.umumiy}"
    
    class Meta:
        verbose_name = 'Export'
        verbose_name_plural = 'Export'
    
class Mijoz(models.Model):
    nomi = models.CharField(max_length=200)
    ism_sharif = models.CharField(max_length=200)
    telefon = models.CharField(max_length=19)
    manzil = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nomi} | {self.ism_sharif} | {self.telefon} | {self.manzil}"
    
    
    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'
    
 
  
    
class Buyurtma(models.Model):
    buyurtma_nomi = models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE, related_name='buyurtma')
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE, related_name='mijoz_buyurtmasi')
    format = models.CharField(choices=format, max_length=10, null=True,blank=True)
    buyurtma_olchov = models.ForeignKey(Mahsulot_olchov, on_delete=models.CASCADE, related_name='olchov_buyurtmasi')
    narx = models.ForeignKey(Mahsulot_olchov, on_delete=models.CASCADE, related_name='narx_buyurtmasi')
    miqdor = models.IntegerField()
    buyurtma_sana = models.DateTimeField(auto_now=True)
    izoh = models.TextField(null=True,blank=True)
    
    @property
    def umumiy(self):
        return self.narx.narx * self.miqdor
    
    
    
    def __str__(self):
        return f"{self.mijoz} | {self.buyurtma_nomi} | {self.format} {self.miqdor} | {self.narx} | {self.buyurtma_sana} | {self.umumiy}"
    
    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'
        
        
class Ombor(models.Model):
    mahsulot_nomi = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE)
    format = models.CharField(choices=format, max_length=10)
    narx = models.IntegerField()
    miqdor = models.IntegerField()
    izoh = models.TextField(null=True,blank=True)
    
    @property
    def umumiy(self):
        return self.narx * self.miqdor
        
    def __str__(self):
        return f"{self.mahsulot_nomi} | {self.format} | {self.narx} | {self.miqdor} | {self.umumiy}"
    
    class Meta:
        verbose_name = 'Ombor'
        verbose_name_plural = 'Omborxona'
    
    
class Hodim(models.Model):
    ism_sharif = models.CharField(max_length=200)
    lavozim = models.CharField(max_length=100)
    stavka = models.FloatField()
    
    
    def __str__(self):
        return f"{self.ism_sharif} | {self.lavozim} | {self.stavka}"
    
    class Meta:
        verbose_name = 'Hodim'
        verbose_name_plural = 'Hodimlar'
        
        
        
        
class Bonus(models.Model):
    bonus_nomi = models.CharField(max_length=300)
    bonus_miqdori = models.FloatField(max_length=1000)
    bonus_muddati = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.bonus_nomi} | {self.bonus_miqdori} | {self.bonus_muddati}"
    
    class Meta:
        verbose_name = 'Bonus'
        verbose_name_plural = 'Bonuslar'
