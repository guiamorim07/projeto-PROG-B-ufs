# 📚 Documentação de Estudo: Script de Seed no Django

Este arquivo serve como guia de estudos para entender a arquitetura, a lógica de execução e a motivação do uso de scripts de povoamento (**seeds**) via **Custom Management Commands** no Django.

---

## 📂 Por que a pasta `management/commands/`?

O Django utiliza a convenção de **Localização de Comandos (Command Discovery)**:

1. Quando você executa `python manage.py <nome_do_comando>`, a central do Django varre a lista de aplicações no `INSTALLED_APPS` em busca de uma estrutura de pacotes específica.
2. O caminho deve ser obrigatoriamente: `seu_app/management/commands/`.
3. Todo arquivo com extensão `.py` criado dentro de `commands/` (exceto `__init__.py`) torna-se automaticamente um comando executável no terminal.

> ⚠️ **Atenção:** Arquivos de documentação colocados dentro desta pasta devem usar extensões como `.md` ou `.txt`. Se você salvar anotações em um arquivo `.py`, o Django tentará executá-lo como um comando de terminal e retornará um erro.

---

## 🔄 Fluxo de Execução da Seed

O script de povoamento executa de forma **sequencial (de cima para baixo)** dividida em três fases bem definidas:

```text
  [ Terminal ]  --->  python manage.py seed_dados
                                │
                                ▼
  ┌────────────────────────────────────────────────────────┐
  │ FASE A: LIMPEZA DO BANCO                               │
  │ • Apaga registros antigos na ORDEM INVERSA das         │
  │   chaves estrangeiras (Laudo -> Exame -> Paciente)     │
  └─────────────────────────────┬──────────────────────────┘
                                │
                                ▼
  ┌────────────────────────────────────────────────────────┐
  │ FASE B: ENTIDADES INDEPENDENTES                        │
  │ • Instancia registros sem dependências (Paciente,      │
  │   Medico, StatusMedicao, TemplateLaudo)                │
  └─────────────────────────────┬──────────────────────────┘
                                │
                                ▼
  ┌────────────────────────────────────────────────────────┐
  │ FASE C: ENTIDADES CONECTADAS                           │
  │ • Instancia modelos com Foreign Keys usando as         │
  │   variáveis instanciadas na Fase B (Exame, Medicao,    │
  │