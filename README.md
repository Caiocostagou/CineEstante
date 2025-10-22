# 🎬 CineEstante  

## 👥 Equipe
- **Nome da equipe:** [Grupo 12]  
- **Membros:**  
  - Gabriel Ricardo Araújo – Matrícula: [2024200073]  
  - Julio Cesar Coutinho Holanda Cavalcanti – Matrícula: [2025200292]  
  - Caio Costa Gouveia – Matrícula: [2024200389]  
 
---

## 🍿 Nome do Produto
**CineEstante**

---

## 🧠 Descrição do Projeto
O **Cine Estante** é um sistema social voltado para amantes do cinema.  
Os usuários podem:
- Criar um perfil personalizado com descrição e foto;
- Adicionar filmes à estante com notas e comentários;
- Marcar críticas com ou sem spoiler;
- Criar listas de filmes para assistir futuramente;
- Sugerir obras para outros usuários;
- Comentar em sagas e franquias;
- Participar de comunidades por nicho de gênero;
- Visualizar rankings e interagir com críticas.

---

## 🚀 Entrega 01  

### 📄 Documentação e Materiais

- **Documento de Histórias:** [Link para o Google Docs](https://docs.google.com/document/d/1gLsDAXkUmLZK5js7OKfs5OLxCrkXJu-9lgcbZwYkCd8/edit?tab=t.0#heading=h.ihj8dpur0xla)  
- **Backlog + Sprint (JIRA):**  
  ![Print do JIRA Backlog](https://github.com/user-attachments/assets/cbd61e64-cab9-4fc5-a786-baf156425c96)  
  ![Print do JIRA Sprint 01](https://github.com/user-attachments/assets/82e1ce61-5768-4b58-8550-4432126c0e91) 
- **Protótipos no Figma:** [Link para o Figma](https://www.figma.com/proto/3QfBXKDWDtn0uVHkLKV5XE/CineEstante-%E2%80%93-Prot%C3%B3tipo-Lo-Fi.?node-id=0-1)  
- **Screencast (YouTube):** [Link do vídeo](https://youtu.be/SKyZwryabZ8)

---

## 📦 Entrega 02

> ⚠️ **Observação:**  
> A Entrega 02 **não foi concluída integralmente**.  
> O grupo optou por prosseguir para a **Entrega 03**, mantendo o foco na continuidade e amadurecimento do sistema.

### 📊 Status da Entrega 02
- **Histórias implementadas:** Parcialmente concluídas  
- **Screencast:** Não realizado  
- **Deploy:** Não realizado  
- **JIRA:** Sprint 02 iniciada, mas não finalizada  
- **Planejamento:** Continuação na Sprint 03  

---

## 🚀 Entrega 03 — Desenvolvimento das Funcionalidades  

Nesta entrega, o grupo avançou com o desenvolvimento completo das histórias definidas no JIRA, priorizando interação social, usabilidade e novas formas de exploração de conteúdo cinematográfico.  

### 🎯 Histórias de Usuário

---

### 1. Perfil e Auto Descrição
**História:**  
Como usuário, quero criar um perfil com uma auto descrição, para personalizar minha identidade dentro da comunidade.

**Cenários de Validação:**  
- Dado que o usuário acesse a área de edição de perfil, Quando inserir seu nome, foto e descrição, Então o sistema deve salvar e exibir essas informações.  
- Dado que o usuário já tenha um perfil criado, Quando editar a descrição, Então o sistema deve atualizar e exibir a nova descrição.  
- Dado que um perfil seja público, Quando outro usuário acessar a página do perfil, Então o sistema deve exibir nome, foto e descrição.  

**Erro:**  
- Quando o nome obrigatório não for preenchido, o sistema deve exibir mensagem de erro e impedir o salvamento.

---

### 2. Adicionar Filmes à Estante
**História:**  
Como usuário, quero adicionar filmes à minha estante com avaliação e justificativa, para organizar meu histórico de filmes.

**Cenários de Validação:**  
- Adicionar filme com nota e comentário.  
- Impedir duplicação de filmes já adicionados.  

**Erro:**  
- Caso nota ou justificativa não sejam preenchidas, exibir mensagem de erro e impedir o salvamento.

---

### 3. Avaliações com ou sem Spoiler
**História:**  
Como usuário, quero avaliar filmes marcando se a crítica contém spoiler ou não, para que outros decidam se querem ler.

**Cenários de Validação:**  
- Marcar críticas com “contém spoiler” para ocultar o texto.  
- Exibir normalmente críticas sem spoiler.  
- Autor sempre visualiza o texto completo.  

**Erro:**  
- Caso o texto não seja preenchido, impedir a publicação e exibir mensagem de erro.

---

### 4. Lista de Filmes para Assistir Futuramente
**História:**  
Como usuário, quero criar uma lista de filmes que desejo assistir futuramente, para organizar minhas próximas sessões de cinema.

**Cenários de Validação:**  
- Adicionar e remover filmes da lista “Quero Assistir”.  
- Exibir lista publicamente, se configurado.  

**Erro:**  
- Caso o filme não exista no catálogo, exibir mensagem de erro e não adicionar.

---

### 5. Sugestões para Outros Usuários
**História:**  
Como usuário, quero sugerir filmes para outros usuários, para compartilhar minhas recomendações pessoais.

**Cenários de Validação:**  
- Enviar sugestões para outros usuários.  
- Visualizar e aceitar/ignorar sugestões nas notificações.  

**Erro:**  
- Caso o usuário selecionado não exista, exibir mensagem de erro e não enviar a sugestão.

---

### 6. Comentários por Saga
**História:**  
Como usuário, quero comentar em páginas de sagas ou franquias de filmes, para debater sobre séries completas.

**Cenários de Validação:**  
- Exibir comentários em páginas de sagas.  
- Permitir respostas e curtidas.  

**Erro:**  
- Texto excedendo limite deve gerar mensagem de erro e não ser salvo.

---

### 7. Ranking de Filmes Mais Bem Avaliados
**História:**  
Como usuário, quero acessar um ranking dos filmes mais bem avaliados, para descobrir os mais recomendados da comunidade.

**Cenários de Validação:**  
- Filtrar rankings por período (semana, mês, ano).  
- Recalcular médias automaticamente.  

**Erro:**  
- Exibir mensagem quando não houver dados suficientes.

---

### 8. Avaliar Críticas de Outros Usuários
**História:**  
Como usuário, quero avaliar (curtir ou reagir) críticas de outros usuários, para valorizar as melhores contribuições.

**Cenários de Validação:**  
- Curtir/descurtir críticas e atualizar contagem.  

**Erro:**  
- Caso o usuário não esteja logado, solicitar login antes da ação.

---

### 9. Comunidades por Nichos
**História:**  
Como usuário, quero participar de comunidades por gênero ou nicho de filmes, para debater com pessoas de gostos parecidos.

**Cenários de Validação:**  
- Visualizar tópicos por gênero.  
- Criar novos tópicos e denunciar conteúdos.  

**Erro:**  
- Campos obrigatórios não preenchidos devem gerar erro e impedir publicação.

---

### 10. Visualizar Meu Perfil e Estante
**História:**  
Como usuário, quero visualizar meu perfil e minha estante de filmes organizados, para acompanhar tudo que já avaliei.

**Cenários de Validação:**  
- Exibir listas e avaliações no perfil.  
- Permitir ordenação por data, nota ou título.  

**Erro:**  
- Em caso de falha de carregamento, solicitar recarregar a página.

---

### 11. Login e Cadastro
**História:**  
Como visitante do site, quero poder me cadastrar e realizar login, para acessar funcionalidades personalizadas e salvar minhas atividades.

**Cenários de Validação:**  
- Cadastro com nome, e-mail e senha.  
- Login com autenticação correta.  

---

### 12. Carrossel de Filmes em Cartas
**História:**  
Como usuário, quero visualizar um carrossel de filmes em formato de cartas, para navegar de forma interativa pelas obras em destaque.

**Cenários de Validação:**  
- Exibir carrossel com pôster, título e nota.  
- Navegar entre os filmes com setas.  
- Redirecionar ao clicar em uma carta.  

**Erro:**  
- Exibir mensagem “Não foi possível carregar os filmes em destaque” caso o sistema falhe.

---

### 13. Visualizar Trailers ao Passar o Mouse
**História:**  
Como usuário, quero visualizar trailers dos filmes em cartaz ao deixar o mouse sobre o pôster, para ter uma prévia rápida da obra.

**Cenários de Validação:**  
- Reproduzir trailer em miniatura ao passar o mouse.  
- Pausar trailer ao remover o cursor.  
- Abrir página de detalhes ao clicar.  

**Erro:**  
- Exibir “Trailer indisponível” quando o vídeo não estiver disponível.

---

## 📋 JIRA e GitHub
- **JIRA (Sprint 03):**  
  ![Sprint 03 - JIRA](https://github.com/user-attachments/assets/SEU-LINK-AQUI)

- **GitHub Issues:**  
  ![GitHub Issues](https://github.com/user-attachments/assets/SEU-LINK-AQUI)






