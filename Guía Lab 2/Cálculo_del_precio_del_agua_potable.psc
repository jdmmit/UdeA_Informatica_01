Algoritmo PrecioAgua
	Definir m3, estrato, costo, total Como Real;
	Escribir 'Ingrese la cantidad de metros cúbicos consumidos:';
	Leer m3;
	Escribir 'Ingrese el estrato (1 a 6):';
	Leer estrato;
	Si m3<=10 Entonces
		costo <- m3*6;
	SiNo
		Si m3<=13 Entonces
			costo <- m3*5;
		SiNo
			costo <- m3*9;
		FinSi
	FinSi
	total <- costo+50;
	Si estrato=1 O estrato=2 Entonces
		total <- total*0.8;
	FinSi
	Escribir 'El total a pagar es: ', total;
FinAlgoritmo
