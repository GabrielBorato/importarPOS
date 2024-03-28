from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
from datetime import datetime
from bot import operar_robo  

app = Flask(__name__)
app.secret_key = 'flavinhodopneu'
base_url = 'http://172.25.95.165'

# Função para autenticar o usuário
def authenticate_user(username, password):
    auth_url = "https://autenticacao.superkoch.com.br/login"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(auth_url, json=data)

    if response.status_code == 200:
        user_data = response.json()
        user_group = user_data.get('GRUPO')
        if user_group == 'agpaineladm' or user_group == 'financeiro':
            return True
        else:
            flash('Você não tem permissão para acessar este recurso.', 'error')
            return False
    elif response.status_code == 401:
        flash('Usuário ou senha incorretos. Tente novamente.', 'error')
        return False
    else:
        flash('Erro de autenticação. Tente novamente mais tarde.', 'error')
        return False

# Rota para renderizar a página inicial de login
@app.route('/')
def index():
    return render_template('login.html')

# Rota para processar o formulário de login
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    
    if authenticate_user(username, password):
        return redirect(url_for('start_index'))  # Redirecionar para a página inicial do robô após autenticação
    else:
        return redirect(url_for('index'))  # Redirecionar de volta para a página de login em caso de falha na autenticação

# Rota para a página inicial do robô
@app.route('/start')
def start_index():
    return render_template('portal.html')

@app.route('/operar-robo', methods=['POST'])
def operar_robo():
    data_recebida = request.form.get('data_recebida')  # Usamos get() para evitar erro caso a chave não exista
    
    if not data_recebida:
        return render_template('portal.html', error="Por favor, insira uma data de operação.")  
    
    data_formatada = datetime.strptime(data_recebida, "%Y-%m-%d")
    
    if data_formatada > datetime.now():
        return render_template('portal.html', error="Por favor, insira uma data válida no passado. Não é possível operar com datas futuras.")
    
    operar_robo = True
    if operar_robo:
        return "Processamento concluído com sucesso."
if __name__ == '__main__':
    app.run(debug=True, host='172.25.95.165', port=5000)
