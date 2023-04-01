#url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url = ""
url = url.strip()
if url == "":
    raise ValueError("A URL ESTA VAZIA")
print(url)

indice_interrogacao = url.find("?")
url_base = (url[:indice_interrogacao])
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_separador = url_parametros.find("&", indice_valor)
if indice_separador == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_separador]
print(valor)
