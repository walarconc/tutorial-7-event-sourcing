""" Interfaces para los repositorios del dominio de vuelos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de vuelos

"""

from abc import ABC
from sta.seedwork.dominio.repositorios import Repositorio

class RepositorioRegulaciones(Repositorio, ABC):
    ...

class RepositorioEventosRegulaciones(Repositorio, ABC):
    ...