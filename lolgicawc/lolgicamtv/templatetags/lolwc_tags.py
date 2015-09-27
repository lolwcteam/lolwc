from django import template

register = template.Library()


#Deprecated
@register.simple_tag
def getTime(pos, minutos, segundos): # Only one argument.
    """Converts a string into all lowercase"""
    pos = int (pos)
    return '<span id="time">tiempo: {} min {} sec</span><br>'.format(minutos[pos], segundos[pos])

@register.simple_tag
def getChampions(pos, array):
    pos = int (pos)
    if(pos!=0):
        pos+=1
        if(pos%2 != 0):
            pos+=1
    return '<span id="player_blue_1_name"> {} </span><br><img id="player_blue_1_img" src="#">'.format(array[pos])

@register.simple_tag
def getChampionsb(pos, array):
    pos = int(pos) + 1
    if(pos%2 == 0):
        pos+=1
    return '<span id="player_blue_1_name"> {} </span><br><img id="player_blue_1_img" src="#">'.format(array[pos])
