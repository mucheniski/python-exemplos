# python-exemplos
https://www.udemy.com/course/intro_python/learn/lecture/15718446#overview


Para quebra de linha, deixar 2 espaços no final da linha   
[Comandos](#vomandos)  
[Variaveis e tipos de dados](#variaveis-tipos-dados)  
[Operadores lógicos relacionas](#operadores-logicos-relacionais)  
[Manipilação de Arquivos](#manipulacao-arquivos)
[Dicionarios](#dicionarios)  

## comandos
Comando para declarar o encoding utf8  
-*- coding: utf-8 -*-

## variaveis-tipos-dados
nome de variável não pode ter caracteres especiais nem espaços
nome_da_variavel
é case sensitive
Nome_da_variavel é diferente de nome_da_variavel
o operador de atribuição é o =

Tipo numérico inteiro 34    
Tipo numérico flutuante 12.89    
String "Hello World"    
Booleana true or false  

## operadores-logicos-relacionais  

'and' Duas condições sejam verdadeiras  
'or'  Pelo menos uma condição seja verdadeira
'not' Inverte o valor, negação  

'==' igual  
'!=' diferente  
'>'  Maior  
'<'  Menor  
'>=' Maior ou igual  
'<=' Menor ou igual  

## manipulacao-arquivos
usar a função open()  
r Somente leitura  
w escrita (caso o arquivo já exista ele será apagado e um novo arquivo vazio será criado)  
a leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)  
r+ leitura e escrita  
w+ escrita (o modo w+ assim como o w também apaga o conteúdo anterior do arquivo)  
a+ leitura e escrita (abre o arquivo para atualização)      

## dicionarios
Em Python, dicionários são arrays associativos, ou seja, um determinado valor passa a ser vinculado a uma chave. Exemplo: 
~~~python 
dicionario_sites = {"Diego": "diegomucheniski.com"}  
~~~
No dicionário acima, a chave "Diego" foi vinculado ao valor "diegomariano.com". Assim, para imprimir o valor chame:
~~~python  
print(dicionario_sites['Diego'])  
~~~
Se o dicionário tiver vários elementos, você pode usar laços para imprimi-los:  
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}

~~~python 
for chave in dicionario_sites:  
    print(dicionario_sites[chave])
~~~