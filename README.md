# Projeto mini-AVA baseado em Microsserviços

Este projeto implementa uma aplicação composta por serviços independentes que permitem gerenciar usuários, conteúdos, cursos e avaliações. A arquitetura utiliza **FastAPI** com o servidor **Uvicorn**, e a comunicação entre os serviços é baseada em APIs REST.

---

## 📦 **Serviços Disponíveis**

1. **Usuário**: Gerenciamento de registro e autenticação de usuários.
2. **Conteúdo**: CRUD para materiais didáticos.
3. **Curso**: Criação e listagem de cursos organizados.
4. **Avaliação**: Criação e gerenciamento de questionários associados a cursos.

Cada serviço opera em uma porta diferente. Siga as instruções para iniciar e interagir com cada um.

---

## 🚀 **Executando os Serviços**

1. Abra um terminal para cada serviço.
2. Navegue até a pasta correspondente ao serviço.
3. Inicie cada serviço com o comando abaixo, substituindo `<porta>` pela porta do serviço:

```bash
uvicorn main:app --reload --port <porta>
```

| Serviço      | Porta  | Comando                                   |
|--------------|--------|-------------------------------------------|
| Usuário      | 8001   | `uvicorn main:app --reload --port 8001`   |
| Conteúdo     | 8002   | `uvicorn main:app --reload --port 8002`   |
| Curso        | 8003   | `uvicorn main:app --reload --port 8003`   |
| Avaliação    | 8004   | `uvicorn main:app --reload --port 8004`   |

---

## 📝 **Operações**

### **Registro de Usuário**
Registra um novo usuário no sistema.  

**Comando PowerShell:**
```powershell
Invoke-WebRequest -Uri "http://localhost:8001/register" -Method POST `
    -Headers @{ "Content-Type" = "application/json" } `
    -Body '{"username": "user1", "password": "pass123"}'
```

---

### **Login de Usuário**
Autentica o usuário e retorna um token JWT para acesso autenticado.  

**Comando PowerShell:**
```powershell
$loginResponse = Invoke-WebRequest -Uri "http://localhost:8001/login" -Method POST `
    -Headers @{ "Content-Type" = "application/json" } `
    -Body '{"username": "user1", "password": "pass123"}'

$token = ($loginResponse.Content | ConvertFrom-Json).token
```

---

### **Criação de Conteúdo**
Cria um novo conteúdo didático no sistema.  

**Comando PowerShell:**
```powershell
Invoke-WebRequest -Uri "http://localhost:8002/content" -Method POST `
    -Headers @{ "Content-Type" = "application/json"; "Authorization" = "Bearer $token" } `
    -Body '{"title": "Aula de Python", "description": "Aula básica de Python", "url": "http://example.com"}'
```

---

### **Listagem de Conteúdo**
Lista todos os conteúdos disponíveis.  

**Comando PowerShell:**
```powershell
Invoke-WebRequest -Uri "http://localhost:8002/content" -Method GET
```

---

### **Criação de Curso**
Cria um curso utilizando conteúdos existentes.  

**Comando cURL:**
```bash
curl -X POST "http://localhost:8003/course" \
    -H "Content-Type: application/json" \
    -d '{"title": "Curso de Programação", "description": "Curso introdutório", "content_ids": [1]}'
```

---

### **Criação de Avaliação**
Cria uma avaliação associada a um curso.  

**Comando cURL:**
```bash
curl -X POST "http://localhost:8004/assessment" \
    -H "Content-Type: application/json" \
    -d '{"course_id": 1, "questions": [{"question": "O que é Python?", "answer": "Linguagem de programação"}]}'
```

---

## 📘 **Pré-requisitos**

- **Python 3.9+**
- Instalar dependências:
  ```bash
  pip install fastapi uvicorn
  ```

---

## 💡 **Contribuição**

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou novos recursos.

--- 

## 📜 **Licença**

Este projeto é distribuído sob a licença [MIT](LICENSE).

  
