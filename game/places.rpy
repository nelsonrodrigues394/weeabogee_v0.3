label pass_hour:
    
    $ clock.next()
    
    return

label hour_check:
    
    if 7 > clock.hour >= 1:
        jump sleep_time
    else:
        return

label check_daytime:
    
    if clock.hour == 7:
        $ current_daytime = "Manhã"
    elif clock.hour == 18:
        $ current_daytime = "Tarde"
    elif clock.hour == 19:
        $ current_daytime = "Noite"        
    return
    
label home:
    
    if current_daytime == "Manhã":
        scene home_a
    elif current_daytime == "Tarde":
        scene home_b
    elif current_daytime == "Noite":
        scene home_c
        
    "O que você deseja fazer?"
    
    menu:
        "Sair de casa":
            "Para onde deseja ir?"
            menu:
                "Centro":
                    call pass_hour
                    call check_daytime
                    call hour_check
                    jump center
                
                "Subúrbio":
                    call pass_hour
                    call check_daytime
                    call hour_check
                    jump suburbs
                
                "Estação":
                    call pass_hour
                    call check_daytime
                    call hour_check
                    jump station
                
        
        "Ficar em casa":
            menu:
                "Mexer no computador" if computer:
                    jump computer
                "Ler um livro":
                    jump book_reading
            jump stay_home

label computer:
    
    scene computer
    
    #######ADICIONAR CONTENT AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump home

label center:
    
    call check_daytime
        
    if current_daytime == "Manhã":
        scene center_a
    elif current_daytime == "Tarde":
        scene center_b
    elif current_daytime == "Noite":
        scene center_c
    
    "Você está no centro. Para onde deseja ir agora?"
    
    menu:
        "Ir ao Shopping Center":
            call pass_hour
            call check_daytime
            call hour_check
            jump shopping
        "Ir ao maid cafe" if current_daytime != "Noite":
            call pass_hour
            call check_daytime
            call hour_check
            jump maidcafe
        "Ir ao hospital":
            call pass_hour
            call check_daytime
            call hour_check
            jump hospital
        "Visitar um escritório":
            call pass_hour
            call check_daytime
            call hour_check
            jump office
        "Ir à um restaurante":
            call pass_hour
            call check_daytime
            call hour_check
            jump restaurant
        "Ir à um bar" if current_daytime == "Noite":
            call pass_hour
            call check_daytime
            call hour_check
            jump pub
        "Ir ao submundo":
            call pass_hour
            call check_daytime
            call hour_check
            if current_daytime != "Noite":
                "Você não encontra nada aberto"
                jump center
            else:
                jump underworld
        "Ir para casa":
            call pass_hour
            call check_daytime
            call hour_check
            jump home
            
label suburbs:
    
    call check_daytime
        
    if current_daytime == "Manhã":
        scene suburbs_a
    elif current_daytime == "Tarde":
        scene suburbs_b
    elif current_daytime == "Noite":
        scene suburbs_c
        
    "Você está no subúrbio. Para onde deseja ir agora?"
    
    menu:
        "Ir ao parque":
            call pass_hour
            call check_daytime
            call hour_check
            jump park
        "Ir à escola":
            call pass_hour
            call check_daytime
            call hour_check
            jump school
        "Ir à igreja":
            call pass_hour
            call check_daytime
            call hour_check
            jump church
        "Ir ao playground infantil":
            call pass_hour
            call check_daytime
            call hour_check
            jump playground
        "Ir à loja de conveniência":
            call pass_hour
            call check_daytime
            call hour_check
            jump convenience
        "Caminhar pelo subúrbio":
            call pass_hour
            call check_daytime
            call hour_check
            jump suburbs_walk
        "Ir para casa":
            call pass_hour
            call check_daytime
            call hour_check
            jump home
        

label station:
    
    call check_daytime
        
    if current_daytime == "Manhã":
        scene station_a
    elif current_daytime == "Tarde":
        scene station_b
    elif current_daytime == "Noite":
        scene station_c
    
    "Você está na estação de trens. O que deseja fazer?"
    
    menu:
        "Comprar uma passagem para a zona rural":
            $ money -= 10
            call pass_hour
            call check_daytime
            call hour_check
            jump rural
        "Comprar uma passagem para as montanhas":
            $ money -= 10
            call pass_hour
            call check_daytime
            call hour_check
            jump mountains
        "Comprar uma passagem para a praia":
            $ money -= 10
            call pass_hour
            call check_daytime
            call hour_check
            jump beach
        "Ir para casa":
            call pass_hour
            call check_daytime
            call hour_check
            jump home
            
label train:
    
    call check_daytime
        
    if current_daytime == "Manhã":
        scene train_a
    elif current_daytime == "Tarde":
        scene train_b
    elif current_daytime == "Noite":
        scene train_c
    
    #######CHECK DE EVENTOS AQUI#######
    
    return
    
#LOCAIS DO CENTRO

label shopping:
    
    call check_daytime
    
    scene shopping
        
    "Você está no Shopping Center. O que deseja fazer?"
    
    menu:
        "Ir à academia":
            call pass_hour
            call check_daytime
            call hour_check
            jump gym
        "Ir ao arcade":
            call pass_hour
            call check_daytime
            call hour_check
            jump arcade
        "Comprar":
            jump shopping_buy
        "Caminhar pelo shopping":
            call pass_hour
            call check_daytime
            call hour_check
            jump shopping_walk
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump center
    
label maidcafe:
    
    call check_daytime
    
    scene maidcafe
        
    if lockpick.getLevel() == 0:
        jump lp_event
    else:
        #######CHECK DE EVENTOS AQUI#######
    
        "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
        jump center
    
label hospital:
    
    call check_daytime
        
    if current_daytime == "Manhã":
        scene hosp_a
    elif current_daytime == "Tarde":
        scene hosp_b
    elif current_daytime == "Noite":
        scene hosp_c
        
    menu:
        "Procurar emprego" if hosp_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump hosp_jobi
        "Trabalhar" if 10 <= clock.hour < 11 and hosp_job1:
            call check_daytime
            call hour_check
            jump hosp_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump center

label office:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene office_a
    elif current_daytime == "Tarde":
        scene office_b
    elif current_daytime == "Noite":
        scene office_c
    
    "Você está na área empresarial. O que deseja fazer?"
    
    menu:
        "Procurar emprego" if office_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump office_jobi
        "Trabalhar" if 10 <= clock.hour < 11 and office_job1:
            call check_daytime
            call hour_check
            jump office_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump center
            
label restaurant:
    
    call check_daytime
    
    scene restau_1
    
    menu:
        "Procurar emprego" if restau_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump restau_jobi
        "Trabalhar" if 10 <= clock.hour < 11 and restau_job1:
            call check_daytime
            call hour_check
            jump restau_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump center
            
label pub:
    
    call check_daytime
    
    scene pub
    
    menu:
        "Socializar com estranhos":
            jump pub_social
        "Procurar emprego" if pub_job1 ==  False:
            call pass_hour
            call check_daytime
            call hour_check
            jump pub_jobi
        "Trabalhar" if 18 <= clock.hour < 19 and pub_job1:
            call check_daytime
            call hour_check
            jump pub_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump center
            
label underworld:
    
    call check_daytime
    
    scene underworld
    
    menu:
        "Ir ao puteiro" if reputacao.getLevel() >= 3:
            call pass_hour
            call check_daytime
            call hour_check
            jump brothel
        "Seguir para a área dos moteis":
            jump motel
        "Ir à loja clandestina" if u_store:
            jump underworld_buy
        
#LOCAIS DO SHOPPING

label gym:
    
    call check_daytime
    
    scene gym
    
    "Você está na academia. O que deseja fazer?"
    
    menu:
        "Malhar":       
            call check_daytime
            call hour_check
            jump workout
        "Procurar emprego" if gym_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump gym_jobi
        "Trabalhar" if 10 <= clock.hour < 11and gym_job1:
            call check_daytime
            call hour_check
            jump gym_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump shopping
            
label arcade:
    
    call check_daytime
    
    scene arcade
    
    "Você está no arcade. O que deseja fazer?"
    
    menu:
        "Procurar emprego" if arcade_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump arcade_jobi
        "Trabalhar" if 10 <= clock.hour < 11 arcade_job1:
            call check_daytime
            call hour_check
            jump arcade_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump shopping
            
label shopping_buy:
    
    call check_daytime
    
    "O que você deseja comprar?"
    
    menu:
        "Computador: $1.000":
            if money < 1000:
                "Você não tem dinheiro suficiente para comprar isso."
                jump shopping_buy
            else:
                "Você comprou um computador."
                $ computer = True
                jump shopping_buy
        "Hacking for dummies: $300":
            if money < 300:
                "Você não tem dinheiro suficiente para comprar isso."
                jump shopping_buy
            else:
                "Você comprou o livro."
                $ hacking.setLevel(1)
                jump shopping_buy
        "Hypnosis for dummies: $400":
            if money < 400:
                "Você não tem dinheiro suficiente para comprar isso."
                jump shopping_buy
            else:
                "Você comprou o livro."
                $ hipnose.setLevel(1)
                jump shopping_buy
        "Retornar":
            jump shopping
    
    jump shopping
    
label shopping_walk:
    
    call check_daytime
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump shopping

    
#LOCAIS DO SUBMUNDO

label brothel:
    
    call check_daytime
    
    scene brothel
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump underworld
    
label motel:
    
    call check_daytime
    
    scene motel
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump underworld
    
label underworld_buy:
    
    call check_daytime
    
    scene underworld_store
    
    #######OPÇÕES DE COMPRA AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump underworld
    
    
#LOCAIS DO SUBÚRBIO

label park:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene park_a
    elif current_daytime == "Tarde":
        scene park_b
    elif current_daytime == "Noite":
        scene park_c
    
    "Você está no parque. O que deseja fazer?"
    
    menu:
        "Observar os pássaros":
            jump bird_watching
    
    jump suburbs
    
label school:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene park_a
    elif current_daytime == "Tarde":
        scene park_b
    elif current_daytime == "Noite":
        scene park_c
        
    "Você está na escola. O que dejesa fazer?"
    
    menu:
        "Ir à uma sala de aula" if school_job1:
            call pass_hour
            call check_daytime
            call hour_check
            jump school_class
        "Ir ao banheiro" if constituicao.getLevel() == 10:
            call pass_hour
            call check_daytime
            call hour_check
            jump school_bathroom
        "Ir à área de esportes" if school_job1:
            call pass_hour
            call check_daytime
            call hour_check
            jump sports_area
        "Ir ao terraço" if school_job1:
            call pass_hour
            call check_daytime
            call hour_check
            jump school_roof
        "Ir à cafeteria" if school_job1:
            call pass_hour
            call check_daytime
            call hour_check
            jump cafeteria
        "Ir à biblioteca" if school_job1:
            call pass_hour
            call check_daytime
            call hour_check
            jump library
        "Ir à enfermaria" if school_job1:
            call pass_hour
            call check_daytime
            call hour_check
            jump infirmary
        "Ir ao laboratório de química" if school_job1 and lockpick.getLevel() >= 2:
            call pass_hour
            call check_daytime
            call hour_check
            jump school_lab
        "Ir ao dormitório" if constituicao.getLevel() == 10:
            call pass_hour
            call check_daytime
            call hour_check
            jump dorms
        "Procurar emprego" if school_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump school_jobi
        "Trabalhar" if 10 <= clock.hour < 11 and school_job1:
            call check_daytime
            call hour_check
            jump school_jobw
            
label church:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene church_a
    elif current_daytime == "Tarde":
        scene church_b
    elif current_daytime == "Noite":
        scene church_c
        
    "Você está na igreja. O que deseja fazer?"

    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump suburbs
    
label playground:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene playground_a
    elif current_daytime == "Tarde":
        scene playground_b
    elif current_daytime == "Noite":
        scene playground_c
        
    "Você está no playground. O que deseja fazer?"
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump suburbs
    
label convenience:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene playground_a
    elif current_daytime == "Tarde":
        scene playground_b
    elif current_daytime == "Noite":
        scene playground_c
        
    "Você está na loja de conveniências. O que deseja fazer?"
    
    menu:
        "Procurar emprego" if conven_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump conven_jobi
        "Trabalhar" if 10 <= clock.hour < 11 and conven_job1:
            call check_daytime
            call hour_check
            jump conven_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump suburbs
            
label suburbs_walk:
    
    call check_daytime
    
    "Você está no playground. O que deseja fazer?"
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump suburbs
    
#LOCAIS DA ESCOLA

label school_class:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene class_a
    elif current_daytime == "Tarde":
        scene class_b
    elif current_daytime == "Noite":
        scene class_c
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump school
    
label school_bathroom:
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump school
    
label sports_area:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene class_a
    elif current_daytime == "Tarde":
        scene class_b
    elif current_daytime == "Noite":
        scene class_c
        
    "Você está na área aberta da escola. Para onde deseja ir?"
    
    menu:
        "Piscina":
            jump school_pool
        "Ginásio":
            jump school_gym
        "Depósito de equipamentos esportivos":
            jump gymdepo
        "Para as outras quadras":
            jump sports_area_event
            
label school_pool:
    
    call check_daytime
    
    scene school_pool
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump sports_area
    
label school_gym:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene school_gym_a
    elif current_daytime == "Tarde":
        scene school_gym_b
    elif current_daytime == "Noite":
        scene school_gym_c
        
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump sports_area

label gymdepo:
    
    scene gymdepo
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump sports_area
    
label sports_area_event: #IMPORTANTÍSSIMO: ISSO VAI NO EVENTS.RPY#
    
    scene black
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump sports_area

label school_roof:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene school_roof_a
    elif current_daytime == "Tarde":
        scene school_roof_b
    elif current_daytime == "Noite":
        scene school_roof_c
        
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump school

label cafeteria:
    
    call check_daytime
    
    scene cafeteria
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump school

label library:
    
    call check_daytime
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump school
    
label infirmary:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene infirmary_a
    elif current_daytime == "Tarde":
        scene infirmary_b
    elif current_daytime == "Noite":
        scene infirmary_c
        
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump school
    
label school_lab:
    
    call check_daytime
    
    scene school_lab
    
    if labSkill.getLevel() == 0:
        jump lab_event
    else:
        
        #######CHECK DE EVENTOS AQUI#######
    
        "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
        jump school
    
label dorms:
    
    call check_daytime
    
    scene dorms
    
    #######CHECK DE EVENTOS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump school

#LOCAIS DA ESTAÇÃO

label rural:
    
    call check_daytime
        
    if current_daytime == "Manhã":
        scene rural_a
    elif current_daytime == "Tarde":
        scene rural_b
    elif current_daytime == "Noite":
        scene rural_c
    
    #######NOVOS LOCAIS AQUI#######
    
    "SOB DESENVOLVIMENTO. VOCÊ RETORNARÁ AO MENU ANTERIOR"
    
    jump station
    
label mountains:
    
    call check_daytime
        
    if current_daytime == "Manhã":
        scene mountains_a
    elif current_daytime == "Tarde":
        scene mountains_b
    elif current_daytime == "Noite":
        scene mountains_c
        
    "Você está nas montanhas. O que deseja fazer?"
    
    menu:
        "Ir ao templo":
            call pass_hour
            call check_daytime
            call hour_check
            jump shrine
        "Ir ao hotel":
            call pass_hour
            call check_daytime
            call hour_check
            jump inn
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump station
            
label beach:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene beach_a
    elif current_daytime == "Tarde":
        scene beach_b
    elif current_daytime == "Noite":
        scene beach_c
        
    "Você está na praia. O que deseja fazer?"
    
    menu:
        "Procurar emprego" if beach_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump beach_jobi
        "Trabalhar" if 10 <= clock.hour < 11 and beach_job1:
            call check_daytime
            call hour_check
            jump beach_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump station
            
            
#LOCAIS DAS MONTANHAS

label shrine:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene shrine_a
    elif current_daytime == "Tarde":
        scene shrine_b
    elif current_daytime == "Noite":
        scene shrine_c
        
    "Você está no templo. O que deseja fazer?"
    
    menu:
        "Caminhar pelo templo":
            call pass_hour
            call check_daytime
            call hour_check
            jump temple_walk
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump mountains
            
label inn:
    
    call check_daytime
    
    if current_daytime == "Manhã":
        scene inn_a
    elif current_daytime == "Tarde":
        scene inn_b
    elif current_daytime == "Noite":
        scene inn_c  
        
    "Você está no hotel. O que deseja fazer?"
    
    menu:
        "Ir ao onsen":
            call pass_hour
            call check_daytime
            call hour_check
            jump onsen
        "Procurar emprego" if inn_job1 == False:
            call pass_hour
            call check_daytime
            call hour_check
            jump inn_jobi
        "Trabalhar" if 10 <= clock.hour < 11 and inn_job1:
            call check_daytime
            call hour_check
            jump inn_jobw
        "Retornar":
            call pass_hour
            call check_daytime
            call hour_check
            jump mountains
