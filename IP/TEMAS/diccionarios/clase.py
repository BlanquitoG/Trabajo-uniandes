'''
 al momento de hacer un imput, no se tiene que poner ',' ya que este no recive parametros
 Lo que se tiene que hacer es +
 
 cel = 1238021840912
 
 input('Ingrese su nombre' + cel +': ')
 
 '''
 
 
direc = {}

direc['Nico'] = 23948912840

direc ['Juan'] = 209389492104

direc['Bautista'] = 21984092814

alias = direc.copy()

alias['Juan'] = 'Borrado'

nombre = {'asfkjlkflkaksf': 84023850,
          'hoa': 29082904}

nombre.pop('asfkjlkflkaksf')


def parametros(a: dict)-> None:
    print(a)
    a['Nico'] = 940928194812
    print(a)


parametros(alias)