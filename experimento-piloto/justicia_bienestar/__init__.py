from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = "justicia_bienestar"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    BONO = 5

    PREGUNTAS = [
        {"id": 1, "pregunta": "¿Cuál es el menor número entero positivo divisible entre 6, 8 y 9?", "opciones": ["36", "72", "48", "144"], "correcta": "72"},
        {"id": 2, "pregunta": "¿Cuánto es 15% de 240?", "opciones": ["24", "30", "36", "40"], "correcta": "36"},
        {"id": 3, "pregunta": "Un producto cuesta S/. 120 con 20% de descuento aplicado. ¿Cuál era el precio original?", "opciones": ["S/. 140", "S/. 150", "S/. 144", "S/. 160"], "correcta": "S/. 150"},
        {"id": 4, "pregunta": "Si todos los gatos son animales y algunos animales son negros, ¿es verdad que todos los gatos son negros?", "opciones": ["Sí, necesariamente", "No, no necesariamente", "Depende del gato", "No hay suficiente información"], "correcta": "No, no necesariamente"},
        {"id": 5, "pregunta": "Completa la secuencia: 1, 3, 6, 10, 15, ___", "opciones": ["18", "19", "20", "21"], "correcta": "21"},
        {"id": 6, "pregunta": "Si hoy es miércoles, ¿qué día será en 10 días?", "opciones": ["Viernes", "Jueves", "Sábado", "Domingo"], "correcta": "Sábado"},
        {"id": 7, "pregunta": "¿Cuál es la capital de Australia?", "opciones": ["Sídney", "Melbourne", "Brisbane", "Canberra"], "correcta": "Canberra"},
        {"id": 8, "pregunta": "¿En qué año terminó la Segunda Guerra Mundial?", "opciones": ["1943", "1944", "1945", "1946"], "correcta": "1945"},
        {"id": 9, "pregunta": "Si 5 máquinas producen 5 piezas en 5 minutos, ¿cuántos minutos necesitan 100 máquinas para producir 100 piezas?", "opciones": ["5", "20", "100", "500"], "correcta": "5"},
        {"id": 10, "pregunta": "¿Cuántas veces aparece el número 3 entre 1 y 30?", "opciones": ["2", "3", "4", "5"], "correcta": "4"},
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        grupos = self.get_groups()
        for i, grupo in enumerate(grupos):
            grupo.tratamiento = (i % 2 != 0)


class Group(BaseGroup):
    tratamiento = models.BooleanField()

    def asignar_bono(self):
        if self.field_maybe_none('tratamiento') is None:
            self.tratamiento = (self.id_in_subsession % 2 == 0)

        p1, p2 = self.get_players()

        # En caso de empate, ganador aleatorio en ambos grupos
        if p1.puntaje == p2.puntaje:
            ganador = random.choice([p1, p2])
        elif self.tratamiento:
            # Tratamiento: gana el de MENOR puntaje
            ganador = p1 if p1.puntaje < p2.puntaje else p2
        else:
            # Control: gana el de MAYOR puntaje
            ganador = p1 if p1.puntaje > p2.puntaje else p2

        ganador.gano_bono = True
        ganador.payoff = C.BONO


class Player(BasePlayer):
    edad = models.IntegerField(label="Edad")
    sexo = models.StringField(label="Sexo", choices=["Masculino", "Femenino"])
    carrera = models.StringField(label="Carrera")
    ciclo = models.IntegerField(label="Ciclo académico")
    promedio = models.StringField(label="Promedio académico", choices=["Menos de 11", "Entre 11 y menos de 13", "Entre 13 y menos de 15", "Entre 15 y menos de 17", "De 17 a más", "Prefiero no responder"])
    beca = models.BooleanField(label="¿Cuentas con beca?", choices=[[True, "Sí"], [False, "No"]])
    practicando = models.BooleanField(label="¿Estás practicando?", choices=[[True, "Sí"], [False, "No"]])
    situacion_economica = models.StringField(label="Situación económica del hogar", choices=["Muy difícil", "Difícil", "Regular", "Cómoda", "Muy cómoda", "Prefiero no responder"])
    horas_sueno = models.StringField(label="Horas de sueño", choices=["Menos de 5", "Entre 5 y menos de 6", "Entre 6 y menos de 7", "Entre 7 y menos de 8", "8 o más"])

    puntaje = models.IntegerField(initial=0)
    gano_bono = models.BooleanField(initial=False)
    r1 = models.StringField(blank=True)
    r2 = models.StringField(blank=True)
    r3 = models.StringField(blank=True)
    r4 = models.StringField(blank=True)
    r5 = models.StringField(blank=True)
    r6 = models.StringField(blank=True)
    r7 = models.StringField(blank=True)
    r8 = models.StringField(blank=True)
    r9 = models.StringField(blank=True)
    r10 = models.StringField(blank=True)

    j1 = models.IntegerField(label="¿Qué tan justa te pareció la regla de asignación del bono?", choices=[1,2,3,4,5])
    j2 = models.IntegerField(label="¿Qué tan justo te pareció el resultado?", choices=[1,2,3,4,5])
    j3 = models.IntegerField(label="¿Qué tanto crees que el bono reflejó el esfuerzo realizado?", choices=[1,2,3,4,5])
    j4 = models.IntegerField(label="¿Qué tan injusta te parecería una regla similar en un contexto académico o laboral?", choices=[1,2,3,4,5])

    m1 = models.IntegerField(label="En este momento me siento frustrado/a", choices=[1,2,3,4,5])
    m2 = models.IntegerField(label="En este momento me siento tenso/a", choices=[1,2,3,4,5])
    m3 = models.IntegerField(label="En este momento me siento preocupado/a", choices=[1,2,3,4,5])
    m4 = models.IntegerField(label="En este momento siento incomodidad con el resultado", choices=[1,2,3,4,5])

    mot1 = models.IntegerField(label="Después de esta experiencia, me sentiría motivado/a a esforzarme en una tarea similar", choices=[1,2,3,4,5])
    mot2 = models.IntegerField(label="Cuando las recompensas dependen del desempeño, siento que vale la pena esforzarse", choices=[1,2,3,4,5])
    mot3 = models.IntegerField(label="Si las recompensas no reconocen el esfuerzo, mi motivación para esforzarme disminuye", choices=[1,2,3,4,5])

    c1 = models.IntegerField(label="Confío en que mi esfuerzo académico puede traducirse en mejores oportunidades", choices=[1,2,3,4,5])
    c2 = models.IntegerField(label="Siento que mi rendimiento académico
