# CNAB
## É necessário ter python 3.10.6 ou maior, não foi testado em versões inferiores
## Use os seguintes comandos no seu terminal para rodar a aplicação
### Clone o repositório primeiro
```
git clone git@github.com:wilsonmesquita03/CNAB.git
cd CNAB
```
### Crie um ambiente virtual
```
python -m venv venv
```
### Ative o ambiente virtual
No Windows
```
.\venv\Scripts\activate
```
No Linux
```
source venv/bin/activate
```
### Instale as dependências 
```
pip install -r requirements.txt
```
## Rodar migrations e servidor
```
python manage.py migrate
python manage.py runserver
```

## Repositório Front: https://github.com/wilsonmesquita03/cnab-web
