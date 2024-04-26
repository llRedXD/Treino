### Criando Apps com Django

## Criando um App

Agora que já sabemos como iniciar um projeto Django, vamos criar um app. Um app é uma aplicação web que faz parte de um projeto Django. Um projeto Django pode ter vários apps, cada app é responsável por uma parte da aplicação.
Por exemplo, um projeto de um blog pode ter um app para gerenciar os posts, outro app para gerenciar os comentários e outro app para gerenciar as categorias.
A estrutura nesse exemplo fica assim:

```
blog/
    posts/
    comments/
    categories/
```

Para criar um app é necessário rodar o comando abaixo:

```powershell
python manage.py startapp nome_do_app
```

se rodar o comando para iniciar o app Django mas indicando o diretório onde o app será criado, é necessário rodar o comando abaixo:

```powershell
python manage.py startapp nome_do_app .
```

Quando fizer isso, será criado um diretório com o nome do app e a seguinte estrutura:

```
nome_do_projeto/
    nome_do_app/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
```

## Entendendo a estrutura de um app

- `__init__.py`: Arquivo que indica que o diretório é um pacote Python.

- `admin.py`: Arquivo onde é possível registrar os modelos para serem gerenciados pelo Django Admin.

  - Exemplo:

  ```python
  from django.contrib import admin
  from .models import NomeDoModelo

  admin.site.register(NomeDoModelo)
  ```

  Assim, o modelo `NomeDoModelo` será gerenciado pelo Django Admin.

- `apps.py`: Arquivo onde é possível configurar o app.

  - Exemplo: Já que criamos o app `posts` dentro do projeto `blog`, o arquivo `apps.py` do app `posts` ficará assim:

  ```python
  from django.apps import AppConfig

  class PostsConfig(AppConfig):
      default_auto_field = 'django.db.models.BigAutoField'
      name = 'blog.posts'
  ```

  Onde `name` é o nome do app.

- `migrations/`: Diretório onde ficam os arquivos de migração do app.

- `models.py`: Arquivo onde ficam os modelos do app.

  - Exemplo:

  ```python
  from django.db import models

  class NomeDoModelo(models.Model):
      campo = models.CharField(max_length=100)
  ```

  Assim, o modelo `NomeDoModelo` terá um campo `campo` do tipo `CharField` com no máximo 100 caracteres.

- `tests.py`: Arquivo onde ficam os testes do app.

  - Exemplo:

  ```python
  from django.test import TestCase

  class NomeDoModeloTestCase(TestCase):
      def test_campo(self):
          modelo = NomeDoModelo(campo='valor')
          self.assertEqual(modelo.campo, 'valor')
  ```

- `views.py`: Arquivo onde ficam as views do app.

  - Exemplo:

  ```python
  from django.shortcuts import render
  from django.http import HttpResponse

  def nome_da_view(request):
      return HttpResponse('Olá, mundo!')
  ```

  Assim, a view `nome_da_view` retorna a mensagem `Olá, mundo!`.

## Registrando o app no projeto

Para que o app seja reconhecido pelo projeto, é necessário registrar o app no arquivo `settings.py` do projeto.

Para isso, é necessário adicionar o nome do app no atributo `INSTALLED_APPS` do arquivo `settings.py`.

- Exemplo:

```python
INSTALLED_APPS = [
    'blog.posts',
]
```

Assim, o app `posts` do projeto `blog` será reconhecido pelo projeto.

## Conclusão

Neste documento, aprendemos a criar um app Django. Vimos como criar um app, entendemos a estrutura de um app e aprendemos a registrar o app no projeto.
