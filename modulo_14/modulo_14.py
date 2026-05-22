import sys
import os
from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.paginator import Paginator
from django.db import models
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from django.contrib import admin
from django.test import TestCase
from django.urls import reverse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='secretkey',
        ROOT_URLCONF=__name__,
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'app',
        ],
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        },
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        }],
    )

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    class Meta:
        app_label = 'app'

    def __str__(self):
        return self.nome

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade']

def lista_produtos(request):
    busca = request.GET.get('busca', '')
    if busca:
        produtos_list = Produto.objects.filter(nome__icontains=busca).order_by('nome')
    else:
        produtos_list = Produto.objects.all().order_by('nome')

    paginator = Paginator(produtos_list, 5)
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)
    return render(request, 'lista.html', {'produtos': produtos, 'busca': busca})

def criar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'form.html', {'form': form, 'titulo': 'Cadastrar Produto'})

def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Produto'})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'confirmar_exclusao.html', {'produto': produto})

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')
    search_fields = ('nome',)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_produtos, name='lista_produtos'),
    path('novo/', criar_produto, name='criar_produto'),
    path('editar/<int:pk>/', atualizar_produto, name='atualizar_produto'),
    path('excluir/<int:pk>/', excluir_produto, name='excluir_produto'),
]

class ProdutoTestCase(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Teclado",
            descricao="Teclado Mecanico",
            preco=250.00,
            quantidade=10
        )

    def test_criacao_produto(self):
        self.assertEqual(self.produto.nome, "Teclado")
        self.assertEqual(self.produto.quantidade, 10)

    def test_view_lista_produtos(self):
        response = self.client.get(reverse('lista_produtos'))
        self.assertEqual(response.status_code, 200)

os.makedirs(os.path.join(BASE_DIR, 'templates'), exist_ok=True)

with open(os.path.join(BASE_DIR, 'templates', 'lista.html'), 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Produtos</title>
</head>
<body>
    <h1>Lista de Produtos</h1>
    <form method="GET" action="">
        <input type="text" name="busca" value="{{ busca }}" placeholder="Buscar por nome...">
        <button type="submit">Buscar</button>
    </form>
    <br>
    <a href="{% url 'criar_produto' %}">➕ Cadastrar Novo Produto</a>
    <br><br>
    <table border="1" cellpadding="5">
        <thead>
            <tr>
                <th>Nome</th>
                <th>Descrição</th>
                <th>Preço</th>
                <th>Quantidade</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            {% for produto in produtos %}
            <tr>
                <td>{{ produto.nome }}</td>
                <td>{{ produto.descricao|default:"-" }}</td>
                <td>R$ {{ produto.preco }}</td>
                <td>{{ produto.quantidade }}</td>
                <td>
                    <a href="{% url 'atualizar_produto' produto.pk %}">Editar</a> | 
                    <a href="{% url 'excluir_produto' produto.pk %}">Excluir</a>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="5">Nenhum produto encontrado.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <br>
    <div>
        {% if produtos.has_previous %}
            <a href="?page=1{% if busca %}&busca={{ busca }}{% endif %}">&laquo; Primeira</a>
            <a href="?page={{ produtos.previous_page_number }}{% if busca %}&busca={{ busca }}{% endif %}">Anterior</a>
        {% endif %}
        <span>Página {{ produtos.number }} de {{ produtos.paginator.num_pages }}</span>
        {% if produtos.has_next %}
            <a href="?page={{ produtos.next_page_number }}{% if busca %}&busca={{ busca }}{% endif %}">Próxima</a>
            <a href="?page={{ produtos.paginator.num_pages }}{% if busca %}&busca={{ busca }}{% endif %}">Última &raquo;</a>
        {% endif %}
    </div>
</body>
</html>''')

with open(os.path.join(BASE_DIR, 'templates', 'form.html'), 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{ titulo }}</title>
</head>
<body>
    <h1>{{ titulo }}</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Salvar</button>
    </form>
    <br>
    <a href="{% url 'lista_produtos' %}">Voltar para a lista</a>
</body>
</html>''')

with open(os.path.join(BASE_DIR, 'templates', 'confirmar_exclusao.html'), 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Excluir Produto</title>
</head>
<body>
    <h1>Excluir Produto</h1>
    <p>Tem a certeza que deseja eliminar o produto "{{ produto.nome }}"?</p>
    <form method="POST">
        {% csrf_token %}
        <button type="submit">Confirmar Exclusão</button>
    </form>
    <br>
    <a href="{% url 'lista_produtos' %}">Cancelar</a>
</body>
</html>''')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.extend(['migrate'])
        execute_from_command_line(sys.argv)
        sys.argv = [sys.argv[0], 'runserver']
    execute_from_command_line(sys.argv)