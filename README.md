# EcoSafeOS

# 🌱 EcoSafe OS

> **Sistema de Gerenciamento de Centros de Reciclagem com Créditos de Carbono**  
> Desenvolvido em Python | Terminal-based | Modular

---

## 📋 Sobre o Projeto

O **EcoSafe OS** é o núcleo (*engine*) de uma plataforma sustentável desenvolvida para gerenciar centros de reciclagem de resíduos sólidos. Por meio de um menu interativo no terminal, o sistema permite cadastrar unidades de reciclagem, registrar cargas de resíduos processados e calcular automaticamente os **créditos de carbono** gerados por cada centro — contribuindo diretamente para a rastreabilidade ambiental e a tomada de decisões sustentáveis.

Este projeto foi desenvolvido por Joao-Thees e Cvfaria

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 🏭 **Cadastrar Centro** | Registra novos centros de reciclagem com ID único |
| ♻️ **Registrar Resíduos** | Adiciona cargas de resíduos (kg) a um centro existente |
| 📊 **Relatório Ambiental** | Exibe painel completo com totais e créditos de carbono |
| 🚪 **Sair do Sistema** | Encerra a aplicação com segurança |

---

## 🧮 Lógica de Créditos de Carbono

O sistema utiliza a seguinte regra de conversão:

```
A cada 100 kg de resíduos processados → 1 crédito de carbono gerado
```

Os créditos são somados automaticamente ao saldo do centro a cada novo registro de carga.

---

## 🗂️ Estrutura de Dados

Cada centro de reciclagem é armazenado em um dicionário Python com a seguinte estrutura:

```python
centros = {
    "C01": {
        "nome": "Centro Verde Leste",
        "residuos": [120.5, 340.0, 80.0],   # histórico de cargas em kg
        "creditos": 5                          # créditos de carbono acumulados
    }
}
```

---

## 📁 Estrutura do Projeto

```
ecosafe-os/
│
├── main.py               # Ponto de entrada — menu interativo (while + match/case)
├── cadastro.py           # Função cadastrar_centro()
├── residuos.py           # Função registrar_residuos()
├── relatorio.py          # Função gerar_relatorio_ambiental()
├── dados.py              # Dicionário global de centros
└── README.md
```

> 💡 A modularização em funções garante código limpo, reutilizável e de fácil manutenção.

---

## 🖥️ Como Executar

### Pré-requisitos

- Python **3.10+** (necessário para `match/case`)

### Passos

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/ecosafe-os.git

# Acesse o diretório
cd EcoSafeOS

# Execute o sistema
python menu.py
```

---

## 🗺️ Menu Principal

```
╔══════════════════════════════════╗
║        🌱  EcoSafe OS            ║
║  Gestão de Centros de Reciclagem ║
╠══════════════════════════════════╣
║  1 - Cadastrar Centro            ║
║  2 - Registrar Resíduos          ║
║  3 - Gerar Relatório Ambiental   ║
║  0 - Sair do Sistema             ║
╚══════════════════════════════════╝
```

---

## 📸 Exemplo de Relatório Ambiental

```
══════════════════════════════════════════════════
         📊 RELATÓRIO AMBIENTAL - EcoSafe OS
══════════════════════════════════════════════════
ID: C01  |  Centro Verde Leste
  ▸ Total de resíduos processados : 540.50 kg
  ▸ Créditos de carbono gerados   : 5 crédito(s)
──────────────────────────────────────────────────
ID: C02  |  EcoPoint Zona Norte
  ▸ Total de resíduos processados : 1.230.00 kg
  ▸ Créditos de carbono gerados   : 12 crédito(s)
══════════════════════════════════════════════════
```

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Paradigma:** Programação estruturada e modular
- **Interface:** Terminal (CLI)
- **Controle de fluxo:** `while True` + `match/case`

---

## 📌 Requisitos Técnicos Implementados

- [x] Dicionário global como estrutura principal de dados
- [x] `cadastrar_centro()` — cadastro de novas unidades
- [x] `registrar_residuos()` — adição de cargas e cálculo de créditos
- [x] `gerar_relatorio_ambiental()` — painel formatado de dados
- [x] Menu interativo com `while True` e `match/case`
- [x] Lógica de créditos de carbono (100 kg = 1 crédito)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos:

1. Faça um *fork* do projeto
2. Crie uma *branch* para sua feature: `git checkout -b feature/minha-feature`
3. Faça o *commit* das suas alterações: `git commit -m 'feat: adiciona minha feature'`
4. Envie para a *branch*: `git push origin feature/minha-feature`
5. Abra um *Pull Request*

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">
  Desenvolvido com 💚 pela equipe <strong>EcoSafe</strong>
</div>
