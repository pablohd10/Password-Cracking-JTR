#!/bin/bash

archivos=("minus_hashed_7.txt" "mayus_hashed_7.txt" "palabras_hashed_1.txt"
          "palabras_hashed_5.txt")

# Loop a través de los archivos
for archivo in "${archivos[@]}"; do
    echo "ATAQUE FUERZA BRUTA INCREMENTAL ALPHA (MAYUS Y MINUS) LONGITUD 7"
    echo "Ejecutando el comando para $archivo"
    rm ~/.john/john.pot
    rm ~/.john/john.log
    time timeout 15m john --format=raw-sha256 --incremental=Alpha --min-length=7 --max-length=7 --fork=4 "$archivo" 
    john --format=raw-sha256 --show "$archivo"
	python3.9 genera_estadisticas.py
    echo
done

