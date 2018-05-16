from django.db import models
from django.utils.translation import ugettext_lazy as _


class tb_Gaget(models.Model):
    Tipo = models.CharField(_('Instrumento'), max_length=50)
    Modelo = models.CharField(_('Modelo'), max_length=50)
    Fabricante = models.CharField(_('Fabricante'), max_length=50)
    Status = models.CharField(_('Status'), max_length=50)
    Torre = models.CharField(_('Torre'), max_length=50)
    Slope = models.FloatField(_('slope'))
    Offset = models.FloatField(_('off-set'))
    Serial = models.CharField(_('Serial #'), max_length=50)
    Calibracao = models.CharField(_('Calibração #'), max_length=50)
    doc_Calibracao = models.FileField(upload_to='static/documents/')
    Data_inicial = models.DateTimeField(_('Data instalação'), auto_now_add=True, blank=True)
    Data_final = models.DateTimeField(_('Data desinstalação'), auto_now_add=True, blank=True)
    Obs = models.TextField(_('Observações'))

    # class Meta:
    #     ordering = ['Tipo']
    #     # verbose_name = "pessoa"
    #     # verbose_name_plural = "pessoas"

    def __str__(self):
        return self.Tipo + ' - ' + self.Serial