from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui
from sklearn import tree
import pandas as pd

uri = "tb_form.csv"
data = pd.read_csv(uri)

total = data['id'].count()

def busca_resposta():
   pergunta = tela_consulta.lineEdit.text()

   X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
   Y = [0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]

   clf = tree.DecisionTreeClassifier()
   clf = clf.fit(X, Y)

   resposta = (clf.predict([[pergunta]]))

   if resposta == 0:
     tela_consulta_resposta_not_trat.show()
     tela_consulta_resposta_not_trat.textEdit.setText(f"Foram entrevistadas um total de {total} pessoas de  Guarulhos e região na pesquisa.")
   elif resposta == 1:
       tela_consulta_resposta.show()
       info_def = data['possui_def']
       possui_deficiencia = info_def[data['possui_def'] == "Sim"].count()
       porcentagem_def = round((possui_deficiencia * 100) / total)
       tela_consulta_resposta.textEdit.setText(f"Aproximadamente {porcentagem_def}% das pessoas entrevistadas possui alguma deficiência ({possui_deficiencia} pessoas).")
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('possui_def_grafico.png'))
   elif resposta == 2:
       tela_consulta_resposta.show()
       info_cond_pontos = data['condicao_pontos']
       cond_pontos_boa = info_cond_pontos[data['condicao_pontos'] == "Boa"].count()
       cond_pontos_ruim = info_cond_pontos[data['condicao_pontos'] == "Ruim"].count()
       porcentagem_cond_pontos_boa = round((cond_pontos_boa * 100) / total)
       porcentagem_cond_pontos_ruim = round((cond_pontos_ruim * 100) / total)
       tela_consulta_resposta.textEdit.setText(f"Aproximadamente {porcentagem_cond_pontos_boa}% das pessoas entrevistadas acham a condição da estrutura dos pontos de ônibus para pessoas deficientes boa ({cond_pontos_boa} pessoas), e aproximadamente {porcentagem_cond_pontos_ruim}% das pessoas entrevistadas acham a condição ruim ({cond_pontos_ruim} pessoas).")
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('cond_pontos_grafico.png'))
   elif resposta == 3:
       tela_consulta_resposta.show()
       info_cond_onibus = data['condicao_onibus']
       cond_onibus_boa = info_cond_onibus[data['condicao_onibus'] == "Boa"].count()
       cond_onibus_ruim = info_cond_onibus[data['condicao_onibus'] == "Ruim"].count()
       porcentagem_cond_onibus_boa = round((cond_onibus_boa * 100) / total)
       porcentagem_cond_onibus_ruim = round((cond_onibus_ruim * 100) / total)
       tela_consulta_resposta.textEdit.setText(f"Aproximadamente {porcentagem_cond_onibus_boa}% das pessoas entrevistadas acham a condição de acessibilidade promovida nos ônibus boa ({cond_onibus_boa} pessoas), e aproximadamente {porcentagem_cond_onibus_ruim}% das pessoas entrevistadas acham a condição ruim ({cond_onibus_ruim} pessoas).")
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('cond_onibus_grafico.png'))
   elif resposta == 4:
       tela_consulta_resposta.show()
       info_rotas = data['rotas']
       possui_rotas = info_rotas[data['rotas'] == "Sim"].count()
       possui_rotas_nao = info_rotas[data['rotas'] == "Não"].count()
       porcentagem_possui_rotas = round((possui_rotas * 100) / total)
       porcentagem_nao_possui_rotas = round((possui_rotas_nao * 100) / total)
       tela_consulta_resposta.textEdit.setText(f"Aproximadamente {porcentagem_possui_rotas}% das pessoas entrevistadas tem duas ou mais opções de ônibus com rotas até o terminal mais próximo ({possui_rotas} pessoas), e aproximadamente {porcentagem_nao_possui_rotas}% das pessoas entrevistadas não tem duas ou mais opções de ônibus com rotas até o terminal mais próximo ({possui_rotas_nao} pessoas).")
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('possui_rotas_grafico.png'))
   elif resposta == 5:
       tela_consulta_resposta.show()
       info_assist = data['como_e_assis']
       assist_boa = info_assist[data['como_e_assis'] == "Boa"].count()
       assist_ruim = info_assist[data['como_e_assis'] == "Ruim"].count()
       porcentagem_assist_boa = round((assist_boa * 100) / total)
       porcentagem_assist_ruim = round((assist_ruim * 100) / total)
       tela_consulta_resposta.textEdit.setText(f"Aproximadamente {porcentagem_assist_boa}% das pessoas entrevistadas julga a assistência que os serviços de transporte público oferecem para a acessibilidade de pessoas deficientes como boa ({assist_boa} pessoas), e aproximadamente {porcentagem_assist_ruim}% das pessoas entrevistadas julga a assistência como ruim ({assist_ruim} pessoas).")
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('como_e_assis_grafico.png'))
   elif resposta == 6:
       tela_consulta_resposta.show()
       info_fisc = data['existe_fisc']
       existe_fisc = info_fisc[data['existe_fisc'] == "Sim"].count()
       nao_existe_fisc = info_fisc[data['existe_fisc'] == "Não"].count()
       nao_sabem_existe_fisc = info_fisc[data['existe_fisc'] == "Não sei"].count()
       porcentagem_existe_fisc = round((existe_fisc * 100) / total)
       porcentagem_nao_existe_fisc = round((nao_existe_fisc * 100) / total)
       porcentagem_nao_sabem_existe_fisc = round((nao_sabem_existe_fisc * 100) / total)
       tela_consulta_resposta.textEdit.setText(f"Aproximadamente {porcentagem_existe_fisc}% das pessoas entrevistadas identificam a atuação de uma fiscalização que acompanha e ajuda a oferecer uma inclusão maior nos transportes públicos da cidade ({existe_fisc} pessoas), e aproximadamente {porcentagem_nao_existe_fisc}% das pessoas entrevistadas não identificam essa atuação ({nao_existe_fisc} pessoas), e aproximadamente {porcentagem_nao_sabem_existe_fisc}% das pessoas entrevistadas não sabem, ou não conhecem sobre essa atuação ({nao_sabem_existe_fisc} pessoas).")
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('existe_fisc_grafico.png'))
   elif resposta == 7:
       tela_consulta_resposta.show()
       tela_consulta.close()
       info_fisc = data['como_e_fisc']
       fisc_boa = info_fisc[data['como_e_fisc'] == "Boa"].count()
       fisc_mediana = info_fisc[data['como_e_fisc'] == "Mediana"].count()
       fisc_ruim = info_fisc[data['como_e_fisc'] == "Ruim"].count()
       porcentagem_fisc_boa = round((fisc_boa * 100) / total)
       porcentagem_fisc_mediana = round((fisc_mediana * 100) / total)
       porcentagem_fisc_ruim = round((fisc_ruim * 100) / total)
       tela_consulta_resposta.textEdit.setText(f"{porcentagem_fisc_boa}% das pessoas entrevistadas julga a atuação da fiscalização para acessibilidade como boa ({fisc_boa} pessoas), e aproximadamente {porcentagem_fisc_mediana}% das pessoas entrevistadas julga a atuação como mediana ({fisc_mediana} pessoas), e aproximadamente {porcentagem_fisc_ruim}% das pessoas entrevistadas julga a atuação como ruim ({fisc_ruim} pessoas).")
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('como_e_fisc_grafico.png'))
   elif resposta == 8:
       tela_consulta_resposta.show()
       regioes = data['regiao']
       regiao1 = regioes[data['regiao'] == "Pimentas"].count()
       porcentagem_regiao1 = round((regiao1 * 100) / total)
       regiao2 = regioes[data['regiao'] == "Taboão"].count()
       porcentagem_regiao2 = round((regiao2 * 100) / total)
       regiao3 = regioes[data['regiao'] == "Centro"].count()
       porcentagem_regiao3 = round((regiao3 * 100) / total)
       regiao4 = regioes[data['regiao'] == "Vila Rio"].count()
       porcentagem_regiao4 = round((regiao4 * 100) / total)

       regiao5 = regioes[data['regiao'] == "Maia"].count()
       porcentagem_regiao5 = round((regiao5 * 100) / total)
       regiao6 = regioes[data['regiao'] == "CECAP"].count()
       porcentagem_regiao6 = round((regiao6 * 100) / total)
       regiao7 = regioes[data['regiao'] == "Vila Galvão"].count()
       porcentagem_regiao7 = round((regiao7 * 100) / total)
       regiao8 = regioes[data['regiao'] == "Cumbica"].count()
       porcentagem_regiao8 = round((regiao8 * 100) / total)
       tela_consulta_resposta.textEdit.setText(f"As quatro regiões que mais se destacaram na obtenção de respostas foram: Pimentas ({porcentagem_regiao1}% das respostas), Taboão ({porcentagem_regiao2}% das respostas), Centro ({porcentagem_regiao3}% das respostas) e Vila Rio ({porcentagem_regiao4}% das respostas). As quatro regiões que menos se destacaram na obtenção de respostas foram: Maia ({porcentagem_regiao5}% das respostas), CECAP ({porcentagem_regiao6}% das respostas), Vila Galvão ({porcentagem_regiao7}% das respostas) e Cumbica ({porcentagem_regiao8}% das respostas).")
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('regioes_grafico.png'))
   elif resposta == 9:
       tela_consulta_resposta.show()
       i = 0
       i2 = 0
       i3 = 0
       i4 = 0

       n_cond_ruim_in_pimentas = 0
       n_cond_ruim_in_taboao = 0
       n_cond_ruim_in_centro = 0
       n_cond_ruim_in_vila_rio = 0
       regioes = data['regiao']
       cond_pontos = data['condicao_pontos']

       while i <= 59:
           if regioes[i] == "Pimentas" and cond_pontos[i] == "Ruim":
               n_cond_ruim_in_pimentas += 1
           i += 1
       regiao_pimentas = regioes[data['regiao'] == "Pimentas"].count()
       porcentagem_cond_ruim_pimentas = round((n_cond_ruim_in_pimentas * 100) / regiao_pimentas)
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('regioes_cond_ruim_grafico.png'))

       while i2 <= 59:
           if regioes[i2] == "Taboão" and cond_pontos[i2] == "Ruim":
               n_cond_ruim_in_taboao += 1
           i2 += 1
       regiao_taboao = regioes[data['regiao'] == "Taboão"].count()
       porcentagem_cond_ruim_taboao = round((n_cond_ruim_in_taboao * 100) / regiao_taboao)
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('regioes_cond_ruim_grafico.png'))

       while i3 <= 59:
           if regioes[i3] == "Centro" and cond_pontos[i3] == "Ruim":
               n_cond_ruim_in_centro += 1
           i3 += 1
       regiao_centro = regioes[data['regiao'] == "Centro"].count()
       porcentagem_cond_ruim_centro = round((n_cond_ruim_in_centro * 100) / regiao_centro)
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('regioes_cond_ruim_grafico.png'))

       while i4 <= 59:
           if regioes[i4] == "Vila Rio" and cond_pontos[i4] == "Ruim":
               n_cond_ruim_in_vila_rio += 1
           i4 += 1
       regiao_vila_rio = regioes[data['regiao'] == "Centro"].count()
       porcentagem_cond_ruim_vila_rio = round((n_cond_ruim_in_vila_rio * 100) / regiao_vila_rio)
       tela_consulta_resposta.label_3.setPixmap(QtGui.QPixmap('regioes_cond_ruim_grafico.png'))

       if porcentagem_cond_ruim_pimentas > porcentagem_cond_ruim_taboao and porcentagem_cond_ruim_pimentas > porcentagem_cond_ruim_centro and porcentagem_cond_ruim_pimentas > porcentagem_cond_ruim_vila_rio:
           tela_consulta_resposta.textEdit.setText(f"A região com menor índice de acessibilidade é o bairro dos Pimentas, com {porcentagem_cond_ruim_pimentas}% das respostas voltadas à acessibilidade definindo a mesma como ruim.")
       elif porcentagem_cond_ruim_taboao > porcentagem_cond_ruim_pimentas and porcentagem_cond_ruim_taboao > porcentagem_cond_ruim_centro and porcentagem_cond_ruim_taboao > porcentagem_cond_ruim_vila_rio:
        tela_consulta_resposta.textEdit.setText(f"A região com menor índice de acessibilidade é o Taboão, com {porcentagem_cond_ruim_taboao}% das respostas voltadas à acessibilidade definindo a mesma como ruim.")
       elif porcentagem_cond_ruim_centro > porcentagem_cond_ruim_pimentas and porcentagem_cond_ruim_centro > porcentagem_cond_ruim_taboao and porcentagem_cond_ruim_centro > porcentagem_cond_ruim_vila_rio:
           tela_consulta_resposta.textEdit.setText(f"A região com menor índice de acessibilidade é o Centro, com {porcentagem_cond_ruim_centro}% das respostas voltadas à acessibilidade definindo a mesma como ruim.")
       elif porcentagem_cond_ruim_vila_rio > porcentagem_cond_ruim_pimentas and porcentagem_cond_ruim_vila_rio > porcentagem_cond_ruim_taboao and porcentagem_cond_ruim_vila_rio > porcentagem_cond_ruim_centro:
           tela_consulta_resposta.textEdit.setText(f"A região com menor índice de acessibilidade é o Vila Rio, com {porcentagem_cond_ruim_vila_rio}% das respostas voltadas à acessibilidade definindo a mesma como ruim.")
   elif resposta == 10:
       tela_consulta_resposta_not_trat.show()
       tela_consulta_resposta_not_trat.textEdit.setText("As sugestões de acessibilidade que mais apareceram na obtenção de respostas foram: Pontos de ônibus mais acessíveis para deficientes (Iluminação e cobertura dos pontos, calçada com rebaixamento, piso tátil, braille identificando as linhas que passam no mesmo), Ônibus adaptados (piso tátil no corredor, rampas de acesso automatizadas e bancos adequados e confortáveis para gestantes e deficientes físicos, terceiro degrau mais baixo para auxiliar pessoas com nanismo, além de revisões periódicas) e profissionais preparados para auxiliar pessoas deficientes e motoristas mais atentos.")

   tela_consulta.close()

def volta_tela_consulta():
    tela_consulta_resposta.close()
    tela_consulta.show()
    tela_consulta.lineEdit.setText("")

def volta_tela_consulta_not_trat():
    tela_consulta_resposta_not_trat.close()
    tela_consulta.show()
    tela_consulta.lineEdit.setText("")

app = QtWidgets.QApplication([])
tela_consulta = uic.loadUi("tela_consulta.ui")
tela_consulta_resposta = uic.loadUi("tela_resposta_consulta.ui")
tela_consulta_resposta_not_trat = uic.loadUi("tela_resposta_consulta_not_trat.ui")
tela_consulta.pushButton.clicked.connect(busca_resposta)
tela_consulta_resposta.pushButton.clicked.connect(volta_tela_consulta)
tela_consulta_resposta_not_trat.pushButton.clicked.connect(volta_tela_consulta_not_trat)
tela_consulta.show()
app.exec()
