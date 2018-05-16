import django_tables2 as tables
from .models import tb_Gaget
class InstrumentTables(tables.Table):
    class Meta:
        model = tb_Gaget
        attrs = {'class': 'table table-striped table-hover table-condensed'}