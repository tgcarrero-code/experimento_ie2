
from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = "justicia_bienestar"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    BONO = 5

    PREGUNTAS = [
        {"id": 1, "pregunta": "¿Cuánto es 17 × 8?", "opciones": ["126", "136", "144", "152"], "correcta": "136"},
        {"id": 2, "pregunta": "¿Cuánto es 15% de 240?", "opciones": ["24", "30", "36", "40"], "correcta": "36"},
        {"id": 3, "pregunta": "Un producto cuesta S/. 120 con 20% de descuento. ¿Cuál era el precio original?", "opciones": ["S/. 140", "S/. 150", "S/. 144", "S/. 160"], "correcta": "S/. 150"},
        {"id": 4, "pregunta": "Si todos los gatos son animales y algunos animales son negros, ¿todos los gatos son negros?", "opciones": ["Sí, necesariamente", "No, no necesariamente", "Depende del gato", "No hay suficiente información"], "correcta": "No, no necesariamente"},
        {"id": 5, "pregunta": "Completa la secuencia: 1, 3, 6, 10, 15, ___", "opciones": ["18", "19", "20", "21"], "correcta": "21"},
        {"id": 6, "pregunta": "Si hoy es miércoles, ¿qué día será en 10 días?", "opciones": ["Viernes", "Jueves", "Sábado", "Domingo"], "correcta": "Sábado"},
        {"id": 7, "pregunta": "¿Cuál es la capital de Australia?", "opciones": ["Sídney", "Melbourne", "Brisbane", "Canberra"], "correcta": "Canberra"},
        {"id": 8, "pregunta": "¿En qué año terminó la Segunda Guerra Mundial?", "opciones": ["1943", "1944", "1945", "1946"], "correcta": "1945"},
        {"id": 9, "pregunta": "¿Cuántas letras a hay en: La naturaleza amazónica alberga una fauna extraordinaria?", "opciones": ["8", "9", "10", "14"], "correcta": "14"},
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
        p1, p2 = self.get_players()
        if self.tratamiento:
            ganador = p1 if p1.puntaje <= p2.puntaje else p2
        else:
            ganador = p1 if p1.puntaje >= p2.puntaje else p2
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

    j1 = models.IntegerField(label="¿Qué tan justa te pareció la regla?", choices=[1,2,3,4,5])
    j2 = models.IntegerField(label="¿Qué tan justo te pareció el resultado?", choices=[1,2,3,4,5])
    j3 = models.IntegerField(label="¿El bono reflejó el esfuerzo realizado?", choices=[1,2,3,4,5])
    j4 = models.IntegerField(label="¿Qué tan injusta sería una regla similar en contexto académico?", choices=[1,2,3,4,5])

    m1 = models.IntegerField(label="En este momento me siento frustrado/a", choices=[1,2,3,4,5])
    m2 = models.IntegerField(label="En este momento me siento tenso/a", choices=[1,2,3,4,5])
    m3 = models.IntegerField(label="En este momento me siento preocupado/a", choices=[1,2,3,4,5])
    m4 = models.IntegerField(label="En este momento siento incomodidad con el resultado", choices=[1,2,3,4,5])

    mot1 = models.IntegerField(label="Me sentiría motivado/a a esforzarme en una tarea similar", choices=[1,2,3,4,5])
    mot2 = models.IntegerField(label="Cuando las recompensas dependen del desempeño, vale la pena esforzarse", choices=[1,2,3,4,5])
    mot3 = models.IntegerField(label="Si las recompensas no reconocen el esfuerzo, mi motivación disminuye", choices=[1,2,3,4,5])

    c1 = models.IntegerField(label="Confío en que mi esfuerzo académico puede traducirse en mejores oportunidades", choices=[1,2,3,4,5])
    c2 = models.IntegerField(label="Mi rendimiento académico puede ayudarme a mejorar mis oportunidades futuras", choices=[1,2,3,4,5])
    c3 = models.IntegerField(label="Esta experiencia me hace pensar con preocupación en si el esfuerzo siempre es recompensado justamente", choices=[1,2,3,4,5])

    def calcular_puntaje(self):
        respuestas = [self.r1, self.r2, self.r3, self.r4, self.r5,
                      self.r6, self.r7, self.r8, self.r9, self.r10]
        correctas = [p["correcta"] for p in C.PREGUNTAS]
        self.puntaje = sum(1 for r, c in zip(respuestas, correctas) if r == c)


class Bienvenida(Page):
    pass

class Demograficos(Page):
    form_model = "player"
    form_fields = ["edad", "sexo", "carrera", "ciclo", "promedio", "beca", "practicando", "situacion_economica", "horas_sueno"]

class Instrucciones(Page):
    pass

class Test(Page):
    form_model = "player"
    form_fields = ["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10"]
    def vars_for_template(self):
        return {"preguntas": C.PREGUNTAS}
    def before_next_page(self, timeout_happened):
        self.player.calcular_puntaje()

class EsperarPareja(WaitPage):
    after_all_players_arrive = "asignar_bono"
    title_text = "Esperando a tu pareja..."
    body_text = "Por favor espera mientras tu pareja termina el test."

class Resultados(Page):
    def vars_for_template(self):
        pareja = self.player.get_others_in_group()[0]
        return {
            "mi_puntaje": self.player.puntaje,
            "puntaje_pareja": pareja.puntaje,
            "gane": self.player.gano_bono,
            "tratamiento": self.group.tratamiento,
        }

class Transicion(Page):
    pass

class PercepcionJusticia(Page):
    form_model = "player"
    form_fields = ["j1", "j2", "j3", "j4"]

class MalestarEmocional(Page):
    form_model = "player"
    form_fields = ["m1", "m2", "m3", "m4"]

class Motivacion(Page):
    form_model = "player"
    form_fields = ["mot1", "mot2", "mot3"]

class Confianza(Page):
    form_model = "player"
    form_fields = ["c1", "c2", "c3"]

class PagoFinal(Page):
    def vars_for_template(self):
        return {
            "pago_variable": C.BONO if self.player.gano_bono else 0,
            "pago_final": 7.50 + (C.BONO if self.player.gano_bono else 0),
        }

page_sequence = [
    Bienvenida, Demograficos, Instrucciones, Test,
    EsperarPareja, Resultados, Transicion,
    PercepcionJusticia, MalestarEmocional, Motivacion, Confianza, PagoFinal,
]
