#!/bin/bash

archivos=("minus_hashed_3.txt" "minus_hashed_4.txt" "minus_hashed_5.txt"
 "minus_hashed_6.txt" "minus_hashed_7.txt" "mayus_hashed_3.txt" 
 "mayus_hashed_4.txt" "mayus_hashed_5.txt" "mayus_hashed_6.txt"  
 "mayus_hashed_7.txt" "num_hashed_3.txt" "num_hashed_4.txt" 
 "num_hashed_5.txt" "num_hashed_6.txt" "num_hashed_7.txt" 
 "alfanum_simb_hashed_3.txt" "alfanum_simb_hashed_4.txt" 
 "alfanum_simb_hashed_5.txt" "alfanum_simb_hashed_6.txt" 
 "alfanum_simb_hashed_7.txt" "palabras_hashed_1.txt" "palabras_hashed_2.txt" 
 "palabras_hashed_3.txt" "palabras_hashed_4.txt" "palabras_hashed_5.txt")

# Loop a través de los archivos
for archivo in "${archivos[@]}"; do
	echo "ATAQUE INCREMENTAL FUERZA BRUTA ASCII LONGITUDES 3,4,5,6,7"
    echo "Ejecutando el comando para $archivo"
    rm ~/.john/john.pot
    rm ~/.john/john.log
    time timeout 15m john --format=raw-sha256 --incremental=ascii --min-length=3 --max-length=7 --fork=4 "$archivo"
    john --format=raw-sha256 --show "$archivo"
    python3.9 genera_estadisticas.py
    echo
done

