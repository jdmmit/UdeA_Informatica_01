Proceso SalarioSemanal
	Definir horas, pago Como Real;
	Definir sucursal Como Cadena;
	Escribir 'Ingrese la cantidad de horas trabajadas:';
	Leer horas;
	Escribir 'Ingrese la sucursal (A o B):';
	Leer sucursal;
	Si sucursal='A' Entonces
		Si horas<=40 Entonces
			pago <- horas*10;
		SiNo
			pago <- (40*10)+((horas-40)*20);
		FinSi
	SiNo
		Si sucursal='B' Entonces
			Si horas<=45 Entonces
				pago <- horas*12;
			SiNo
				pago <- (45*12)+((horas-45)*25);
			FinSi
		SiNo
			Escribir 'Sucursal no válida.';
			pago <- 0;
		FinSi
	FinSi
	Escribir 'El salario semanal es: ', pago;
FinProceso
