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
Pode-se usar o comando python caso seja o Python 2 instalado. Caso não tenha o módulo venv, pode ser instalado pelo comando informado no erro e executar o comando acima novamente.
7. Instale os requirements:
```bash
pip install -r requirements.txt
```
8. Após estas instalações você possivelmente será capaz de inicializar o projeto:
```bash
python main.py # Or python3 main.py
```
10. Consulte a documentação da API acessando: http://localhost:8001/docs
   
