#!/bin/bash

archivos=("palabras_hashed_1.txt" "palabras_hashed_2.txt"
 		  "palabras_hashed_3.txt" "palabras_hashed_4.txt"
 		   "palabras_hashed_5.txt")

# Loop a través de los archivos
for archivo in "${archivos[@]}"; do
	echo "ATAQUE DE DICCIONARIO CON REGLA CREADA POR NOSOTROS"
    echo "Ejecutando el comando para $archivo"
    rm ~/.john/john.pot
    rm ~/.john/john.log
    time timeout 15m john --rule=My_rule --fork=4 --format=raw-sha256 --wordlist=diccionario.txt "$archivo"
    john --format=raw-sha256 --show "$archivo"
    python3.9 genera_estadisticas.py
    echo
done
