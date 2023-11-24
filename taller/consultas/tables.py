import django_tables2 as tables
from .models import Personas, Efectivo, ConfeCamaras, DeclaracionRenta, ActosNotariales, Cambiarias, Productos, RegistroROS, SeguridadSocial


class EfectivoTable(tables.Table):
    contraparte = tables.Column(accessor='id2', verbose_name='Contraparte')
    class Meta:
        model = Efectivo
        fields = ('producto','titular','fechaTransaccion','Valor_Transaccion','tipoTransaccion','nombreBanco','departamento','municipio')
        sequence = ('producto','titular','contraparte','fechaTransaccion','Valor_Transaccion','tipoTransaccion','nombreBanco','departamento','municipio')
        template_name = 'django_tables2/bootstrap4.html'


class ConfeCamarasTable(tables.Table):
    class Meta:
        model = ConfeCamaras
        fields = ('estadoMatricula', 'fechaCreacion', 'fechaRenovacionMatricula', 'fechaCancelacionMatricula', 'empresa', 'socio', 'composicion')
        template_name = 'django_tables2/bootstrap4.html'


class DeclaracionRentaTable(tables.Table):
    class Meta:
        model = DeclaracionRenta
        fields = ('anioDeclaracion', 'declarante', 'patrimonio_Bruto', 'patrimonio_Liquido', 'ingreso_Bruto', 'ingreso_Liquido', 'pasivos', 'gasto')
        template_name = 'django_tables2/bootstrap4.html'


class ActosNotarialesTable(tables.Table):
    notarias = tables.Column(accessor='escribanos', verbose_name='Notaria No.')
    class Meta:
        model = ActosNotariales
        fields = ('notarias', 'noEscritura', 'fechaEscritura', 'Valor_Transaccion', 'personaActo', 'claseTramite','calidadActo','departamento','municipio')
        template_name = 'django_tables2/bootstrap4.html'


class CambiariasTable(tables.Table):
    beneficiario_remitente = tables.Column(accessor='remitente', verbose_name='Remitente/Beneficiario')
    class Meta:
        model = Cambiarias
        fields = ('personaTransaccion','tipoTransaccion','fechaTransaccion','TransaccionValor','nombreTransaccion','paisTransaccion','paisDestino','beneficiario_remitente')
        template_name = 'django_tables2/bootstrap4.html'


class ProductosTable(tables.Table):
    class Meta:
        model = Productos
        fields = ('bancoProducto', 'producto','titularProducto','noProducto','fechaVinculacion')
        template_name = 'django_tables2/bootstrap4.html'


class RegistroROSTable(tables.Table):
    entidad_reportante = tables.Column(accessor='bancoReportante', verbose_name='EntidadReportante')
    class Meta:
        model = RegistroROS
        fields = ('entidad_reportante','codigoROS','fechaReporte','personaPrincipal','Valor_Operacion','descripcionOperacion')
        template_name = 'django_tables2/bootstrap4.html'

class SeguridadSocialTable(tables.Table):
    class Meta:
        model = SeguridadSocial
        fields = ('tipoid','idBeneficiario','nombreBeneficiario','edadBeneficiario','calidadBeneficiario','tipoIdTitular','idTitular','nombreTitular','edadTitular')
        template_name = 'django_tables2/bootstrap4.html'