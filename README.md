Este repositório contém uma aplicação que utiliza Docker para facilitar a execução e configuração. Abaixo estão as instruções para configurar e utilizar o projeto.

Configuração
Construir e Executar a Aplicação

Execute os seguintes comandos para construir e iniciar a aplicação:
Copiar código
docker compose build
docker compose up app
Configuração das Variáveis de Ambiente

Defina os valores das variáveis de ambiente necessárias:
typescript
Copiar código
export OPENAI_API_KEY=<sua-chave-da-API-da-OpenAI>
export SECRET_KEY=<sua-string-secreta>
Substitua <sua-chave-da-API-da-OpenAI> com sua chave da API da OpenAI e <sua-string-secreta> com uma string de sua escolha para construir a sessão do usuário.
Endpoints Disponíveis
[POST] /user/create

Cria um novo usuário.
Payload necessário:
json
Copiar código
{
    "name": "nome-do-usuario",
    "password": "senha-do-usuario"
}
[POST] /user/login

Realiza o login de um usuário existente.
Payload necessário:
json
Copiar código
{
    "name": "nome-do-usuario",
    "password": "senha-do-usuario"
}
[POST] /suggestionFromPrompt

Envia uma pergunta para a API da OpenAI e retorna uma sugestão.
Payload necessário:
json
Copiar código
{
    "data": "sua-pergunta-para-a-API-da-OpenAI"
}
[GET] /getHistory/<userId>

Obtém o histórico de mensagens de um usuário.
Substitua <userId> pelo ID do usuário desejado.
Observações
Certifique-se de configurar corretamente as variáveis de ambiente antes de utilizar os endpoints que dependem delas.
Para garantir o funcionamento correto dos endpoints que requerem autenticação (como /user/login e /getHistory/<userId>), utilize informações válidas de usuário e senha.
Qualquer dúvida ou problema, consulte a documentação adicional fornecida ou entre em contato com a equipe responsável.

Esse README fornecerá as informações necessárias para configurar e utilizar sua aplicação de forma eficiente.
