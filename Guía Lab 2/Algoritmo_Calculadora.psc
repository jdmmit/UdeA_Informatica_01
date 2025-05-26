Algoritmo Calculadora
	Definir A, B, opcion Como Entero;
	Repetir
		// Pedir los valores de A y B
		Escribir 'Ingrese el valor de A: ';
		Leer A;
		Escribir 'Ingrese el valor de B: ';
		Leer B;
		// Mostrar men� de opciones
		Escribir '------------------------------------';
		Escribir '         MEN� DE OPCIONES';
		Escribir '------------------------------------';
		Escribir '1) Multiplicaci�n (A * B)';
		Escribir '2) Residuo (A mod B)';
		Escribir '3) Potencia (A^B)';
		Escribir '4) Mayor de los dos n�meros';
		Escribir '5) Salir';
		Escribir '------------------------------------';
		Escribir 'Seleccione una opci�n (1-5): ';
		Leer opcion;
		Seg�n opcion Hacer
			1:
				// Multiplicaci�n
				Escribir 'Resultado de A * B = ', A*B;
			2:
				// Residuo (A mod B)
				Si B<>0 Entonces
					Escribir 'El residuo de A / B es: ', A MOD B;
				SiNo
					Escribir 'Error: no se puede obtener residuo con B = 0.';
				FinSi
			3:
				// Potencia usando la funci�n Pot
				Escribir 'A^B = ', (A^B);
			4:
				// Mayor de los dos n�meros
				Si A>B Entonces
					Escribir 'El mayor de A y B es A = ', A;
				SiNo
					Si B>A Entonces
						Escribir 'El mayor de A y B es B = ', B;
					SiNo
						Escribir 'Ambos n�meros son iguales.';
					FinSi
				FinSi
			5:
				Escribir 'Saliendo del programa...';
			De Otro Modo:
				Escribir 'Opci�n inv�lida. Intente de nuevo.';
		FinSeg�n
	Hasta Que opcion=5
FinAlgoritmo
