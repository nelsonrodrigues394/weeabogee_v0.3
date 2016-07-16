init:
    
    $ office_job1 = False
    $ arcade_job1 = False
    $ hosp_job1 = False
    $ restau_job1 = False
    $ pub_job1 = False
    $ school_job1 = False
    $ conven_job1 = False
    $ inn_job1 = False
    $ beach_job1 = False
    $ gym_job1 = False
    $ rural_job1 = False   
    
    
label office_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como office boy."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = True
            $ arcade_job1 = False
            $ hosp_job1 = False
            $ restau_job1 = False
            $ pub_job1 = False
            $ school_job1 = False
            $ conven_job1 = False
            $ inn_job1 = False
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump office
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump office
            
label arcade_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como balconista."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = True
            $ hosp_job1 = False
            $ restau_job1 = False
            $ pub_job1 = False
            $ school_job1 = False
            $ conven_job1 = False
            $ inn_job1 = False
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump arcade
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump arcade
            
label hosp_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como faxineiro."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = False
            $ hosp_job1 = True
            $ restau_job1 = False
            $ pub_job1 = False
            $ school_job1 = False
            $ conven_job1 = False
            $ inn_job1 = False
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump hospital
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump hospital
            
label restau_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como garçom."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = False
            $ hosp_job1 = False
            $ restau_job1 = True
            $ pub_job1 = False
            $ school_job1 = False
            $ conven_job1 = False
            $ inn_job1 = False
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump restaurant
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump restaurant
            
label pub_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como bartender."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = False
            $ hosp_job1 = False
            $ restau_job1 = False
            $ pub_job1 = True
            $ school_job1 = False
            $ conven_job1 = False
            $ inn_job1 = False
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump pub
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump pub
            
label school_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como zelador."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = False
            $ hosp_job1 = False
            $ restau_job1 = False
            $ pub_job1 = False
            $ school_job1 = True
            $ conven_job1 = False
            $ inn_job1 = False
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump school
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump school
    
label conven_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como caixa."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = False
            $ hosp_job1 = False
            $ restau_job1 = False
            $ pub_job1 = False
            $ school_job1 = False
            $ conven_job1 = True
            $ inn_job1 = False
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump convenience
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump convenience
            
label inn_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como cozinheiro."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = False
            $ hosp_job1 = False
            $ restau_job1 = False
            $ pub_job1 = False
            $ school_job1 = False
            $ conven_job1 = False
            $ inn_job1 = True
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump inn
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump inn
            
label beach_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como vendedor de chinelo."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = False
            $ hosp_job1 = False
            $ restau_job1 = False
            $ pub_job1 = False
            $ school_job1 = False
            $ conven_job1 = False
            $ inn_job1 = False
            $ beach_job1 = True
            $ gym_job1 = False
            $ rural_job1 = False
            "Você aceitou a oferta de trabalho."
            jump beach
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump beach
            
label gym_jobi:

    if  constituicao.getLevel() >= 3:
        "Existe uma oferta de trabalho. A oferta é de $25 por dia como personal trainer."
        "Você deseja aceitar a vaga?"
        menu:
            "Aceitar":
                $ office_job1 = False
                $ arcade_job1 = False
                $ hosp_job1 = False
                $ restau_job1 = False
                $ pub_job1 = False
                $ school_job1 = False
                $ conven_job1 = False
                $ inn_job1 = False
                $ beach_job1 = False
                $ gym_job1 = True
                $ rural_job1 = False
                "Você aceitou a oferta de trabalho."
                jump gym
            "Recusar":
                "Você recusa educadamente a oferta de trabalho e se retira."
                jump gym
    else:
        "Você não está qualificado para esta oferta de trabalho"
        jump gym

label rural_jobi:
    
    "Existe uma oferta de trabalho. A oferta é de $10 por dia como motorista de trator sem camisa."
    "Você deseja aceitar a vaga?"
    
    menu:
        "Aceitar":
            $ office_job1 = False
            $ arcade_job1 = False
            $ hosp_job1 = False
            $ restau_job1 = False
            $ pub_job1 = False
            $ school_job1 = False
            $ conven_job1 = False
            $ inn_job1 = False
            $ beach_job1 = False
            $ gym_job1 = False
            $ rural_job1 = True
            "Você aceitou a oferta de trabalho."
            jump rural
        "Recusar":
            "Você recusa educadamente a oferta de trabalho e se retira."
            jump rural


### ----

label office_jobw:
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump office
            
label arcade_jobw:
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump arcade
            
label hosp_jobiw
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump hospital
            
label restau_jobw:
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump restaurant
            
label pub_jobw:
    
   "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump pub
            
label school_jobw:
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump school
    
label conven_jobw:
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump convenience
            
label inn_jobw:
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump inn
            
label beach_jobw:
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump beach
            
label gym_jobw:

    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump gym

label rural_jobw:
    
    "Você trabalhou hoje durante 6 horas e ganhou $10"
    $ money += 10
    $ clock.jobHour()
    
    jump rural