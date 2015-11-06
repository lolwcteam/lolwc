from django import template

register = template.Library()


@register.filter()
def toInt(value):
    return int(value)

@register.filter
def getItem(dictionary, key):
    return dictionary

#Deprecated
@register.simple_tag
def getTime(pos, minutos, segundos): # Only one argument.
    """Converts a string into all lowercase"""
    pos = int (pos)
    return '<span id="time">tiempo: {} min {} sec</span><br>'.format(minutos[pos], segundos[pos])

@register.simple_tag
def getChampions(pos, array):
    pos = int(pos)
    pos=pos*2
    for x in range(5):
        if(x==1):
            personajes=array[pos]
            pj1=personajes[0]
        elif(x==2):
            personajes=array[pos]
            pj2=personajes[1]
        elif(x==3):
            personajes=array[pos]
            pj3=personajes[2]
        elif(x==4):
            personajes=array[pos]
            pj4=personajes[3]
        else:
            personajes=array[pos]
            pj5=personajes[4]

    return """<span id="player_blue_1_name">
{}
<br>
{}
<br>
{}
<br>
{}
<br>
{} </span><br><img id="player_blue_1_img" src="#">""".format(pj1, pj2, pj3, pj4, pj5)

@register.simple_tag
def getChampionsb(pos, array):
    pos = int(pos)
    pos=1+pos*2
    for x in range(5):
        if(x==1):
            personajes=array[pos]
            pj1=personajes[0]
        elif(x==2):
            personajes=array[pos]
            pj2=personajes[1]
        elif(x==3):
            personajes=array[pos]
            pj3=personajes[2]
        elif(x==4):
            personajes=array[pos]
            pj4=personajes[3]
        else:
            personajes=array[pos]
            pj5=personajes[4]
    return """<span id="player_blue_1_name">
{}
<br>
{}
<br>
{}
<br>
{}
<br>
{} </span><br><img id="player_blue_1_img" src="#">""".format(pj1, pj2, pj3, pj4, pj5)
