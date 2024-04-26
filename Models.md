# Models Django

Agora que temos um app criado, vamos criar um modelo para ele. O modelo é uma classe que representa uma tabela no banco de dados. Para criar um modelo, é necessário criar uma classe que herda de `models.Model` e definir os campos da tabela como atributos da classe.

Por exemplo, vamos criar um modelo para um blog. O modelo `Post` representa uma tabela no banco de dados que armazena os posts do blog. O modelo `Comment` representa uma tabela no banco de dados que armazena os comentários dos posts.

A estrutura fica assim:

```
blog/
    posts/
        models.py
    comments/
        models.py
```

## Criando um modelo

Vamos criar primeiro o model `Post`. Para isso, é necessário abrir o arquivo `models.py` do app `posts` e adicionar o seguinte código:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

Agora vamos entender o que cada campo faz:

- `title`: Campo do tipo `CharField` que armazena o título do post. O parâmetro `max_length` define o tamanho máximo do campo.

- `content`: Campo do tipo `TextField` que armazena o conteúdo do post.

- `created_at`: Campo do tipo `DateTimeField` que armazena a data e hora de criação do post. O parâmetro `auto_now_add=True` faz com que o campo seja preenchido automaticamente com a data e hora atuais quando o post é criado.

- `updated_at`: Campo do tipo `DateTimeField` que armazena a data e hora da última atualização do post. O parâmetro `auto_now=True` faz com que o campo seja atualizado automaticamente com a data e hora atuais sempre que o post é salvo.

- `__str__`: Método que retorna uma representação em string do objeto. Neste caso, retorna o título do post.

Agora vamos criar o model `Comment`. Para isso, é necessário abrir o arquivo `models.py` do app `comments` e adicionar o seguinte código:

```python
from django.db import models

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
```

No caso do model `Comment` temos um tipo de campo novo que é o `ForeignKey`. O campo `post` é uma chave estrangeira que relaciona o comentário ao post ao qual ele pertence. O parâmetro `on_delete=models.CASCADE` indica que se o post ao qual o comentário está relacionado for excluído, o comentário também será excluído.

Nesse caso estamos usando `on_delete=models.CASCADE` para que quando um post for excluído, todos os comentários relacionados a ele também sejam excluídos. Existem outras opções de comportamento para o parâmetro `on_delete`, como `models.SET_NULL`, `models.SET_DEFAULT`, `models.PROTECT`, entre outros.

Esses são os campos mais comuns usados em modelos do Django, mas existem outros tipos de campos disponíveis, como `IntegerField`, `FloatField`, `BooleanField`, `DateField`, `TimeField`, `EmailField`, `ImageField`, entre outros. Para saber mais sobre os tipos de campos disponíveis, consulte a [documentação oficial do Django](https://docs.djangoproject.com/en/3.2/ref/models/fields/).

## Registrando os modelos no admin

Agora que temos os modelos criados, vamos registrá-los no admin do Django para que possamos gerenciá-los através de uma interface web.

Para isso, é necessário abrir o arquivo `admin.py` do app `posts` e adicionar o seguinte código:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

E no arquivo `admin.py` do app `comments` adicionar o seguinte código:

```python
from django.contrib import admin
from .models import Comment

admin.site.register(Comment)
```

Agora, ao acessar o admin do Django em `http://localhost:8000/admin/`, você verá os modelos `Post` e `Comment` disponíveis para serem gerenciados.

## Migrando o banco de dados

Agora que temos nossos models feitos e registrados no admin, precisamos aplicar as migrações para criar as tabelas no banco de dados.

Para isso, é necessário rodar os seguintes comandos:

```powershell
python manage.py makemigrations
```

Aqui nós estamos criando as migrações, que são arquivos que contêm as alterações que serão feitas no banco de dados.

```powershell
python manage.py migrate
```

E aqui nós estamos aplicando as migrações, ou seja, fazendo as alterações no banco de dados.

Agora, se você acessar o admin do Django em `http://localhost:8000/admin/`, você verá que as tabelas `Post` e `Comment` foram criadas no banco de dados e estão disponíveis para serem gerenciadas.

Com isso, temos os modelos criados, registrados no admin e as migrações aplicadas no banco de dados. Agora podemos começar a criar as views e templates para interagir com esses modelos.
