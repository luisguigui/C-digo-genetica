import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MendelGeneticsPro(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("🧬 MENDEL GENETICS PRO - Simulador Genético")
        self.geometry("1200x800")
        ctk.set_appearance_mode("dark")
        
        # Configurar layout principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="🧬 MENDEL PRO", 
                    font=("Roboto", 24, "bold"), text_color="#2ecc71").pack(pady=30)
        
        # Seção de Configuração
        ctk.CTkLabel(self.sidebar, text="CONFIGURAÇÃO GENÉTICA", 
                    font=("Roboto", 14, "bold"), text_color="gray").pack(pady=(20,10))
        
        # Tipo de Herança
        self.inheritance_var = ctk.StringVar(value="Autossômica Dominante")
        ctk.CTkLabel(self.sidebar, text="Tipo de Herança:").pack(pady=(10,5))
        inheritance_options = ["Autossômica Dominante", "Autossômica Recessiva", 
                              "Codominância", "Dominância Incompleta"]
        self.inheritance_combo = ctk.CTkComboBox(self.sidebar, 
                                               values=inheritance_options,
                                               variable=self.inheritance_var)
        self.inheritance_combo.pack(pady=5, padx=20)
        
        # Nomes dos Alelos
        self.dominant_var = ctk.StringVar(value="A")
        self.recessive_var = ctk.StringVar(value="a")
        
        ctk.CTkLabel(self.sidebar, text="Alelo Dominante:").pack(pady=(10,5))
        self.entry_dominant = ctk.CTkEntry(self.sidebar, 
                                          textvariable=self.dominant_var,
                                          width=100, justify="center")
        self.entry_dominant.pack(pady=5)
        
        ctk.CTkLabel(self.sidebar, text="Alelo Recessivo:").pack(pady=(10,5))
        self.entry_recessive = ctk.CTkEntry(self.sidebar, 
                                           textvariable=self.recessive_var,
                                           width=100, justify="center")
        self.entry_recessive.pack(pady=5)
        
        # Parentais
        ctk.CTkLabel(self.sidebar, text="\nPARENTAIS", 
                    font=("Roboto", 14, "bold"), text_color="gray").pack(pady=(20,10))
        
        # Parental 1 - CORRIGIDO
        self.parental1_var = ctk.StringVar(value="Aa")
        self.create_parental_section("Parental 1 (♀)", self.sidebar, "#3498db", self.parental1_var)
        
        # Parental 2 - CORRIGIDO
        self.parental2_var = ctk.StringVar(value="Aa")
        self.create_parental_section("Parental 2 (♂)", self.sidebar, "#e74c3c", self.parental2_var)
        
        # Botão de Simulação
        self.btn_simulate = ctk.CTkButton(self.sidebar, 
                                         text="🧬 SIMULAR CRUZAMENTO",
                                         font=("Roboto", 14, "bold"),
                                         fg_color="#9b59b6",
                                         hover_color="#8e44ad",
                                         height=50,
                                         command=self.simulate_cross)
        self.btn_simulate.pack(pady=30, padx=20)
        
        # Botão Limpar
        ctk.CTkButton(self.sidebar, 
                     text="🔄 LIMPAR TUDO",
                     font=("Roboto", 12),
                     fg_color="#e74c3c",
                     hover_color="#c0392b",
                     height=40,
                     command=self.clear_all).pack(pady=10, padx=20)
        
        # --- ÁREA PRINCIPAL ---
        self.main_area = ctk.CTkFrame(self, fg_color="transparent")
        self.main_area.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")
        self.main_area.columnconfigure(0, weight=1)
        self.main_area.rowconfigure(1, weight=1)
        
        # Título Principal
        self.title_label = ctk.CTkLabel(self.main_area, 
                                       text="SIMULAÇÃO GENÉTICA - 1ª LEI DE MENDEL",
                                       font=("Roboto", 22, "bold"))
        self.title_label.grid(row=0, column=0, pady=(0,20))
        
        # Abas de Resultados
        self.tabview = ctk.CTkTabview(self.main_area)
        self.tabview.grid(row=1, column=0, sticky="nsew")
        
        # Criar abas
        self.tabview.add("Quadrado de Punnett")
        self.tabview.add("Estatísticas")
        self.tabview.add("Gráfico")
        self.tabview.add("Análise")
        
        # Configurar cada aba
        self.setup_punnett_tab()
        self.setup_stats_tab()
        self.setup_chart_tab()
        self.setup_analysis_tab()
    
    def create_parental_section(self, title, parent, color, variable):
        """Cria seção para configurar um parental - CORRIGIDO"""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(frame, text=title, text_color=color, 
                    font=("Roboto", 12, "bold")).pack(anchor="w", pady=(0,5))
        
        # Seleção de genótipo
        genotype_frame = ctk.CTkFrame(frame, fg_color="transparent")
        genotype_frame.pack(fill="x")
        
        genotypes = ["AA", "Aa", "aa"]
        
        for i, genotype in enumerate(genotypes):
            rb = ctk.CTkRadioButton(genotype_frame, text=genotype,
                                   variable=variable,
                                   value=genotype, text_color="white")
            rb.pack(side="left", padx=5)
    
    def setup_punnett_tab(self):
        """Configura a aba do Quadrado de Punnett"""
        tab = self.tabview.tab("Quadrado de Punnett")
        
        # Container para o quadrado
        self.punnett_container = ctk.CTkFrame(tab, fg_color="#1a1a1a")
        self.punnett_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Grid para o quadrado (3x3)
        self.punnett_grid = ctk.CTkFrame(self.punnett_container, fg_color="transparent")
        self.punnett_grid.pack(expand=True)
        
        # Criar células 3x3
        self.punnett_cells = []
        for row in range(3):
            row_cells = []
            for col in range(3):
                cell = ctk.CTkFrame(self.punnett_grid, width=100, height=100, 
                                   corner_radius=10, fg_color="#2b2b2b")
                cell.grid(row=row, column=col, padx=2, pady=2)
                
                # Label dentro da célula
                label = ctk.CTkLabel(cell, text="", font=("Roboto", 16, "bold"))
                label.place(relx=0.5, rely=0.5, anchor="center")
                row_cells.append(label)
            self.punnett_cells.append(row_cells)
    
    def setup_stats_tab(self):
        """Configura a aba de Estatísticas"""
        tab = self.tabview.tab("Estatísticas")
        
        # Frame para estatísticas
        self.stats_frame = ctk.CTkFrame(tab, fg_color="transparent")
        self.stats_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Container com scroll
        self.stats_scroll = ctk.CTkScrollableFrame(self.stats_frame)
        self.stats_scroll.pack(fill="both", expand=True)
        
        # Labels para estatísticas
        self.genotypic_stats = []
        self.phenotypic_stats = []
        
        # Título Genótipos
        ctk.CTkLabel(self.stats_scroll, text="📊 DISTRIBUIÇÃO GENOTÍPICA",
                    font=("Roboto", 16, "bold")).pack(pady=(0,10))
        
        # Criar 3 cards para genótipos
        genotypes = ["Homozigoto Dominante", "Heterozigoto", "Homozigoto Recessivo"]
        colors = ["#2ecc71", "#f1c40f", "#e74c3c"]
        
        for i, genotype in enumerate(genotypes):
            frame = ctk.CTkFrame(self.stats_scroll, height=80, corner_radius=10,
                               fg_color="#2b2b2b")
            frame.pack(fill="x", pady=5)
            
            ctk.CTkLabel(frame, text=genotype, font=("Roboto", 12, "bold"),
                        text_color=colors[i]).pack(side="left", padx=20)
            
            count_label = ctk.CTkLabel(frame, text="0/16 (0%)", 
                                      font=("Roboto", 14, "bold"))
            count_label.pack(side="right", padx=20)
            
            self.genotypic_stats.append(count_label)
        
        # Título Fenótipos
        ctk.CTkLabel(self.stats_scroll, text="\n🎯 DISTRIBUIÇÃO FENOTÍPICA",
                    font=("Roboto", 16, "bold")).pack(pady=(20,10))
        
        # Criar 2 cards para fenótipos
        phenotypes = ["Fenótipo Dominante", "Fenótipo Recessivo"]
        p_colors = ["#3498db", "#9b59b6"]
        
        for i, phenotype in enumerate(phenotypes):
            frame = ctk.CTkFrame(self.stats_scroll, height=80, corner_radius=10,
                               fg_color="#2b2b2b")
            frame.pack(fill="x", pady=5)
            
            ctk.CTkLabel(frame, text=phenotype, font=("Roboto", 12, "bold"),
                        text_color=p_colors[i]).pack(side="left", padx=20)
            
            count_label = ctk.CTkLabel(frame, text="0/16 (0%)", 
                                      font=("Roboto", 14, "bold"))
            count_label.pack(side="right", padx=20)
            
            self.phenotypic_stats.append(count_label)
    
    def setup_chart_tab(self):
        """Configura a aba de Gráficos"""
        tab = self.tabview.tab("Gráfico")
        
        self.chart_frame = ctk.CTkFrame(tab, fg_color="transparent")
        self.chart_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Placeholder para gráfico
        self.chart_label = ctk.CTkLabel(self.chart_frame, 
                                       text="Clique em SIMULAR para gerar gráfico...",
                                       font=("Roboto", 14), text_color="gray")
        self.chart_label.pack(expand=True)
    
    def setup_analysis_tab(self):
        """Configura a aba de Análise"""
        tab = self.tabview.tab("Análise")
        
        # Área de texto para análise detalhada
        self.analysis_text = ctk.CTkTextbox(tab, font=("Consolas", 12))
        self.analysis_text.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Texto inicial
        initial_text = """=== ANÁLISE GENÉTICA DETALHADA ===

1. PRINCÍPIO DA SEGREGAÇÃO:
   - Cada organismo possui dois alelos para cada característica
   - Os alelos segregam-se durante a formação dos gametas
   - Cada gameta recebe apenas um alelo de cada par

2. HIPÓTESE DA DOMINÂNCIA:
   - Um alelo pode ser dominante sobre outro
   - O fenótipo dominante se expressa em heterozigotos
   - O fenótipo recessivo só se expressa em homozigotos

3. PROBABILIDADES:
   - Cruzamento entre heterozigotos (Aa x Aa):
     * 25% AA (homozigoto dominante)
     * 50% Aa (heterozigoto)
     * 25% aa (homozigoto recessivo)
     * Proporção fenotípica: 3:1

Digite os genótipos e clique em SIMULAR para ver a análise completa."""
        self.analysis_text.insert("1.0", initial_text)
    
    def simulate_cross(self):
        """Executa a simulação do cruzamento - CORRIGIDO"""
        try:
            # Obter dados dos parentais - AGORA FUNCIONANDO
            parental1 = self.parental1_var.get()
            parental2 = self.parental2_var.get()
            
            dominant = self.dominant_var.get().upper()
            recessive = self.recessive_var.get().lower()
            
            if not dominant or not recessive:
                messagebox.showwarning("Aviso", "Defina os alelos dominante e recessivo!")
                return
            
            if dominant == recessive:
                messagebox.showwarning("Aviso", "Os alelos devem ser diferentes!")
                return
            
            # Gerar gametas
            gametes1 = self.get_gametes(parental1, dominant, recessive)
            gametes2 = self.get_gametes(parental2, dominant, recessive)
            
            # Atualizar Quadrado de Punnett
            self.update_punnett_grid(gametes1, gametes2, dominant, recessive)
            
            # Calcular estatísticas
            self.calculate_statistics(gametes1, gametes2, dominant, recessive)
            
            # Gerar gráfico
            self.generate_chart(gametes1, gametes2, dominant, recessive)
            
            # Atualizar análise
            self.update_analysis(parental1, parental2, dominant, recessive)
            
            messagebox.showinfo("Sucesso", "Simulação concluída com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na simulação: {str(e)}")
    
    def get_gametes(self, genotype, dominant, recessive):
        """Retorna os gametas possíveis para um genótipo"""
        if genotype == "AA":
            return [dominant]
        elif genotype == "aa":
            return [recessive]
        else:  # Aa
            return [dominant, recessive]
    
    def update_punnett_grid(self, gametes1, gametes2, dominant, recessive):
        """Atualiza o quadrado de Punnett na interface"""
        # Limpar células
        for row in range(3):
            for col in range(3):
                self.punnett_cells[row][col].configure(text="")
        
        # Cabeçalhos
        self.punnett_cells[0][0].configure(text="♀\\n♂", text_color="white")
        
        # Gametas do parental 1 (linhas)
        for i, gamete in enumerate(gametes1):
            self.punnett_cells[i+1][0].configure(text=gamete, text_color="#3498db")
        
        # Gametas do parental 2 (colunas)
        for j, gamete in enumerate(gametes2):
            self.punnett_cells[0][j+1].configure(text=gamete, text_color="#e74c3c")
        
        # Prole (cruzamentos)
        for i, g1 in enumerate(gametes1):
            for j, g2 in enumerate(gametes2):
                # Ordenar para genótipo padronizado
                genotype = ''.join(sorted([g1.upper(), g2.upper()], key=lambda x: x.islower()))
                
                # Determinar cor baseada no genótipo
                if genotype == dominant * 2:
                    color = "#2ecc71"  # Verde - homozigoto dominante
                elif genotype.lower() == recessive * 2:
                    color = "#e74c3c"  # Vermelho - homozigoto recessivo
                else:
                    color = "#f1c40f"  # Amarelo - heterozigoto
                
                self.punnett_cells[i+1][j+1].configure(text=genotype, text_color=color)
    
    def calculate_statistics(self, gametes1, gametes2, dominant, recessive):
        """Calcula estatísticas genotípicas e fenotípicas"""
        total = len(gametes1) * len(gametes2)
        
        # Contar genótipos
        genotype_counts = {"AA": 0, "Aa": 0, "aa": 0}
        phenotype_counts = {"Dominante": 0, "Recessivo": 0}
        
        for g1 in gametes1:
            for g2 in gametes2:
                genotype = ''.join(sorted([g1.upper(), g2.upper()], key=lambda x: x.islower()))
                
                # Contar genótipos
                if genotype == dominant * 2:
                    genotype_counts["AA"] += 1
                    phenotype_counts["Dominante"] += 1
                elif genotype.lower() == recessive * 2:
                    genotype_counts["aa"] += 1
                    phenotype_counts["Recessivo"] += 1
                else:  # Aa ou aA
                    genotype_counts["Aa"] += 1
                    phenotype_counts["Dominante"] += 1
        
        # Atualizar interface - Genótipos
        genotypes = ["AA", "Aa", "aa"]
        for i, genotype in enumerate(genotypes):
            count = genotype_counts[genotype]
            percentage = (count / total) * 100 if total > 0 else 0
            self.genotypic_stats[i].configure(
                text=f"{count}/{total} ({percentage:.1f}%)",
                text_color=["#2ecc71", "#f1c40f", "#e74c3c"][i]
            )
        
        # Atualizar interface - Fenótipos
        phenotypes = ["Dominante", "Recessivo"]
        for i, phenotype in enumerate(phenotypes):
            count = phenotype_counts[phenotype]
            percentage = (count / total) * 100 if total > 0 else 0
            self.phenotypic_stats[i].configure(
                text=f"{count}/{total} ({percentage:.1f}%)",
                text_color=["#3498db", "#9b59b6"][i]
            )
    
    def generate_chart(self, gametes1, gametes2, dominant, recessive):
        """Gera gráfico de distribuição"""
        # Limpar frame anterior
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        
        # Calcular distribuição
        total = len(gametes1) * len(gametes2)
        genotype_counts = {"AA": 0, "Aa": 0, "aa": 0}
        phenotype_counts = {"Dominante": 0, "Recessivo": 0}
        
        for g1 in gametes1:
            for g2 in gametes2:
                genotype = ''.join(sorted([g1.upper(), g2.upper()], key=lambda x: x.islower()))
                
                if genotype == dominant * 2:
                    genotype_counts["AA"] += 1
                    phenotype_counts["Dominante"] += 1
                elif genotype.lower() == recessive * 2:
                    genotype_counts["aa"] += 1
                    phenotype_counts["Recessivo"] += 1
                else:
                    genotype_counts["Aa"] += 1
                    phenotype_counts["Dominante"] += 1
        
        # Criar figura
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), facecolor='#2b2b2b')
        
        # Gráfico de pizza - Genótipos
        genotypes = ['AA', 'Aa', 'aa']
        counts = [genotype_counts["AA"], genotype_counts["Aa"], genotype_counts["aa"]]
        colors = ['#2ecc71', '#f1c40f', '#e74c3c']
        
        ax1.pie(counts, labels=genotypes, colors=colors, autopct='%1.1f%%',
               startangle=90, textprops={'color': 'white', 'weight': 'bold'})
        ax1.set_title('Distribuição Genotípica', color='white', pad=20)
        
        # Gráfico de barras - Fenótipos
        phenotypes = ['Dominante', 'Recessivo']
        p_counts = [phenotype_counts["Dominante"], phenotype_counts["Recessivo"]]
        p_colors = ['#3498db', '#9b59b6']
        
        bars = ax2.bar(phenotypes, p_counts, color=p_colors)
        ax2.set_title('Distribuição Fenotípica', color='white', pad=20)
        ax2.set_ylabel('Contagem', color='white')
        ax2.set_facecolor('#2b2b2b')
        ax2.tick_params(colors='white')
        
        # Adicionar valores nas barras
        for bar, count in zip(bars, p_counts):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    str(count), ha='center', va='bottom', color='white', fontweight='bold')
        
        # Ajustar layout
        plt.tight_layout()
        
        # Integrar no CustomTkinter
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def update_analysis(self, parental1, parental2, dominant, recessive):
        """Atualiza a aba de análise com resultados"""
        analysis_text = f"""=== RESULTADOS DA SIMULAÇÃO ===

CONFIGURAÇÃO:
• Parental 1 (♀): {parental1}
• Parental 2 (♂): {parental2}
• Alelo dominante: {dominant}
• Alelo recessivo: {recessive}
• Tipo de herança: {self.inheritance_var.get()}

ANÁLISE DO CRUZAMENTO:
• Gametas Parental 1: {self.get_gametes(parental1, dominant, recessive)}
• Gametas Parental 2: {self.get_gametes(parental2, dominant, recessive)}
• Total de combinações: {len(self.get_gametes(parental1, dominant, recessive)) * len(self.get_gametes(parental2, dominant, recessive))}

PROPORÇÕES ESPERADAS (1ª Lei de Mendel):
1. Princípio da Segregação:
   - Cada gameta recebe apenas um alelo do par
   - Alelos segregam-se independentemente

2. Proporção Genotípica:
   • 25% {dominant}{dominant} (Homozigoto dominante)
   • 50% {dominant}{recessive} (Heterozigoto)
   • 25% {recessive}{recessive} (Homozigoto recessivo)

3. Proporção Fenotípica (3:1):
   • 75% Fenótipo dominante
   • 25% Fenótipo recessivo

IMPLICAÇÕES GENÉTICAS:
• Este cruzamento demonstra a segregação independente dos alelos
• Os heterozigotos expressam o fenótipo dominante
• A proporção 3:1 é característica de cruzamentos entre heterozigotos"""
        
        self.analysis_text.delete("1.0", "end")
        self.analysis_text.insert("1.0", analysis_text)
    
    def clear_all(self):
        """Limpa todos os dados e resultados"""
        # Resetar variáveis
        self.parental1_var.set("Aa")
        self.parental2_var.set("Aa")
        self.dominant_var.set("A")
        self.recessive_var.set("a")
        self.inheritance_var.set("Autossômica Dominante")
        
        # Limpar Punnett
        for row in range(3):
            for col in range(3):
                self.punnett_cells[row][col].configure(text="")
        
        # Limpar estatísticas
        for label in self.genotypic_stats:
            label.configure(text="0/16 (0%)", text_color="white")
        
        for label in self.phenotypic_stats:
            label.configure(text="0/16 (0%)", text_color="white")
        
        # Limpar gráfico
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        
        self.chart_label = ctk.CTkLabel(self.chart_frame, 
                                       text="Clique em SIMULAR para gerar gráfico...",
                                       font=("Roboto", 14), text_color="gray")
        self.chart_label.pack(expand=True)
        
        # Limpar análise
        self.analysis_text.delete("1.0", "end")
        self.analysis_text.insert("1.0", "=== ANÁLISE GENÉTICA DETALHADA ===\n\nClique em SIMULAR para ver os resultados...")
        
        messagebox.showinfo("Limpeza", "Todos os dados foram resetados!")

# Executar aplicação
if __name__ == "__main__":
    app = MendelGeneticsPro()
    app.mainloop()