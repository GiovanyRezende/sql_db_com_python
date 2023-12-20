# Projeto Python-SQLite

*Este projeto tem o objetivo de criar um **banco de dados SQL** utilizando a biblioteca **sqlite3** para futuras aplicações, mais precisamente com o intuito de servir como uma fonte de dados para um próximo projeto de **Machine Learning**.* O tema do banco (db_astro) é Astronomia, com dados sobre objetos astronômicos como planetas, estrelas, planetas anões, satélites e asteroides. Essas informações serão utilizadas para treinar um modelo de ML que irá classificar corpos celestes, além de por si só servir para estudos astronômicos com consultas SQL.

# Por que o SQLite?

Simplesmente pelo fato da biblioteca sqlite3 criar um arquivo do banco todo e facilitar as exportações dos dados por meio de, por exemplo, e-mails. *Entretanto, o projeto pode ser feito com qualquer SGBD que possa ter uma conexão com o Python, como o MySQL e o PostgreSQL.*

# Modelo Conceitual
![modelo_conceitual](https://github.com/GiovanyRezende/sql_db_com_python/assets/111097597/2c18349f-0847-42d7-a467-886e5973919c)

# Modelo Lógico
![modelo_logico](https://github.com/GiovanyRezende/sql_db_com_python/assets/111097597/0a76e9a1-09d5-49ab-a408-c488899ffc87)

# Modelo Físico e Código Python

## Importação da biblioteca, estabelecimento da conexão e criação do cursor

```
import sqlite3
conn = sqlite3.connect('db_astro.db')
cursor = conn.cursor()
```

## Tabelas do banco
Em ordem de cadastro, as tabelas criadas são:
- tb_galaxia
- tb_sistema_solar
- tb_substancia
- tb_classificacao
- tb_corpo_celeste
- tb_estrela
- tb_corpo_sistema
- tb_planeta
- tb_nao_planeta
- tb_satelite
- tb_planeta_anao
- tb_asteroide
- tb_corpo_celeste_substancia (sendo essa uma associativa)

Ainda que já exista um modo de classificar os corpos, é necessário que cada classificação tenha a sua tabela, mesmo que tenha apenas um ID e uma chave estrangeira, pois, astronomicamente, cada objeto pode ter atributos e relações diferentes. Um exemplo sobre atributo é que corpos que não são estrelas têm dados orbitais relevantes para o banco, como o periélio, afélio e período de translação da órbita, enquanto para estrelas essas informações não são relevantes nesse caso. Um exemplo sobre relação é que um satélite orbita um planeta enquanto um planeta anão não terá uma orbita afetada por um planeta necessária para cadastrar nesse cenário.

## Criação do banco com tratamento de exceção
O tratamento com ```try```, ```except``` e ```else``` é usado para evitar que um erro de SQL crie um problema no código. Exemplo:

```
try:
  tabela = '''CREATE TABLE IF NOT EXISTS tb_galaxia(
  id INT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL
)'''
  cursor.execute(tabela)
  insert = '''INSERT INTO tb_galaxia VALUES (1,'Via Láctea')'''
  cursor.execute(insert)
except:
  print("Algum erro de SQL impediu o cadastro da tabela tb_galaxia")
```
Quando não há erro na criação da tabela e nem no cadastro dos dados, a posterior poderá ser criada com um else:
```
else:
  try:
    tabela = '''CREATE TABLE IF NOT EXISTS tb_sistema_solar(
    id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    id_galaxia INT NOT NULL,
    CONSTRAINT fk_id_galaxia_sistema_solar
    FOREIGN KEY (id_galaxia) REFERENCES tb_galaxia (id)
    )'''
    cursor.execute(tabela)
    for x in sistema:
      insert = '''INSERT INTO tb_sistema_solar VALUES (?,?,1)'''
      cursor.execute(insert,(sistema.index(x)+1,x))
  except:
    print("Algum erro de SQL impediu o cadastro da tabela tb_sistema_solar")
```
Isso deverá ser feito até o último cadastro, que no banco será o da tabela associativa, enquanto o último else de todo o tratamento permite o commit de ```conn.commit()```:
```
                        try:
                          tabela = '''CREATE TABLE IF NOT EXISTS tb_corpo_celeste_substancia(
                          id_corpo INT,
                          id_substancia INT,
                          PRIMARY KEY (id_corpo,id_substancia),
                          CONSTRAINT fk_id_corpo_corpo_celeste_substancia
                          FOREIGN KEY (id_corpo) REFERENCES tb_corpo_celeste (id),
                          CONSTRAINT fk_id_substancia_corpo_celeste_substancia
                          FOREIGN KEY (id_substancia) REFERENCES tb_substancia (id)
                          )'''
                          cursor.execute(tabela)
                          for x in associativa:
                            insert = '''INSERT INTO tb_corpo_celeste_substancia VALUES (?,?)'''
                            cursor.execute(insert,(x[0],x[1]))
                        except:
                          print("Algum erro de SQL impediu o cadastro da tabela associativa")
                        else:
                          conn.commit()
```

## Inserção de dados
Primeiramente, os dados foram armazenados no código Python em listas e/ou listas de listas como nos dois exemplos:
```
sistema = ["Sistema Solar","Alpha Centauri","Sirius"]
```
```
associativa = [[1,8],[4,1],[4,2],[4,3],[4,4],[5,5],[4,6],[6,7],[3,9],[4,9]]
```
Depois, no ```try``` de cada tabela, há um loop que navega em cada lista ou lista de listas. Um exemplo para cada um dos dois casos são:
```
subst = ["Água","Dióxido de Carbono","Nitrogênio","Oxigênio","Compostos Ferrosos","Silicatos","Hidrogênio Molecular",
"Hélio","Metano", "Amônia", "Metanol", "Etanol", "Ácido Sulfúrico", "Methanethiol"]

    try:
      tabela = '''CREATE TABLE IF NOT EXISTS tb_substancia(
        id INT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL
        )'''
      cursor.execute(tabela)
      for x in subst:
        insert = '''INSERT INTO tb_substancia VALUES (?,?)'''
        cursor.execute(insert,(subst.index(x)+1,x))
```
```
associativa = [[1,8],[4,1],[4,2],[4,3],[4,4],[5,5],[4,6],[6,7],[3,9],[4,9]]

                        try:
                          tabela = '''CREATE TABLE IF NOT EXISTS tb_corpo_celeste_substancia(
                          id_corpo INT,
                          id_substancia INT,
                          PRIMARY KEY (id_corpo,id_substancia),
                          CONSTRAINT fk_id_corpo_corpo_celeste_substancia
                          FOREIGN KEY (id_corpo) REFERENCES tb_corpo_celeste (id),
                          CONSTRAINT fk_id_substancia_corpo_celeste_substancia
                          FOREIGN KEY (id_substancia) REFERENCES tb_substancia (id)
                          )'''
                          cursor.execute(tabela)
                          for x in associativa:
                            insert = '''INSERT INTO tb_corpo_celeste_substancia VALUES (?,?)'''
                            cursor.execute(insert,(x[0],x[1]))
```

Para evitar o cadastro de um ID = 0, ```.index(x)+1``` é eventualmente obrigatório em casos sem AUTOINCREMENT disponível.

## Realização de consultas SQL e conversão para arquivo CSV

Consultas SQL podem ser realizadas e ainda armazenadas em uma constante/variável. Por exemplo, se quisermos uma constante com o valor de 1 UA (unidade-astronômica), nós pegamos a distância média da Terra ao Sol. Como temos o periélio e o afélio da Terra cadastrados no banco, realizamos a consulta:
```
cursor.execute('''SELECT (s.perielio_km + s.afelio_km)/2
                FROM tb_corpo_sistema AS s
                INNER JOIN tb_corpo_celeste AS c
                ON s.id_corpo = c.id
                WHERE c.nome = 'Terra' ''')
unid_astro = cursor.fetchone()[0]
```

Com ```cursor.fetchall()```, uma lista de tuplas com a consulta SQL é gerada e com possibilidade de ser armazenada em uma constante/variável. Logo, se for de interesse extrair dados físicos e orbitais dos planetas do Sistema Solar, podemos realizar o seguinte código:
```
cursor.execute('''SELECT c.nome,
              c.massa_kg,
              c.raio_medio_km,
              c.temperatura_k,
              s.periodo_ano,
              ((s.perielio_km + s.afelio_km)/2)/?,
              POWER(s.periodo_ano,2)/POWER(((s.perielio_km + s.afelio_km)/2)/?,3)
              FROM tb_corpo_celeste AS c
              INNER JOIN tb_corpo_sistema AS s
              ON c.id = s.id_corpo
              INNER JOIN tb_sistema_solar AS si
              ON si.id = c.id_sistema
              INNER JOIN tb_classificacao AS cl
              ON cl.id = c.id_classificacao
              WHERE si.nome = 'Sistema Solar' AND cl.classificacao = 'Planeta'
              ''',(unid_astro,unid_astro))

query = cursor.fetchall()
```
Ainda, se for de interesse usar os dados dessa consulta para um projeto de ML que use Pandas, podemos converter ```query``` para um arquivo CSV, como em:
```
colunas = ('nome','massa_kg','raio_medio_km','temperatura_k','t_ano','r_ua','trc_kepler')

import csv

a_csv = 'planetas.csv'

with open(a_csv, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(colunas)
    for x in query:
        escritor_csv.writerow(x)

cursor.close()
conn.close()

import pandas as pd

df = pd.read_csv(a_csv)
print(df)
```

<div align= center>

# Redes sociais e formas de contato



[![logo](https://cdn-icons-png.flaticon.com/256/174/174857.png)](https://br.linkedin.com/in/giovanyrezende)
[![logo](https://images.crunchbase.com/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/v1426048404/y4lxnqcngh5dvoaz06as.png)](https://github.com/GiovanyRezende)[
![logo](https://logospng.org/download/gmail/logo-gmail-256.png)](mailto:giovanyrmedeiros@gmail.com)

</div>
