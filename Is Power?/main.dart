/*
* Recursos utilizados para entender el algoritmo:
* - https://www.superprof.es/diccionario/matematicas/aritmetica/radicacion.html#:~:text=La%20radicaci%C3%B3n%20es%20la%20operaci%C3%B3n,en%20este%20caso%20se%20omite.
* - https://stackoverflow.com/questions/58033509/how-to-get-n-power-square-of-a-number-or-cube-etc-of-a-number-in-flutter
*/

import 'dart:math';

bool solution(int n) {
  int base = 2;
  double number = double.parse(n.toString());

  // Mientras que la raíz exacta sea 2 o mayor a 2 ya que 1 elevado a cualquier numero es 1
  // Vamos probando con todas los números a partir de 2 como indice de la raíz de n hasta encontrar la raíz exacta que sera elevada al indice utilizado para hallarla igual al numero n.
  while (number >= 2) {
    // Hacemos la operación contraria a la potenciación, la radicación, para obtener la raíz exacta que elevada a la base da el numero n.
    // Dividimos 1 porque la formula para sacar la raíz exacta de un numero con un potencia es:
    // n^(1/indice) = raizExacta^indice = n
    // Para calcular la raíz de un numero n equivale ha hacer la potencia de ese numero entre 0.5 por ejemplo
    number = double.parse(pow(n, (1 / base)).toStringAsFixed(2));

    // Comparamos si el numero es un entero, si es entero es porque es una potencia de un numero, por eso hallamos el entero menor y mayor
    final int min = number.floor();
    final int max = number.ceil();

    if (max == min) return true;

    base++;
  }

  // Si el numero es 1 es porque es 0^0
  return n == 1;
}
