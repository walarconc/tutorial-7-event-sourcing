from aeroalpes.seedwork.aplicacion.comandos import ComandoHandler
from aeroalpes.modulos.auditoria.infraestructura.fabricas import FabricaRepositorio
from aeroalpes.modulos.auditoria.dominio.fabricas import FabricaAuditorias

class CrearRegulacionBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias   
    