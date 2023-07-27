# SistemaBancario

Classe ContaBancaria:

A classe representa uma conta bancária simples, com métodos para depósito, saque e exibição do extrato.
Possui dois atributos privados: _saldo (representando o saldo da conta) e _saques_realizados_hoje (número de saques feitos no dia).
Define duas constantes de classe: LIMITE_SAQUES_DIARIOS e LIMITE_SAQUE_DIARIO, que indicam o limite máximo de saques por dia e o valor máximo de saque, respectivamente.
Método deposito:

Recebe como parâmetro o valor a ser depositado.
Se o valor for positivo, adiciona o valor ao saldo da conta, atualiza o atributo _saldo e imprime uma mensagem de sucesso.
Caso o valor seja negativo, imprime uma mensagem de erro.
Método saque:

Recebe como parâmetro o valor a ser sacado.
Verifica se o valor é positivo e se ainda é possível realizar saques no dia (respeitando o limite diário) e se o saldo é suficiente para o saque.
Se todas as condições forem atendidas, subtrai o valor do saldo da conta, atualiza o atributo _saldo, incrementa o contador de saques _saques_realizados_hoje e imprime uma mensagem de sucesso.
Caso contrário, imprime uma mensagem de erro informando o motivo pelo qual o saque não pode ser realizado.
Método extrato:

Imprime um resumo das movimentações realizadas no dia e o saldo atual da conta.
Se não houver saques no dia, informa que não foram realizadas movimentações.
Caso contrário, exibe o número de saques realizados.
Bloco if __name__ == "__main__":

Este bloco é executado somente quando o arquivo Python é executado diretamente (não quando é importado como módulo em outro script).
Cria uma instância da classe ContaBancaria chamada conta.
Em seguida, entra em um loop while True, que continuará executando até que o usuário escolha a opção "0 - Sair".
Loop de interação com o usuário:

Exibe um menu com as opções disponíveis: depósito, saque, extrato e sair.
O usuário insere o número correspondente à opção desejada.
Se a opção for 1 (depósito), solicita o valor do depósito ao usuário, converte para float e chama o método deposito da instância conta.
Se a opção for 2 (saque), solicita o valor do saque ao usuário, converte para float e chama o método saque da instância conta.
Se a opção for 3 (extrato), chama o método extrato da instância conta.
Se a opção for 0 (sair), imprime uma mensagem e encerra o loop, finalizando o programa.
