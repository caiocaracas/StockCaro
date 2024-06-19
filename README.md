# StockCaro

O projeto faz a utilização de um banco de dados local, para o funcionamento correto do mesmo é necessário a instalação do mySQL e a criação do database `gerenciador_mercado`, além da alteração da senha no arquivo main.py para a senha do sql da máquina previamente a execução do código.
O banco de dados pode ser criado através dos seguintes comandos:
`mysql -u root -p` em seguida insira a senha para acessar o mysql
`CREATE DATABASE gerenciador_mercado;`
`USE gerenciador_mercado;`
`SOURCE caminho/para/projeto/database/Modelagem_fisica.sql;`