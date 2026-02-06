# 📦 Sistema de Gestão de Estoque

Aplicação **fullstack** desenvolvida com **Django**, utilizando **templates server-side** para a interface web e **Django REST Framework (DRF)** para exposição de endpoints RESTful como camada adicional.

O projeto foi pensado para simular um cenário real de produção, com regras de negócio bem definidas, organização de código e possibilidade de evolução para integrações futuras (frontend moderno, mobile ou serviços externos).

---

## 🚀 Tecnologias Utilizadas

* **Python 3.11+**
* **Django 5.x**
* **Django REST Framework (DRF)**
* **SQLite** (ambiente de desenvolvimento)
* **HTML5 / CSS3** (Django Templates)

---

## 🎯 Objetivo do Projeto

Criar um sistema de gestão de estoque funcional, focado em:

* Controle de entrada e saída de produtos
* Organização e manutenção de dados
* Boas práticas de desenvolvimento com Django
* Preparação para consumo via API REST

---

## 🧩 Funcionalidades

* Cadastro de **Produtos**
* Cadastro de **Categorias**
* Cadastro de **Marcas**
* Cadastro de **Fornecedores**
* Controle automático de **estoque**
* Autenticação de usuários
* Controle de acesso por permissões
* Interface web utilizando Django Templates
* Endpoints RESTful para integração futura

---

## 🏗️ Arquitetura

O projeto utiliza uma abordagem híbrida:

* **Django Templates** para renderização server-side
* **DRF** para disponibilização de endpoints REST

Essa estratégia permite que a aplicação funcione de forma completa no modelo tradicional do Django, mas já esteja preparada para evoluir para uma arquitetura mais desacoplada.

---

## 🔌 API REST (DRF)

A API foi adicionada como um *plus*, permitindo integração com:

* Frontends modernos (React, Vue, etc.)
* Aplicações mobile
* Serviços externos

### Exemplos de recursos expostos:

* `/api/v1/produtos/`
* `/api/v1/categorias/`
* `/api/v1/marcas/`
* `/api/v1/fornecedores/`

> A documentação pode ser facilmente estendida com Swagger ou Redoc.

---

## ⚙️ Como Executar o Projeto Localmente

```bash
# Clone o repositório
git clone https://github.com/Francelmo87/estoque.git

# Acesse a pasta do projeto
cd estoque

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 🧪 Boas Práticas Aplicadas

* Regras de negócio centralizadas no backend
* Organização clara de apps, views e serializers
* Uso de ViewSets e Routers no DRF
* Código legível e preparado para manutenção

---

## 📌 Próximos Passos (Roadmap)

* Implementar testes automatizados
* Adicionar documentação interativa da API (Swagger/Redoc)
* Melhorar controle de permissões
* Criar relatórios de movimentação de estoque

---

## 👨‍💻 Autor

**Francelmo Sousa da Silva**
Desenvolvedor Python | Django

* GitHub: [https://github.com/Francelmo87](https://github.com/Francelmo87)

---

## 📄 Licença

Este projeto está sob a licença MIT.
