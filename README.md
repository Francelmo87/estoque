# 📦 Sistema de Gestão de Estoque

Aplicação **fullstack** desenvolvida com **Django**, utilizando **templates server-side** para a interface web e **Django REST Framework (DRF)** para exposição de endpoints RESTful como camada adicional.

O projeto foi pensado para simular um cenário real de produção, com regras de negócio bem definidas, organização de código e possibilidade de evolução para integrações futuras (frontend moderno, mobile ou serviços externos).

---
## 🧠 Visão Geral

Este projeto foi desenvolvido para simular um cenário real de controle de estoque, indo além de um simples CRUD.

A aplicação evoluiu ao longo do desenvolvimento, incorporando melhorias arquiteturais e tecnológicas, com foco em:

* Consistência de dados
* Organização de código
* Escalabilidade
* Preparação para produção

---
## 🐳 Arquitetura com Docker

A aplicação está totalmente containerizada, com separação clara de serviços:

* **estoque_web** → aplicação Django
* **estoque_db** → PostgreSQL 15
```
[ Cliente ]
     ↓
[ Django App (estoque_web) ]
     ↓
[ PostgreSQL (estoque_db) ]
```
✔️ Benefícios
* Ambiente padronizado
* Isolamento de serviços
* Facilidade de deploy
* Persistência de dados com volumes
---

## 🚀 Tecnologias 

* **Python 3.11+**
* **Django 5.x**
* **Django REST Framework (DRF)**
* **PostgreSQL 15** 
* **Docker & Docker Composes**
* **HTML5 / CSS3** (Django Templates)

---
## 🧩 Funcionalidades

**📊 Cadastros**
* Produtos
* Categorias
* Marcas
* Fornecedores
**📦 Controle de Estoque**
* Entrada de produtos
* Saída controlada
* Atualização automática do estoque
* Garantia de integridade dos dados
**🔐 Segurança**
* Autenticação de usuários
* Controle de permissões
**🌐 API REST**
* Endpoints estruturados com DRF
* Preparado para integrações externas

---
## 🔌 API REST (DRF)

A API foi adicionada como um *plus*, permitindo integração com:

* Frontends modernos (React, Vue, etc.)
* Aplicações mobile
* Serviços externos

**Exemplos de recursos expostos:**
```
/api/v1/produtos/
/api/v1/categorias/
/api/v1/marcas
/api/v1/fornecedores
```

---
## ⚙️ Execução com Docker
``` Bash
# Clone o repositório
git clone https://github.com/Francelmo87/estoque.git

# Acesse a pasta do projeto
cd estoque

# suba os Contaners
docker compose u --build
```

Acesse no navegador:

👉 http://localhost:8000/

---
## 🧪 Boas Práticas Aplicadas

* Separação de responsabilidades
* Regras de negócio centralizadas no backend
* Uso consistente do ORM do Django
* Estrutura modular por apps
* Uso de ViewSets e Serializers (DRF)
*Containerização da aplicação
* Uso de variáveis de ambiente

---
## 🔐 Segurança e Configuração

A aplicação utiliza variáveis de ambiente para proteger dados sensíveis:

* Credenciais do banco de dados
* Configurações críticas do sistema

Boas práticas adotadas:
* Uso de arquivo .env
* Evitar hardcode de informações sensíveis
* Preparação para múltiplos ambientes

---
## 🧠 Decisões Técnicas
🔹 Evolução da Arquitetura

O projeto foi desenvolvido de forma incremental:

**1. Monolito com Django Templates**
* Renderização server-side
* Foco nas regras de negócio
**2. Introdução do DRF**
* Criação de API REST
* Preparação para frontend desacoplado
* Possibilidade de integração com mobile e serviços externos
**3. Containerização com Docker**
* Padronização do ambiente
* Isolamento de serviços
* Uso de PostgreSQL em container

---
**🔹 Modelagem do Banco de Dados**
* Modelagem planejada previamente utilizando Whimsical
* Estrutura pensada para:
** Normalização
** Consistência
** Escalabilidade

---
**🔹 Escolha do PostgreSQL**
* Substituição do SQLite por PostgreSQL
* Melhor suporte a:
** Concorrência
** Integridade de dados
** Ambientes de produção

---
**🔹 Uso do Docker**
* Containers separados para aplicação e banco
* Uso de volumes para persistência
* Uso de healthcheck para garantir disponibilidade do banco
* Comunicação via rede interna Docker

---
**🔹 Decisão: Uso do runserver**
O uso do runserver foi mantido intencionalmente neste estágio:

* Simplicidade no ambiente de desenvolvimento
* Facilidade de testes
* Foco na lógica de negócio

📌 A substituição por um servidor WSGI está prevista como evolução natural.

---
## 🏗️ Estratégia de Deploy e Escalabilidade

A arquitetura foi planejada para evoluir para produção com:
* Gunicorn como servidor WSGI
* Nginx como reverse proxy
* Melhor controle de performance e concorrência
```
[ Cliente ]
     ↓
[ Nginx ]
     ↓
[ Gunicorn + Django ]
     ↓
[ PostgreSQL ]
```

---
## 🎯 Destaques Técnicos

Este projeto demonstra:
* Evolução arquitetural consciente
* Uso real de Docker em aplicações Django
* Integração com PostgreSQL
* Preocupação com segurança
* Organização e escalabilidade
* Conhecimento prático de DRF

---
## 💡 Considerações Finais

Este projeto representa uma base sólida para evolução em:

* Sistemas de almoxarifado
* ERPs simplificados
* APIs corporativas
* Integrações com BI e dashboards

---
## 👨‍💻 Autor
**Francelmo Sousa da Silva**
Desenvolvedor Python | Django

* GitHub: [https://github.com/Francelmo87](https://github.com/Francelmo87)

---
## 📄 Licença

Este projeto está sob a licença MIT.