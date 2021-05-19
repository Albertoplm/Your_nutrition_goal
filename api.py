  
import streamlit as st
from tools.configuration import db, collection, collection2
import tools.getdata as get
import pandas as pd
import altair as alt
from PIL import Image
import tools.funciones as funciones
#from mplsoccer import Radar, FontManager
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Your nutrition goal", page_icon="🤸‍♂️", layout='centered', initial_sidebar_state='auto')

menu = ["Home", "Login", "SignUp"]
menu_choice = st.sidebar.selectbox('Menu', menu)
if menu_choice == "Login":
    st.subheader("Login")

    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.checkbox("Login"):
        result = get.iniciar_sesion(username, password)
        if result: 

            st.success("Logged in as {}".format(username))
            task = st.selectbox("Acción", ["Añadir comidas del día", "Información", "Perfil"])
            if task == "Añadir comidas del día":
                alimentos = []
                for x in get.nombre_alimentos():
                    for k in x:
                        valor = x[k]
                        alimentos.append(valor) 

                st.subheader("Añade tus comidas")
                #Defino suma de macros para que no me de error si se pone 0 en algun horario
                
                linea_desayuno = "0"
                linea_comida = "0"
                linea_cena = "0"
                linea_otros = "0"
                desayuno = 0
                comida = 0
                cena = 0
                otros = 0
                suma_macros_desayuno = 0
                suma_macros_comida = 0
                suma_macros_cena = 0
                suma_macros_otros = 0

                #DESAYUNO

                st.subheader("Desayuno")
                if st.checkbox("¿Quieres añadir alimentos para el desayuno?"):
                    mas = ["0","+1", "+2", "+3", "+4", "+5"]
                    linea_desayuno = st.radio(
                        '¿Cuantos alimentos deseas añadir al desayuno?',
                        mas)
                    'Has seleccionado: ', linea_desayuno

                    des1 = 0 
                    des2 = 0 
                    des3 = 0 
                    des4 = 0 
                    des5 = 0
                    desayuno1 = 0 
                    desayuno2 = 0 
                    desayuno3 = 0 
                    desayuno4 = 0 
                    desayuno5 = 0


                    if linea_desayuno == "+1" or linea_desayuno == "+2" or linea_desayuno == "+3" or linea_desayuno == "+4" or linea_desayuno == "+5":
                        desayuno1 = st.selectbox(
                            'Seleccione alimento:',
                            alimentos)
                        'Has seleccionado: ', desayuno1
                        gr = st.slider('¿Cual es la cantidad en gramos?', 0, 500)
                        p_gr= gr/100
                        des1 = pd.DataFrame(get.buscar_alimento_usuario(desayuno1))
                        des1 = funciones.alimentos_gr(des1, p_gr)
                        st.write(des1)



                    if linea_desayuno == "+2" or linea_desayuno == "+3" or linea_desayuno == "+4" or linea_desayuno == "+5":
                        desayuno2 = st.selectbox(
                        'Seleccione el segundo alimento',
                        alimentos)
                        'Has seleccionado: ', desayuno2
                        gr = st.slider('¿Cual es la cantidad en gramos para el segundo alimento?', 0, 500)
                        p_gr= gr/100
                        des2 = pd.DataFrame(get.buscar_alimento_usuario(desayuno2))
                        des2 = funciones.alimentos_gr(des2, p_gr)
                        st.write(des2)


                    if linea_desayuno == "+3" or linea_desayuno == "+4" or linea_desayuno == "+5":
                        desayuno3 = st.selectbox(
                        'Seleccione el tercero alimento',
                        alimentos)
                        'Has seleccionado: ', desayuno3
                        gr = st.slider('¿Cual es la cantidad en gramos para el tercer alimento?', 0, 500)
                        p_gr= gr/100
                        des3 = pd.DataFrame(get.buscar_alimento_usuario(desayuno3))
                        des3 = funciones.alimentos_gr(des3, p_gr)
                        st.write(des3)

                    if linea_desayuno == "+4" or linea_desayuno == "+5":
                        desayuno4 = st.selectbox(
                        'Seleccione el cuarto alimento',
                        alimentos)
                        'Has seleccionado: ', desayuno4
                        gr = st.slider('¿Cual es la cantidad en gramos para el cuarto alimento?', 0, 500)
                        p_gr= gr/100
                        des4 = pd.DataFrame(get.buscar_alimento_usuario(desayuno4))
                        des4 = funciones.alimentos_gr(des4, p_gr)
                        st.write(des4)

                    if linea_desayuno == "+5":
                        desayuno5 = st.selectbox(
                        'Seleccione el quinto alimento',
                        alimentos)
                        'Has seleccionado: ', desayuno5
                        gr = st.slider('¿Cual es la cantidad en gramos para el quinto alimento?', 0, 500)
                        p_gr= gr/100
                        des5 = pd.DataFrame(get.buscar_alimento_usuario(desayuno5))
                        des5 = funciones.alimentos_gr(des5, p_gr)
                        st.write(des5)
                    

                    if linea_desayuno != "0":
                        numero_desayuno = int(linea_desayuno[-1]) + 1
                        desayuno_lista = [(globals()[f"des{i}"]) for i in range(1,numero_desayuno)]
                        desayuno = pd.concat(desayuno_lista[:numero_desayuno])
                        st.write("Este es tu resumen del desayuno:", desayuno)


                    if linea_desayuno != "0":
                        suma_macros_desayuno = desayuno[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
                        st.write("Este es el total de tus macros para el desayuno", suma_macros_desayuno)

                #COMIDA

                st.subheader("Comida")
                if st.checkbox("¿Quieres añadir alimentos para la comida?"):
                    mas = ["0","+1", "+2", "+3", "+4", "+5"]
                    linea_comida = st.radio(
                        '¿Cuantos alimentos deseas añadir a la comida?',
                        mas)
                    'Has seleccionado: ', linea_comida

                    comida1 = 0 
                    comida2 = 0 
                    comida3 = 0 
                    comida4 = 0 
                    comida5 = 0


                    if linea_comida == "+1" or linea_comida == "+2" or linea_comida == "+3" or linea_comida == "+4" or linea_comida == "+5":
                        comida1 = st.selectbox(
                            'Seleccione alimento para la comida:',
                            alimentos)
                        'Has seleccionado: ', comida1
                        gr = st.slider('¿Cual es la cantidad en gramos para este alimento de la comida?', 0, 500)
                        p_gr= gr/100
                        com1 = pd.DataFrame(get.buscar_alimento_usuario(comida1))
                        com1 = funciones.alimentos_gr(com1, p_gr)
                        st.write(com1)



                    if linea_comida == "+2" or linea_comida == "+3" or linea_comida == "+4" or linea_comida == "+5":
                        comida2 = st.selectbox(
                        'Seleccione el segundo alimento para la comida',
                        alimentos)
                        'Has seleccionado: ', comida2
                        gr = st.slider('¿Cual es la cantidad en gramos para el segundo alimento de la comida?', 0, 500)
                        p_gr= gr/100
                        com2 = pd.DataFrame(get.buscar_alimento_usuario(comida2))
                        com2 = funciones.alimentos_gr(com2, p_gr)
                        st.write(com2)


                    if linea_comida == "+3" or linea_comida == "+4" or linea_comida == "+5":
                        comida3 = st.selectbox(
                        'Seleccione el tercero alimento para la comida',
                        alimentos)
                        'Has seleccionado: ', comida3
                        gr = st.slider('¿Cual es la cantidad en gramos para el tercer alimento de la comida?', 0, 500)
                        p_gr= gr/100
                        com3 = pd.DataFrame(get.buscar_alimento_usuario(comida3))
                        com3 = funciones.alimentos_gr(com3, p_gr)
                        st.write(com3)

                    if linea_comida == "+4" or linea_comida == "+5":
                        comida4 = st.selectbox(
                        'Seleccione el cuarto alimento para la comida',
                        alimentos)
                        'Has seleccionado: ', comida4
                        gr = st.slider('¿Cual es la cantidad en gramos para el cuarto alimento de la comida?', 0, 500)
                        p_gr= gr/100
                        com4 = pd.DataFrame(get.buscar_alimento_usuario(comida4))
                        com4 = funciones.alimentos_gr(com4, p_gr)
                        st.write(com4)

                    if linea_comida == "+5":
                        comida5 = st.selectbox(
                        'Seleccione el quinto alimento para la comida',
                        alimentos)
                        'Has seleccionado: ', comida5
                        gr = st.slider('¿Cual es la cantidad en gramos para el quinto alimento de la comida?', 0, 500)
                        p_gr= gr/100
                        com5 = pd.DataFrame(get.buscar_alimento_usuario(comida5))
                        com5 = funciones.alimentos_gr(com5, p_gr)
                        st.write(com5)

                    if linea_comida != "0":
                        numero_comida = int(linea_comida[-1]) + 1
                        comida_lista = [(globals()[f"com{i}"]) for i in range(1,numero_comida)]
                        comida = pd.concat(comida_lista[:numero_comida])
                        st.write("Este es tu resumen del comida:", comida)

                    if linea_comida != "0":
                        suma_macros_comida = comida[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
                        st.write("Este es el total de tus macros para la comida", suma_macros_comida)

                #CENA

                st.subheader("Cena")
                
                if st.checkbox("¿Quieres añadir alimentos para la cena?"):
                    
                    mas = ["0","+1", "+2", "+3", "+4", "+5"]
                    linea_cena = st.radio(
                        '¿Cuantos alimentos deseas añadir a la cena?',
                        mas)
                    'Has seleccionado: ', linea_cena

                    cena1 = 0 
                    cena2 = 0 
                    cena3 = 0 
                    cena4 = 0 
                    cena5 = 0
                

                    if linea_cena == "+1" or linea_cena == "+2" or linea_cena == "+3" or linea_cena == "+4" or linea_cena == "+5":
                        cena1 = st.selectbox(
                            'Seleccione alimento para la cena:',
                            alimentos)
                        'Has seleccionado: ', cena1
                        gr = st.slider('¿Cual es la cantidad en gramos para este alimento de la cena?', 0, 500)
                        p_gr= gr/100
                        cen1 = pd.DataFrame(get.buscar_alimento_usuario(cena1))
                        cen1 = funciones.alimentos_gr(cen1, p_gr)
                        st.write(cen1)



                    if linea_cena == "+2" or linea_cena == "+3" or linea_cena == "+4" or linea_cena == "+5":
                        cena2 = st.selectbox(
                        'Seleccione el segundo alimento para la cena',
                        alimentos)
                        'Has seleccionado: ', cena2
                        gr = st.slider('¿Cual es la cantidad en gramos para el segundo alimento de la cena?', 0, 500)
                        p_gr= gr/100
                        cen2 = pd.DataFrame(get.buscar_alimento_usuario(cena2))
                        cen2 = funciones.alimentos_gr(cen2, p_gr)
                        st.write(cen2)


                    if linea_cena == "+3" or linea_cena == "+4" or linea_cena == "+5":
                        cena3 = st.selectbox(
                        'Seleccione el tercero alimento para la cena',
                        alimentos)
                        'Has seleccionado: ', cena3
                        gr = st.slider('¿Cual es la cantidad en gramos para el tercer alimento de la cena?', 0, 500)
                        p_gr= gr/100
                        cen3 = pd.DataFrame(get.buscar_alimento_usuario(cena3))
                        cen3 = funciones.alimentos_gr(cen3, p_gr)
                        st.write(cen3)

                    if linea_cena == "+4" or linea_cena == "+5":
                        cena4 = st.selectbox(
                        'Seleccione el cuarto alimento para la cena',
                        alimentos)
                        'Has seleccionado: ', cena4
                        gr = st.slider('¿Cual es la cantidad en gramos para el cuarto alimento de la cena?', 0, 500)
                        p_gr= gr/100
                        cen4 = pd.DataFrame(get.buscar_alimento_usuario(cena4))
                        cen4 = funciones.alimentos_gr(cen4, p_gr)
                        st.write(cen4)

                    if linea_cena == "+5":
                        cena5 = st.selectbox(
                        'Seleccione el quinto alimento para la cena',
                        alimentos)
                        'Has seleccionado: ', cena5
                        gr = st.slider('¿Cual es la cantidad en gramos para el quinto alimento de la cena?', 0, 500)
                        p_gr= gr/100
                        cen5 = pd.DataFrame(get.buscar_alimento_usuario(cena5))
                        cen5 = funciones.alimentos_gr(cen5, p_gr)
                        st.write(cen5)

                    if linea_cena != "0":
                        numero_cena = int(linea_cena[-1]) + 1
                        cena_lista = [(globals()[f"cen{i}"]) for i in range(1,numero_cena)]
                        cena = pd.concat(cena_lista[:numero_cena])
                        st.write("Este es tu resumen del cena:", cena)

                    if linea_cena != "0":
                        suma_macros_cena = cena[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
                        st.write("Este es el total de tus macros para la cena", suma_macros_cena)

                #OTROS

                st.subheader("Otros")
                if st.checkbox("¿Quieres añadir más alimentos?"):
                    mas = ["0","+1", "+2", "+3", "+4", "+5"]
                    linea_otros = st.radio(
                        '¿Cuantos alimentos deseas añadir a otros?',
                        mas)
                    'Has seleccionado: ', linea_otros

                    otros1 = 0 
                    otros2 = 0 
                    otros3 = 0 
                    otros4 = 0 
                    otros5 = 0


                    if linea_otros == "+1" or linea_otros == "+2" or linea_otros == "+3" or linea_otros == "+4" or linea_otros == "+5":
                        otros1 = st.selectbox(
                            'Seleccione alimento para otros:',
                            alimentos)
                        'Has seleccionado: ', otros1
                        gr = st.slider('¿Cual es la cantidad en para este alimento de otros?', 0, 500)
                        p_gr= gr/100
                        otr1 = pd.DataFrame(get.buscar_alimento_usuario(otros1))
                        otr1 = funciones.alimentos_gr(otr1, p_gr)
                        st.write(otr1)



                    if linea_otros == "+2" or linea_otros == "+3" or linea_otros == "+4" or linea_otros == "+5":
                        otros2 = st.selectbox(
                        'Seleccione el segundo alimento para otros',
                        alimentos)
                        'Has seleccionado: ', otros2
                        gr = st.slider('¿Cual es la cantidad en gramos para el segundo alimento de otros?', 0, 500)
                        p_gr= gr/100
                        otr2 = pd.DataFrame(get.buscar_alimento_usuario(otros2))
                        otr2 = funciones.alimentos_gr(otr2, p_gr)
                        st.write(otr2)


                    if linea_otros == "+3" or linea_otros == "+4" or linea_otros == "+5":
                        otros3 = st.selectbox(
                        'Seleccione el tercero alimento para otros',
                        alimentos)
                        'Has seleccionado: ', otros3
                        gr = st.slider('¿Cual es la cantidad en gramos para el tercer alimento de otros?', 0, 500)
                        p_gr= gr/100
                        otr3 = pd.DataFrame(get.buscar_alimento_usuario(otros3))
                        otr3 = funciones.alimentos_gr(otr3, p_gr)
                        st.write(otr2)

                    if linea_otros == "+4" or linea_otros == "+5":
                        otros4 = st.selectbox(
                        'Seleccione el cuarto alimento para otros',
                        alimentos)
                        'Has seleccionado: ', otros4
                        gr = st.slider('¿Cual es la cantidad en gramos para el cuarto alimento de otros?', 0, 500)
                        p_gr= gr/100
                        otr4 = pd.DataFrame(get.buscar_alimento_usuario(otros4))
                        otr4 = funciones.alimentos_gr(otr4, p_gr)
                        st.write(otr4)

                    if linea_otros == "+5":
                        otros5 = st.selectbox(
                        'Seleccione el quinto alimento para otros',
                        alimentos)
                        'Has seleccionado: ', otros5
                        gr = st.slider('¿Cual es la cantidad en gramos para el quinto alimento de otros?', 0, 500)
                        p_gr= gr/100
                        otr5 = pd.DataFrame(get.buscar_alimento_usuario(otros5))
                        otr5 = funciones.alimentos_gr(otr5, p_gr)
                        st.write(otr5)

                    if linea_otros != "0":
                        numero_otros = int(linea_otros[-1]) + 1
                        otros_lista = [(globals()[f"otr{i}"]) for i in range(1,numero_otros)]
                        otros = pd.concat(otros_lista[:numero_otros])
                        st.write("Este es tu resumen del otros:", otros)

                    if linea_otros != "0":
                        suma_macros_otros = otros[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
                        st.write("Este es el total de tus macros para otros", suma_macros_otros)

                if linea_desayuno != "0" or linea_comida != "0" or linea_cena != "0" or linea_otros != "0":
                    total = suma_macros_desayuno+suma_macros_comida+suma_macros_cena+suma_macros_otros
                    st.subheader("La suma total de las kcal para todo el día son:")
                    st.write(total)


                if linea_desayuno != "0" or linea_comida != "0" or linea_cena != "0" or linea_otros != "0":
                    alimentos_dia = funciones.concatenar(comida, desayuno, cena, otros)
                    st.write("Estos son todos los alimentos que vas a tomar hoy:", alimentos_dia)
                    alimentos = []
                    for x in alimentos_dia["Nombre"]:
                        alimentos.append(x)
                
                    alimentos_dia_dict = alimentos_dia.to_dict('records')
                    if st.checkbox("Añadir alimentos a mi perfil"):
                        get.añadir_comdias_dia_total(username, alimentos_dia_dict)
                        st.write("Se han añadido correctamente a tu perfil!")

            elif task == "Información":
                st.subheader("Información")

                st.write("¿Quieres añadir tu peso de esta semana?(Recomendamos añadir los lunes)")
                if st.checkbox("Si"):
                    peso = st.slider('¿Cual es tu peso actual en kg?', 0.0, 150.0)
                    cambio = st.slider('¿Cual su cambio en kg?', -5.0, +5.0)
                    if st.checkbox("Confirma que quiere añadir estos datos"):
                        get.añadir_peso_semanal(username, peso, cambio)
                        st.write("Su cambio se ha añadido correctametne")

                st.subheader("Evolución de tu peso:")
                evolucion_peso = get.evolucion_peso(username)
                st.area_chart(data=evolucion_peso)
                st.subheader("Gráfico perdidas y ganancias de peso:")
                evolucion_PyG = get.evolucion_PyG(username)
                st.bar_chart(data=evolucion_PyG)
                st.write("Llevas",get.dias_comida(username), "días en los que has introducido tus comidas")
                st.write("Tu media de macronutrientes ha sido de:", get.media_historico(username))
                media = get.media_historico(username)
                fig, ax = plt.subplots(figsize=(10, 5))
                ax1 = plt.barh('Macronutrientes','Media', data=media, align='center', alpha=0.5)
                st.pyplot(fig)
                top = get.top_alimentos(username)
                st.subheader("Top 10 alimentos:")
                st.write(top)

                #Gráfico kcal ingeridas por día

            elif task == ("Perfil"):
                st.subheader("Perfil del usuario")
                user_result = get.informacion_sesion(username, password)
                user_info = pd.DataFrame(user_result)
                st.write(user_info)
                st.write("¿Quieres cambiar la contraseña?")
                new_password = st.text_input("Nueva contraseña",type= 'password')
                new_password2 = st.text_input("Confirma tu nueva contraseña",type= 'password')
                if new_password == new_password2:
                    if st.checkbox("Confirmar nueva contraseña"):
                        get.change_password(username, new_password)
                        st.write("Tu contraseña se cambio correctamente")
        else:
            st.warning("Incorrect Username/Password")
if menu_choice == "SignUp":
    st.subheader("Crear nueva cuenta")
    new_user = st.text_input("Usuario")
    new_password = st.text_input("Contraseña", type= 'password')

    if st.button("Registrarse"):
        if get.comprobar_usuario(new_user) == [{'nombre': new_user}]:
            st.write("Usuario no disponible")
        else:
            get.añadir_usuario(new_user, new_password)
            st.success("Te has registrado correctamente")
            st.info("Ve a Menu para entrar con tu usuario")

if menu_choice == "Home":

    imagen = Image.open("images/finalproject.jpeg")
    col1, col2, col3 = st.beta_columns([2.5,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(imagen)
    with col3:
        st.write("")

    st.markdown("<h1 style='text-align: center; color: black; font-size: +4'>¿Preparado para cambiar tu estilo de vida?</h1>", unsafe_allow_html=True)
    st.write("<h1 style='text-align: center; color: black; font-size: medium'>¿Quieres conocer cuantas kcal deberías tomar a diario para cumplir tu objetivo?</h1>", unsafe_allow_html=True)            
    #select box to choose objective
    param_area = "Objetivo"
    objetivo = ["Perder peso", "Ganar masa muscular"]
    objetivo = st.selectbox(
        'Seleccione su objetivo',
        objetivo)
    'Has seleccionado: ', objetivo

    #select box to choose sex
    param_area = "Sexo"
    sexo = ["Hombre", "Mujer"]
    sexo = st.selectbox(
        'Seleccione su sexo',
        sexo)
    'Has seleccionado: ', sexo

    #select slider to choose age
    edad = st.slider('¿Cuál es tu edad?', 0, 100)

    #select slider to choose weight
    peso = st.slider('¿Cuál es su peso actual?', 0.0, 150.0)

    #select slider to choose height
    estatura = st.slider('¿Cuál es tu estatura actual en cm?', 0, 250)

    st.write("Has seleccionado:", edad, "años", peso, "kg", estatura, "cm")

    #Kcal to consume daily
    if sexo == "Hombre":
        TMBH = 66 + (13.7 * (peso)) + (5 * (estatura)) - (6.75 * (edad))
        if objetivo == "Perder peso":
            perdida = st.slider('¿Cuántos kg deseas perder?', 0.0, 50.0)
            st.write("Este seria tu peso final:", peso - perdida)
            st.write("Tu cuerpo consume", round(TMBH), "kcal en reposo, sin hacer nada, por lo tanto, debes consumir", round(TMBH*1.2 - 1000),"al día para perder", perdida ,"kg en ",round(perdida*7),
            " días (Se recomienda no perder más de un kilo por semana). En el caso de realizar deporte deberás sumarle esas kcal extra, es decir kcal extra +" , round(TMBH*1.2 - 1000))
        if objetivo == "Ganar masa muscular":
            ganancia = st.slider('¿Cuántos kg deseas ganar?', 0.0, 50.0)
            st.write("Este seria tu peso final:", peso + ganancia)
            st.write("Tu cuerpo consume", round(TMBH), "kcal en reposo, sin hacer nada, por lo tanto, debes consumir", round(TMBH*1.2 + 500),"al día para ganar", ganancia ,"kg en ",round((ganancia*2)*7),
            " días (Se recomienda no ganar más de medio kilo por semana). En el caso de realizar deporte deberás sumarle esas kcal extra, es decir kcal extra +" , round(TMBH*1.2 + 500))
    elif sexo == "Mujer":
        TMBM = 655 + (9.6 * peso) + (1.8 * estatura) - (4.7 * edad)
        if objetivo == "Perder peso":
            perdida = st.slider('¿Cuántos kg deseas perder?', 0.0, 50.0)
            st.write("Este seria tu peso final:", peso - perdida)
            st.write("Tu cuerpo consume", round(TMBM), "kcal en reposo, sin hacer nada, por lo tanto, debes consumir", round(TMBM*1.2 - 1000),"al día para perder", perdida ,"kg en ",round(perdida*7),
            " días (Se recomienda no perder más de un kilo por semana). En el caso de realizar deporte deberás sumarle esas kcal extra, es decir kcal extra +" , round(TMBM*1.2 - 1000))
        if objetivo == "Ganar masa muscular":
            ganancia = st.slider('¿Cuántos kg deseas ganar?', 0.0, 100.0)
            st.write("Este seria tu peso final:", peso + ganancia)
            st.write("Tu cuerpo consume", round(TMBM), "kcal en reposo, sin hacer nada, por lo tanto, debes consumir", round(TMBM*1.2 + 500),"al día para ganar", ganancia ,"kg en ",round((ganancia*2)*7),
            " días (Se recomienda no ganar más de medio kilo por semana). En el caso de realizar deporte deberás sumarle esas kcal extra, es decir kcal extra +" , round(TMBM*1.2 + 500))

    #Macros
    #st.write("<h1 style='text-align: center; color: black; font-size: medium'>Ahora que ya conoces cuantas kcal debes consumir al día para cumplir tu objetivo, quieres dar un paso más para mejorar tu alimentación??</h1>", unsafe_allow_html=True)
    st.subheader("Ahora que ya conoces cuantas kcal debes consumir al día para cumplir tu objetivo, ¿quieres dar un paso más para mejorar tu alimentación?")
    st.write("<h1 style='text-align: center; color: black; font-size: medium'>¿Que son las macros??</h1>", unsafe_allow_html=True)

    st.write("Los macros no son otra cosa que los macronutrientes, los grupos de alimentos que nuestro cuerpo necesita para vivir: los carbohidratos, las proteínas y las grasas. Todos ellos contienen micronutrientes, es decir, vitaminas y minerales. La dieta de los macros o dieta flexible propone adelgazar o mantener el peso controlando los gramos de macronutrientes que ingerimos diariamente ¡Vamos a ello!")

    if sexo == "Hombre":
        if objetivo == "Perder peso":
            kcal_c = (TMBH*1.2 - 1000)
            st.write("Kcal totales", round(kcal_c))
            st.write("Proteinas entre:", round(kcal_c*0.25), "y", round(kcal_c*0.35), "de las kcal totales")
            st.write("Carbohidratos entre:", round(kcal_c*0.35), "y" ,round(kcal_c*0.45), "de las kcal totales")
            st.write("Grasas entre:", round(kcal_c*0.15), "y" ,round(kcal_c*0.25), "de las kcal totales")
        if objetivo == "Ganar masa muscular":
            kcal_c = (TMBH*1.2 + 500)
            st.write("Kcal totales", round(kcal_c*1.2 + 500))
            st.write("Proteinas entre:", round(kcal_c*0.20), "y", round(kcal_c*0.25), "de las kcal totales")
            st.write("Carbohidratos entre:", round(kcal_c*0.50), "y" ,round(kcal_c*0.55), "de las kcal totales")
            st.write("Grasas entre:", round(kcal_c*0.25) ,"y" ,round(kcal_c*0.30), "de las kcal totales")
    if sexo == "Mujer":
        if objetivo == "Perder peso":
            kcal_c = (TMBM*1.2 - 1000)
            st.write("Kcal totales", round(kcal_c*1.2 - 1000))
            st.write("Proteinas entre:", round(kcal_c*0.25), "y", round(kcal_c*0.35), "de las kcal totales")
            st.write("Carbohidratos entre:", round(kcal_c*0.35), "y" ,round(kcal_c*0.45), "de las kcal totales")
            st.write("Grasas entre:", round(kcal_c*0.15), "y" ,round(kcal_c*0.25), "de las kcal totales")
        if objetivo == "Ganar masa muscular":
            kcal_c = (TMBM*1.2 - 500)
            st.write("Kcal totales", round(kcal_c*1.2 + 500))
            st.write("Proteinas entre:", round(kcal_c*0.20), "y", round(kcal_c*0.25), "de las kcal totales")
            st.write("Carbohidratos entre:", round(kcal_c*0.50), "y" ,round(kcal_c*0.55), "de las kcal totales")
            st.write("Grasas entre:", round(kcal_c*0.25) ,"y" ,round(kcal_c*0.30), "de las kcal totales")

    #st.write("<h1 style='text-align: center; color: black; font-size: medium'>Para ayudarte a cumplir tu objetivo te facilitamos acceso a nuestra lista de alimentos con su información nutricional x 100gr</h1>", unsafe_allow_html=True)
    st.subheader("Para ayudarte a cumplir tu objetivo te facilitamos acceso a nuestra lista de alimentos con su información nutricional x 100gr")
    #Seleccion de alimentos

    #alimentosquerie = [get.nombre_alimentos()]
    alimentos = []
    for x in get.nombre_alimentos():
        for k in x:
            valor = x[k]
            alimentos.append(valor)
    alimento = st.selectbox(
        'Seleccione alimento',
        alimentos)
    'Has seleccionado: ', alimento

    st.write(pd.DataFrame(get.buscar_alimento_usuario(alimento)))

    st.subheader("Vamos a ver cómo podemos cuadrar los alimentos de mañana")

    #Defino suma de macros para que no me de error si se pone 0 en algun horario

    linea_desayuno = "0"
    linea_comida = "0"
    linea_cena = "0"
    linea_otros = "0"
    suma_macros_desayuno = 0
    suma_macros_comida = 0
    suma_macros_cena = 0
    suma_macros_otros = 0
    desayuno = 0
    comida = 0
    cena = 0
    otros = 0
    #DESAYUNO

    st.subheader("Desayuno")
    if st.checkbox("¿Quieres añadir alimentos para el desayuno?"):
        mas = ["0","+1", "+2", "+3", "+4", "+5"]
        linea_desayuno = st.radio(
            '¿Cuantos alimentos deseas añadir al desayuno?',
            mas)
        'Has seleccionado: ', linea_desayuno

        des1 = 0 
        des2 = 0 
        des3 = 0 
        des4 = 0 
        des5 = 0
        desayuno1 = 0 
        desayuno2 = 0 
        desayuno3 = 0 
        desayuno4 = 0 
        desayuno5 = 0


        if linea_desayuno == "+1" or linea_desayuno == "+2" or linea_desayuno == "+3" or linea_desayuno == "+4" or linea_desayuno == "+5":
            desayuno1 = st.selectbox(
                'Seleccione alimento:',
                alimentos)
            'Has seleccionado: ', desayuno1
            gr = st.slider('¿Cuál es la cantidad en gramos?', 0, 500)
            p_gr= gr/100
            des1 = pd.DataFrame(get.buscar_alimento_usuario(desayuno1))
            des1 = funciones.alimentos_gr(des1, p_gr)
            st.write(des1)



        if linea_desayuno == "+2" or linea_desayuno == "+3" or linea_desayuno == "+4" or linea_desayuno == "+5":
            desayuno2 = st.selectbox(
            'Seleccione el segundo alimento',
            alimentos)
            'Has seleccionado: ', desayuno2
            gr = st.slider('¿Cuál es la cantidad en gramos para el segundo alimento?', 0, 500)
            p_gr= gr/100
            des2 = pd.DataFrame(get.buscar_alimento_usuario(desayuno2))
            des2 = funciones.alimentos_gr(des2, p_gr)
            st.write(des2)


        if linea_desayuno == "+3" or linea_desayuno == "+4" or linea_desayuno == "+5":
            desayuno3 = st.selectbox(
            'Seleccione el tercero alimento',
            alimentos)
            'Has seleccionado: ', desayuno3
            gr = st.slider('¿Cuál es la cantidad en gramos para el tercer alimento?', 0, 500)
            p_gr= gr/100
            des3 = pd.DataFrame(get.buscar_alimento_usuario(desayuno3))
            des3 = funciones.alimentos_gr(des3, p_gr)
            st.write(des3)

        if linea_desayuno == "+4" or linea_desayuno == "+5":
            desayuno4 = st.selectbox(
            'Seleccione el cuarto alimento',
            alimentos)
            'Has seleccionado: ', desayuno4
            gr = st.slider('¿Cuál es la cantidad en gramos para el cuarto alimento?', 0, 500)
            p_gr= gr/100
            des4 = pd.DataFrame(get.buscar_alimento_usuario(desayuno4))
            des4 = funciones.alimentos_gr(des4, p_gr)
            st.write(des4)

        if linea_desayuno == "+5":
            desayuno5 = st.selectbox(
            'Seleccione el quinto alimento',
            alimentos)
            'Has seleccionado: ', desayuno5
            gr = st.slider('¿Cuál es la cantidad en gramos para el quinto alimento?', 0, 500)
            p_gr= gr/100
            des5 = pd.DataFrame(get.buscar_alimento_usuario(desayuno5))
            des5 = funciones.alimentos_gr(des5, p_gr)
            st.write(des5)
        

        if linea_desayuno != "0":
            numero_desayuno = int(linea_desayuno[-1]) + 1
            desayuno_lista = [(globals()[f"des{i}"]) for i in range(1,numero_desayuno)]
            desayuno = pd.concat(desayuno_lista[:numero_desayuno])
            st.write("Este es tu resumen del desayuno:", desayuno)


        if linea_desayuno != "0":
            suma_macros_desayuno = desayuno[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
            st.write("Este es el total de tus macros para el desayuno", suma_macros_desayuno)

    #COMIDA

    st.subheader("Comida")
    if st.checkbox("¿Quieres añadir alimentos para la comida?"):
        mas = ["0","+1", "+2", "+3", "+4", "+5"]
        linea_comida = st.radio(
            '¿Cuantos alimentos deseas añadir a la comida?',
            mas)
        'Has seleccionado: ', linea_comida

        comida1 = 0 
        comida2 = 0 
        comida3 = 0 
        comida4 = 0 
        comida5 = 0


        if linea_comida == "+1" or linea_comida == "+2" or linea_comida == "+3" or linea_comida == "+4" or linea_comida == "+5":
            comida1 = st.selectbox(
                'Seleccione alimento para la comida:',
                alimentos)
            'Has seleccionado: ', comida1
            gr = st.slider('¿Cuál es la cantidad en gramos para este alimento de la comida?', 0, 500)
            p_gr= gr/100
            com1 = pd.DataFrame(get.buscar_alimento_usuario(comida1))
            com1 = funciones.alimentos_gr(com1, p_gr)
            st.write(com1)



        if linea_comida == "+2" or linea_comida == "+3" or linea_comida == "+4" or linea_comida == "+5":
            comida2 = st.selectbox(
            'Seleccione el segundo alimento para la comida',
            alimentos)
            'Has seleccionado: ', comida2
            gr = st.slider('¿Cuál es la cantidad en gramos para el segundo alimento de la comida?', 0, 500)
            p_gr= gr/100
            com2 = pd.DataFrame(get.buscar_alimento_usuario(comida2))
            com2 = funciones.alimentos_gr(com2, p_gr)
            st.write(com2)


        if linea_comida == "+3" or linea_comida == "+4" or linea_comida == "+5":
            comida3 = st.selectbox(
            'Seleccione el tercero alimento para la comida',
            alimentos)
            'Has seleccionado: ', comida3
            gr = st.slider('¿Cuál es la cantidad en gramos para el tercer alimento de la comida?', 0, 500)
            p_gr= gr/100
            com3 = pd.DataFrame(get.buscar_alimento_usuario(comida3))
            com3 = funciones.alimentos_gr(com3, p_gr)
            st.write(com3)

        if linea_comida == "+4" or linea_comida == "+5":
            comida4 = st.selectbox(
            'Seleccione el cuarto alimento para la comida',
            alimentos)
            'Has seleccionado: ', comida4
            gr = st.slider('¿Cuál es la cantidad en gramos para el cuarto alimento de la comida?', 0, 500)
            p_gr= gr/100
            com4 = pd.DataFrame(get.buscar_alimento_usuario(comida4))
            com4 = funciones.alimentos_gr(com4, p_gr)
            st.write(com4)

        if linea_comida == "+5":
            comida5 = st.selectbox(
            'Seleccione el quinto alimento para la comida',
            alimentos)
            'Has seleccionado: ', comida5
            gr = st.slider('¿Cuál es la cantidad en gramos para el quinto alimento de la comida?', 0, 500)
            p_gr= gr/100
            com5 = pd.DataFrame(get.buscar_alimento_usuario(comida5))
            com5 = funciones.alimentos_gr(com5, p_gr)
            st.write(com5)

        if linea_comida != "0":
            numero_comida = int(linea_comida[-1]) + 1
            comida_lista = [(globals()[f"com{i}"]) for i in range(1,numero_comida)]
            comida = pd.concat(comida_lista[:numero_comida])
            st.write("Este es tu resumen del comida:", comida)

        if linea_comida != "0":
            suma_macros_comida = comida[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
            st.write("Este es el total de tus macros para la comida", suma_macros_comida)

    #CENA

    st.subheader("Cena")
    
    if st.checkbox("¿Quieres añadir alimentos para la cena?"):
        
        mas = ["0","+1", "+2", "+3", "+4", "+5"]
        linea_cena = st.radio(
            '¿Cuantos alimentos deseas añadir a la cena?',
            mas)
        'Has seleccionado: ', linea_cena

        cena1 = 0 
        cena2 = 0 
        cena3 = 0 
        cena4 = 0 
        cena5 = 0
    

        if linea_cena == "+1" or linea_cena == "+2" or linea_cena == "+3" or linea_cena == "+4" or linea_cena == "+5":
            cena1 = st.selectbox(
                'Seleccione alimento para la cena:',
                alimentos)
            'Has seleccionado: ', cena1
            gr = st.slider('¿Cuál es la cantidad en gramos para este alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen1 = pd.DataFrame(get.buscar_alimento_usuario(cena1))
            cen1 = funciones.alimentos_gr(cen1, p_gr)
            st.write(cen1)



        if linea_cena == "+2" or linea_cena == "+3" or linea_cena == "+4" or linea_cena == "+5":
            cena2 = st.selectbox(
            'Seleccione el segundo alimento para la cena',
            alimentos)
            'Has seleccionado: ', cena2
            gr = st.slider('¿Cuál es la cantidad en gramos para el segundo alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen2 = pd.DataFrame(get.buscar_alimento_usuario(cena2))
            cen2 = funciones.alimentos_gr(cen2, p_gr)
            st.write(cen2)


        if linea_cena == "+3" or linea_cena == "+4" or linea_cena == "+5":
            cena3 = st.selectbox(
            'Seleccione el tercero alimento para la cena',
            alimentos)
            'Has seleccionado: ', cena3
            gr = st.slider('¿Cuál es la cantidad en gramos para el tercer alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen3 = pd.DataFrame(get.buscar_alimento_usuario(cena3))
            cen3 = funciones.alimentos_gr(cen3, p_gr)
            st.write(cen3)

        if linea_cena == "+4" or linea_cena == "+5":
            cena4 = st.selectbox(
            'Seleccione el cuarto alimento para la cena',
            alimentos)
            'Has seleccionado: ', cena4
            gr = st.slider('¿Cuál es la cantidad en gramos para el cuarto alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen4 = pd.DataFrame(get.buscar_alimento_usuario(cena4))
            cen4 = funciones.alimentos_gr(cen4, p_gr)
            st.write(cen4)

        if linea_cena == "+5":
            cena5 = st.selectbox(
            'Seleccione el quinto alimento para la cena',
            alimentos)
            'Has seleccionado: ', cena5
            gr = st.slider('¿Cuál es la cantidad en gramos para el quinto alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen5 = pd.DataFrame(get.buscar_alimento_usuario(cena5))
            cen5 = funciones.alimentos_gr(cen5, p_gr)
            st.write(cen5)

        if linea_cena != "0":
            numero_cena = int(linea_cena[-1]) + 1
            cena_lista = [(globals()[f"cen{i}"]) for i in range(1,numero_cena)]
            cena = pd.concat(cena_lista[:numero_cena])
            st.write("Este es tu resumen del cena:", cena)

        if linea_cena != "0":
            suma_macros_cena = cena[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
            st.write("Este es el total de tus macros para la cena", suma_macros_cena)

    #OTROS

    st.subheader("Otros")
    if st.checkbox("¿Quieres añadir más alimentos?"):
        mas = ["0","+1", "+2", "+3", "+4", "+5"]
        linea_otros = st.radio(
            '¿Cuantos alimentos deseas añadir a otros?',
            mas)
        'Has seleccionado: ', linea_otros

        otros1 = 0 
        otros2 = 0 
        otros3 = 0 
        otros4 = 0 
        otros5 = 0


        if linea_otros == "+1" or linea_otros == "+2" or linea_otros == "+3" or linea_otros == "+4" or linea_otros == "+5":
            otros1 = st.selectbox(
                'Seleccione alimento para otros:',
                alimentos)
            'Has seleccionado: ', otros1
            gr = st.slider('¿Cuál es la cantidad en para este alimento de otros?', 0, 500)
            p_gr= gr/100
            otr1 = pd.DataFrame(get.buscar_alimento_usuario(otros1))
            otr1 = funciones.alimentos_gr(otr1, p_gr)
            st.write(otr1)



        if linea_otros == "+2" or linea_otros == "+3" or linea_otros == "+4" or linea_otros == "+5":
            otros2 = st.selectbox(
            'Seleccione el segundo alimento para otros',
            alimentos)
            'Has seleccionado: ', otros2
            gr = st.slider('¿Cuál es la cantidad en gramos para el segundo alimento de otros?', 0, 500)
            p_gr= gr/100
            otr2 = pd.DataFrame(get.buscar_alimento_usuario(otros2))
            otr2 = funciones.alimentos_gr(otr2, p_gr)
            st.write(otr2)


        if linea_otros == "+3" or linea_otros == "+4" or linea_otros == "+5":
            otros3 = st.selectbox(
            'Seleccione el tercero alimento para otros',
            alimentos)
            'Has seleccionado: ', otros3
            gr = st.slider('¿Cuál es la cantidad en gramos para el tercer alimento de otros?', 0, 500)
            p_gr= gr/100
            otr3 = pd.DataFrame(get.buscar_alimento_usuario(otros3))
            otr3 = funciones.alimentos_gr(otr3, p_gr)
            st.write(otr2)

        if linea_otros == "+4" or linea_otros == "+5":
            otros4 = st.selectbox(
            'Seleccione el cuarto alimento para otros',
            alimentos)
            'Has seleccionado: ', otros4
            gr = st.slider('¿Cuál es la cantidad en gramos para el cuarto alimento de otros?', 0, 500)
            p_gr= gr/100
            otr4 = pd.DataFrame(get.buscar_alimento_usuario(otros4))
            otr4 = funciones.alimentos_gr(otr4, p_gr)
            st.write(otr4)

        if linea_otros == "+5":
            otros5 = st.selectbox(
            'Seleccione el quinto alimento para otros',
            alimentos)
            'Has seleccionado: ', otros5
            gr = st.slider('¿Cuál es la cantidad en gramos para el quinto alimento de otros?', 0, 500)
            p_gr= gr/100
            otr5 = pd.DataFrame(get.buscar_alimento_usuario(otros5))
            otr5 = funciones.alimentos_gr(otr5, p_gr)
            st.write(otr5)

        if linea_otros != "0":
            numero_otros = int(linea_otros[-1]) + 1
            otros_lista = [(globals()[f"otr{i}"]) for i in range(1,numero_otros)]
            otros = pd.concat(otros_lista[:numero_otros])
            st.write("Este es tu resumen del otros:", otros)

        if linea_otros != "0":
            suma_macros_otros = otros[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
            st.write("Este es el total de tus macros para otros", suma_macros_otros)

    if linea_desayuno != "0" or linea_comida != "0" or linea_cena != "0" or linea_otros != "0":
        total = suma_macros_desayuno+suma_macros_comida+suma_macros_cena+suma_macros_otros
        st.subheader("La suma total de las kcal para todo el día son:")
        st.write(total)
    if linea_desayuno != "0" or linea_comida != "0" or linea_cena != "0" or linea_otros != "0":
        alimentos_dia = funciones.concatenar(comida, desayuno, cena, otros)

        st.write("Estos son todos los alimentos que vas a tomar hoy:", alimentos_dia)


    st.write("¿Te gustaría poder ir almacenando tus comidas diarias? Haz click en SignUp en el Menu de la izquierda")