from datetime import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin

# from .form import *
from .models import *
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, View, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.db.models import Sum


class AdmBase(LoginRequiredMixin, TemplateView):
    template_name = 'adm/comuns/adm_base.html'


class Adm(LoginRequiredMixin, TemplateView):
    template_name = 'adm/comuns/adm.html'


class Cadastro(LoginRequiredMixin, TemplateView):
    template_name = 'adm/cadastro/cadastro_base.html'


class CadastroVenda(LoginRequiredMixin, CreateView):
    template_name = 'adm/cadastro/venda.html'
    model = Venda
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_venda')


class CadastroFornecedor(LoginRequiredMixin, CreateView):
    template_name = 'adm/cadastro/fornecedor.html'
    model = Fornecedor
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_fornecedor')


class CadastroEmpresa(LoginRequiredMixin, CreateView):
    template_name = 'adm/cadastro/empresa.html'
    model = Empresa
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_empresa')


class CadastroPagamento(LoginRequiredMixin, CreateView):
    template_name = 'adm/cadastro/pagamento.html'
    model = Pagamento
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_pagamento')


class CadastroLocalRecebimento(LoginRequiredMixin, CreateView):
    template_name = 'adm/cadastro/local_recebimento.html'
    model = LocalRecebimento
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_local_recebimento')


class Gerenciamento(LoginRequiredMixin, TemplateView):
    template_name = 'adm/gerenciamento/gerenciamento_base.html'


class ListaVenda(LoginRequiredMixin, ListView):
    template_name = 'adm/gerenciamento/lista/venda.html'
    model = Venda
    fields = '__all__'
    paginate_by = 2


class ListaFornecedor(LoginRequiredMixin, ListView):
    template_name = 'adm/gerenciamento/lista/fornecedor.html'
    model = Fornecedor
    fields = '__all__'
    paginate_by = 2


class ListaEmpresa(LoginRequiredMixin, ListView):
    template_name = 'adm/gerenciamento/lista/empresa.html'
    model = Empresa
    fields = '__all__'
    paginate_by = 2


class ListaPagamento(LoginRequiredMixin, ListView):
    template_name = 'adm/gerenciamento/lista/pagamento.html'
    model = Pagamento
    fields = '__all__'
    paginate_by = 2


class ListaLocalRecebimento(LoginRequiredMixin, ListView):
    template_name = 'adm/gerenciamento/lista/local_recebimento.html'
    model = LocalRecebimento
    fields = '__all__'
    paginate_by = 2


class AtualizaVenda(LoginRequiredMixin, UpdateView):
    template_name = 'adm/gerenciamento/atualiza/venda.html'
    model = Venda
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_venda')


class AtualizaFornecedor(LoginRequiredMixin, UpdateView):
    template_name = 'adm/gerenciamento/atualiza/fornecedor.html'
    model = Fornecedor
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_fornecedor')


class AtualizaEmpresa(LoginRequiredMixin, UpdateView):
    template_name = 'adm/gerenciamento/atualiza/empresa.html'
    model = Empresa
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_empresa')


class AtualizaPagamento(LoginRequiredMixin, UpdateView):
    template_name = 'adm/gerenciamento/atualiza/pagamento.html'
    model = Pagamento
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_pagamento')


class AtualizaLocalRecebimento(LoginRequiredMixin, UpdateView):
    template_name = 'adm/gerenciamento/atualiza/local_recebimento.html'
    model = LocalRecebimento
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_local_recebimento')


class DetalheVenda(LoginRequiredMixin, DetailView):
    template_name = 'adm/gerenciamento/detalhe/venda.html'
    model = Venda


class DetalheEmpresa(LoginRequiredMixin, DetailView):
    template_name = 'adm/gerenciamento/detalhe/empresa.html'
    model = Empresa


class DetalheFornecedor(LoginRequiredMixin, DetailView):
    template_name = 'adm/gerenciamento/detalhe/fornecedor.html'
    model = Fornecedor


class DetalhePagamento(LoginRequiredMixin, DetailView):
    template_name = 'adm/gerenciamento/detalhe/pagamento.html'
    model = Pagamento
    field = '__all__'


class DetalheLocalRecebimento(LoginRequiredMixin, DetailView):
    template_name = 'adm/gerenciamento/detalhe/local_recebimento.html'
    model = LocalRecebimento
    field = '__all__'


class DeletaVenda(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = 'adm/gerenciamento/deleta/venda.html'

    def get_success_url(self):
        return reverse_lazy('lista_venda')


class DeletaEmpresa(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'adm/gerenciamento/deleta/empresa.html'

    def get_success_url(self):
        return reverse_lazy('lista_empresa')


class DeletaPagamento(LoginRequiredMixin, DeleteView):
    model = Pagamento
    template_name = 'adm/gerenciamento/deleta/pagamento.html'

    def get_success_url(self):
        return reverse_lazy('lista_pagamento')


class DeletaFornecedor(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'adm/gerenciamento/deleta/fornecedor.html'

    def get_success_url(self):
        return reverse_lazy('lista_fornecedor')


class DeletaLocalRecebimento(LoginRequiredMixin, DeleteView):
    model = LocalRecebimento
    template_name = 'adm/gerenciamento/deleta/local_recebimento.html'

    def get_success_url(self):
        return reverse_lazy('lista_local_recebimento')


class Grafico(LoginRequiredMixin, TemplateView):
    template_name = 'adm/grafico/grafico_base.html'


class GraficoContaPagarReceber(LoginRequiredMixin, TemplateView):
    template_name = 'adm/grafico/grafico_conta_pagar_receber.html'

    def get_context_data(self, **kwargs):
        ctx = super(GraficoContaPagarReceber, self).get_context_data(**kwargs)
        ctx['pagar'] = Pagamento.objects.aggregate(Sum('valor'))
        ctx['receber'] = Venda.objects.aggregate(Sum('valor'))
        return ctx


class GraficoContaPagaPorEmpresa(LoginRequiredMixin, TemplateView):
    template_name = 'adm/grafico/grafico_paga_por_empresa.html'

    def get_context_data(self, **kwargs):
        ctx = super(GraficoContaPagaPorEmpresa, self).get_context_data(**kwargs)
        ctx['empresas'] = Empresa.objects.all()
        ctx['valores'] = Pagamento.objects.values('empresa_id').annotate(Sum('valor'))
        return ctx


class Relatorio(LoginRequiredMixin, TemplateView):
    template_name = 'adm/relatorio/relatorio_base.html'


class RelAPagar(LoginRequiredMixin, ListView, PDFTemplateResponseMixin):
    template_name = 'adm/relatorio/a_pagar.html'
    model = Pagamento
    fields = '__all__'


class Index(TemplateView):
    template_name = 'site/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(Index, self).get_context_data(**kwargs)
        ctx['banners'] = Banner.objects.all()
        return ctx


class Contato(TemplateView):
    template_name = 'site/contato.html'


class Parceiro(TemplateView):
    template_name = 'site/parceiro.html'


class Sistema(TemplateView):
    template_name = 'adm/sistema.html'




