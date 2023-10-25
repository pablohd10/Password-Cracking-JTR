#/bin/bash

archivos=("alfanum_simb_hashed_3.txt" "alfanum_simb_hashed_4.txt" 
		  "alfanum_simb_hashed_5.txt" "palabras_hashed_4.txt")

# Loop a través de los archivos
for archivo in "${archivos[@]}"; do
    echo "ATAQUE FUERZA BRUTA INCREMENTAL ASCII LONGITUDES 3, 4 y 5"
    echo "Ejecutando el comando para $archivo"
    rm ~/.john/john.pot
    rm ~/.john/john.log
    time timeout 15m john --format=raw-sha256 --incremental=ascii --min-length=3 --max-length=5 --fork=4 "$archivo"
    john --format=raw-sha256 --show "$archivo"
    python3.9 genera_estadisticas.py
    echo
done

