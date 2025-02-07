# Playwright DemoBlaze Bot

## 📌 Objetivo
Este projeto utiliza Playwright para automatizar a interação com o site **DemoBlaze**. O robô realiza as seguintes tarefas:

✅ Acessa o site e clica em um produto aleatório.

✅ Adiciona o produto ao carrinho e confirma a adição.

✅ Retorna à página inicial e adiciona outro produto.

✅ Valida a presença dos produtos no carrinho.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Playwright**

## 📂 Estrutura do Projeto
```
.
├── main.py                    # Script principal
├── README.md                  # Documentação do projeto
```

## 🚀 Como Executar o Projeto
### 1️⃣ Instalar dependências
Se ainda não tiver o Playwright instalado, execute:
```bash
pip install playwright
playwright install
```

### 2️⃣ Executar o script
Para rodar o robô, execute:
```bash
python main.py
```

## 🔍 Funcionamento
1. O script acessa a página inicial do **DemoBlaze**.
2. Seleciona dois produtos aleatórios.
3. Adiciona os produtos ao carrinho e confirma a adição.
4. Retorna à página inicial e repete o processo.
5. Verifica se os produtos adicionados estão no carrinho.

## 📌 Requisitos
- Python 3.10+
- Playwright

## 📝 Observações
Caso os produtos não sejam adicionados corretamente, verifique se o site **DemoBlaze** está funcionando conforme esperado.



