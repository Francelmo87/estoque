# Sistema de Gestão de Estoque

O objetivo deste projeto visa ter uma gestão das entradas e saidas do estoque de uma empresa.

## Motivação

De acordo com as melhores prática administrativas é de suma importância a gestão de materiais de qualquer ente, seja privado ou público,
este sistema tem o objetivo de controlar o patrimonio bem como auxiliar na tomada de decisão quanto a que comprar é uma ferramenta de
auxilio a gestão

## Tecnologias

- Linguagem: python 3.17
- Framework: django 5.2
- Desenvolvimento: FullStack(django/bootstrap) e API REST(DRF)

 ## Características

Requisitos funcionais

* Cadastro de fornecedores, marcas, categorias, produtos entradas e saidas
* Filtros por produtos e tipo de categoria e marcas
* Aumento automaticos de Produtos quando são dadas as entradas
* Diminuição automaticos de Produtos quando são dadas as saídas
* Sistema de login para usuários do sistema – administrador, gerente, padrão,
* Controle de permissões de usuários e/ou grupo, com diferentes níveis de acesso
 * Administrador – Cadastros geral (tudo)
 * Gerente – Responsável pelas as entradas no estoque 
 * Padrão – funcionario responsável pela as saidas do estoque
 * suporte a futuras integrações/ automações

Requisitos não funcionais

* Segurança
* Desempenho	
* Escalabilidade
* Usabilidade
* Mantenabilidade
* Responsividade

Como rodar o projeto?
- Clone esse repositório.
- Crie um virtualenv com Python 3.
- Ative o virtualenv.
- Instale as dependências.
- Rode as migrações.

```
git clone https://github.com/Francelmo87/estoque.git
cd app
python3 -m venv .venv
source .venv/bin/activate 
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
 ```



