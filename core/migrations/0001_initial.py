# Generated by Django 2.2.5 on 2020-01-03 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('foto', models.FileField(blank=True, null=True, upload_to='banner')),
            ],
            options={
                'db_table': 'banner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=255, verbose_name='Razão Social (*)')),
                ('nome_fantasia', models.CharField(max_length=255, verbose_name='Nome Fantasia (*)')),
                ('cnpj_cpf', models.CharField(max_length=255, verbose_name='CNPJ ou CPF (*)')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=255, verbose_name='Razão Social (*)')),
                ('nome_fantasia', models.CharField(max_length=255, verbose_name='Nome Fantasia (*)')),
                ('cnpj_cpf', models.CharField(max_length=255, verbose_name='CNPJ ou CPF (*)')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone (*)')),
                ('tipo_de_parceria', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tipo de Parceria')),
            ],
        ),
        migrations.CreateModel(
            name='LocalRecebimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título (*)')),
                ('adm_cartao', models.CharField(max_length=255, verbose_name='Administradora de Cartão (*)')),
                ('bandeira_cartao', models.CharField(max_length=255, verbose_name='Bandeira do Cartão (*)')),
            ],
        ),
        migrations.CreateModel(
            name='ModoDePagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatusDoPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor (*)')),
                ('parcelas', models.IntegerField(verbose_name='Parcelas (*)')),
                ('data', models.DateField(max_length=255, verbose_name='Data (*) EX. DD/MM/AAA')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Empresa', verbose_name='Empresa (*)')),
                ('local_de_recebimento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LocalRecebimento', verbose_name='Local de Pagamento (*)')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_documento', models.CharField(max_length=255, verbose_name='Número de documento (*)')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição do Documento (*)')),
                ('data_de_vencimento', models.DateField(verbose_name='Data de Vencimento (*) EX. DD/MM/AAA')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor R$ (*)')),
                ('parcela', models.CharField(blank=True, max_length=255, null=True)),
                ('competencia', models.CharField(blank=True, max_length=255, null=True)),
                ('valor_juros', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('data_de_pagamento', models.DateField(blank=True, null=True)),
                ('empresa', models.ForeignKey(null=True, on_delete='SEL_NULL', to='core.Empresa', verbose_name='Empresa (*)')),
                ('fornecedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Fornecedor')),
                ('status_pagamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.StatusDoPagamento', verbose_name='Status do Pagamento (*)')),
                ('tipo_de_pagamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.TipoPagamento', verbose_name='Tipo de Pagamento(*)')),
            ],
        ),
        migrations.AddField(
            model_name='localrecebimento',
            name='modo_pagamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.ModoDePagamento', verbose_name='Modo de Pagamento (*)'),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=9)),
                ('cidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Cidade')),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Estado')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Estado'),
        ),
    ]