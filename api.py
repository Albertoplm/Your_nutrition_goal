  
import streamlit as st
from tools.configuration import db, collection, collection2
import tools.getdata as get
import pandas as pd
import matplotlib.pyplot as plt


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

                suma_macros_desayuno = 0
                suma_macros_comida = 0
                suma_macros_cena = 0
                suma_macros_otros = 0

                #DESAYUNO

                st.subheader("Desayuno")

                mas = ["0","+1", "+2", "+3", "+4", "+5"]
                linea = st.radio(
                    'Si desea añadir otros alimento haga click en:',
                    mas)
                'Has seleccionado: ', linea

                desayuno1 = 0 
                desayuno2 = 0 
                desayuno3 = 0 
                desayuno4 = 0 
                desayuno5 = 0


                if linea == "+1" or linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
                    desayuno1 = st.selectbox(
                        'Seleccione alimento:',
                        alimentos)
                    'Has seleccionado: ', desayuno1
                    gr = st.slider('Cual es la cantidad en gramos?', 0, 500)
                    p_gr= gr/100
                    des1 = pd.DataFrame(get.buscar_alimento_usuario(desayuno1))
                    des1["Energia(kcal)"] = des1["Energia(kcal)"] * p_gr
                    des1["Grasas"] = des1["Grasas"] * p_gr
                    des1["Proteina"] = des1["Proteina"] * p_gr
                    des1["Carbohidratos"] = des1["Carbohidratos"] * p_gr
                    st.write(des1)



                if linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
                    desayuno2 = st.selectbox(
                    'Seleccione el segundo alimento',
                    alimentos)
                    'Has seleccionado: ', desayuno2
                    gr = st.slider('Cual es la cantidad en gramos para el segundo alimento?', 0, 500)
                    p_gr= gr/100
                    des2 = pd.DataFrame(get.buscar_alimento_usuario(desayuno2))
                    des2["Energia(kcal)"] = des2["Energia(kcal)"] * p_gr
                    des2["Grasas"] = des2["Grasas"] * p_gr
                    des2["Proteina"] = des2["Proteina"] * p_gr
                    des2["Carbohidratos"] = des2["Carbohidratos"] * p_gr
                    st.write(des2)


                if linea == "+3" or linea == "+4" or linea == "+5":
                    desayuno3 = st.selectbox(
                    'Seleccione el tercero alimento',
                    alimentos)
                    'Has seleccionado: ', desayuno3
                    gr = st.slider('Cual es la cantidad en gramos para el tercer alimento?', 0, 500)
                    p_gr= gr/100
                    des3 = pd.DataFrame(get.buscar_alimento_usuario(desayuno3))
                    des3["Energia(kcal)"] = des3["Energia(kcal)"] * p_gr
                    des3["Grasas"] = des3["Grasas"] * p_gr
                    des3["Proteina"] = des3["Proteina"] * p_gr
                    des3["Carbohidratos"] = des3["Carbohidratos"] * p_gr
                    st.write(des3)

                if linea == "+4" or linea == "+5":
                    desayuno4 = st.selectbox(
                    'Seleccione el cuarto alimento',
                    alimentos)
                    'Has seleccionado: ', desayuno4
                    gr = st.slider('Cual es la cantidad en gramos para el cuarto alimento?', 0, 500)
                    p_gr= gr/100
                    des4 = pd.DataFrame(get.buscar_alimento_usuario(desayuno4))
                    des4["Energia(kcal)"] = des4["Energia(kcal)"] * p_gr
                    des4["Grasas"] = des4["Grasas"] * p_gr
                    des4["Proteina"] = des4["Proteina"] * p_gr
                    des4["Carbohidratos"] = des4["Carbohidratos"] * p_gr
                    st.write(des4)

                if linea == "+5":
                    desayuno5 = st.selectbox(
                    'Seleccione el quinto alimento',
                    alimentos)
                    'Has seleccionado: ', desayuno5
                    gr = st.slider('Cual es la cantidad en gramos para el quinto alimento?', 0, 500)
                    p_gr= gr/100
                    des5 = pd.DataFrame(get.buscar_alimento_usuario(desayuno5))
                    des5["Energia(kcal)"] = des5["Energia(kcal)"] * p_gr
                    des5["Grasas"] = des5["Grasas"] * p_gr
                    des5["Proteina"] = des5["Proteina"] * p_gr
                    des5["Carbohidratos"] = des5["Carbohidratos"] * p_gr
                    st.write(des5)

                if linea != "0":
                    desayuno = pd.DataFrame(get.buscar_comidas_usuario(desayuno1, desayuno2, desayuno3, desayuno4, desayuno5))
                    st.write("Este es tu resumen del desayuno:", desayuno)

                if linea != "0":
                    suma_macros_desayuno = desayuno[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
                    st.write("Este es el total de tus macros para el desayuno", suma_macros_desayuno)

                #COMIDA

                st.subheader("Comida")

                mas = ["0","+1", "+2", "+3", "+4", "+5"]
                linea = st.radio(
                    'Si desea añadir otros alimento a la comida haga click en:',
                    mas)
                'Has seleccionado: ', linea

                comida1 = 0 
                comida2 = 0 
                comida3 = 0 
                comida4 = 0 
                comida5 = 0


                if linea == "+1" or linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
                    comida1 = st.selectbox(
                        'Seleccione alimento para la comida:',
                        alimentos)
                    'Has seleccionado: ', comida1
                    gr = st.slider('Cual es la cantidad en gramos para este alimento de la comida?', 0, 500)
                    p_gr= gr/100
                    com1 = pd.DataFrame(get.buscar_alimento_usuario(comida1))
                    com1["Energia(kcal)"] = com1["Energia(kcal)"] * p_gr
                    com1["Grasas"] = com1["Grasas"] * p_gr
                    com1["Proteina"] = com1["Proteina"] * p_gr
                    com1["Carbohidratos"] = com1["Carbohidratos"] * p_gr
                    st.write(com1)



                if linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
                    comida2 = st.selectbox(
                    'Seleccione el segundo alimento para la comida',
                    alimentos)
                    'Has seleccionado: ', comida2
                    gr = st.slider('Cual es la cantidad en gramos para el segundo alimento de la comida?', 0, 500)
                    p_gr= gr/100
                    com2 = pd.DataFrame(get.buscar_alimento_usuario(comida2))
                    com2["Energia(kcal)"] = com2["Energia(kcal)"] * p_gr
                    com2["Grasas"] = com2["Grasas"] * p_gr
                    com2["Proteina"] = com2["Proteina"] * p_gr
                    com2["Carbohidratos"] = com2["Carbohidratos"] * p_gr
                    st.write(com2)


                if linea == "+3" or linea == "+4" or linea == "+5":
                    comida3 = st.selectbox(
                    'Seleccione el tercero alimento para la comida',
                    alimentos)
                    'Has seleccionado: ', comida3
                    gr = st.slider('Cual es la cantidad en gramos para el tercer alimento de la comida?', 0, 500)
                    p_gr= gr/100
                    com3 = pd.DataFrame(get.buscar_alimento_usuario(comida3))
                    com3["Energia(kcal)"] = com3["Energia(kcal)"] * p_gr
                    com3["Grasas"] = com3["Grasas"] * p_gr
                    com3["Proteina"] = com3["Proteina"] * p_gr
                    com3["Carbohidratos"] = com3["Carbohidratos"] * p_gr
                    st.write(com3)

                if linea == "+4" or linea == "+5":
                    comida4 = st.selectbox(
                    'Seleccione el cuarto alimento para la comida',
                    alimentos)
                    'Has seleccionado: ', comida4
                    gr = st.slider('Cual es la cantidad en gramos para el cuarto alimento de la comida?', 0, 500)
                    p_gr= gr/100
                    com4 = pd.DataFrame(get.buscar_alimento_usuario(comida4))
                    com4["Energia(kcal)"] = com4["Energia(kcal)"] * p_gr
                    com4["Grasas"] = com4["Grasas"] * p_gr
                    com4["Proteina"] = com4["Proteina"] * p_gr
                    com4["Carbohidratos"] = com4["Carbohidratos"] * p_gr
                    st.write(com4)

                if linea == "+5":
                    comida5 = st.selectbox(
                    'Seleccione el quinto alimento para la comida',
                    alimentos)
                    'Has seleccionado: ', comida5
                    gr = st.slider('Cual es la cantidad en gramos para el quinto alimento de la comida?', 0, 500)
                    p_gr= gr/100
                    com5 = pd.DataFrame(get.buscar_alimento_usuario(comida5))
                    com5["Energia(kcal)"] = com5["Energia(kcal)"] * p_gr
                    com5["Grasas"] = com5["Grasas"] * p_gr
                    com5["Proteina"] = com5["Proteina"] * p_gr
                    com5["Carbohidratos"] = com5["Carbohidratos"] * p_gr
                    st.write(com5)

                if linea != "0":
                    comida = pd.DataFrame(get.buscar_comidas_usuario(comida1, comida2, comida3, comida4, comida5))
                    st.write("Este es tu resumen de la comida:", comida)

                if linea != "0":
                    suma_macros_comida = comida[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
                    st.write("Este es el total de tus macros para la comida", suma_macros_comida)

                #CENA

                st.subheader("Cena")

                mas = ["0","+1", "+2", "+3", "+4", "+5"]
                linea = st.radio(
                    'Si desea añadir otros alimento a la cena haga click en:',
                    mas)
                'Has seleccionado: ', linea

                cena1 = 0 
                cena2 = 0 
                cena3 = 0 
                cena4 = 0 
                cena5 = 0


                if linea == "+1" or linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
                    cena1 = st.selectbox(
                        'Seleccione alimento para la cena:',
                        alimentos)
                    'Has seleccionado: ', cena1
                    gr = st.slider('Cual es la cantidad en gramos para este alimento de la cena?', 0, 500)
                    p_gr= gr/100
                    cen1 = pd.DataFrame(get.buscar_alimento_usuario(cena1))
                    cen1["Energia(kcal)"] = cen1["Energia(kcal)"] * p_gr
                    cen1["Grasas"] = cen1["Grasas"] * p_gr
                    cen1["Proteina"] = cen1["Proteina"] * p_gr
                    cen1["Carbohidratos"] = cen1["Carbohidratos"] * p_gr
                    st.write(cen1)



                if linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
                    cena2 = st.selectbox(
                    'Seleccione el segundo alimento para la cena',
                    alimentos)
                    'Has seleccionado: ', cena2
                    gr = st.slider('Cual es la cantidad en gramos para el segundo alimento de la cena?', 0, 500)
                    p_gr= gr/100
                    cen2 = pd.DataFrame(get.buscar_alimento_usuario(cena2))
                    cen2["Energia(kcal)"] = cen2["Energia(kcal)"] * p_gr
                    cen2["Grasas"] = cen2["Grasas"] * p_gr
                    cen2["Proteina"] = cen2["Proteina"] * p_gr
                    cen2["Carbohidratos"] = cen2["Carbohidratos"] * p_gr
                    st.write(cen2)


                if linea == "+3" or linea == "+4" or linea == "+5":
                    cena3 = st.selectbox(
                    'Seleccione el tercero alimento para la cena',
                    alimentos)
                    'Has seleccionado: ', cena3
                    gr = st.slider('Cual es la cantidad en gramos para el tercer alimento de la cena?', 0, 500)
                    p_gr= gr/100
                    cen3 = pd.DataFrame(get.buscar_alimento_usuario(cena3))
                    cen3["Energia(kcal)"] = cen3["Energia(kcal)"] * p_gr
                    cen3["Grasas"] = cen3["Grasas"] * p_gr
                    cen3["Proteina"] = cen3["Proteina"] * p_gr
                    cen3["Carbohidratos"] = cen3["Carbohidratos"] * p_gr
                    st.write(cen3)

                if linea == "+4" or linea == "+5":
                    cena4 = st.selectbox(
                    'Seleccione el cuarto alimento para la cena',
                    alimentos)
                    'Has seleccionado: ', cena4
                    gr = st.slider('Cual es la cantidad en gramos para el cuarto alimento de la cena?', 0, 500)
                    p_gr= gr/100
                    cen4 = pd.DataFrame(get.buscar_alimento_usuario(cena4))
                    cen4["Energia(kcal)"] = cen4["Energia(kcal)"] * p_gr
                    cen4["Grasas"] = cen4["Grasas"] * p_gr
                    cen4["Proteina"] = cen4["Proteina"] * p_gr
                    cen4["Carbohidratos"] = cen4["Carbohidratos"] * p_gr
                    st.write(cen4)

                if linea == "+5":
                    cena5 = st.selectbox(
                    'Seleccione el quinto alimento para la cena',
                    alimentos)
                    'Has seleccionado: ', cena5
                    gr = st.slider('Cual es la cantidad en gramos para el quinto alimento de la cena?', 0, 500)
                    p_gr= gr/100
                    cen5 = pd.DataFrame(get.buscar_alimento_usuario(cena5))
                    cen5["Energia(kcal)"] = cen5["Energia(kcal)"] * p_gr
                    cen5["Grasas"] = cen5["Grasas"] * p_gr
                    cen5["Proteina"] = cen5["Proteina"] * p_gr
                    cen5["Carbohidratos"] = cen5["Carbohidratos"] * p_gr
                    st.write(cen5)

                if linea != "0":
                    cena = pd.DataFrame(get.buscar_comidas_usuario(cena1, cena2, cena3, cena4, cena5))
                    st.write("Este es tu resumen de la cena:", cena)

                if linea != "0":
                    suma_macros_cena = cena[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
                    st.write("Este es el total de tus macros para la cena", suma_macros_cena)

                #OTROS

                st.subheader("Otros")

                mas = ["0","+1", "+2", "+3", "+4", "+5"]
                linea = st.radio(
                    'Si desea añadir otros alimento a otros haga click en:',
                    mas)
                'Has seleccionado: ', linea

                otros1 = 0 
                otros2 = 0 
                otros3 = 0 
                otros4 = 0 
                otros5 = 0


                if linea == "+1" or linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
                    otros1 = st.selectbox(
                        'Seleccione alimento para otros:',
                        alimentos)
                    'Has seleccionado: ', otros1
                    gr = st.slider('Cual es la cantidad en para este alimento de otros?', 0, 500)
                    p_gr= gr/100
                    otr1 = pd.DataFrame(get.buscar_alimento_usuario(otros1))
                    otr1["Energia(kcal)"] = otr1["Energia(kcal)"] * p_gr
                    otr1["Grasas"] = otr1["Grasas"] * p_gr
                    otr1["Proteina"] = otr1["Proteina"] * p_gr
                    otr1["Carbohidratos"] = otr1["Carbohidratos"] * p_gr
                    st.write(otr1)



                if linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
                    otros2 = st.selectbox(
                    'Seleccione el segundo alimento para otros',
                    alimentos)
                    'Has seleccionado: ', otros2
                    gr = st.slider('Cual es la cantidad en gramos para el segundo alimento de otros?', 0, 500)
                    p_gr= gr/100
                    otr2 = pd.DataFrame(get.buscar_alimento_usuario(otros2))
                    otr2["Energia(kcal)"] = otr2["Energia(kcal)"] * p_gr
                    otr2["Grasas"] = otr2["Grasas"] * p_gr
                    otr2["Proteina"] = otr2["Proteina"] * p_gr
                    otr2["Carbohidratos"] = otr2["Carbohidratos"] * p_gr
                    st.write(otr2)


                if linea == "+3" or linea == "+4" or linea == "+5":
                    otros3 = st.selectbox(
                    'Seleccione el tercero alimento para otros',
                    alimentos)
                    'Has seleccionado: ', otros3
                    gr = st.slider('Cual es la cantidad en gramos para el tercer alimento de otros?', 0, 500)
                    p_gr= gr/100
                    otr3 = pd.DataFrame(get.buscar_alimento_usuario(otros3))
                    otr2["Energia(kcal)"] = otr2["Energia(kcal)"] * p_gr
                    otr2["Grasas"] = otr2["Grasas"] * p_gr
                    otr2["Proteina"] = otr2["Proteina"] * p_gr
                    otr2["Carbohidratos"] = otr2["Carbohidratos"] * p_gr
                    st.write(otr2)

                if linea == "+4" or linea == "+5":
                    otros4 = st.selectbox(
                    'Seleccione el cuarto alimento para otros',
                    alimentos)
                    'Has seleccionado: ', otros4
                    gr = st.slider('Cual es la cantidad en gramos para el cuarto alimento de otros?', 0, 500)
                    p_gr= gr/100
                    otr4 = pd.DataFrame(get.buscar_alimento_usuario(otros4))
                    otr4["Energia(kcal)"] = otr4["Energia(kcal)"] * p_gr
                    otr4["Grasas"] = otr4["Grasas"] * p_gr
                    otr4["Proteina"] = otr4["Proteina"] * p_gr
                    otr4["Carbohidratos"] = otr4["Carbohidratos"] * p_gr
                    st.write(otr4)

                if linea == "+5":
                    otros5 = st.selectbox(
                    'Seleccione el quinto alimento para otros',
                    alimentos)
                    'Has seleccionado: ', otros5
                    gr = st.slider('Cual es la cantidad en gramos para el quinto alimento de otros?', 0, 500)
                    p_gr= gr/100
                    otr5 = pd.DataFrame(get.buscar_alimento_usuario(otros5))
                    otr5["Energia(kcal)"] = otr5["Energia(kcal)"] * p_gr
                    otr5["Grasas"] = otr5["Grasas"] * p_gr
                    otr5["Proteina"] = otr5["Proteina"] * p_gr
                    otr5["Carbohidratos"] = otr5["Carbohidratos"] * p_gr
                    st.write(otr5)

                if linea != "0":
                    otros = pd.DataFrame(get.buscar_comidas_usuario(otros1, otros2, otros3, otros4, otros5))
                    st.write("Este es tu resumen para otros:", otros)

                if linea != "0":
                    suma_macros_otros = otros[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
                    st.write("Este es el total de tus macros para otros", suma_macros_otros)

                if linea != "0":
                    total = suma_macros_desayuno+suma_macros_comida+suma_macros_cena+suma_macros_otros
                    st.subheader("La suma total de las kcal para todo el día son:")
                    st.write(total)

                alimentos_dia = pd.concat([desayuno,comida,cena,otros])
                
                st.write("Estos son todos los alimentos que vas a tomar hoy:", alimentos_dia)

                alimentos = []
                for x in alimentos_dia["Nombre"]:
                    alimentos.append(x)
                
                alimentos_dia_dict = alimentos_dia.to_dict('records')

                if linea != "0":
                    if st.checkbox("Añadir alimentos a mi perfil"):
                        get.añadir_comdias_dia_total(username, alimentos_dia_dict)
                        st.write("Se han añadido correctamente a tu perfil!")

                




            elif task == "Información":
                st.subheader("Información")
            elif task == ("Perfil"):
                st.subheader("Perfil del usuario")
                user_result = get.iniciar_sesion(username, password)
                user_info = pd.DataFrame(user_result)
                st.write(user_info)
        else:
            st.warning("Incorrect Username/Password")
if menu_choice == "SignUp":
    st.subheader("Crear nueva cuenta")
    new_user = st.text_input("Usuario")
    new_password = st.text_input("Contraseña", type= 'password')

    if st.button("Registrarse"):
        get.añadir_usuario(new_user, new_password)
        st.success("Te has registrado correctamente")
        st.info("Ve a Menu para entrar con tu usuario")

if menu_choice == "Home":

    st.markdown("<h1 style='text-align: center; color: black; font-size: +4'>Preparado para cambiar tu estilo de vida??</h1>", unsafe_allow_html=True)
    st.write("<h1 style='text-align: center; color: black; font-size: medium'>Quieres conocer cuantas kcal deberías tomar a diario para cumplir tu objetivo??</h1>", unsafe_allow_html=True)            
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
    edad = st.slider('Cual es tu edad?', 0, 100)

    #select slider to choose weight
    peso = st.slider('Cual es tu peso actual en kg?', 0, 150)

    #select slider to choose height
    estatura = st.slider('Cual es tu estatura actual en cm?', 0, 250)

    st.write("Has seleccionado:", edad, "años", peso, "kg", estatura, "cm")

    #Kcal to consume daily
    if sexo == "Hombre":
        TMBH = 66 + (13.7 * (peso)) + (5 * (estatura)) - (6.75 * (edad))
        if objetivo == "Perder peso":
            perdida = st.slider('Cuantos kg deseas perder?', 0, 100)
            st.write("Tu cuerpo consume", round(TMBH), "kcal en reposo, sin hacer nada por lo tanto. Debes consumir", round(TMBH*1.2 - 1000),"al día para perder", perdida ,"kg en ",perdida*7,
            " días (Se recomienda no perder más de un kilo por semana). En el caso de realizar deporte deberás sumarle esas kcal extra, es decir kcal extra +" , round(TMBH*1.2 - 1000))
        if objetivo == "Ganar masa muscular":
            ganancia = st.slider('Cuantos kg deseas ganar?', 0, 100)
            st.write("Tu cuerpo consume", round(TMBH), "kcal en reposo, sin hacer nada por lo tanto. Debes consumir", round(TMBH*1.2 + 500),"al día para ganar", ganancia ,"kg en ",(ganancia*2)*7,
            " días (Se recomienda no ganar más de medio kilo por semana). En el caso de realizar deporte deberás sumarle esas kcal extra, es decir kcal extra +" , round(TMBH*1.2 + 500))
    elif sexo == "Mujer":
        TMBM = 655 + (9.6 * peso) + (1.8 * estatura) - (4.7 * edad)
        if objetivo == "Perder peso":
            perdida = st.slider('Cuantos kg deseas perder?', 0, 50)
            st.write("Tu cuerpo consume", round(TMBM), "kcal en reposo, sin hacer nada por lo tanto. Debes consumir", round(TMBM*1.2 - 1000),"al día para perder", perdida ,"kg en ",perdida*7,
            " días (Se recomienda no perder más de un kilo por semana). En el caso de realizar deporte deberás sumarle esas kcal extra, es decir kcal extra +" , round(TMBM*1.2 - 1000))
        if objetivo == "Ganar masa muscular":
            ganancia = st.slider('Cuantos kg deseas ganar?', 0, 100)
            st.write("Tu cuerpo consume", round(TMBM), "kcal en reposo, sin hacer nada por lo tanto. Debes consumir", round(TMBM*1.2 + 500),"al día para ganar", ganancia ,"kg en ",(ganancia*2)*7,
            " días (Se recomienda no ganar más de medio kilo por semana). En el caso de realizar deporte deberás sumarle esas kcal extra, es decir kcal extra +" , round(TMBM*1.2 + 500))

    #Macros
    #st.write("<h1 style='text-align: center; color: black; font-size: medium'>Ahora que ya conoces cuantas kcal debes consumir al día para cumplir tu objetivo, quieres dar un paso más para mejorar tu alimentación??</h1>", unsafe_allow_html=True)
    st.subheader("Ahora que ya conoces cuantas kcal debes consumir al día para cumplir tu objetivo, quieres dar un paso más para mejorar tu alimentación??")
    st.write("<h1 style='text-align: center; color: black; font-size: medium'>Que son las macros??</h1>", unsafe_allow_html=True)

    st.write("Los macros no son otra cosa que los macronutrientes, los grupos de alimentos que nuestro cuerpo necesita para vivir: los carbohidratos, las proteínas y las grasas. Todos ellos contienen micronutrientes, es decir vitaminas y minerales . La dieta de los macros o dieta flexible propone adelgazar o mantener el peso controlando los gramos de macronutrientes que ingerimos diariamente. Vamos con ello!")

    if sexo == "Hombre":
        if objetivo == "Perder peso":
            st.write("Kcal totales", round(TMBH))
            st.write("Proteinas entre:", round(TMBH*0.25), "y", round(TMBH*0.35), "de las kcal totales")
            st.write("Carbohidratos entre:", round(TMBH*0.35), "y" ,round(TMBH*0.45), "de las kcal totales")
            st.write("Grasas entre:", round(TMBH*0.15), "y" ,round(TMBH*0.25), "de las kcal totales")
        if objetivo == "Ganar masa muscular":
            st.write("Kcal totales", round(TMBH))
            st.write("Proteinas entre:", round(TMBH*0.20), "y", round(TMBH*0.25), "de las kcal totales")
            st.write("Carbohidratos entre:", round(TMBH*0.50), "y" ,round(TMBH*0.55), "de las kcal totales")
            st.write("Grasas entre:", round(TMBH*0.25) ,"y" ,round(TMBH*0.30), "de las kcal totales")
    if sexo == "Mujer":
        if objetivo == "Perder peso":
            st.write("Kcal totales", round(TMBM))
            st.write("Proteinas entre:", round(TMBM*0.25), "y", round(TMBM*0.35), "de las kcal totales")
            st.write("Carbohidratos entre:", round(TMBM*0.35), "y" ,round(TMBM*0.45), "de las kcal totales")
            st.write("Grasas entre:", round(TMBM*0.15), "y" ,round(TMBM*0.25), "de las kcal totales")
        if objetivo == "Ganar masa muscular":
            st.write("Kcal totales", round(TMBM))
            st.write("Proteinas entre:", round(TMBM*0.20), "y", round(TMBM*0.25), "de las kcal totales")
            st.write("Carbohidratos entre:", round(TMBM*0.50), "y" ,round(TMBM*0.55), "de las kcal totales")
            st.write("Grasas entre:", round(TMBM*0.25) ,"y" ,round(TMBM*0.30), "de las kcal totales")

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

    st.subheader("Vamos ver como podemos cuadrar los alimentos de mañana")

    #Defino suma de macros para que no me de error si se pone 0 en algun horario

    suma_macros_desayuno = 0
    suma_macros_comida = 0
    suma_macros_cena = 0
    suma_macros_otros = 0

    #DESAYUNO

    st.subheader("Desayuno")

    mas = ["0","+1", "+2", "+3", "+4", "+5"]
    linea = st.radio(
        'Si desea añadir otros alimento haga click en:',
        mas)
    'Has seleccionado: ', linea

    desayuno1 = 0 
    desayuno2 = 0 
    desayuno3 = 0 
    desayuno4 = 0 
    desayuno5 = 0


    if linea == "+1" or linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
        desayuno1 = st.selectbox(
            'Seleccione alimento:',
            alimentos)
        'Has seleccionado: ', desayuno1
        gr = st.slider('Cual es la cantidad en gramos?', 0, 500)
        p_gr= gr/100
        des1 = pd.DataFrame(get.buscar_alimento_usuario(desayuno1))
        des1["Energia(kcal)"] = des1["Energia(kcal)"] * p_gr
        des1["Grasas"] = des1["Grasas"] * p_gr
        des1["Proteina"] = des1["Proteina"] * p_gr
        des1["Carbohidratos"] = des1["Carbohidratos"] * p_gr
        st.write(des1)



    if linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
        desayuno2 = st.selectbox(
        'Seleccione el segundo alimento',
        alimentos)
        'Has seleccionado: ', desayuno2
        gr = st.slider('Cual es la cantidad en gramos para el segundo alimento?', 0, 500)
        p_gr= gr/100
        des2 = pd.DataFrame(get.buscar_alimento_usuario(desayuno2))
        des2["Energia(kcal)"] = des2["Energia(kcal)"] * p_gr
        des2["Grasas"] = des2["Grasas"] * p_gr
        des2["Proteina"] = des2["Proteina"] * p_gr
        des2["Carbohidratos"] = des2["Carbohidratos"] * p_gr
        st.write(des2)


    if linea == "+3" or linea == "+4" or linea == "+5":
        desayuno3 = st.selectbox(
        'Seleccione el tercero alimento',
        alimentos)
        'Has seleccionado: ', desayuno3
        gr = st.slider('Cual es la cantidad en gramos para el tercer alimento?', 0, 500)
        p_gr= gr/100
        des3 = pd.DataFrame(get.buscar_alimento_usuario(desayuno3))
        des3["Energia(kcal)"] = des3["Energia(kcal)"] * p_gr
        des3["Grasas"] = des3["Grasas"] * p_gr
        des3["Proteina"] = des3["Proteina"] * p_gr
        des3["Carbohidratos"] = des3["Carbohidratos"] * p_gr
        st.write(des3)

    if linea == "+4" or linea == "+5":
        desayuno4 = st.selectbox(
        'Seleccione el cuarto alimento',
        alimentos)
        'Has seleccionado: ', desayuno4
        gr = st.slider('Cual es la cantidad en gramos para el cuarto alimento?', 0, 500)
        p_gr= gr/100
        des4 = pd.DataFrame(get.buscar_alimento_usuario(desayuno4))
        des4["Energia(kcal)"] = des4["Energia(kcal)"] * p_gr
        des4["Grasas"] = des4["Grasas"] * p_gr
        des4["Proteina"] = des4["Proteina"] * p_gr
        des4["Carbohidratos"] = des4["Carbohidratos"] * p_gr
        st.write(des4)

    if linea == "+5":
        desayuno5 = st.selectbox(
        'Seleccione el quinto alimento',
        alimentos)
        'Has seleccionado: ', desayuno5
        gr = st.slider('Cual es la cantidad en gramos para el quinto alimento?', 0, 500)
        p_gr= gr/100
        des5 = pd.DataFrame(get.buscar_alimento_usuario(desayuno5))
        des5["Energia(kcal)"] = des5["Energia(kcal)"] * p_gr
        des5["Grasas"] = des5["Grasas"] * p_gr
        des5["Proteina"] = des5["Proteina"] * p_gr
        des5["Carbohidratos"] = des5["Carbohidratos"] * p_gr
        st.write(des5)

    if linea != "0":
        desayuno = pd.DataFrame(get.buscar_comidas_usuario(desayuno1, desayuno2, desayuno3, desayuno4, desayuno5))
        st.write("Este es tu resumen del desayuno:", desayuno)

    if linea != "0":
        suma_macros_desayuno = desayuno[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
        st.write("Este es el total de tus macros para el desayuno", suma_macros_desayuno)

    #COMIDA

    st.subheader("Comida")

    mas = ["0","+1", "+2", "+3", "+4", "+5"]
    linea = st.radio(
        'Si desea añadir otros alimento a la comida haga click en:',
        mas)
    'Has seleccionado: ', linea

    comida1 = 0 
    comida2 = 0 
    comida3 = 0 
    comida4 = 0 
    comida5 = 0


    if linea == "+1" or linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
        comida1 = st.selectbox(
            'Seleccione alimento para la comida:',
            alimentos)
        'Has seleccionado: ', comida1
        gr = st.slider('Cual es la cantidad en gramos para este alimento de la comida?', 0, 500)
        p_gr= gr/100
        com1 = pd.DataFrame(get.buscar_alimento_usuario(comida1))
        com1["Energia(kcal)"] = com1["Energia(kcal)"] * p_gr
        com1["Grasas"] = com1["Grasas"] * p_gr
        com1["Proteina"] = com1["Proteina"] * p_gr
        com1["Carbohidratos"] = com1["Carbohidratos"] * p_gr
        st.write(com1)



    if linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
        comida2 = st.selectbox(
        'Seleccione el segundo alimento para la comida',
        alimentos)
        'Has seleccionado: ', comida2
        gr = st.slider('Cual es la cantidad en gramos para el segundo alimento de la comida?', 0, 500)
        p_gr= gr/100
        com2 = pd.DataFrame(get.buscar_alimento_usuario(comida2))
        com2["Energia(kcal)"] = com2["Energia(kcal)"] * p_gr
        com2["Grasas"] = com2["Grasas"] * p_gr
        com2["Proteina"] = com2["Proteina"] * p_gr
        com2["Carbohidratos"] = com2["Carbohidratos"] * p_gr
        st.write(com2)


    if linea == "+3" or linea == "+4" or linea == "+5":
        comida3 = st.selectbox(
        'Seleccione el tercero alimento para la comida',
        alimentos)
        'Has seleccionado: ', comida3
        gr = st.slider('Cual es la cantidad en gramos para el tercer alimento de la comida?', 0, 500)
        p_gr= gr/100
        com3 = pd.DataFrame(get.buscar_alimento_usuario(comida3))
        com3["Energia(kcal)"] = com3["Energia(kcal)"] * p_gr
        com3["Grasas"] = com3["Grasas"] * p_gr
        com3["Proteina"] = com3["Proteina"] * p_gr
        com3["Carbohidratos"] = com3["Carbohidratos"] * p_gr
        st.write(com3)

    if linea == "+4" or linea == "+5":
        comida4 = st.selectbox(
        'Seleccione el cuarto alimento para la comida',
        alimentos)
        'Has seleccionado: ', comida4
        gr = st.slider('Cual es la cantidad en gramos para el cuarto alimento de la comida?', 0, 500)
        p_gr= gr/100
        com4 = pd.DataFrame(get.buscar_alimento_usuario(comida4))
        com4["Energia(kcal)"] = com4["Energia(kcal)"] * p_gr
        com4["Grasas"] = com4["Grasas"] * p_gr
        com4["Proteina"] = com4["Proteina"] * p_gr
        com4["Carbohidratos"] = com4["Carbohidratos"] * p_gr
        st.write(com4)

    if linea == "+5":
        comida5 = st.selectbox(
        'Seleccione el quinto alimento para la comida',
        alimentos)
        'Has seleccionado: ', comida5
        gr = st.slider('Cual es la cantidad en gramos para el quinto alimento de la comida?', 0, 500)
        p_gr= gr/100
        com5 = pd.DataFrame(get.buscar_alimento_usuario(comida5))
        com5["Energia(kcal)"] = com5["Energia(kcal)"] * p_gr
        com5["Grasas"] = com5["Grasas"] * p_gr
        com5["Proteina"] = com5["Proteina"] * p_gr
        com5["Carbohidratos"] = com5["Carbohidratos"] * p_gr
        st.write(com5)

    if linea != "0":
        comida = pd.DataFrame(get.buscar_comidas_usuario(comida1, comida2, comida3, comida4, comida5))
        st.write("Este es tu resumen de la comida:", comida)

    if linea != "0":
        suma_macros_comida = comida[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
        st.write("Este es el total de tus macros para la comida", suma_macros_comida)

    #CENA

    st.subheader("Cena")

    mas = ["0","+1", "+2", "+3", "+4", "+5"]
    linea = st.radio(
        'Si desea añadir otros alimento a la cena haga click en:',
        mas)
    'Has seleccionado: ', linea

    cena1 = 0 
    cena2 = 0 
    cena3 = 0 
    cena4 = 0 
    cena5 = 0


    if linea == "+1" or linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
        cena1 = st.selectbox(
            'Seleccione alimento para la cena:',
            alimentos)
        'Has seleccionado: ', cena1
        gr = st.slider('Cual es la cantidad en gramos para este alimento de la cena?', 0, 500)
        p_gr= gr/100
        cen1 = pd.DataFrame(get.buscar_alimento_usuario(cena1))
        cen1["Energia(kcal)"] = cen1["Energia(kcal)"] * p_gr
        cen1["Grasas"] = cen1["Grasas"] * p_gr
        cen1["Proteina"] = cen1["Proteina"] * p_gr
        cen1["Carbohidratos"] = cen1["Carbohidratos"] * p_gr
        st.write(cen1)



    if linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
        cena2 = st.selectbox(
        'Seleccione el segundo alimento para la cena',
        alimentos)
        'Has seleccionado: ', cena2
        gr = st.slider('Cual es la cantidad en gramos para el segundo alimento de la cena?', 0, 500)
        p_gr= gr/100
        cen2 = pd.DataFrame(get.buscar_alimento_usuario(cena2))
        cen2["Energia(kcal)"] = cen2["Energia(kcal)"] * p_gr
        cen2["Grasas"] = cen2["Grasas"] * p_gr
        cen2["Proteina"] = cen2["Proteina"] * p_gr
        cen2["Carbohidratos"] = cen2["Carbohidratos"] * p_gr
        st.write(cen2)


    if linea == "+3" or linea == "+4" or linea == "+5":
        cena3 = st.selectbox(
        'Seleccione el tercero alimento para la cena',
        alimentos)
        'Has seleccionado: ', cena3
        gr = st.slider('Cual es la cantidad en gramos para el tercer alimento de la cena?', 0, 500)
        p_gr= gr/100
        cen3 = pd.DataFrame(get.buscar_alimento_usuario(cena3))
        cen3["Energia(kcal)"] = cen3["Energia(kcal)"] * p_gr
        cen3["Grasas"] = cen3["Grasas"] * p_gr
        cen3["Proteina"] = cen3["Proteina"] * p_gr
        cen3["Carbohidratos"] = cen3["Carbohidratos"] * p_gr
        st.write(cen3)

    if linea == "+4" or linea == "+5":
        cena4 = st.selectbox(
        'Seleccione el cuarto alimento para la cena',
        alimentos)
        'Has seleccionado: ', cena4
        gr = st.slider('Cual es la cantidad en gramos para el cuarto alimento de la cena?', 0, 500)
        p_gr= gr/100
        cen4 = pd.DataFrame(get.buscar_alimento_usuario(cena4))
        cen4["Energia(kcal)"] = cen4["Energia(kcal)"] * p_gr
        cen4["Grasas"] = cen4["Grasas"] * p_gr
        cen4["Proteina"] = cen4["Proteina"] * p_gr
        cen4["Carbohidratos"] = cen4["Carbohidratos"] * p_gr
        st.write(cen4)

    if linea == "+5":
        cena5 = st.selectbox(
        'Seleccione el quinto alimento para la cena',
        alimentos)
        'Has seleccionado: ', cena5
        gr = st.slider('Cual es la cantidad en gramos para el quinto alimento de la cena?', 0, 500)
        p_gr= gr/100
        cen5 = pd.DataFrame(get.buscar_alimento_usuario(cena5))
        cen5["Energia(kcal)"] = cen5["Energia(kcal)"] * p_gr
        cen5["Grasas"] = cen5["Grasas"] * p_gr
        cen5["Proteina"] = cen5["Proteina"] * p_gr
        cen5["Carbohidratos"] = cen5["Carbohidratos"] * p_gr
        st.write(cen5)

    if linea != "0":
        cena = pd.DataFrame(get.buscar_comidas_usuario(cena1, cena2, cena3, cena4, cena5))
        st.write("Este es tu resumen de la cena:", cena)

    if linea != "0":
        suma_macros_cena = cena[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
        st.write("Este es el total de tus macros para la cena", suma_macros_cena)

    #OTROS

    st.subheader("Otros")

    mas = ["0","+1", "+2", "+3", "+4", "+5"]
    linea = st.radio(
        'Si desea añadir otros alimento a otros haga click en:',
        mas)
    'Has seleccionado: ', linea

    otros1 = 0 
    otros2 = 0 
    otros3 = 0 
    otros4 = 0 
    otros5 = 0


    if linea == "+1" or linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
        otros1 = st.selectbox(
            'Seleccione alimento para otros:',
            alimentos)
        'Has seleccionado: ', otros1
        gr = st.slider('Cual es la cantidad en para este alimento de otros?', 0, 500)
        p_gr= gr/100
        otr1 = pd.DataFrame(get.buscar_alimento_usuario(otros1))
        otr1["Energia(kcal)"] = otr1["Energia(kcal)"] * p_gr
        otr1["Grasas"] = otr1["Grasas"] * p_gr
        otr1["Proteina"] = otr1["Proteina"] * p_gr
        otr1["Carbohidratos"] = otr1["Carbohidratos"] * p_gr
        st.write(otr1)



    if linea == "+2" or linea == "+3" or linea == "+4" or linea == "+5":
        otros2 = st.selectbox(
        'Seleccione el segundo alimento para otros',
        alimentos)
        'Has seleccionado: ', otros2
        gr = st.slider('Cual es la cantidad en gramos para el segundo alimento de otros?', 0, 500)
        p_gr= gr/100
        otr2 = pd.DataFrame(get.buscar_alimento_usuario(otros2))
        otr2["Energia(kcal)"] = otr2["Energia(kcal)"] * p_gr
        otr2["Grasas"] = otr2["Grasas"] * p_gr
        otr2["Proteina"] = otr2["Proteina"] * p_gr
        otr2["Carbohidratos"] = otr2["Carbohidratos"] * p_gr
        st.write(otr2)


    if linea == "+3" or linea == "+4" or linea == "+5":
        otros3 = st.selectbox(
        'Seleccione el tercero alimento para otros',
        alimentos)
        'Has seleccionado: ', otros3
        gr = st.slider('Cual es la cantidad en gramos para el tercer alimento de otros?', 0, 500)
        p_gr= gr/100
        otr3 = pd.DataFrame(get.buscar_alimento_usuario(otros3))
        otr2["Energia(kcal)"] = otr2["Energia(kcal)"] * p_gr
        otr2["Grasas"] = otr2["Grasas"] * p_gr
        otr2["Proteina"] = otr2["Proteina"] * p_gr
        otr2["Carbohidratos"] = otr2["Carbohidratos"] * p_gr
        st.write(otr2)

    if linea == "+4" or linea == "+5":
        otros4 = st.selectbox(
        'Seleccione el cuarto alimento para otros',
        alimentos)
        'Has seleccionado: ', otros4
        gr = st.slider('Cual es la cantidad en gramos para el cuarto alimento de otros?', 0, 500)
        p_gr= gr/100
        otr4 = pd.DataFrame(get.buscar_alimento_usuario(otros4))
        otr4["Energia(kcal)"] = otr4["Energia(kcal)"] * p_gr
        otr4["Grasas"] = otr4["Grasas"] * p_gr
        otr4["Proteina"] = otr4["Proteina"] * p_gr
        otr4["Carbohidratos"] = otr4["Carbohidratos"] * p_gr
        st.write(otr4)

    if linea == "+5":
        otros5 = st.selectbox(
        'Seleccione el quinto alimento para otros',
        alimentos)
        'Has seleccionado: ', otros5
        gr = st.slider('Cual es la cantidad en gramos para el quinto alimento de otros?', 0, 500)
        p_gr= gr/100
        otr5 = pd.DataFrame(get.buscar_alimento_usuario(otros5))
        otr5["Energia(kcal)"] = otr5["Energia(kcal)"] * p_gr
        otr5["Grasas"] = otr5["Grasas"] * p_gr
        otr5["Proteina"] = otr5["Proteina"] * p_gr
        otr5["Carbohidratos"] = otr5["Carbohidratos"] * p_gr
        st.write(otr5)

    if linea != "0":
        otros = pd.DataFrame(get.buscar_comidas_usuario(otros1, otros2, otros3, otros4, otros5))
        st.write("Este es tu resumen para otros:", otros)

    if linea != "0":
        suma_macros_otros = otros[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
        st.write("Este es el total de tus macros para otros", suma_macros_otros)

    if linea != "0":
        total = suma_macros_desayuno+suma_macros_comida+suma_macros_cena+suma_macros_otros
        st.subheader("La suma total de las kcal para todo el día son:")
        st.write(total)