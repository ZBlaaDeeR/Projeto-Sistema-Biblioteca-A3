from MODEL.membro import Membro

class MembroController:
    def __init__(self):
        pass

    def atualizarDadosMembro(self, id_membro, nome, gmail, telefone, cpf):
        membro = Membro()
        return membro.atualizar_dados_membro(id_membro, nome, gmail, telefone, cpf)


    def exibirDadosMembro(self,IDmembro):
        membro = Membro()
        return membro.buscarMembroPorID(IDmembro)

    def pesquisarMembro(self,termo):
        membro = Membro()
        return membro.buscarMembro(termo)

    def excluirMembro(self,membroID):
        membro = Membro()
        membro.excluir_membro(membroID)

    
    def exibirMembros(self):
        membro = Membro()
        return membro.exibir_membros()

    def cadastrarMembro(self, nome, gmail, telefone, CPF):
        membro = Membro(nome, gmail, telefone, CPF)
        membro.adicionar_membro()

    def verificarTelefone(self,texto: str) -> bool:
      return len(texto) >= 15

    def validadorCpf(self,cpf: str) -> bool:
        # Remove pontos, traços e outros caracteres
        cpf = ''.join(filter(str.isdigit, cpf))

        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Rejeita CPFs com todos os dígitos iguais (ex: 00000000000, 11111111111)
        if cpf == cpf[0] * 11:
            return False

        # Valida o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        # Valida o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        # Compara com os dígitos do CPF informado
        return cpf[-2:] == f"{digito1}{digito2}"
