image bg black = "black.jpg"
image bg PC = "bg PC.jpg"
    
init python:
    clock = Clock(7,0)

    show_date = False
    show_clock = False
    
label start:    
    
    $ calendar = Calendar(1, 1, 2016)
    $ current_daytime = None
    $ actions = 0
    $ money = 0
    
    $ percepcao = Level("Percepção")
    $ constituicao = Level("Constituição")
    $ inteligencia = Level("Inteligência")
    $ carisma = Level("Carisma")
    $ reputacao = Level("Reputação")
    
    $ sorte = Level("Sorte")
    
    $ lockpick = Level("Arrombamento", 0, 0)
    $ hipnose = Level("Hipnose", 0, 0)
    $ hacking = Level("Hacking", 0, 0)
    $ labSkill = Level("Sinteticos",0 ,0)
    
    $ was_home = True
    
    "Seja bem-vindo."
    "Hoje é o seu primeiro dia nesta nova cidade."
    "Divirta-se!"
    
    jump day
    
label was_home_true:
    $ was_home = True
    
    return
    
label day:
    scene bg black
    show screen menu_button
    show screen calendar_screen
    show screen clock_screen
    
    call check_daytime
    
    jump home
    
label was_home_false:
    $ was_home = False
    return

label sleep_time:
    
    "Você está cansado e resolve voltar para casa dormir."
    
    scene bg black
    
    "Você teve uma ótima noite de sono."
    
    $ calendar.next()
    $ clock.dayHour()
    
    jump day
