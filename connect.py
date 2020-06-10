import http.client


HOST = "b2b.mobility.com.br"


PAYLOAD_TPL = """
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:wsm="http://schemas.datacontract.org/2004/07/wsMobilityEngine.Classes.Request">
  <soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing"><wsa:Action>Autenticar</wsa:Action></soap:Header>
  <soap:Body>
    <AutenticacaoRQ xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <ClienteFilialAtendimentoId>26</ClienteFilialAtendimentoId>
        <Idioma>pt_BR</Idioma>
        <Login>%(user)s</Login>
        <Senha>%(pwd)s</Senha>
    </AutenticacaoRQ>
   </soap:Body>
  </soap:Envelope>
"""


def connect(user, pwd):
    conn = http.client.HTTPSConnection(HOST)

    final_payload = PAYLOAD_TPL.format(user=user, pwd=pwd)
    headers = {
        'Accept-Encoding': "gzip,deflate",
        'Action': 'http://tempuri.org/IMobility/Autenticar',
        'Content-Type': 'application/soap+xml;charset=UTF-8',
        'Host': HOST,
        'Connection': "Keep-Alive",
    }

    print(headers)

    conn.request(
        "POST",
        "/Homologacao/webservice/Mobility.svc",
        final_payload,
        headers
    )

    res = conn.getresponse()

    print("Response")
    print("Status: ", res.status)
    print("\nHeaders: ")
    print(res.headers)
    print("------")

    data = res.read()
    print("Body: ", data.decode("utf-8"))
    print("------")


if __name__ == '__main__':
    import sys
    user = sys.argv[1]
    pwd = sys.argv[2]
    connect(user, pwd)
