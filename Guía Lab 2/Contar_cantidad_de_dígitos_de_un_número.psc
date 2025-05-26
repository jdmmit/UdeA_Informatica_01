Algoritmo CantidadDigitos
	Definir N, contador Como Entero;
	Escribir 'Ingrese un número:';
	Leer N;
	contador <- 0;
	Mientras N>0 Hacer
		N <- trunc(N/10);
		contador <- contador+1;
	FinMientras
	Escribir 'El número tiene ', contador, ' dígitos.';
FinAlgoritmo
