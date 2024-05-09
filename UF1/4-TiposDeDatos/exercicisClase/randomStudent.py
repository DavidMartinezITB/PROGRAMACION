from random import choice

STUDENTS = (
    "jofre.aleman.7e7@itb.cat",
    "alex.valdemoro.7e4@itb.cat",
    "daniel.arco.7e5@itb.cat",
    "izan.arnaiz.7e5@itb.cat",
    "adam.benahmed.7e7@itb.cat",
    "axel.benitez.7e7@itb.cat",
    "ruben.blas.7e6@itb.cat",
    "iker.blazquez.7e7@itb.cat",
    "franz.camacho.7e6@itb.cat",
    "cristhian.contreras.7e7@itb.cat",
    "roger.domingo.7e7@itb.cat",
    "erik.doral.7e4@itb.cat",
    "axel.garcia.7e7@itb.cat",
    "alex.jimenez.7e7@itb.cat",
    "josue.loor.7e4@itb.cat",
    "ruddy.mamani.7e5@itb.cat",
    "david.martinez.parra.7e7@itb.cat",
    "jonathan.merce.7e7@itb.cat",
    "jaume.sampera.7e5@itb.cat",
    "laura.olivera.7e7@itb.cat",
    "javier.ortega.7e7@itb.cat",
    "david.quintas.7e7@itb.cat",
    "carlos.quintos.7e3@itb.cat",
    "david.sanchez.7e7@itb.cat",
    "fatima.saoudi.7e7@itb.cat",
    "david.vargas.mercado@itb.cat"
    "omar.vargas.7e7@itb.cat",
    "jose.villalba.7e7@itb.cat",
    "oscar.bravo.7e5@itb.cat",
    "ion.zarija.7e5@itb.cat"
)
while True:
    print("\033c", end='') # Clear term
    input(f'-> {choice(STUDENTS)} <- \n[!] Pulsa enter para escoger otro alumno!')
    # input(f'-> {STUDENTS[randint(0, len(STUDENTS) - 1)]} <- \n[!] Pulsa enter para escoger otro alumno!')