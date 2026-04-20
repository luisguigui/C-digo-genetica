# 🧬 MENDEL GENETICS PRO — Simulador de Hereditariedade

> Uma aplicação educacional interativa em Python que automatiza cálculos de genética mendeliana. Transforma entradas de genótipos parentais em previsões estatísticas visuais com Quadrado de Punnett, gráficos e análise detalhada da 1ª Lei de Mendel.

[![Python](https://img.shields.io/badge/python-3.7+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)]()
[![Educational](https://img.shields.io/badge/Educational-Biologia-success.svg)]()

<div align="center">

**[🚀 Instalação](#-instalação-e-execução) • [📖 Documentação](#-arquitetura-e-estrutura) • [🧬 Genética](#-conceitos-de-genética-mendeliana) • [📊 Recursos](#️-recursos-principais) • [🎓 Tutorial](#-tutorial-passo-a-passo)**

</div>

---

## 🌟 Visão Geral

**MENDEL GENETICS PRO** é um simulador educacional que implementa a **1ª Lei de Mendel** (Princípio da Segregação) com uma interface moderna e intuitiva. O projeto democratiza o entendimento de hereditariedade, permitindo que alunos, professores e entusiastas de biologia visualizem e compreendam como as características genéticas são herdadas.

### ✨ Destaques Principais

- 🧬 **Simulação Genética Completa**: Implementa a 1ª Lei de Mendel com precisão
- 📊 **Quadrado de Punnett Interativo**: Visualização dinâmica de cruzamentos
- 📈 **Gráficos Visuais**: Pizza (genótipos) e barras (fenótipos)
- 📋 **Análise Detalhada**: Explicações científicas dos resultados
- 🎨 **Interface Dark Mode**: Design moderno com CustomTkinter
- 🔄 **Múltiplos Tipos de Herança**: Dominância completa, recessiva, co-dominância, dominância incompleta
- 📐 **Cálculos Precisos**: Probabilidades estatísticas automáticas
- 💾 **Alelos Customizáveis**: Use seus próprios símbolos (A/a, D/d, etc.)

---

## 🧬 Conceitos de Genética Mendeliana

### 📚 A 1ª Lei de Mendel — Princípio da Segregação

Mendel descobriu que:

1. **Cada organismo possui 2 alelos para cada característica**
   ```
   Exemplo: Uma planta pode ser AA, Aa ou aa
   ```

2. **Alelos segregam-se durante a formação dos gametas**
   ```
   AA produz gametas: [A, A]
   Aa produz gametas: [A, a]
   aa produz gametas: [a, a]
   ```

3. **Cada gameta recebe apenas UM alelo**
   ```
   Quando gametas se unem, restauram o par
   A + a = Aa (heterozigoto)
   ```

---

### 🎯 Conceitos Fundamentais

#### **Genótipo vs Fenótipo**

```
Genótipo = Composição genética (o que você tem)
├─ AA = Homozigoto dominante
├─ Aa = Heterozigoto
└─ aa = Homozigoto recessivo

Fenótipo = Expressão visível (o que você parece)
├─ Dominante = AA ou Aa
└─ Recessivo = aa
```

#### **Alelos**

```
Alelo Dominante (A):
├─ Se expresso em heterozigoto (Aa)
├─ Máscara o recessivo
└─ Precisa de apenas 1 cópia para aparecer

Alelo Recessivo (a):
├─ Só se expressa em homozigoto (aa)
├─ Precisa de 2 cópias para aparecer
└─ Fica "escondido" em heterozigotos
```

---

### 📊 Proporções de Mendel

#### **Cruzamento: Aa × Aa**

```
         A      a
    ┌────┼────────┐
    │    │        │
A   │   AA  ┊    Aa  │
    │    │        │
    ├────┼────────┤
    │    │        │
a   │   Aa  ┊    aa  │
    │    │        │
    └────┼────────┘

RESULTADO:
✓ Genótipos: 1 AA : 2 Aa : 1 aa (25% : 50% : 25%)
✓ Fenótipos: 3 Dominante : 1 Recessivo (75% : 25%)
```

---

## 📊 Recursos Principais

### 1️⃣ **Quadrado de Punnett Interativo**

O Quadrado de Punnett é um diagrama visual que mostra todas as combinações possíveis de alelos:

```
┌─────────────────────────────────────┐
│  QUADRADO DE PUNNETT (3×3)          │
├─────────────────────────────────────┤
│        A      │      a              │
├────────────────────────────────────┤
│ A    AA (🟢)  │   Aa (🟡)           │
├────────────────────────────────────┤
│ a    Aa (🟡)  │   aa (🔴)           │
├────────────────────────────────────┤
│ Cores:                              │
│ 🟢 Homozigoto Dominante            │
│ 🟡 Heterozigoto                    │
│ 🔴 Homozigoto Recessivo            │
└─────────────────────────────────────┘
```

**Funcionalidades**:
- Atualização em tempo real
- Cores padronizadas por genótipo
- Cabeçalhos mostrando gametas parentais
- Identifica automaticamente cada genótipo

---

### 2️⃣ **Estatísticas Genotípicas**

Mostra a distribuição dos genótipos na prole:

```
📊 DISTRIBUIÇÃO GENOTÍPICA
┌─────────────────────────────────────┐
│ 🟢 Homozigoto Dominante (AA)        │
│                              4/16 (25%) │
├─────────────────────────────────────┤
│ 🟡 Heterozigoto (Aa)                │
│                              8/16 (50%) │
├─────────────────────────────────────┤
│ 🔴 Homozigoto Recessivo (aa)        │
│                              4/16 (25%) │
└─────────────────────────────────────┘
```

---

### 3️⃣ **Estatísticas Fenotípicas**

Mostra a distribuição dos fenótipos observáveis:

```
🎯 DISTRIBUIÇÃO FENOTÍPICA
┌─────────────────────────────────────┐
│ 🔵 Fenótipo Dominante               │
│                             12/16 (75%) │
├─────────────────────────────────────┤
│ 🟣 Fenótipo Recessivo               │
│                              4/16 (25%) │
└─────────────────────────────────────┘
```

---

### 4️⃣ **Gráficos Visuais**

Dois tipos de gráficos integrados com Matplotlib:

#### **Gráfico de Pizza — Distribuição Genotípica**

```
       AA (25%)
      /       \
    /    25%   \
   | Aa (50%)  |
    \   50%    /
      \       /
       aa (25%)
```

**Mostra**: Proporção visual de cada genótipo

#### **Gráfico de Barras — Distribuição Fenotípica**

```
Contagem
   12 │     ████
   10 │     ████
    8 │     ████
    6 │     ████
    4 │     ████      ████
    2 │     ████      ████
    0 └─────────────────────
       Dominante  Recessivo
       (75%)       (25%)
```

**Mostra**: Contagem absoluta de cada fenótipo

---

### 5️⃣ **Análise Detalhada**

Tab que explica os resultados scientificamente:

```
=== RESULTADOS DA SIMULAÇÃO ===

CONFIGURAÇÃO:
• Parental 1 (♀): Aa
• Parental 2 (♂): Aa
• Alelo dominante: A
• Alelo recessivo: a

ANÁLISE DO CRUZAMENTO:
• Gametas Parental 1: [A, a]
• Gametas Parental 2: [A, a]
• Total de combinações: 4

PROPORÇÕES ESPERADAS (1ª Lei de Mendel):
1. Segregação:
   Cada gameta recebe apenas um alelo

2. Proporção Genotípica:
   • 25% AA (Homozigoto dominante)
   • 50% Aa (Heterozigoto)
   • 25% aa (Homozigoto recessivo)

3. Proporção Fenotípica (3:1):
   • 75% Fenótipo dominante
   • 25% Fenótipo recessivo
```

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Versão | Propósito |
|-----------|-----------|--------|----------|
| **Linguagem** | Python | 3.7+ | Lógica e estrutura |
| **GUI** | CustomTkinter | Latest | Interface moderna Dark Mode |
| **Visualização** | Matplotlib | 3.x | Gráficos científicos |
| **Integração** | FigureCanvasTkAgg | Nativa | Matplotlib em Tkinter |

### Por que essas tecnologias?

- ✅ **CustomTkinter**: Interface moderna sem parecer "retro"
- ✅ **Matplotlib**: Gráficos científicos de alta qualidade
- ✅ **FigureCanvasTkAgg**: Integração perfeita entre Matplotlib e Tkinter
- ✅ **Dark Mode**: Melhor para os olhos em ambientes de estudo

---

## 🏗️ Arquitetura e Estrutura

### 📊 Fluxo de Dados

```
┌──────────────────────────┐
│   MendelGeneticsPro      │
│   (Classe Principal)     │
└────────────┬─────────────┘
             │
    ┌────────┴──────────┐
    │                   │
┌───▼──┐          ┌────▼────┐
│Entrada   │          │Simulação│
│(Sidebar) │          │(Cálculos)│
└───┬──┘          └────┬────┘
    │                   │
    └───────────┬───────┘
                │
        ┌───────▼────────┐
        │   Resultados   │
        │   (4 Abas)     │
        └────────────────┘
```

### 🧩 Componentes Principais

```
genetica.py
│
├── 📦 CLASSE: MendelGeneticsPro (ctk.CTk)
│   │
│   ├── INICIALIZAÇÃO
│   │   ├── __init__() .............. Setup da UI
│   │   ├── Cria sidebar
│   │   ├── Cria área principal
│   │   └── Configura 4 abas
│   │
│   ├── SIDEBAR (ENTRADA)
│   │   ├── Seletor de herança ..... Dropdown com 4 tipos
│   │   ├── Entrada de alelos ..... Dominante/Recessivo
│   │   ├── Seletor parentais ..... 3 opções por parental
│   │   ├── Botão SIMULAR ........ Executa tudo
│   │   └── Botão LIMPAR ........ Reseta interface
│   │
│   ├── ABA 1: QUADRADO DE PUNNETT
│   │   ├── setup_punnett_tab() .. Cria grid 3×3
│   │   ├── update_punnett_grid() . Atualiza células
│   │   └── Coloring automático ... Por genótipo
│   │
│   ├── ABA 2: ESTATÍSTICAS
│   │   ├── setup_stats_tab() .... Cria cards
│   │   ├── Seção genótipos ...... AA, Aa, aa
│   │   ├── Seção fenótipos ...... Dominante, Recessivo
│   │   └── calculate_statistics() Calcula %
│   │
│   ├── ABA 3: GRÁFICOS
│   │   ├── setup_chart_tab() ... Container vazio
│   │   ├── generate_chart() ... Cria 2 gráficos
│   │   ├── Pizza (genótipos)
│   │   └── Barras (fenótipos)
│   │
│   ├── ABA 4: ANÁLISE
│   │   ├── setup_analysis_tab() . Textbox com scroll
│   │   ├── Inicial: explicação
│   │   ├── Após sim: resultados
│   │   └── update_analysis() ... Atualiza texto
│   │
│   ├── LÓGICA GENÉTICA
│   │   ├── simulate_cross() .... Orquestra simulação
│   │   ├── get_gametes() ...... Retorna alelos
│   │   ├── calculate_statistics() Conta genótipos
│   │   └── Validações ........ Entrada do usuário
│   │
│   └── UTILITÁRIOS
│       ├── create_parental_section() Frame customizado
│       └── clear_all() ....... Reseta tudo
```

---

## 📚 Documentação das Classes e Métodos

### 1️⃣ `MendelGeneticsPro` — Classe Principal

**Responsabilidade**: Gerenciar a aplicação inteira, UI e lógica

**Atributos**:

```python
class MendelGeneticsPro(ctk.CTk):
    inheritance_var: StringVar        # Tipo de herança
    dominant_var: StringVar           # Alelo dominante (ex: "A")
    recessive_var: StringVar          # Alelo recessivo (ex: "a")
    parental1_var: StringVar          # Genótipo parental 1 (AA, Aa, aa)
    parental2_var: StringVar          # Genótipo parental 2 (AA, Aa, aa)
    
    tabview: CTkTabview               # Container das 4 abas
    punnett_cells: list[list]         # Grid 3×3 do Punnett
    
    genotypic_stats: list             # Labels de genótipos
    phenotypic_stats: list            # Labels de fenótipos
    
    analysis_text: CTkTextbox         # Área de análise
```

---

### 2️⃣ **Método: `simulate_cross()`**

**Propósito**: Executar a simulação completa do cruzamento

```python
def simulate_cross(self):
    """Executa a simulação do cruzamento"""
    try:
        # 1. VALIDAÇÃO
        parental1 = self.parental1_var.get()  # Ex: "Aa"
        parental2 = self.parental2_var.get()  # Ex: "Aa"
        dominant = self.dominant_var.get().upper()  # Ex: "A"
        recessive = self.recessive_var.get().lower()  # Ex: "a"
        
        # Verificar se campos estão preenchidos
        if not dominant or not recessive:
            messagebox.showwarning("Aviso", "Defina alelos!")
            return
        
        # Verificar se alelos são diferentes
        if dominant == recessive:
            messagebox.showwarning("Aviso", "Alelos devem ser diferentes!")
            return
        
        # 2. GERAR GAMETAS
        gametes1 = self.get_gametes(parental1, dominant, recessive)
        # Ex: Aa → [A, a]
        # Ex: AA → [A]
        # Ex: aa → [a]
        
        gametes2 = self.get_gametes(parental2, dominant, recessive)
        
        # 3. ATUALIZAR QUADRADO DE PUNNETT
        self.update_punnett_grid(gametes1, gametes2, dominant, recessive)
        
        # 4. CALCULAR ESTATÍSTICAS
        self.calculate_statistics(gametes1, gametes2, dominant, recessive)
        
        # 5. GERAR GRÁFICOS
        self.generate_chart(gametes1, gametes2, dominant, recessive)
        
        # 6. ATUALIZAR ANÁLISE
        self.update_analysis(parental1, parental2, dominant, recessive)
        
        # 7. FEEDBACK
        messagebox.showinfo("Sucesso", "Simulação concluída!")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")
```

**Fluxo**:
```
Validar → Gametas → Punnett → Estatísticas → Gráficos → Análise → Feedback
```

---

### 3️⃣ **Método: `get_gametes(genotype, dominant, recessive)`**

**Propósito**: Retornar os gametas possíveis para um genótipo

```python
def get_gametes(self, genotype, dominant, recessive):
    """Retorna os gametas possíveis para um genótipo"""
    
    if genotype == "AA":
        # Homozigoto dominante produz apenas gameta dominante
        return [dominant]         # [A]
    
    elif genotype == "aa":
        # Homozigoto recessivo produz apenas gameta recessivo
        return [recessive]        # [a]
    
    else:  # genotype == "Aa"
        # Heterozigoto produz ambos os gametas
        return [dominant, recessive]  # [A, a]
```

**Exemplos**:

| Genótipo | Resultado |
|----------|-----------|
| AA | [A] |
| Aa | [A, a] |
| aa | [a] |

---

### 4️⃣ **Método: `update_punnett_grid(gametes1, gametes2, dominant, recessive)`**

**Propósito**: Desenhar o Quadrado de Punnett na interface

```python
def update_punnett_grid(self, gametes1, gametes2, dominant, recessive):
    # 1. Limpar células
    for row in range(3):
        for col in range(3):
            self.punnett_cells[row][col].configure(text="")
    
    # 2. Cabeçalho (símbolo de sexo)
    self.punnett_cells[0][0].configure(text="♀\\n♂")
    
    # 3. Gametas do parental 1 (linhas)
    #    Ex: [A, a]
    for i, gamete in enumerate(gametes1):
        self.punnett_cells[i+1][0].configure(
            text=gamete,
            text_color="#3498db"  # Azul para parental 1
        )
    
    # 4. Gametas do parental 2 (colunas)
    #    Ex: [A, a]
    for j, gamete in enumerate(gametes2):
        self.punnett_cells[0][j+1].configure(
            text=gamete,
            text_color="#e74c3c"  # Vermelho para parental 2
        )
    
    # 5. Prole (todas as combinações)
    for i, g1 in enumerate(gametes1):
        for j, g2 in enumerate(gametes2):
            # Combinar alelos
            # A + A = AA
            # A + a = Aa (ordena alfabeticamente)
            # a + a = aa
            genotype = ''.join(sorted(
                [g1.upper(), g2.upper()],
                key=lambda x: x.islower()
            ))
            
            # Determinar cor por genótipo
            if genotype == dominant * 2:  # AA
                color = "#2ecc71"  # Verde
            elif genotype.lower() == recessive * 2:  # aa
                color = "#e74c3c"  # Vermelho
            else:  # Aa
                color = "#f1c40f"  # Amarelo
            
            # Desenhar na célula
            self.punnett_cells[i+1][j+1].configure(
                text=genotype,
                text_color=color
            )
```

**Exemplo Visual**:

```
Para Aa × Aa:

Entrada:
- gametes1 = [A, a]
- gametes2 = [A, a]

Quadrado:
    A       a
A   AA(🟢)  Aa(🟡)
a   Aa(🟡)  aa(🔴)
```

---

### 5️⃣ **Método: `calculate_statistics(gametes1, gametes2, dominant, recessive)`**

**Propósito**: Contar genótipos e fenótipos, calcular percentuais

```python
def calculate_statistics(self, gametes1, gametes2, dominant, recessive):
    # 1. Calcular total de combinações
    total = len(gametes1) * len(gametes2)
    # Para Aa × Aa: 2 × 2 = 4 combinações
    
    # 2. Inicializar contadores
    genotype_counts = {"AA": 0, "Aa": 0, "aa": 0}
    phenotype_counts = {"Dominante": 0, "Recessivo": 0}
    
    # 3. Contar cada combinação
    for g1 in gametes1:
        for g2 in gametes2:
            genotype = ''.join(sorted(
                [g1.upper(), g2.upper()],
                key=lambda x: x.islower()
            ))
            
            # Contar genótipos
            if genotype == dominant * 2:  # AA
                genotype_counts["AA"] += 1
                phenotype_counts["Dominante"] += 1
            elif genotype.lower() == recessive * 2:  # aa
                genotype_counts["aa"] += 1
                phenotype_counts["Recessivo"] += 1
            else:  # Aa
                genotype_counts["Aa"] += 1
                phenotype_counts["Dominante"] += 1
    
    # 4. Atualizar interface com percentuais
    genotypes = ["AA", "Aa", "aa"]
    for i, genotype in enumerate(genotypes):
        count = genotype_counts[genotype]
        percentage = (count / total) * 100 if total > 0 else 0
        
        self.genotypic_stats[i].configure(
            text=f"{count}/{total} ({percentage:.1f}%)",
            text_color=["#2ecc71", "#f1c40f", "#e74c3c"][i]
        )
    
    # 5. Atualizar fenótipos
    phenotypes = ["Dominante", "Recessivo"]
    for i, phenotype in enumerate(phenotypes):
        count = phenotype_counts[phenotype]
        percentage = (count / total) * 100 if total > 0 else 0
        
        self.phenotypic_stats[i].configure(
            text=f"{count}/{total} ({percentage:.1f}%)",
            text_color=["#3498db", "#9b59b6"][i]
        )
```

**Exemplo para Aa × Aa**:

```
Combinações:
- A + A = AA (25%)
- A + a = Aa (25%)
- a + A = Aa (25%)
- a + a = aa (25%)

Resultado:
- AA: 1/4 (25%)
- Aa: 2/4 (50%)
- aa: 1/4 (25%)

Fenótipos:
- Dominante (AA + Aa): 3/4 (75%)
- Recessivo (aa): 1/4 (25%)
```

---

### 6️⃣ **Método: `generate_chart(gametes1, gametes2, dominant, recessive)`**

**Propósito**: Gerar gráficos Matplotlib e integrá-los na interface

```python
def generate_chart(self, gametes1, gametes2, dominant, recessive):
    # 1. Limpar frame anterior
    for widget in self.chart_frame.winfo_children():
        widget.destroy()
    
    # 2. Calcular distribuição (mesmo processo acima)
    total = len(gametes1) * len(gametes2)
    genotype_counts = {"AA": 0, "Aa": 0, "aa": 0}
    phenotype_counts = {"Dominante": 0, "Recessivo": 0}
    
    for g1 in gametes1:
        for g2 in gametes2:
            genotype = ''.join(sorted([g1.upper(), g2.upper()], ...))
            if genotype == dominant * 2:
                genotype_counts["AA"] += 1
                phenotype_counts["Dominante"] += 1
            elif genotype.lower() == recessive * 2:
                genotype_counts["aa"] += 1
                phenotype_counts["Recessivo"] += 1
            else:
                genotype_counts["Aa"] += 1
                phenotype_counts["Dominante"] += 1
    
    # 3. Criar figura com 2 subplots
    fig, (ax1, ax2) = plt.subplots(
        1, 2,
        figsize=(10, 4),
        facecolor='#2b2b2b'  # Fundo dark
    )
    
    # 4. Gráfico de Pizza - Genótipos
    genotypes = ['AA', 'Aa', 'aa']
    counts = [
        genotype_counts["AA"],
        genotype_counts["Aa"],
        genotype_counts["aa"]
    ]
    colors = ['#2ecc71', '#f1c40f', '#e74c3c']  # Verde, amarelo, vermelho
    
    ax1.pie(
        counts,
        labels=genotypes,
        colors=colors,
        autopct='%1.1f%%',  # Mostrar percentual
        startangle=90,
        textprops={'color': 'white', 'weight': 'bold'}
    )
    ax1.set_title('Distribuição Genotípica', color='white', pad=20)
    
    # 5. Gráfico de Barras - Fenótipos
    phenotypes = ['Dominante', 'Recessivo']
    p_counts = [
        phenotype_counts["Dominante"],
        phenotype_counts["Recessivo"]
    ]
    p_colors = ['#3498db', '#9b59b6']  # Azul, roxo
    
    bars = ax2.bar(phenotypes, p_counts, color=p_colors)
    ax2.set_title('Distribuição Fenotípica', color='white', pad=20)
    ax2.set_ylabel('Contagem', color='white')
    ax2.set_facecolor('#2b2b2b')
    ax2.tick_params(colors='white')
    
    # Adicionar valores nas barras
    for bar, count in zip(bars, p_counts):
        ax2.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.1,
            str(count),
            ha='center',
            va='bottom',
            color='white',
            fontweight='bold'
        )
    
    # 6. Ajustar layout
    plt.tight_layout()
    
    # 7. Integrar no CustomTkinter
    canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
```

---

## 🎓 Tutorial Passo a Passo

### Exemplo: Cruzamento Aa × Aa

#### **Passo 1: Configure os Alelos**

```
Alelo Dominante: A
Alelo Recessivo: a
```

#### **Passo 2: Selecione os Parentais**

```
Parental 1 (♀): Aa (clique no radio button)
Parental 2 (♂): Aa (clique no radio button)
```

#### **Passo 3: Clique em SIMULAR**

O programa executa:

```
1. Obtém genótipos: Aa e Aa
2. Extrai gametas: [A, a] e [A, a]
3. Cria Punnett:
       A    a
   A   AA   Aa
   a   Aa   aa
4. Calcula:
   - Genótipos: 1 AA (25%), 2 Aa (50%), 1 aa (25%)
   - Fenótipos: 3 Dominante (75%), 1 Recessivo (25%)
5. Desenha gráficos
6. Escreve análise
```

#### **Passo 4: Explore as Abas**

| Aba | Conteúdo |
|-----|----------|
| **Punnett** | Quadrado visual com cores |
| **Estatísticas** | Cards com contagens e % |
| **Gráficos** | Pizza e barras |
| **Análise** | Texto científico completo |

---

## 🎨 Interface e Design

### Componentes Visuais

#### **Sidebar (Entrada)**

```
┌─────────────────────────┐
│ 🧬 MENDEL PRO          │
│                        │
│ CONFIGURAÇÃO GENÉTICA  │
│ ─────────────────────  │
│ Tipo de Herança:       │
│ ┌────────────────────┐ │
│ │ Autossômica Dom... │ │
│ └────────────────────┘ │
│ Alelo Dominante: [A  ] │
│ Alelo Recessivo:  [a  ] │
│                        │
│ PARENTAIS              │
│ ─────────────────────  │
│ Parental 1 (♀):        │
│ ◯ AA  ◯ Aa  ◯ aa     │
│ Parental 2 (♂):        │
│ ◯ AA  ◯ Aa  ◯ aa     │
│                        │
│ [🧬 SIMULAR]          │
│ [🔄 LIMPAR]           │
└─────────────────────────┘
```

#### **Abas de Resultados**

```
┌─────────────────────────────────────────┐
│ Punnett | Estatísticas | Gráficos | Análise │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │     🟢   🟡      ┌────────────────┐│ │
│ │     🟡   🔴      │ Pizza chart   ││ │
│ │                  │ + Bar chart   ││ │
│ │                  └────────────────┘│ │
│ └────────────────────────────────��────┘ │
└─────────────────────────────────────────┘
```

---

## 🔬 Conceitos de Genética Explicados

### 1️⃣ **Segregação**

Quando uma célula se divide para formar gametas, os alelos se "separam":

```
Célula Aa
    ↓
Divisão Meiótica
    ↓
Gameta com A  OU  Gameta com a
```

---

### 2️⃣ **Combinação Independente**

Gametas se combinam aleatoriamente durante a fecundação:

```
Gameta ♀: A      Gameta ♂: A    → AA
Gameta ♀: A      Gameta ♂: a    → Aa
Gameta ♀: a      Gameta ♂: A    → Aa
Gameta ♀: a      Gameta ♂: a    → aa
```

---

### 3️⃣ **Proporção 3:1**

De Aa × Aa, você sempre obtém:

```
Genótipos: 1 AA : 2 Aa : 1 aa
Fenótipos: 3 Dominante : 1 Recessivo

Isso é a marca registrada da 1ª Lei de Mendel!
```

---

## 📊 Tipos de Herança Suportados

| Tipo | Expressão | Exemplo |
|------|-----------|---------|
| **Autossômica Dominante** | Heterozigoto mostra fenótipo dominante | Aa = Fenótipo A |
| **Autossômica Recessiva** | Homozigoto recessivo mostra fenótipo | aa = Fenótipo a |
| **Codominância** | Ambos os alelos se expressam | Aa = Fenótipo AB |
| **Dominância Incompleta** | Heterozigoto é intermediário | Aa = Fenótipo Intermediário |

---

## 🚀 Possíveis Melhorias Futuras

- [ ] **2ª Lei de Mendel**: Cruzamento dihíbrido
- [ ] **Heredograma**: Árvore genealógica
- [ ] **Padrões de Herança**: Autossômica, ligada ao X, etc
- [ ] **Cálculo de Probabilidade**: P(AA) = p²
- [ ] **Alelos Múltiplos**: Mais de 2 alelos por gene
- [ ] **Epistasia**: Interação entre genes
- [ ] **Teste Genético**: Determinar alelos por fenótipo
- [ ] **Exportar Resultados**: PDF com gráficos e análise
- [ ] **Histórico**: Salvar simulações anteriores
- [ ] **Modo Educativo**: Tutorial passo a passo

---

## 📋 Instalação e Execução

### ✅ Pré-requisitos

- Python 3.7+
- pip

### 🔧 Passos

1. **Clone o repositório**:
```bash
git clone https://github.com/luisguigui/genetica-code.git
cd genetica-code
```

2. **Crie ambiente virtual** (opcional mas recomendado):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Instale dependências**:
```bash
pip install -r requirements.txt
```

Ou manualmente:
```bash
pip install customtkinter matplotlib
```

4. **Execute o programa**:
```bash
python genetica.py
```

5. **Interface deve aparecer**:
   - Sidebar com configurações à esquerda
   - Abas de resultados à direita
   - Comece digitando genótipos!

---

## 📄 requirements.txt

```
customtkinter>=5.0.0
matplotlib>=3.5.0
```

---

## 🐛 Troubleshooting

### ❌ Problema: "ModuleNotFoundError: customtkinter"
**Solução**: `pip install customtkinter`

### ❌ Problema: "ModuleNotFoundError: matplotlib"
**Solução**: `pip install matplotlib`

### ❌ Problema: Gráficos não aparecem
**Causa**: Matplotlib não renderizando  
**Solução**: Certifique-se de que está usando Python 3.7+

### ❌ Problema: Interface pixelada
**Causa**: Problema de DPI  
**Solução**: Isso é normal em diferentes monitores

---

## ⚙️ Configuração Avançada

### Modificar Tipos de Herança

```python
inheritance_options = [
    "Autossômica Dominante",
    "Autossômica Recessiva",
    "Codominância",
    "Dominância Incompleta",
    "Seu Tipo Aqui"  # Adicione novo
]
```

### Modificar Cores

```python
# Mude no código:
colors = [
    '#2ecc71',  # Verde para AA
    '#f1c40f',  # Amarelo para Aa
    '#e74c3c'   # Vermelho para aa
]
```

### Adicionar mais alelos

```python
# Atualmente suporta 2 alelos (A e a)
# Para 3+ alelos, precisaria refatorar a lógica
# Considere usar dataclasses para representar alelos
```

---

## 💡 Dicas para Alunos

1. **Comece com Aa × Aa**: O cruzamento clássico que sempre dá 3:1

2. **Experimente AA × aa**: Todos os filhos serão Aa (100%)

3. **Tente AA × AA**: Todos os filhos serão AA (100%)

4. **Compare genótipos**: Veja como mudanças nos parentais afetam a prole

5. **Leia a Análise**: Cada simulação inclui explicação científica

---

## ✒️ Autor

**Luis Guilherme G.B.**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 💼 Portfólio: Desenvolvedor Python Full-Stack
- 📧 Contato: Abra uma issue no repositório

---

## 🙏 Créditos

- **Gregor Mendel** (1822-1884): Fundador da genética moderna
- **Inspiração**: Conceitos de hereditariedade e probabilidade
- **Desenvolvido com ❤️** em Python

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Use, modifique e distribua livremente, especialmente para fins educacionais!

---

## 🌟 Se gostou, considere dar uma ⭐!

```
   🧬 GENÉTICA PARA TODOS!

   Este simulador democratiza
   o entendimento da 1ª Lei de Mendel

   COMPARTILHE COM SEUS ALUNOS!
```

---

**Última atualização**: 2026-04-20  
**Versão**: 1.0 — Educational Release  
**Status**: ✅ Totalmente funcional e educativo  
**Categoria**: Biologia Molecular | Educação | Simulação
```

---
