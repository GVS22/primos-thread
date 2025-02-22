# Projeto Primos-Thread

Projeto desenvolvido como trabalho de aproveitamento de estudo para a disciplina de **Laboratório de Sistemas Operacionais**.  
O objetivo é demonstrar o uso integrado de **Threads**, **Docker** e **Kubernetes** para resolver um problema real de processamento paralelo.

📄 [Acesse a documentação completa (PDF)](./documentacao.pdf)

---

## 1. Introdução

Esta aplicação em Python utiliza múltiplas threads para realizar cálculos intensivos, especificamente a verificação de números primos em intervalos aleatórios. A solução foi empacotada em uma imagem Docker e pode ser orquestrada com Kubernetes, permitindo escalabilidade e balanceamento de carga.

---

## 2. Tecnologias Utilizadas

- **Python & Threads:** Implementa processamento paralelo para a verificação de números primos.
- **Docker:** Empacota a aplicação em containers, garantindo portabilidade, isolamento e facilidade de distribuição.
- **Kubernetes:** Orquestra os containers, possibilitando escalabilidade e balanceamento de carga de forma automatizada.

---

## 3. Estrutura do Projeto

- `primos-thread.py`: Script principal contendo a lógica de verificação de números primos utilizando threads.
- `Dockerfile`: Arquivo para construir a imagem Docker da aplicação.
- `kubernetes/deployment.yaml` (Opcional): Manifest para deploy no Kubernetes. Pode ser substituído pelos comandos do `kubectl`.
- `README.md`: Este arquivo, com todas as instruções para build, deploy e execução.

Repositório GitHub: [https://github.com/GVS22/primos-thread](https://github.com/GVS22/primos-thread)

---

## 4. Código Fonte

O código fonte da aplicação está em `primos-thread.py` e cria múltiplas threads para verificar a primalidade de números aleatórios.  
**Nota:** Os resultados dos cálculos de números primos são exibidos nos logs da aplicação.

---

## 5. Docker

### 5.1. Construção e Publicação da Imagem

1. **Construir a Imagem:**

   ```bash
   docker build -t gvs22/primos-thread:v4 .
