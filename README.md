# VisionSense – Sistema de Inspeção de Módulos de Visão para Robôs

Sistema em Python para prototipar o controle de qualidade de módulos de visão computacional da empresa fictícia **VisionSense**, usados em robôs industriais.

O programa faz:
- Cadastro de peças (módulos) com `id`, `peso`, `cor` e `comprimento`;
- Aprovação ou reprovação automática conforme critérios de qualidade;
- Organização das peças aprovadas em caixas de até 10 unidades;
- Geração de relatórios consolidados de produção e qualidade.

---

## 1. Contexto do Desafio

Na indústria 4.0, módulos de visão computacional são fundamentais para:
- inspeção automática de peças;
- navegação de robôs colaborativos;
- monitoramento em tempo real da linha de produção.

Antes de um módulo entrar em operação com algoritmos de **visão computacional e IA**, é essencial garantir que ele foi montado dentro das especificações físicas.  
Este sistema simula essa etapa de inspeção digital usando Python.

---

## 2. Regras de Qualidade

Cada peça cadastrada possui:
- **ID**: identificador único do módulo;
- **Peso (g)**;
- **Cor** da carcaça (`azul` ou `verde`);
- **Comprimento (cm)`.

Critérios para aprovação:

- Peso entre **95 g e 105 g** (inclusive);
- Cor **azul** ou **verde**;
- Comprimento entre **10 cm e 20 cm** (inclusive).

Se qualquer critério for violado, a peça é **reprovada** e o sistema registra **todos os motivos** de reprovação.

---

## 3. Funcionalidades do Sistema

Menu principal:

1. **Cadastrar nova peça**  
   - Solicita ID, peso, comprimento e cor;  
   - Aplica as regras de qualidade e informa se foi aprovada ou reprovada.

2. **Listar peças aprovadas/reprovadas**  
   - Mostra todas as peças cadastradas, separando aprovadas e reprovadas;  
   - Em cada peça reprovada, lista os motivos.

3. **Remover peça cadastrada**  
   - Remove uma peça com base no ID informado.

4. **Listar caixas fechadas**  
   - Agrupa as peças aprovadas em caixas de **10 unidades**;  
   - Exibe apenas as caixas completamente cheias;  
   - Informa se existe uma caixa em abertura (menos de 10 peças).

5. **Gerar relatório final**  
   - Total de peças cadastradas;  
   - Total de aprovadas e reprovadas;  
   - Contagem dos motivos de reprovação;  
   - Quantidade de caixas usadas, caixas fechadas e caixas em abertura.

0. **Sair**  
   - Encerra o sistema.

A interface limpa a tela a cada operação para evitar poluição visual no terminal e, após cada ação, o usuário pode pressionar **Enter** para voltar ao menu principal.

---

## 4. Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Paradigma:** Programação estruturada com funções
- **Principais recursos da linguagem:**
  - Estruturas de decisão (`if/elif/else`);
  - Laço de repetição (`while`);
  - Listas e dicionários;
  - List comprehensions;
  - Módulo `os` para limpar a tela no terminal.

---

## 5. Como Executar o Projeto

### 5.1. Pré-requisitos

- Python 3 instalado (3.8 ou superior recomendado).
- Terminal ou prompt de comando.

### 5.2. Passo a passo

1. Clone ou baixe este repositório.
2. Abra a pasta do projeto no terminal.
3. Execute:

```bash
python visionsense_inspecao_modulos.py
