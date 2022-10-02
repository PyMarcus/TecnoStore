from flask import Flask, request, render_template, redirect, url_for
import sys
sys.path.append("../controllers/")
from models.Client import Client
from models.Market import Market


credentials = []  # funciona como uma sessão


class TecnoStore:

    app = Flask(__name__)
    x = 0
    @staticmethod
    @app.route("/", methods=["GET", "POST"])
    def index():
        """
        Realiza cadastro do cliente
        de forma simples, sem banco de dados
        :return:
        """
        print(request.form)
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            cpf = request.form["cpf"]
            birth = request.form["birth"]
            cash = request.form["saldo"]
            client = Client(name=name,
                            email=email,
                            cpf=cpf,
                            cash=float(cash),
                            birth=birth,
            )  # padrao criador
            credentials.append(name)
            credentials.append(email)
            credentials.append(cpf)
            credentials.append(birth)
            credentials.append(cash)

            return redirect(url_for("tecnostore", client=client))
        return render_template("index.html")

    @staticmethod
    @app.route("/tecnostore/<client>", methods=["GET", "POST"])
    def tecnostore(client):
        if request.method == "GET":
            market = Market()
            context = market.content()
            return render_template("tecnostore.html", context=context, enumere=enumerate(context))
        return redirect(url_for("card", client=client, product=request.form))

    @staticmethod
    @app.route("/card/<client>/<product>")
    def card(client, product):
        print(credentials)
        client = Client(name=credentials[0],
                        email=credentials[1],
                        cpf=credentials[2],
                        birth=credentials[3],
                        cash=float(credentials[4]))
        prod = ''.join([d for d in product if d.isdigit()])
        context = Market().content()
        content = {}
        if request.method == "GET":
            for index, item in enumerate(context):
                if index == int(prod):
                    client.add_to_card(item['name'])
                    print('adicionado')
                    content = item
                    credentials.append(item)
                    break
            return render_template("card.html", add=content)
        else:
            client.buy()
            print("COMPRADO")
            return render_template("cupom.html", add=content)

    @staticmethod
    @app.route("/cupom", methods=["GET", "POST"])
    def cupom():
        card = credentials[5]
        return render_template("cupom.html", card=card)

    @classmethod
    def start(cls):
        cls.app.run(debug=False)


if __name__ == '__main__':
    TecnoStore.start()
