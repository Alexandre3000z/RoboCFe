import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from Interface.app_state import app_state

def openMainPage(lastPage):
    
   

    def save_and_close():
        """Captura os valores dos campos e armazena no estado global antes de fechar a janela."""

        inscricao_estadual = Ie_entry.get()
        mes = Month_entry.get()
        ano = Year_entry.get()

        # Atualiza os dados globais
        app_state.set_data(inscricao_estadual, mes, ano)

        # Fecha a janela principal
        mainPage.destroy()
        
        
    # Fecha a janela de login
    lastPage.destroy()

    # Cria a nova janela principal
    mainPage = ctk.CTk()
    mainPage.title("Main Page")
    mainPage.geometry("1280x720")
    mainPage.configure(fg_color="#25412D")



    mainPage_frame = ctk.CTkFrame(mainPage, width=1200, height=600, corner_radius=20,fg_color="transparent")
    mainPage_frame.pack(fill="both", expand=True, padx=20, pady=20)
    

#------------------------------------------------------------------#
#--------------------------LADO ESQUERDO---------------------------#
#------------------------------------------------------------------#

    # Frame da esquerda (não visível, mas organiza o conteúdo)
    MainLeft_frame = ctk.CTkFrame(mainPage_frame, 
                                  fg_color="transparent",
                                  
                                  )
    
    MainLeft_frame.pack(side="left", 
                        fill="both", 
                        expand=True,
                        padx=20, 
                        pady=20)

#-------------------- CHECK BOXES --------------------#

    # Titulo
    IeTitleLabel = ctk.CTkLabel(MainLeft_frame, 
                                text=" LOGIN AMBIENTE SEGURO ", 
                                font=("Consolas", 30, "bold"), 
                                text_color="#25412D",
                                width=600,
                                height=50,
                                corner_radius=6,
                                fg_color='white')
    
    IeTitleLabel.pack(anchor='w', pady=(0, 5))
    

   # Titulo de usuario
    UserLabel = ctk.CTkLabel(MainLeft_frame,
                           text="CPF DO CONTADOR:",
                           font=("Consolas", 20, "bold"), 
                           text_color="white")
    
    UserLabel.pack(anchor='w', pady=(20, 10))
    
    # Campo para usuario
    User_entry = ctk.CTkEntry(MainLeft_frame, 
                            text_color='black',
                            width=175, 
                            font=("Consolas", 18, "bold"), 
                            border_color='white')
    
    User_entry.pack(anchor='w', pady=0, padx=20)
    
    # Titulo de SENHA
    UserLabel = ctk.CTkLabel(MainLeft_frame,
                           text="SENHA:",
                           font=("Consolas", 20, "bold"), 
                           text_color="white")
    
    UserLabel.pack(anchor='w', pady=(20, 10))
    
    # Campo para SENHA
    User_entry = ctk.CTkEntry(MainLeft_frame, 
                            text_color='black',
                            width=175, 
                            font=("Consolas", 18, "bold"), 
                            border_color='white')
    
    User_entry.pack(anchor='w', pady=0, padx=20)
    
#-------------- CAMPO DE INSCRIÇÃO ESTADUAL --------------#

    # Titulo
    IeTitleLabel = ctk.CTkLabel(MainLeft_frame, 
                                text=" DADOS DE CONSULTA ", 
                                font=("Consolas", 30, "bold"), 
                                width=600,
                                height=50,
                                text_color="#25412D",
                                corner_radius=6,
                                fg_color='white')
    
    IeTitleLabel.pack(anchor='w', pady=(70, 5))
    
    # Titulo de Inscrição
    IeLabel = ctk.CTkLabel(MainLeft_frame,
                           text="INSCRIÇÃO:",
                           font=("Consolas", 20, "bold"), 
                           text_color="white")
    
    IeLabel.pack(anchor='w', pady=(30, 5))
    
    # Campo para inscrição
    Ie_entry = ctk.CTkEntry(MainLeft_frame, 
                            text_color='black',
                            width=175, 
                            font=("Consolas", 18, "bold"), 
                            border_color='white')
    
    Ie_entry.pack(anchor='w', pady=0, padx=20)

#-------------- FRAME PARA ALINHAR MÊS E ANO ----------------#

    date_frame = ctk.CTkFrame(MainLeft_frame, fg_color="transparent")
    date_frame.pack(anchor='w', pady=(30, 5))

    #-------------- CAMPO MÊS --------------# 
   
    # Frame individual para o Mês
    month_frame = ctk.CTkFrame(date_frame, fg_color="transparent")
    month_frame.pack(side="left", padx=0)
    
    # Título Mês
    MonthLabel = ctk.CTkLabel(month_frame, 
                              text="MÊS:", 
                              font=("Consolas", 20, "bold"), 
                              text_color="white")
    
    MonthLabel.pack(anchor='w')
    
    # Campo para Mês
    Month_entry = ctk.CTkEntry(month_frame, 
                               text_color='black',
                               width=100, 
                               font=("Consolas", 18, "bold"), 
                               border_color='white',)
    
    Month_entry.pack(anchor='w', pady=5, padx=20)
    
    #-------------- CAMPO ANO --------------# 
    
    # Frame individual para o Ano
    year_frame = ctk.CTkFrame(date_frame, fg_color="transparent")
    year_frame.pack(side="left", padx=0)

    # Título Ano
    YearLabel = ctk.CTkLabel(year_frame, 
                             text="ANO:", 
                             font=("Consolas", 20, "bold"), 
                             text_color="white")
    
    YearLabel.pack(anchor='w')
    
    # Campo para Ano
    Year_entry = ctk.CTkEntry(year_frame, 
                              text_color='black',
                              width=100, 
                              font=("Consolas", 18, "bold"), 
                              border_color='white')
    
    Year_entry.pack(anchor='w', pady=5, padx=20)

#------------------------------------------------------------------#
#---------------------------LADO DIREITO---------------------------#
#------------------------------------------------------------------#
       
    # Frame da direita (não visível, mas organiza o conteúdo)
    MainRight_frame = ctk.CTkFrame(mainPage_frame, fg_color="transparent")
    MainRight_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)
    
    logo_frame = ctk.CTkFrame(MainRight_frame, width=550, height=500, corner_radius=100, fg_color="white")
    logo_frame.pack(side="right", fill="both", expand=True)
    logo_frame.pack_propagate(False)
    
    try:
        
        logo_image = ctk.CTkImage(dark_image=Image.open("logo.png"), size=(500,500))
        logo_label = ctk.CTkLabel(logo_frame, image=logo_image, text="")
        logo_label.pack(expand=True)
        
    except:
        
        # Caso não tenha o logo, exibe texto como placeholder
        logo_label = ctk.CTkLabel(logo_frame, text="BUSINESS PRO\nCONTÁBIL", font=("Arial", 24, "bold"), text_color="#1e3d2f")
        logo_label.pack(expand=True)

    
    
    # Botão para sair do app
    MainexitButton = ctk.CTkButton(MainLeft_frame,
                                   font=("Consolas", 20, "bold"), 
                                   text_color='black', 
                                   text="EXECUTAR", 
                                   fg_color='white', 
                                   command=save_and_close)
    
    MainexitButton.pack(pady=0, side='bottom' , expand=True)

    # Executa a nova janela
    mainPage.mainloop()


