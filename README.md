# Ovo je projekt iz kolegija Poslovni i informacijski sustavi

## Mylist
Osnovne funkcionalnosti : Login zaposlenika, sign up i log out, unos obaveza i brisanje obaveza, pregled obaveza

## Pokretanje aplikacije lokalno
1. Preuzimanje i raspakiravanje svih podataka sa git repozitorija u direktorij

2. Navigacija u terminalu u navedeni direktorij

3. Izrada docker image-a upisivanjem naredbe

    docker build --tag python-flask-app:1.0 .

4. Pokretanje kontejnera na temelju stvorene slike na portu 8080

    docker run  -p 8080:8080 -d python-flask-app:1.0

5. Otvaranje preglednika na adresi

   localhost:8080



