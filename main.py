from cpf_cnpj import Documento
from telefones_br import TelefoneBr
from datas_dr import DatasBr
from acesso_cep import BuscaEndereco

cpf_um = Documento.cria_documento("45778190824")
cnpj_um = Documento.cria_documento("33915604000117")
print(cpf_um)
print(cnpj_um)
telefone = TelefoneBr("5511952753132")
print(telefone)

date = DatasBr()
print(date.momento_cadastro)
print(date.mes_cadastro())
print(date.semana_cadastro())
print(date.format_data())
print(date)

cep = "01134000"
obj = BuscaEndereco(cep)
bairro, cidade, uf = obj.acessa_cep_api()
print(bairro)
print(cidade)
print(uf)
