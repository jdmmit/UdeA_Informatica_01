Algoritmo CantidadDigitos
	Definir N, contador Como Entero;
	Escribir 'Ingrese un n�mero:';
	Leer N;
	contador <- 0;
	Mientras N>0 Hacer
		N <- trunc(N/10);
		contador <- contador+1;
	FinMientras
	Escribir 'El n�mero tiene ', contador, ' d�gitos.';
FinAlgoritmo
