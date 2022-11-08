from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/camisetas', methods=['GET'])
def GET_preco():
        if 'X-tamanho-pequeno' in request.headers:
                totalPequeno = float(request.headers['X-tamanho-pequeno']) * 10
        if 'X-tamanho-medio' in request.headers:
                totalMedio = float(request.headers['X-tamanho-medio']) * 12
        if 'X-tamanho-grande' in request.headers:
                totalGrande = float(request.headers['X-tamanho-grande']) * 15
        
        return '''Preço Final: R${}'''.format(totalPequeno + totalMedio + totalGrande)
      
             
@app.route('/salario', methods=['GET'])
def GET_salario_bruto():

        if 'X-hora-normal' in request.headers:
                valorNormal = float(request.headers['X-hora-normal']) * 40
        if 'X-hora-extra' in request.headers:
                valorExtra = float(request.headers['X-hora-extra']) * 50

        salarioBruto = valorNormal + valorExtra
        return '''Salário Líquido: R${}'''.format(salarioBruto * 0.9)


if __name__ == "__main__":
        app.run()
        
        

