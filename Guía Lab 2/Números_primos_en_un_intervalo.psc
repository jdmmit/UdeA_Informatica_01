Algoritmo NumerosPrimos
	Definir inicio, limiteFin, i, j, esPrimo Como Entero;
	Escribir 'Ingrese el intervalo (inicio y fin):';
	Leer inicio, limiteFin;
	Para i<-inicio Hasta limiteFin Hacer
		esPrimo <- 1;
		Si i<=1 Entonces // Se asume que es primo
			esPrimo <- 0;
		SiNo
			j <- 2;
			Mientras j<=i-1 Y esPrimo=1 Hacer
				Si i MOD j=0 Entonces
					esPrimo <- 0;
				FinSi
				j <- j+1;
			FinMientras
		FinSi
		Si esPrimo=1 Entonces
			Escribir i;
		FinSi
	FinPara
FinAlgoritmo
