from django.db import models


class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=255, null=False, blank=False, verbose_name="Razão Social (*)")
    nome_fantasia = models.CharField(max_length=255, null=False, blank=False, verbose_name="Nome Fantasia (*)")
    cnpj_cpf = models.CharField(max_length=255, null=False, blank=False, verbose_name="CNPJ ou CPF (*)")
    telefone = models.CharField(max_length=255, null=False, blank=False, verbose_name="Telefone (*)")
    tipo_de_parceria = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tipo de Parceria")

    def __str__(self):
        return self.razao_social


class Empresa(models.Model):
    razao_social = models.CharField(max_length=255, null=False, blank=False, verbose_name="Razão Social (*)")
    nome_fantasia = models.CharField(max_length=255, null=False, blank=False, verbose_name="Nome Fantasia (*)")
    cnpj_cpf = models.CharField(max_length=255, null=False, blank=False, verbose_name="CNPJ ou CPF (*)")

    def __str__(self):
        return self.razao_social


class ModoDePagamento(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.descricao


class LocalRecebimento(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False, verbose_name="Título (*)")
    adm_cartao = models.CharField(max_length=255, null=False, blank=False, verbose_name="Administradora de Cartão (*)")
    bandeira_cartao = models.CharField(max_length=255, null=False, blank=False, verbose_name="Bandeira do Cartão (*)")
    modo_pagamento = models.ForeignKey(ModoDePagamento, on_delete=models.SET_NULL, null=True, blank=False,
                                       verbose_name="Modo de Pagamento (*)")

    def __str__(self):
        return self.titulo


class Venda(models.Model):
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False, verbose_name="Valor (*)")
    parcelas = models.IntegerField(null=False, blank=False, verbose_name="Parcelas (*)")
    data = models.DateField(max_length=255, null=False, blank=False, verbose_name="Data (*) EX. DD/MM/AAA")
    local_de_recebimento = models.ForeignKey(LocalRecebimento, on_delete=models.SET_NULL, null=True, blank=False,
                                             verbose_name="Local de Pagamento (*)")
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Empresa (*)")

    def __str__(self):
        return "R${} - Data:{} - Local de Recebimento:{}".format(self.valor, self.data, self.local_de_recebimento)


class TipoPagamento(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.descricao


class StatusDoPagamento(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.descricao


class Pagamento(models.Model):
    numero_documento = models.CharField(max_length=255, null=False, blank=False, verbose_name="Número de documento (*)")
    descricao = models.CharField(max_length=255, null=False, blank=False, verbose_name="Descrição do Documento (*)")
    empresa = models.ForeignKey(Empresa, on_delete='SEL_NULL', null=True, blank=False, verbose_name="Empresa (*)")
    tipo_de_pagamento = models.ForeignKey(TipoPagamento, on_delete=models.SET_NULL, null=True, blank=False,
                                          verbose_name="Tipo de Pagamento(*)")
    data_de_vencimento = models.DateField(null=False, blank=False,
                                          verbose_name="Data de Vencimento (*) EX. DD/MM/AAA")
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False, verbose_name="Valor R$ (*)")
    status_pagamento = models.ForeignKey(StatusDoPagamento, on_delete=models.SET_NULL, null=True, blank=False,
                                         verbose_name="Status do Pagamento (*)")

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=False)
    parcela = models.CharField(max_length=255, null=True, blank=True)
    competencia = models.CharField(max_length=255, null=True, blank=True)
    valor_juros = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    data_de_pagamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.descricao


class Estado(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    sigla = models.CharField(max_length=2, null=True, blank=False)


class Cidade(models.Model):
    descricao = models.CharField(max_length=255, null=True, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=False)


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255, null=False, blank=False)
    bairro = models.CharField(max_length=255, null=False, blank=False)
    cep = models.CharField(max_length=9, null=False, blank=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=False)


class Banner(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.FileField(blank=True, null=True, upload_to='banner')

    class Meta:
        managed = False
        db_table = 'banner'
