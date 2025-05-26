Algoritmo Fibonacci
	Definir N, a, b, aux, i Como Entero;
	Escribir 'Ingrese la cantidad de términos:';
	Leer N;
	a <- 0;
	b <- 1;
	Para i<-1 Hasta N Hacer
		Escribir a;
		aux <- a+b;
		a <- b;
		b <- aux;
	FinPara
FinAlgoritmo
