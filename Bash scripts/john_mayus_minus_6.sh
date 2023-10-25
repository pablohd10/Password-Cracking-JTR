#!/bin/bash

archivos=("minus_hashed_6.txt" "mayus_hashed_6.txt" "palabras_hashed_1.txt"
          "palabras_hashed_5.txt")

# Loop a través de los archivos
for archivo in "${archivos[@]}"; do
    echo "ATAQUE FUERZA BRUTA INCREMENTAL ALPHA (MAYUS Y MINUS) LONGITUD 6"
    echo "Ejecutando el comando para $archivo"
    rm ~/.john/john.pot
    rm ~/.john/john.log
    time timeout 15m john --format=raw-sha256 --incremental=Alpha --min-length=6 --max-length=6 --fork=4 "$archivo"
    john --format=raw-sha256 --show "$archivo"
	python3.9 genera_estadisticas.py
    echo
done

