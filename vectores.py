"""
Tercera tarea de APA: multiplicacion de vectores y ortogonalidad.
Autor: NOMBRE Y APELLIDOS

Este modulo define la clase Vector y las operaciones de multiplicacion por un
escalar, producto de Hadamard, producto escalar y descomposicion de un vector
en sus componentes paralela y perpendicular.
"""

import doctest
from numbers import Number


class Vector:
    """
    Representa un vector matematico.

    Argumentos:
        iterable: Iterable que contiene las componentes del vector.

    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])
    >>> v1 * 2
    Vector([2, 4, 6])
    >>> v1 * v2
    Vector([4, 10, 18])
    >>> v1 @ v2
    32
    >>> v1 = Vector([2, 1, 2])
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> v1 // v2
    Vector([1.0, 2.0, 1.0])
    >>> v1 % v2
    Vector([1.0, -1.0, 1.0])
    >>> v1 == (v1 // v2) + (v1 % v2)
    True
    """

    def __init__(self, iterable):
        """Construye un vector a partir de las componentes de un iterable."""
        self.componentes = list(iterable)

    def __repr__(self):
        """Devuelve una representacion evaluable del vector."""
        return f"Vector({self.componentes!r})"

    def __len__(self):
        """Devuelve el numero de componentes del vector."""
        return len(self.componentes)

    def __getitem__(self, indice):
        """Devuelve la componente situada en el indice indicado."""
        return self.componentes[indice]

    def __eq__(self, other):
        """Indica si dos vectores tienen las mismas componentes."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.componentes == other.componentes

    def _comprobar_dimension(self, other):
        """Comprueba que dos vectores tienen la misma dimension."""
        if len(self) != len(other):
            raise ValueError("los vectores deben tener la misma dimension")

    def __add__(self, other):
        """Devuelve la suma componente a componente de dos vectores."""
        if not isinstance(other, Vector):
            return NotImplemented
        self._comprobar_dimension(other)
        return Vector(a + b for a, b in zip(self.componentes,
                                            other.componentes))

    def __sub__(self, other):
        """Devuelve la resta componente a componente de dos vectores."""
        if not isinstance(other, Vector):
            return NotImplemented
        self._comprobar_dimension(other)
        return Vector(a - b for a, b in zip(self.componentes,
                                            other.componentes))

    def __mul__(self, other):
        """
        Multiplica el vector por un escalar o calcula el producto de Hadamard.

        Argumentos:
            other: Escalar o segundo vector.

        Salida:
            Un nuevo Vector con el resultado.
        """
        if isinstance(other, Number):
            return Vector(componente * other
                          for componente in self.componentes)
        if isinstance(other, Vector):
            self._comprobar_dimension(other)
            return Vector(a * b for a, b in zip(self.componentes,
                                                other.componentes))
        return NotImplemented

    def __rmul__(self, other):
        """Multiplica el vector por un escalar situado a su izquierda."""
        return self * other

    def __matmul__(self, other):
        """
        Calcula el producto escalar de dos vectores.

        Argumentos:
            other: Segundo Vector del producto.

        Salida:
            La suma de los productos de las componentes correspondientes.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        self._comprobar_dimension(other)
        return sum(a * b for a, b in zip(self.componentes,
                                         other.componentes))

    def __floordiv__(self, other):
        """
        Obtiene la componente de este vector paralela a otro.

        Argumentos:
            other: Vector que establece la direccion de la proyeccion.

        Salida:
            La componente paralela como un nuevo Vector.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        self._comprobar_dimension(other)
        norma_cuadrado = other @ other
        if norma_cuadrado == 0:
            raise ValueError("no se puede proyectar sobre el vector nulo")
        return ((self @ other) / norma_cuadrado) * other

    def __mod__(self, other):
        """
        Obtiene la componente de este vector perpendicular a otro.

        Argumentos:
            other: Vector que establece la direccion de referencia.

        Salida:
            La componente perpendicular como un nuevo Vector.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self - self // other


if __name__ == "__main__":
    doctest.testmod(verbose=True)
