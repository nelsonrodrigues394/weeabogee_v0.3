##############################################################################
# Events
#
# This file is used to store all the events triggered as you play through the
# game. Events can be triggered by a choice made by the player or by stats.

    
label workout:
    
    #aumento de stat aqui
    
    call pass_hour
    call pass_hour
    call pass_hour
    call pass_hour
    call hour_check
    $ constituicao.giveExp(100)
    
    "Você malhou e se sente em melhor forma."
    
    jump gym
    
label bird_watching:
    
    call pass_hour
    call pass_hour
    call pass_hour
    call pass_hour
    call hour_check
    $ percepcao.giveExp(1)
    "Você passou algum tempo observando os pássaros ao ar livre."
    jump park
    
label book_reading:
    
    call pass_hour
    call pass_hour
    call pass_hour
    call pass_hour
    call hour_check
    $ inteligencia.giveExp(1)
    "Você passou algumas horas lendo um bom livro."
    jump home
    
label pub_social:
    
    call pass_hour
    call pass_hour
    call pass_hour
    call pass_hour
    call hour_check
    $ carisma.giveExp(1)
    "Você conheceu novas pessoas e se entreteu."
    jump pub
    

##############################################################################
# SKILL RELEASES
#
#
#

label lp_event:
    
    "Você adentra o Maid Cafe e é recebido calorosamente pelas maids do
     estabelecimento. Uma delas lhe guia à sua mesa e lhe dá um menu."
    "Após fazer o seu pedido, você sente uma vontade insana de ir ao banheiro."
    scene black with fade
    "Aliviado, você lava suas mãos e abre a porta."
    "*THUD*"
    "Você atingiu algo com força com a porta. Saindo rapidamente, você descobre
     que trata-se de um rapaz, gordo, nos seus trinta e poucos anos."
    lp_teacher "Caralho! Toma mais cuidado, porra!"
    "Ele se levanta, enquanto recolhe algumas coisas do chão. Você nota que
     tratam-se de pequeno objetos metálicos. Ele estava tentando arrombar
     uma das portas."
    mc "Ei, que caralho você está fazendo?"
    lp_teacher "O quê? Não, não é nada."
    mc "Não é nada? Eu vou chamar o gerente."
    lp_teacher "Ei, ei, ei, pera, pera. OK, você venceu."
    lp_teacher "Eu estava tentando invadir o vestiário das garotas pra... 
                Você sabe, né?"
    lp_teacher "Enfim, você não quer me ajudar? Fica ali no fim do corredor
                e caso alguém venha, você me avisa."
    mc "Você está maluco. Eu não quero ser pego por tão pouco."
    lp_teacher "Que tal se em troca eu te dar esse meu estojo de arrombamento
                e te ensinar umas manhas? Assim você sai ganhando e eu cheiro
                as minhas calcinhas."
    "Sem nem pensar você dá meia volta e monta guarda no fim do corredor."
    scene maidcafe with fade
    "..."
    "... ..."
    "... ... ..."
    "Depois de algum tempo, você resolve checar o gordo e o mesmo já não estava
     mais lá."
    scene black
    mc "Cadê esse filho da..."
    "Você corre em direção ao vestiário e atravessa sua porta. O que você
     encontra não é a coisa mais agradável aos olhos..."
    "O gordo está abrindo as portas dos armários e enfiando todas as calcinhas
     que encontra dentro de sua mochila. Não tarda e ele te nota."
    lp_teacher "Que houve? Tem alguém vindo?"
    mc "Não... Eu só..."
    "No mesmo instante, você ouve vozes que se aproximam de você pelo corredor."
    mc "TÃO VINDO, PORRA!"
    lp_teacher "CARALHO, MAS VOCÊ É UM IDIOTA! POR QUE SAIU DE LÁ?"
    mc "Vai se foder! Eu achei que você tinha fugido!"
    lp_teacher "Fugido?! Pau no seu... Enfim... Precisamos sair daqui. AGORA."
    mc "Ali, pela janela, rápido!"
    "Você e o gordo começam a correr em direção à janela. Chegando primeiro,
     você a abre e pula."
    mc "Puta que pariu, mas que merda..."
    "Quando você volta o olhar, vê o gordo entalado."
    mc "Isso só pode ser brincadeira... DEIXA A MOCHILA!"
    lp_teacher "MAS NEM FODENDO!"
    mc "Pelo amor... OK, OK, me passa ela primeiro, depois você sai. OK?"
    lp_teacher "OK..."
    
    call check_daytime
        
    if current_daytime == "Manhã":
        scene center_a
    elif current_daytime == "Tarde":
        scene center_b
    elif current_daytime == "Noite":
        scene center_c
        
    "Ofegantes, você só param de correr quando chegam ao centro, longe do
     Maid Cafe"
    lp_teacher "Hahaha... *respiração pesada* Missão cumprida!"
    mc "Pra puta que lhe pariu! Me dá logo esse estojo pra eu dar o fora daqui."
    lp_teacher "Pra que a pressa?"
    "O gordo abre a mochila e começa a procurar por algo."
    lp_teacher "Cadê a minha bombinha...?"
    mc "Você tá de sacanagem, porra! Me dá logo essa merda."
    lp_teacher "OK, OK..."
    "Ele retira e te dá um pequeno estojo da mochila. Em seguida lhe ensina
     como usá-lo e vai embora, agradecendo e acenando ao longe."
    
    $ lockpick.setLevel(1)
    call pass_hour
    call pass_hour
    
    jump center
    
    
label lab_event:
    
    "Você entra no laboratório de química da escola."
    "Ali você descobre equipamentos e livros sobre química básica. Um deles
     sobre desenvolvimento de drogas sintéticas chama-lhe a atenção."
    "Você o leva para casa emprestado."
    
    $ labSkill.setLevel(1)
    call pass_hour
    
    jump school
    
    
    
    

##############################################################################
# ENTREVISTAS DE EMPREGO
#
# 
#
