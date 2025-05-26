Algoritmo BinarioADecimal
	Definir binario, decimal, base, digito Como Entero;
	Escribir 'Ingrese un número en binario:';
	Leer binario;
	decimal <- 0;
	base <- 1;
	Mientras binario>0 Hacer
		digito <- binario MOD 10;
		decimal <- decimal+(digito*base);
		base <- base*2;
		binario <- trunc(binario/10);
	FinMientras
	Escribir 'El número en decimal es: ', decimal;
FinAlgoritmo
