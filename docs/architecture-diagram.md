# 🏗️ Arquitetura do Octofit Tracker

## Visão Geral da Estrutura do Projeto

```
📦 Exercicio_Gith (Repositório Principal)
│
├── 🐙 octofit-tracker/                    [NOVO - Aplicação Principal Django]
│   ├── 📂 backend/
│   │   ├── 🐍 venv/                       Virtual Environment Python
│   │   ├── ⚙️ octofit_tracker/            Projeto Django
│   │   │   ├── __init__.py
│   │   │   ├── settings.py                Configurações Django
│   │   │   ├── urls.py                    Rotas principais
│   │   │   ├── asgi.py                    Configuração ASGI
│   │   │   └── wsgi.py                    Configuração WSGI
│   │   ├── manage.py                      CLI Django
│   │   └── requirements.txt               Dependências Python
│   │
│   └── 📂 frontend/                        [FUTURO - React App]
│
└── 🌐 app/ (Flask - Legado)               [EXISTENTE - Aplicação Flask Original]
    ├── __init__.py                         Factory Flask
    ├── models.py                           Modelos de dados
    └── routes.py                           Rotas API
```

## 📊 Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────────┐
│                      OCTOFIT TRACKER APP                        │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────────┐          ┌──────────────────────┐
│   FRONTEND (Futuro)  │          │   BACKEND (Django)   │
│                      │          │                      │
│  ⚛️ React            │◄────────►│  🐍 Django 4.1.7     │
│  📱 Responsive UI    │   HTTP   │  📡 REST Framework   │
│  🎨 Modern Design    │  Request │  🔐 django-allauth   │
│                      │          │  🌐 CORS Headers     │
└──────────────────────┘          └──────────────────────┘
                                           │
                                           │ djongo
                                           ▼
                                  ┌──────────────────────┐
                                  │   DATABASE           │
                                  │                      │
                                  │  🍃 MongoDB          │
                                  │  📊 Coleções:        │
                                  │    - Users           │
                                  │    - Activities      │
                                  │    - Teams           │
                                  │    - Leaderboard     │
                                  └──────────────────────┘
```

## 🎯 Funcionalidades Planejadas

```
┌─────────────────────────────────────────────────────────────┐
│                    OCTOFIT TRACKER                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  👤 Autenticação e Perfis                                   │
│     ├── Login/Logout                                        │
│     ├── Registro de usuários                                │
│     └── Gerenciamento de perfil                             │
│                                                             │
│  📝 Registro de Atividades                                  │
│     ├── Log de treinos                                      │
│     ├── Tracking de exercícios                              │
│     └── Histórico de atividades                             │
│                                                             │
│  👥 Gestão de Equipes                                       │
│     ├── Criar equipes                                       │
│     ├── Adicionar membros                                   │
│     └── Gerenciar equipes                                   │
│                                                             │
│  🏆 Leaderboard Competitivo                                 │
│     ├── Rankings individuais                                │
│     ├── Rankings de equipes                                 │
│     └── Estatísticas                                        │
│                                                             │
│  💡 Sugestões Personalizadas                                │
│     ├── Recomendações de treinos                            │
│     ├── Metas personalizadas                                │
│     └── Insights de progresso                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 📦 Stack Tecnológico

```
┌──────────────────────────────────────────────────────────┐
│                    TECNOLOGIAS                           │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Backend Framework:                                      │
│  ├── Django 4.1.7                                        │
│  ├── Django REST Framework 3.14.0                        │
│  └── dj-rest-auth 2.2.6                                  │
│                                                          │
│  Autenticação:                                           │
│  ├── django-allauth 0.51.0                               │
│  └── PyJWT (JSON Web Tokens)                             │
│                                                          │
│  Database:                                               │
│  ├── MongoDB (via djongo 1.3.6)                          │
│  └── pymongo 3.12                                        │
│                                                          │
│  Integrações:                                            │
│  ├── django-cors-headers 4.5.0                           │
│  └── requests-oauthlib                                   │
│                                                          │
│  Frontend (Planejado):                                   │
│  └── React                                               │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## 🔄 Fluxo de Dados (Planejado)

```
   Usuario              Frontend            Backend API          MongoDB
     │                     │                     │                 │
     │──── Ação ─────────►│                     │                 │
     │                     │──── Request ───────►│                 │
     │                     │    (HTTP/JSON)      │                 │
     │                     │                     │──── Query ─────►│
     │                     │                     │                 │
     │                     │                     │◄─── Data ───────│
     │                     │◄─── Response ───────│                 │
     │◄─── Atualização ───│    (JSON)           │                 │
     │                     │                     │                 │
```

## 🚀 Status Atual

### ✅ Concluído
- [x] Estrutura de diretórios criada
- [x] Ambiente virtual Python configurado
- [x] Dependências instaladas
- [x] Projeto Django inicializado
- [x] Configuração básica do Django

### 🔨 Em Desenvolvimento
- [ ] Apps Django (users, activities, teams, leaderboard)
- [ ] Modelos de dados
- [ ] APIs REST
- [ ] Autenticação de usuários
- [ ] Frontend React

### 📋 Próximos Passos
1. Configurar MongoDB no settings.py
2. Criar apps Django para cada módulo
3. Implementar modelos de dados
4. Desenvolver APIs REST
5. Configurar autenticação
6. Iniciar desenvolvimento do frontend

---

**Versão:** 1.0  
**Data:** 17 de Novembro de 2025  
**Branch:** build-octofit-app
