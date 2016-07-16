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
    
    
    
    

##############################################################################
# ENTREVISTAS DE EMPREGO
#
# 
#