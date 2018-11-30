# -*-coding: utf-8 -*-
class Student:
    #FUNCIONES PARA CREAR EL ESTUDIANTE Y SUS CARACTERISTICAS
    def __init__(self,nombre,apellido,id,semestre):
        self.name = nombre
        self.lastname =  apellido
        self.identification = id
        self.semester = semestre
    def setname(self):
        self.name = input("Ingrese su nombre :")
    def setlastname(self):
        self.lastname = input("Ingrese su apellido :")
    def setid(self):
        self.identification = str(input("Ingrese su numero de identificacion :"))
    def setsemester(self):
        self.semester = input("Ingrese su semestre :")
# ESTA FUNCION RETORNA EL SEMESTRE INGRESADO POR EL USUARIO PARA USARLO EN LA SIGUIENTE CLASE    
    def getsemester(self):
        return int(self.semester)
    def __str__(self):
        return ("Estudiante identificado como\n" + "- " + self.name +" " + self.lastname + "\n"+ "Con numero de ID" + "\n- " +"{0}".format(self.identification) + "\nActualmente en " + "\n- {0}".format(self.semester) + " Semestre")

class Materias_x_semestre :
    # LISTAS DE MATERIAS POR SEMESTRE DEL PENSUM DE ECONOMIA Y FINANZAS
    primer_semestre = ["Introduccion a la ciencia economica ", "Doctrinas economicas ", "Calculo 1 ", "Logica y matematicas discretas ","Catedra rosarista "]
    segundo_semestre = ["Medicion economica ", "Historia economica general ","Calculo 2 ","Electiva general "]
    tercer_semestre = ["Microeconomia 1 ","Etica ","Algebra lineal ","Electiva general "]
    cuarto_semestre = ["Microeconomia 2 ", "Macroeconomia 1 ", "Economia matematica ", "Probabilidad ","Electiva general "]
    quinto_semestre = ["Microeconomia 3 ","Macroeconomia 2 ","Electiva complementaria ","Estadistica ","Lectura critica para economia y finanzas "]
    sexto_semestre = ["Macroeconomia 3 ","Econometria basica ", "Electiva complementaria ", "Electiva complementaria ", "Escritura academica para economia y finanzas "]
    septimo_semestre = ["Historia economica colombiana ", "Econometria intermedia ", "Electiva complementaria ", "Electiva general ","Constitucion politica e instruccion civica "]
    # LISTA VACIA USADA PARA MATERIAS QUE APROBO(AL ESCRIBIR "SI")
    materias_aprobadas = []
    #LISTA VACIA DE MATERIAS QUE SE ABRIRAN POR PRERREQUISITOS Y LAS QUE NO APROBO.
    materias_proximo_semestre = []
    
    def __init__(self,semestre):
        self.semester = semestre
        
# ESTA FUNCION DEPENDIENDO DEL SEMESTRE QUE INGRESE EL USUARIO, VA A PREGUNTAR QUE MATERIAS APROBO Y DE ACUERDO A ESO, A LAS QUE NO APROBO Y A CIERTOS PRERREQUISITOS, VA A RETORNAR LAS MATERIAS DISPONIBLES PARA EL SIGUIENTE SEMESTRE        
    def materias_vistas(self):   
        print('Ingrese "si" o "no" aprobo las siguientes materias : ') 
        
        """------------------------------------ PRIMER SEMESTRE ----------------------------------"""
        
        if (self.semester == 1):
            #COPIA DE LA LISTA DE SEGUNDO SEMESTRE
            self.materias_proximo_semestre = self.segundo_semestre[:]
            
            """ materias aprobadas primer semestre"""
            for i in self.primer_semestre:   
                materias = input(i)
                if materias == "si":
                    self.materias_aprobadas.append(i)
            """ materias para el proximo semestre"""        
            for I in self.primer_semestre:
                if I not in self.materias_aprobadas :
                    self.materias_proximo_semestre.append(I)
            """ prerrequisitos """        
            if "Calculo 1 " not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Calculo 2 ")  
                 
            print ("\nEstas son las materias disponibles para el siguiente semestre\n")
            print (self.materias_proximo_semestre)       
                    
                                         
        """----------------------------------- SEGUNDO SEMESTRE ------------------------------------"""
        
        if (self.semester == 2):
            #COPIA DE LA LISTA DE TERCER SEMESTRE
            self.materias_proximo_semestre = self.tercer_semestre[:]
            
            """ materias aprobadas primer semestre"""
            for i in self.primer_semestre:
                materias = input(i)
                if materias == "si":
                    self.materias_aprobadas.append(i) 
            """ materias aprobadas segundo semestre"""             
            for l in self.segundo_semestre:
                materias = input(l)
                if materias == "si":
                    self.materias_aprobadas.append(l)   
            """ materias para el proximo semestre"""             
            for I in self.primer_semestre:
                if I not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(I)        
            for L in self.segundo_semestre:
                if L not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(L)
            """ prerrequisitos """        
            if ("Introduccion a la ciencia economica " and "Calculo 1 ") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Microeconomia 1 ")
                
            print ("\nEstas son las materias disponibles para el siguiente semestre\n")
            print (self.materias_proximo_semestre)  
            
                
        """ ---------------------------------- TERCER SEMESTRE ----------------------------- """    
        
        if (self.semester == 3):
            #COPIA DE LA LISTA DE CUARTO SEMESTRE
            self.materias_proximo_semestre = self.cuarto_semestre[:]
            for i in self.primer_semestre:
                self.materias_aprobadas.append(i)
            
            """ materias aprobadas segundo semestre """
            for l in self.segundo_semestre:
                materias = input(l)
                if materias == "si":
                    self.materias_aprobadas.append(l)
            """ materias aprobadas tercer semestre """        
            for m in self.tercer_semestre:
                materias = input(m)
                if materias == "si":
                    self.materias_aprobadas.append(m)
            """ materias para el proximo semestre """
            for L in self.segundo_semestre:
                if L not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(L)        
            for M in self.tercer_semestre:
                if M not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(M)
            """ prerrequisitos """
            if ("Introduccion a la ciencia economica " and "Algebra lineal ") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Economia matematica ")
            if ("Microeconomia 1 ") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Microeconomia 2 ")
            if ("Calculo 2 ") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Probabilidad ")
            if ("Medicion economica " and "Calculo 1") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Macroeconomia 1 ")
            
            print ("\nEstas son las materias disponibles para el siguiente semestre\n")
            print (self.materias_proximo_semestre) 
            
        """ --------------------------------- CUARTO SEMESTRE ------------------------------------ """
        
        if (self.semester == 4):
            #COPIA DE LA LISTA QUINTO SEMESTRE
            self.materias_proximo_semestre = self.quinto_semestre[:]
            for i in self.primer_semestre:
                self.materias_aprobadas.append(i)
            for l in self.segundo_semestre:
                self.materias_aprobadas.append(l)
            
            """ materias aprobadas tercer semestre """
            for m in self.tercer_semestre:
                materias = input(m)
                if materias == "si":
                    self.materias_aprobadas.append(m)
            """ materias aprobadas cuarto semestre """        
            for n in self.cuarto_semestre:
                materias = input(n)
                if materias == "si":
                    self.materias_aprobadas.append(n)
            """ materias para el proximo semestre """
            for M in self.tercer_semestre:
                if M not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(M)        
            for N in self.cuarto_semestre:
                if N not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(N)
            """ prerrequisitos """
            if ("Algebra lineal " and "Probabilidad ") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Estadistica ")
            if ("Macroeconomia 1 " and "Microeconomia 1 ") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Macroeconomia 2 ")
            if ("Microeconomia 1 " and "Economia matematica ") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Microeconomia 3 ")
                
            print ("\nEstas son las materias disponibles para el siguiente semestre\n")
            print (self.materias_proximo_semestre)      
        
        """----------------------------------------- QUINTO SEMESTRE ----------------------------------- """
        
        if (self.semester == 5):
            #COPIA LISTA SEXTO SEMESTRE
            self.materias_proximo_semestre = self.sexto_semestre[:]
            for i in self.primer_semestre:
                self.materias_aprobadas.append(i)
            for l in self.segundo_semestre:
                self.materias_aprobadas.append(l)
            for m in self.tercer_semestre:
                self.materias_aprobadas.append(m)
                
            """ materias aprobadas cuarto semestre """
            for n in self.cuarto_semestre:
                materias = input(n)
                if materias == "si":
                    self.materias_aprobadas.append(n)
            """ materias aprobadas quinto semestre """        
            for k in self.quinto_semestre:
                materias = input(k)
                if materias == "si":
                    self.materias_aprobadas.append(k)
            """ materias para el proximo semestre """
            for N in self.cuarto_semestre:
                if N not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(N)        
            for K in self.quinto_semestre:
                if K not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(K)
            """ prerrequisitos """
            if "Estadistica " not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Econometria basica ")
            if ("Macroeconomia 2 " and "Economia matematica ") not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Macroeconomia 3 ")
            if "Lectura critica para economia y finanzas " not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Escritura academica para economia y finanzas ")  
            
            print ("\nEstas son las materias disponibles para el siguiente semestre\n")
            print (self.materias_proximo_semestre)  
            
        """ ---------------------------------- SEXTO SEMESTRE ----------------------------"""    
        
        if (self.semester == 6):
            #COPIA LISTA SEPTIMO SEMESTRE
            self.materias_proximo_semestre = self.septimo_semestre[:]
            for i in self.primer_semestre:
                self.materias_aprobadas.append(i)
            for l in self.segundo_semestre:
                self.materias_aprobadas.append(l)
            for m in self.tercer_semestre:
                self.materias_aprobadas.append(m)
            for n in self.cuarto_semestre:
                self.materias_aprobadas.append(n)
            
            """ materias aprobadas quinto semestre """    
            for k in self.quinto_semestre:
                materias = input(k)
                if materias == "si":
                    self.materias_aprobadas.append(k)
            """ materias aprobadas sexto semestre """
            for u in self.sexto_semestre:
                materias = input(u)
                if materias == "si":
                    self.materias_aprobadas.append(u)
            """ materias para el proximo semestre """
            for K in self.quinto_semestre:
                if K not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(K)        
            for U in self.sexto_semestre:
                if U not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(U)
            """ prerrequisitos """
            if "Macroeconomia 1 " not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Historia economica colombiana ")
            if "Econometria basica " not in self.materias_aprobadas:
                self.materias_proximo_semestre.remove("Econometria intermedia ")
            
            print ("\nEstas son las materias disponibles para el siguiente semestre\n")
            print (self.materias_proximo_semestre)  
            
        """ -------------------------------------- SEPTIMO SEMESTRE ----------------------------------"""
        
        if (self.semester == 7):
            #COPIA LISTA OCTAVO SEMESTRE
            self.materias_proximo_semestre = self.septimo_semestre[:]
            for i in self.primer_semestre:
                self.materias_aprobadas.append(i)
            for l in self.segundo_semestre:
                self.materias_aprobadas.append(l)
            for m in self.tercer_semestre:
                self.materias_aprobadas.append(m)
            for n in self.cuarto_semestre:
                self.materias_aprobadas.append(n)
            for k in self.quinto_semestre:
                self.materias_aprobadas.append(k)
                
            """ materias aprobadas sexto semestre """    
            for u in self.sexto_semestre:
                materias = input(u)
                if materias == "si":
                    self.materias_aprobadas.append(u)
            """ materias aprobadas septimo semestre """
            for w in self.septimo_semestre:
                materias = input(w)
                if materias == "si":
                    self.materias_aprobadas.append(w)
            """ materias para el proximo semestre """
            for U in self.sexto_semestre:
                if U not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(U)        
            for W in self.septimo_semestre:
                if W not in self.materias_aprobadas:
                    self.materias_proximo_semestre.append(W)
           
            print ("\nEstas son las materias disponibles para el siguiente semestre\n")
            print (self.materias_proximo_semestre)
    
# ESTA FUNCION VA A RETORNARME LA LISTA DE LAS MATERIAS DISPONIBLES PARA EL SIGUIENTE SEMESTRE, PARA USARLO EN LA SIGUIENTE CLASE   
    def get_materias_proximo_semestre(self):  
        return self.materias_proximo_semestre

class Horario:
    #LISTA VACIA DE MATERIAS A LAS QUE SE LES ESCRIBIO SI PARA QUERER DAR EN EL PROXIMO SEMESTRE 
    materias_para_horario = []
    # DICCIONARIO CON MATERIA Y HORARIO
    horario_para_materias = {"Medicion economica ": "Lunes y miercoles de 11-1", "Historia economica general ": "Martes y jueves de 7-9", "Etica ": "Lunes de 9-11", "Calculo 2 ": "Lunes y viernes de 1-3", "Algebra lineal ": "Jueves y viernes de 11-1", "Microeconomia 1 ": "Martes y jueves de 9-11", "Electiva complementaria ": "Martes y jueves de 5-7", "Economia matematica ": "Miercoles y viernes de 9-11", "Probabilidad ": "Martes y viernes de 1-3", "Microeconomia 2 ": "Lunes y miercoles de 1-3", "Macroeconomia 1 ": "Martes y jueves de 3-5", "Estadistica ": "jueves y viernes de 1-3", "Constitucion politica e instruccion civica ": "Jueves de 1-3", "Macroeconomia 2 ": "Martes y viernes de 7-9", "Microeconomia 3 ": "Martes y miercoles de 7-9", "Econometria basica ": "Martes y jueves de 3-5", "Lectura critica para economia y finanzas ": "Lunes y miercoles de 7-9", "Historia economica colombiana ": "Lunes de 3-5", "Macroeconomia 3 ": "Miercoles y viernes de 7-9", "Econometria intermedia ": "Jueves de 7-9", "Escritura academica para economia y finanzas ": "Lunes y jueves de 11-1", "Electiva general ": "Lunes de 5-7" }
    #DICCIONARIO ANTERIOR ALREVEZ
    horario_para_materias_2 = {"Lunes y miercoles de 11-1": "Medicion economica ", "Martes y jueves de 7-9": "Historia economica general ", "Lunes de 9-11": "Etica ", "Lunes y viernes de 1-3": "Calculo 2 ", "Jueves y viernes de 11-1": "Algebra lineal ", "Martes y jueves de 9-11": "Microeconomia 1 ", "Martes y jueves de 5-7": "Electiva complementaria ", "Miercoles y viernes de 9-11": "Economia matematica ", "Martes y viernes de 1-3": "Probabilidad ", "Lunes y miercoles de 1-3": "Microeconomia 2", "Martes y jueves de 3-5": "Macroeconomia 1", "jueves y viernes de 1-3": "Estadistica ", "Jueves de 1-3": "Constitucion politica ", "Martes y viernes de 7-9": "Macroeconomia 2 ", "Martes y miercoles de 7-9": "Microeconomia 3 ", "Martes y jueves de 3-5": "Econometria basica ", "Lunes y miercoles de 7-9": "Lectura critica para economia y finanzas ", "Lunes de 3-5": "Historia economica de colombia ", "Miercoles y viernes de 7-9": "Macroeconomia 3 ", "Jueves de 7-9": "Econometria intermedia ", "Lunes y jueves de 11-1": "Escritura academica para economia y finanzas ", "Lunes de 5-7": "Electiva general "}
    #CLAVES DE LOS DICCIONARIOS
    claves = horario_para_materias.keys()
    claves_2 = horario_para_materias_2.keys()
    
    #Esta lista son los valores (de la lista horario_para_materias) para las claves en materias_para_horario
    valores_de_materias_para_horario = []
    # LISTAS DE LOS DIAS VACIAS
    lunes = []
    martes = []
    miercoles = []
    jueves = []
    viernes = []
    
    def __init__(self,lista):
        self.materias_preliminares_para_horario = lista
        
    # ESTA FUNCION RETORNA LAS MATERIAS FINALES YA PARA EL HORARIO
    def numero_max_materias(self):
        print ('\nIngrese que materias quiere ver el proximo semestre (maximo 6, ingrese "si" o "no") : ')
        for i in self.materias_preliminares_para_horario:
            materias = input(i)
            if materias == "si":
                self.materias_para_horario.append(i)
                if len(self.materias_para_horario) > 6:
                    print("Ingresaste mas de 6 materias")
                    
    #ESTA FUNCION COMPARA LAS CLAVES DE (HORARIO PARA MATERIAS) CON LA LISTA DE (MATERIAS PARA HORARIO). PARA ASI AÑADIR LOSVALORES CORRESPONDIENTES A ESAS CLAVES A LA LISTA (VALORES_DE_MATERIAS_PARA_HORARIO)
    def comparacion_y_horario_de_materias(self):
        for i in self.claves:
            for l in self.materias_para_horario:
                if i == l:
                    self.valores_de_materias_para_horario.append(self.horario_para_materias[i])
        print(self.valores_de_materias_para_horario)            
    
    #UNES A LAS LISTAS DE DIAS VACIAS, LOS VALORES DE (horario_para_materias_2(recuerde que es un diccionario alrevez del anterior)), USANDO SUS CLAVES.
    def dias_del_hoario(self):
        for i in self.valores_de_materias_para_horario:
            if ("Lunes" in i) or ("lunes" in i):
                self.lunes.append(self.horario_para_materias_2[i])
                    
        for i in self.valores_de_materias_para_horario:
            if ("Martes" in i) or ("martes" in i):     
                self.martes.append(self.horario_para_materias_2[i]) 
                      
        for i in self.valores_de_materias_para_horario:
            if ("Miercoles" in i) or ("miercoles" in i):
                self.miercoles.append(self.horario_para_materias_2[i])
        
        for i in self.valores_de_materias_para_horario:    
            if ("Jueves" in i) or ("jueves" in i):
                self.jueves.append(self.horario_para_materias_2[i]) 
                    
        for i in self.valores_de_materias_para_horario: 
            if ("Viernes" in i)  or ("viernes" in i):
                self.viernes.append(self.horario_para_materias_2[i])
    
    # CREA EL ESQUEMA FINAL DEL HORARIO
    def esquema_del_horario(self):     
        print("HORARIO")                  
        print ("\nLUNES\n")
        for i in self.lunes:
            print (i)   
        
        print ("\nMARTES\n")
        for i in self.martes:
            print(i)
        
        print ("\nMIERCOLES\n")
        for i in self.miercoles:
            print(i)
        
        print ("\nJUEVES\n")   
        for i in self.jueves:
            print(i)
        
        print ("\nVIERNES\n")
        for i in self.viernes:
            print(i) 
            
       
                    
            
        
            
        
        
        
        
         
 
                         
             
    