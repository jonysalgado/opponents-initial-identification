<h1 align="center">Initial Opponents Identification</h1>
<img src="https://img.shields.io/static/v1?label=Version&message=1.0.0&color=7159c1?style=for-the-badge"/> 

<p align="center">
    <img src="/material/images/team_logo.png">
</p>

<h2 align="center">✅ Tabela de conteúdos</h2>
<!--ts-->
👉 [Para que serve esse projeto?](#introduction)<br/>
👉 [Instalação](#install)<br/>
👉 [Como rodar o projeto?](#rodar_projeto)<br/>
👉 [Mudando os parâmetros de projeto](#parametros)<br/>
👉 [Organização do projeto](#organization)<br/>
👉 [Problemas a serem resolvidos nas próximas versões](#problems)<br/>
<!--te-->

<h2 align="center" href="#introduction">✅ Para que serve esse projeto?</h2>
<h5 align="justify">
&emsp;Esse projeto é destinado a fazer um modelo utilizando algoritmos de machine learning para identificar os oponentes com quem jogamos utilizando-se apenas das métricas que o coach do nosso time tem acesso.
</h5>

<h5 align="justify">
&emsp;O projeto consiste de duas partes: mineração de dados e predição. A parte de mineração pode ser utilizada para outros projetos da equipe, pois ela inicia os jogos, pega os logs e cria os datasets com as métricas que foram utilizadas. Essa parte foi feita de forma a ser o mais escalável possivel, isto é, de forma a poder alterar os parâmetros para criação do dataset que será melhor descrita na seção de parâmetros.
</h5>

<h5 align="justify">
&emsp;A parte de predição é a seção do projeto destinada a testar e aplicar modelos. Foram testados dois modelos: Naive Bayes e K-nearest Neighboors (KNN). Esses dois modelos foram escolhidos devido a sua simplicidade. Durante os testes, descobriu-se que o KNN obtinha uma taxa de acerto maior (90,5%).
</h5>



<h2 align="center" href="#install">✅ Instalação</h2>


<h5 align="justify">
&emsp;Primeiro, clone este repositório no seu pc:
</h5>

```bash
git clone https://gitlab.com/itandroids/projects/soccer2d/itas2d-opponents_identification.git
```

<h5 align="justify">
&emsp;Agora, caso você queira testar os modelos e trabalhar em modelos melhores, instale as libs de python necessárias. Entre na pasta raiz do repositório e digite o comando abaixo:
</h5>

```bash
pip3 install -r requirements.txt
```

<h2 align="center" href="rodar_projeto">✅ Como rodar o projeto?</h2>

<h5 align="justify">
&emsp;Primeiramente, coloque os times que você deseja identificar em um jogo na pasta teams. Tenha em mente que ele classifica os times com base nos times presentes no dataset apenas. Verifique se há um script na pasta raiz do time denominado <i>start.sh</i>, pois o projeto espera esse script de inicialização.
<br/>
<br/>
&emsp;Antes de rodar o projeto, é recomendado que mude os parâmetros de criação do dataset. Para saber sobre os parâmetros, siga para a seção de parâmetros abaixo.
</h5>

<h5 align="justify">
&emsp;Para rodar o projeto basta está na pasta raiz e digitar o comando abaixo no terminal:
</h5>

```bash
python opponents_identification.py
```
<h2 href="parametros" align="center">✅ Mudando os parâmetros de projeto</h2>

<h5 align="justify">
&emsp;Os parâmetros recomendados para se mudar foram descritos abaixo:
</h5>
<h5 align="justify">
<u>CYCLES:</u> Esse parâmetro é usado para indicar quantos frames serão utilizados por jogo para a criação do dataset. A Contagem sempre começa no primeiro frame do jogo.
<br/>
<br/>
<u>NUMBER_MATCHES:</u> Esse parâmetros é usado para indicar quantos jogos com cada time serão feitos. Serão retirados de cada um dos jogos o número de frames iniciais igual ao parâmetro <u>CYCLO</u>.
<br/>
<br/>
<u>ROBOCUP_SERVER_DIR</u>: Esse parâmetro tem que ser alterado para o path do server da Robocup no seu PC. Não modifique a parte <i>os.getcwd()</i>, pois essa função retorna o path atual do programa. Modifique apenas a parte adicional, tendo como path de partida a pasta mining do projeto.
<br/>
<br/>
<u>ROBOCUP_MONITOR_DIR</u>: Da mesma mesma forma como no parâmetro anterior, modifique este parâmetro, porém colocando o path do soccerwindow da Robocup no seu computador.
<br/>
<br/>
<u>LEFT_DIR</u>: Esse parâmetro é o path do script <i>start.sh</i> do time da ITAndroids. Modifique esse parâmetro apenas se deseja colocar o time em outro local ou se o ano do time mudar.
<br/>
<br/>
<u>TEAM_NAMES</u>: Esse parâmetro é uma lista do nome dos times utilizados. Coloque nome igual a pasta do time que foi colocada na pasta <i>teams</i> na raiz do projeto.
<br/>
<br/>
<u>SERVER_FAST</u>: Esse parâmetro é o comando usado para iniciar o server em modo rápido. Não há a necessidade de modificar esse parâmetro.
<br/>
<br/>
<u>PLAYERS_NUMBER</u>: Aqui você coloca a quantidade de players do oponente que você deseja colocar no dataset. O recomendado é 11, porém esse valor é modificável.
</h5>

<h2 align="center" href="organization">✅ Organização do projeto</h2>

```ditaa {cmd=true args=["-E"]}
+-----------------+
|   Pasta raiz    |
+-------+---------+
        |
        |    +---------+
        +--->|   csv   |
        |    +---------+
        |
        |    +---------+
        +--->|  logs   |
        |    +---------+
        |
        |    +----------+
        +--->| material |
        |    +----------+
        |
        |    +--------+
        +--->| mining |
        |    +---+----+
        |        |     +------+
        |        +---->| test |
        |              +------+
        |
        |    +------------+
        +--->| prediction |
        |    +-----+------+
        |          |     +----------+
        |          +---->| datasets |
        |          |     +----------+
        |          |
        |          |     +-----+
        |          +---->| Knn |
        |          |     +-----+        
        |          |
        |          |    +------+
        |          +--->| test |
        |               +------+
        |
        |    +-------+
        +--->| teams |
             +-------+
```

<h5 align="justify">
<u>CSV</u>: Nesta pasta são colocados os os arquivos csv formados na parte <i>mining</i>.
<br/><br/>
<u>logs</u>: Aqui se colocam os logs dos jogos rodados.
<br/><br/>
<u>material</u>: Aqui estão alguns papers que podem auxiliar na manutenção do projeto.
<br/><br/>
<u>mining</u>: Aqui estão todos os scripts necessários para rodas os jogos, o arquivo com os parâmetros e o script para criação dos datasets. Caso queira testar novas modificações, use a pasta <i>test</i>.
<br/><br/>
<u>prediction</u>: Nesta pasta estão todos os arquivos utilizados para a criação e utilização do modelo. Caso queira testar novos modelos (o que seria ótimo para o projeto) faça na pasta <i>test</i>.
<br/><br/>
<u>datasets</u>: Aqui se tem uma cópia do dataset principal criado na parte <i>mining</i>, um dataset de teste (Aqui se tem todas as feactures do dataset criado, porém sem o campo dos times) e um dataset gerado com a saída do modelo.
<br/><br/>
<u>Knn</u>: Aqui estão os arquivos para a criação do modelo em c++ e os arquivos de compilação. Esse modelo deve ser implantado no coach do time da ITAndroids.
<br/><br/>
<u>teams</u>: Aqui deve-se colocar as pastas com os times para a criação do dataset.
</h5>

<h2 align="center" href="problems">✅ Problemas a serem resolvidos nas próximas versões</h2>

<h5 align="justify">
&emsp;Percebi após a criação do modelo em c++ que o desempenho não está muito bom. Porém, em python a taxha de acerto é de cerca de 90%. O problema está na passagem do modelo para c++ e isso pode ser corrigido em uma versão superior.
</h5>


<h5 align="justify">
&emsp;Qualquer problema, pode entrar em contato comigo!
</h5>
<h5 align="right">
Jony Salgado T22
</h5>