<h1 align="center">
Agendamento de Consulta de Vista
</h1>
<p align="center">
Projeto desenvolvido para disciplina de Sistemas Distribuídos - Ciências da Computação, UFAL Arapiraca
</p>

## Servidor
1. Precisa ter o Python instalado
2. Clone o repositório
```bash
git clone https://github.com/LucasBarbosaSilva/agendamento-CNH-WebService.git
```
4. Nagegue até a pasta servidor
```bash
cd servidor
```
5. Crie um ambiente virtual:
```bash
python3 -m venv .env
```
Pode-se usar o comando python caso seja o Python 2 instalado. Caso não tenha o módulo venv, pode ser instalado pelo comando informado no erro e executar o comando acima novamente. <br>
6. Instale os requirements:
```bash
pip install -r requirements.txt
```
7. Após estas instalações você possivelmente será capaz de inicializar o projeto:
```bash
python main.py # Or python3 main.py
```
8. Consulte a documentação da API acessando: http://localhost:8001/docs
   
## App

1. Precisa ter **npm** e **node.js** instalados na máquina. Caso não possua instalado, siga os passos [aqui](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
2. Nagegue até a pasta app
```bash
cd app
```
3. Instale as dependências com o seguinte comando
```bash
npm install
```
5. Inicie a aplicação
```bash
npm run dev   
```
6. A aplicação estará rodando na porta 5173 http://localhost:5173/.
