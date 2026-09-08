# 🔄 Documentação de Estudo: Fluxo do Ciclo de Vida das Migrations no Django

Este guia de estudos detalha o conceito, a ordem de execução e a mecânica das **Migrations** (migrações) no Django ORM.

---

## 💡 O que é uma Migration?

Uma migration é um **controle de versão para a estrutura do banco de dados**. 
Assim como o Git gerencia o histórico e as alterações do seu código-fonte Python, as migrations registram o histórico de modificações no esquema do banco SQL (criação de tabelas, adição ou remoção de colunas, alteração de tipos de dados, etc.).

---

## 📜 A Ordem do Processo (Visão Geral)

O ciclo de vida de uma alteração no banco de dados com Django segue **sempre** estas 3 etapas em ordem rígida:

```text
 ┌───────────────────────────┐
 │  1. Alteração no Código   │ -> Você edita/cria suas classes no models.py
 └─────────────┬─────────────┘
               │
               ▼
 ┌───────────────────────────┐
 │ 2. Gerar a Migration      │ -> python manage.py makemigrations
 │    (Cria o Arquivo .py)   │    (Escreve o código Python na pasta migrations/)
 └─────────────┬─────────────┘
               │
               ▼
 ┌───────────────────────────┐
 │ 3. Executar a Migration   │ -> python manage.py migrate
 │    (Altera o Banco SQL)   │    (Traduz o Python para SQL e cria/altera as tabelas)
 └───────────────────────────┘