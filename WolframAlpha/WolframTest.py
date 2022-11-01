import wolframalpha

client = wolframalpha.Client("K5UKEX-25P242T692")

res = client.query('Start of WW2')

print(res)

