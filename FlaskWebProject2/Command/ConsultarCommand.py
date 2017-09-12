from Command.AbstractCommand import AbstractCommand
class ConsultarCommand(AbstractCommand):
    """description of class"""
    def execute(self,EntidadeDominio):
        return self.fa.Consultar(EntidadeDominio)

