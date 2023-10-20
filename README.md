# twitter-api

Projeto criado utilizando python e tweepy para consumir a API do Twitter (Level Free) para a criação e postagem de tweets.

Caso ainda não tenha crie sua conta no portal Developer Twitter:
https://developer.twitter.com/en/portal/dashboard

Estou utilizando o nível FREE da API, que permite criar/deletar posts e pesquisar usuários.

No Portal Developer Twitter, crie um projeto e atrele um app.
	
Configure o app conforme informações abaixo:
Em "User Authentications Settings" configure os seguintes itens:
	"App Permission" como "Read/Write";
	"Type of App" como "Web App, Automated App or Bot";
 	Em "App info" configure "Web App, Automated App or Bot" e "Website URL" com a url do seu perfil no Twitter. exemplo: https://twitter.com/SEU_USUARIO.

Salve as configurações.	
	
Gere as chaves and tokens do App e salve as chaves abaixo:
	"Consumer Keys";
	"Authentication Tokens".


Instale o tweepy com o comando: pip install tweepy

Clone o projeto:
https://github.com/andersonsoaresmartins/twitter_api.git

Insira as chaves e tokens no arquivo config.py.

Abra o arquivo app.py edite a variável "tweet" com seu texto e execute o arquivo.

Enjoy ;)


