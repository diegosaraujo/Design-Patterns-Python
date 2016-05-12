from impostos import calcula_ISS, calcula_ICMS
class Calculador_de_impostos(object):
      def realiza_calculo(self, orcamento, imposto):
            if (imposto == 'ISS'):
                  imposto_calculado = calcula_ISS(orcamento)
            if (imposto == 'ICMS'):
                  imposto_calculado = calcula_ICMS(orcamento)
            print (('O valor do %s = %s') % (imposto, imposto_calculado))

#O codigo abaixo esta sendo executado so para evitar de criar uma outra classe para isso
#Basta executar este .py para obter o resultado. Caso importe este .py o codigo abaixo nao sera executado
if __name__ == '__main__':
      from orcamento import Orcamento

      calculador = Calculador_de_impostos()

      orcamento = Orcamento(500)

      calculador.realiza_calculo(orcamento, 'ISS')
      calculador.realiza_calculo(orcamento, 'ICMS')
