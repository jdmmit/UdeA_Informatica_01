Algoritmo Calculadora
	Definir A, B, opcion Como Entero;
	Repetir
		// Pedir los valores de A y B
		Escribir 'Ingrese el valor de A: ';
		Leer A;
		Escribir 'Ingrese el valor de B: ';
		Leer B;
		// Mostrar menú de opciones
		Escribir '------------------------------------';
		Escribir '         MENÚ DE OPCIONES';
		Escribir '------------------------------------';
		Escribir '1) Multiplicación (A * B)';
		Escribir '2) Residuo (A mod B)';
		Escribir '3) Potencia (A^B)';
		Escribir '4) Mayor de los dos números';
		Escribir '5) Salir';
		Escribir '------------------------------------';
		Escribir 'Seleccione una opción (1-5): ';
		Leer opcion;
		Según opcion Hacer
			1:
				// Multiplicación
				Escribir 'Resultado de A * B = ', A*B;
			2:
				// Residuo (A mod B)
				Si B<>0 Entonces
					Escribir 'El residuo de A / B es: ', A MOD B;
				SiNo
					Escribir 'Error: no se puede obtener residuo con B = 0.';
				FinSi
			3:
				// Potencia usando la función Pot
				Escribir 'A^B = ', (A^B);
			4:
				// Mayor de los dos números
				Si A>B Entonces
					Escribir 'El mayor de A y B es A = ', A;
				SiNo
					Si B>A Entonces
						Escribir 'El mayor de A y B es B = ', B;
					SiNo
						Escribir 'Ambos números son iguales.';
					FinSi
				FinSi
			5:
				Escribir 'Saliendo del programa...';
			De Otro Modo:
				Escribir 'Opción inválida. Intente de nuevo.';
		FinSegún
	Hasta Que opcion=5
FinAlgoritmo
