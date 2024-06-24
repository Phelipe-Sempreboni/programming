'''

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Created by: Luiz Phelipe Utiama Sempreboni

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Função resumida do script:
- Realizar a exclusão de arquivos do repositório e/ou servidor e mantém o arquivo do tipo Excel.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Para mais informações sobre as funções do script, consulte o arquivo README.md deste repositório.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ \

'''

# Modelo para excluir arquivos de qualquer tipo de extensão de um determinado repositório (pasta) e manter o arquivo do tipo Excel.
# Neste caso o arquivo principal da variável (nome_arquivo) é ignorado, ou seja, mantido no repositório, e os demais arquivos serão excluídos.
# Altere o nome das variáveis para funcionar corretamente em seu script.

# Importação de biblioteca.
import os  # Módulo para fornecer acesso a funções específicas do sistema para lidar com o sistema de arquivos, processos, planejador, etc.


# Declaração do caminho origem, ou seja, onde os arquivos se encontram.
caminho_origem = r'C:\Windows\Temp\testes'

# Declaração de variável com o nome do arquivo, que neste caso irá facilitar para utilização no decorrer do script.
nome_arquivo = 'Sou-Milionário.xlsx'

# Loop para verificar os arquivos existentes no caminho origem, ou seja, na variável que carrega o caminho.
for root, dirs, files in os.walk(caminho_origem):

    # Este (if) verifica se o (local - root) é o mesmo do repositório (nome_caminho), visto que os arquivos utilizados estão neste repositório.
    # Também certifica que o script não percorra outros repositórios dentro do repositório principal da variável (caminho_origem).
    if root == caminho_origem:

        # Loop para verificar somente os arquivos do for acima.
        for file in files:

            # If para verificar somente o arquivo com o noem da variável (nome_arquivo).
            if file == nome_arquivo:

                # Caso o arquivo da variável (nome_arquivo) seja localizado, então o processo irá prosseguir e ignorar este arquivo.
                continue
                        
            # Else para excluir os demais arquivos que estiverem no caminho origem, ou seja, na variável que carrega o caminho.
            else:

                # Remove os arquivos que não tem o nome da variável (nome_arquivo).
                os.remove(caminho_origem + '\\' + file)

                # Imprimi na tela a mensagem dos arquivos que foram excluídos.
                print('Arquivo', file, 'removido com sucesso!\n')

                # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                print('=======================================================================================================================================================================\n')
