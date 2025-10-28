# Atividade-POO---Classes-e-UML
Atividade 24/10/2025
# Sistema Bancário Simples

## Descrição do Projeto
Este projeto implementa um sistema bancário básico em Python, composto pelas classes `Conta` e `Banco`. A classe `Conta` representa uma conta bancária individual com funcionalidades de crédito, débito e consulta de saldo. A classe `Banco` gerencia múltiplas contas, permitindo operações como cadastro, busca, crédito, débito, consulta de saldo e transferências entre contas. O sistema inclui validações para contas inexistentes e saldos insuficientes.

O projeto foi desenvolvido como atividade prática, completando a implementação da classe `Banco` com os métodos `creditar`, `transferir` e `saldo`, além de um programa principal para testes. Um diagrama UML de classes foi gerado para visualizar a estrutura e relacionamentos.

## Estrutura das Classes

### Classe `Conta`
- **Atributos:**
  - `numero` (int): Número único da conta.
  - `saldo` (float): Saldo atual da conta (inicializado em 0 por padrão).
- **Métodos:**
  - `__init__(numero, saldo=0)`: Inicializa a conta com número e saldo opcional.
  - `get_numero()`: Retorna o número da conta.
  - `get_saldo()`: Retorna o saldo atual.
  - `debitar(valor)`: Debita um valor do saldo, se houver saldo suficiente; caso contrário, exibe mensagem de erro.
  - `creditar(valor)`: Credita um valor ao saldo.

### Classe `Banco`
- **Atributos:**
  - `contas` (list[Conta]): Lista de contas cadastradas (inicializada com 100 posições None).
  - `indice` (int): Índice para controlar o cadastro de contas.
- **Métodos:**
  - `__init__()`: Inicializa o banco com uma lista vazia de contas.
  - `cadastrar(conta: Conta)`: Adiciona uma conta à lista.
  - `procurar_conta(numero)`: Busca e retorna uma conta pelo número; retorna None se não encontrada.
  - `creditar(numero, valor)`: Credita um valor em uma conta existente; exibe erro se a conta não existir.
  - `debitar(numero, valor)`: Debita um valor de uma conta existente; exibe erro se a conta não existir ou saldo insuficiente.
  - `saldo(numero)`: Retorna o saldo de uma conta; exibe erro se a conta não existir.
  - `transferir(origem, destino, valor)`: Transfere um valor entre duas contas, verificando existência e saldo; exibe mensagens de sucesso ou erro.

## Diagrama UML
O diagrama UML de classes ilustra a estrutura do sistema, incluindo atributos, métodos e relacionamentos. Ele foi gerado no estilo clássico com caixas para classes e setas para agregação.

- **Descrição:**
  - A classe `Conta` é independente e representa entidades individuais.
  - A classe `Banco` agrega múltiplas instâncias de `Conta` (relacionamento de agregação com multiplicidade 1..*, indicando que um banco pode gerenciar várias contas).
  - Não há herança ou dependências complexas; o foco é em operações básicas de banco.

Para gerar ou editar o diagrama, use o código PlantUML incluído no repositório (arquivo `diagrama_uml.puml`).

## Como Executar
1. **Pré-requisitos:** Python 3.x instalado.
2. **Execução:**
   - Baixe ou clone o repositório.
   - Execute o arquivo principal (ex.: `banco.py`) via terminal: `python banco.py`.
   - O programa principal cria contas de exemplo, cadastra no banco e testa operações como saldo, crédito, débito e transferência, exibindo resultados no console.
3. **Exemplos de Saída Esperada:**
   - Saldo inicial: "Saldo da conta 123: R$ 1000".
   - Após operações: Mensagens de sucesso ou erro (ex.: "Conta Inexistente!" para contas não cadastradas).

## Testes e Validações
- O programa principal inclui testes automáticos para cenários normais e de erro.
- Cenários cobertos: Cadastro, busca, crédito/débito com saldo suficiente/insuficiente, transferências válidas/inválidas e contas inexistentes.
- Para testes manuais, modifique o código no bloco `if __name__ == "__main__":`.

## Contribuições
- Este projeto foi implementado como atividade educacional. Sugestões de melhorias (ex.: adicionar persistência em arquivo ou interface gráfica) são bem-vindas via pull requests.

## Licença
Este projeto é de uso educacional e não possui licença específica.
