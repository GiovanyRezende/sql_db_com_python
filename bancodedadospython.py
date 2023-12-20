# -*- coding: utf-8 -*-
"""BancoDeDadosPython

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LxSLcPvFiha2IG_7LuI3lW8Ipcp4oay7
"""

import sqlite3
conn = sqlite3.connect('db_astro.db')
cursor = conn.cursor()

sistema = ["Sistema Solar","Alpha Centauri","Sirius"]
subst = ["Água","Dióxido de Carbono","Nitrogênio","Oxigênio","Compostos Ferrosos","Silicatos","Hidrogênio Molecular",
"Hélio","Metano", "Amônia", "Metanol", "Etanol", "Ácido Sulfúrico", "Methanethiol"]
classif = ["Planeta","Estrela","Planeta Anão","Satélite","Asteroide"]

#nome, massa_kg, raio_medio_km, temperatura_k, Sistema Solar (1), classificacao
corpo = [["Sol",1.9891e30,6.96e5,5778,1,2],["Mercúrio",3.3011e23,2439.7,166.85+273.15,1,1],
["Vênus",4.8685e24,6051.8,461+273.15,1,1],["Terra",5.9736e24,6378.1,14+273.15,1,1],["Marte",6.4174e23,3396.2,-63+273.15,1,1],
["Júpiter",1.8986e27,71492,-108+273.15,1,1],["Saturno",5.6834e26,58232,-139+273.15,1,1],
["Urano", 8.6810e25,25362,-220+273.15,1,1],["Netuno",1.0241e26,24622,-223.15+273.15,1,1],

  ["Plutão",1.303e22,1188.3,44,1,3],["Éris",1.6466e22,1163,37,1,3],["Haumea",4.006e21,816,32,1,3],
  ["Makemake",3.14e21,715.0,30.0,1,3],["Ceres",9.3835e20,590.0,168.0,1,3],

    # Satélites da Terra
    ["Lua", 7.342e22, 1737.5, 220.0, 1, 4],

    # Satélites de Marte
    ["Fobos", 1.072e16, 11.1, 233.0, 1, 4],
    ["Deimos", 1.4762e15, 6.2, 233.0, 1, 4],

    # Satélites de Júpiter
    ["Io", 8.9319e22, 1821.6, 110.0, 1, 4],
    ["Europa", 4.7998e22, 1560.8, 102.0, 1, 4],
    ["Ganimedes", 1.4819e23, 2634.1, 110.0, 1, 4],
    ["Calisto", 1.0759e23, 2410.3, 134.0, 1, 4],
    ["Amalteia", 2.08e18, 83.5, 165.0, 1, 4],

    # Satélites de Saturno
    ["Mimas", 3.7493e19, 198.2, 64.0, 1, 4],
    ["Encélado", 1.08022e20, 252.1, 75.0, 1, 4],
    ["Tétis", 6.17449e20, 536.3, 86.0, 1, 4],
    ["Dione", 1.095452e21, 562.5, 87.0, 1, 4],
    ["Reia", 2.306518e21, 764.3, 53.0, 1, 4],

    # Satélites de Urano
    ["Titânia", 3.527e21, 788.9, 70.0, 1, 4],
    ["Óberon", 3.014e21, 761.4, 80.0, 1, 4],
    ["Umbriel", 1.275e21, 584.7, 76.0, 1, 4],
    ["Ariel", 1.353e21, 578.9, 60.0, 1, 4],
    ["Míranda", 6.3e19, 235.8, 86.0, 1, 4],

    # Satélites de Netuno
    ["Tritão", 2.14e22, 1353.4, 38.0, 1, 4],
    ["Nereida", 3.08e19, 170.0, 48.0, 1, 4],
    ["Larissa", 4.2e18, 97.0, 84.0, 1, 4],
    ["Proteu", 5.02e18, 210.0, 53.0, 1, 4],
    ["Despina", 2.2e18, 74.7, 78.0, 1, 4],

    ["Vesta", 2.59076e20, 525.4, 167.0, 1, 5],
    ["Pallas", 2.11143e20, 512.0, 164.0, 1, 5],
    ["Hygiea", 8.97e19, 434.0, 163.0, 1, 5],
    ["Eunomia", 1.8567e19, 268.3, 152.0, 1, 5],

    ["Alpha Centauri A", 2.24e30, 1.22e6, 5790, 2, 2],
    ["Alpha Centauri B", 1.68e30, 865000, 5260, 2, 2],
    ["Proxima Centauri", 2.08e29, 169140, 3042, 2, 2],
    ["Sirius A", 2.02e30, 1.711e6, 9940, 3, 2],
    ["Sirius B", 9.93e29, 1.21e4, 25000, 3, 2]
]

estrela = [1,42,43,44,45,46]

dados_orbitais = [
    # Planetas do Sistema Solar
    [0.240846, 46001200, 69816900, 2, 1],
    [0.615, 107477000, 108939000, 3, 1],
    [1.0, 147095000, 152100000, 4, 1],
    [1.88089, 206700000, 249200000, 5, 1],
    [11.862, 740520000, 816040000, 6, 1],
    [29.457, 1349820000, 1503500000, 7, 1],
    [84.012, 2734990000, 3005860000, 8, 1],
    [164.79, 4459750000, 4536780000, 9, 1],
    [248.59, 4436750000, 7375930000, 10, 1],

    # Planetas Anões e Luas
    [557.04, 5.91e9, 7.38e9, 11, 1],
    [285.33, 5.7e9, 7.8e9, 12, 1],
    [309.88, 5.8e9, 8.6e9, 13, 1],
    [309.88, 5.8e9, 8.6e9, 14, 1],
    [27.322, 363300, 405500, 15, 1],
    [0.31891, 9376, 9517, 16, 1],
    [1.26244, 23455, 23455, 17, 1],
    [1.769, 421800, 421800, 18, 1],
    [3.551, 671034, 676938, 19, 1],
    [7.155, 1.07041e6, 1.07041e6, 20, 1],
    [16.689, 1.87497e6, 1.87497e6, 21, 1],
    [0.498, 1.813e8, 1.864e8, 22, 1],
    [0.942, 1.88e8, 1.94e8, 23, 1],
    [1.887, 2.39e8, 2.39e8, 24, 1],
    [2.736, 2.38e8, 2.38e8, 25, 1],
    [4.518, 2.97e8, 2.97e8, 26, 1],
    [15.945, 3.88e8, 3.88e8, 27, 1],
    [8.706, 4.36e8, 4.36e8, 28, 1],
    [13.463, 5.91e8, 5.91e8, 29, 1],
    [4.144, 5.81e8, 5.81e8, 30, 1],
    [2.520, 5.82e8, 5.82e8, 31, 1],
    [1.769, 1.9e8, 1.9e8, 32, 1],
    [5.877, 2.36e8, 2.36e8, 33, 1],
    [360.13, 3.56e8, 3.56e8, 34, 1],
    [360.13, 3.56e8, 3.56e8, 35, 1],
    [1.122, 3.58e8, 3.58e8, 36, 1],
    [1.122, 3.58e8, 3.58e8, 37, 1],
    [0.571, 3.44e8, 3.44e8, 38, 1],
    [4.616, 3.26e8, 3.26e8, 39, 1],
    [5.572, 3.07e8, 3.07e8, 40, 1],
    [5.77, 2.98e8, 2.98e8, 41, 1]
]

planeta = [2,3,4,5,6,7,8,9]

nao_planeta = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

satelite = [
    [384400, 3, 6],
    [9380, 4, 7],
    [23460, 4, 8],
    [421800, 5, 9],
    [671034, 5, 10],
    [1.07041e6, 5, 11],
    [1.87497e6, 5, 12],
    [181300, 5, 13],
    [185539, 6, 14],
    [238040, 6, 15],
    [294619, 6, 16],
    [377396, 6, 17],
    [527108, 6, 18],
    [435910, 7, 19],
    [583520, 7, 20],
    [266300, 7, 21],
    [191020, 7, 22],
    [129860, 7, 23],
    [354800, 8, 24],
    [551300, 8, 25],
    [187900, 8, 26],
    [117600, 8, 27],
    [52800, 8, 28]
]

planeta_anao = [10, 11, 12, 13, 14, 15]

asteroide = [38,39,40,41]

associativa = [[1,8],[4,1],[4,2],[4,3],[4,4],[5,5],[4,6],[6,7],[3,9],[4,9]]

#Cadastro de tabelas e seus respectivos dados
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
  else:
    try:
      tabela = '''CREATE TABLE IF NOT EXISTS tb_substancia(
        id INT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL
        )'''
      cursor.execute(tabela)
      for x in subst:
        insert = '''INSERT INTO tb_substancia VALUES (?,?)'''
        cursor.execute(insert,(subst.index(x)+1,x))
    except:
      print("Algum erro de SQL impediu o cadastro da tabela tb_substancia")
    else:
      try:
        tabela = '''CREATE TABLE IF NOT EXISTS tb_classificacao(
          id INT PRIMARY KEY,
          classificacao VARCHAR(50)
          )'''
        cursor.execute(tabela)
        for x in classif:
          insert = '''INSERT INTO tb_classificacao VALUES (?,?)'''
          cursor.execute(insert,(classif.index(x)+1,x))
      except:
        print("Algum erro de SQL impediu o cadastro da tabela tb_classificacao")
      else:
        try:
          tabela = '''CREATE TABLE IF NOT EXISTS tb_corpo_celeste(
              id INT PRIMARY KEY,
              nome VARCHAR(255),
              massa_kg FLOAT NOT NULL,
              raio_medio_km FLOAT NOT NULL,
              temperatura_k FLOAT NOT NULL,
              id_sistema INT,
              id_classificacao INT NOT NULL,
              CONSTRAINT fk_id_sistema_corpo_celeste
              FOREIGN KEY (id_sistema) REFERENCES tb_sistema_solar (id),
              CONSTRAINT fk_id_classificacao_corpo_celeste
              FOREIGN KEY (id_classificacao) REFERENCES tb_classificacao (id)
          )'''
          cursor.execute(tabela)
          for x in corpo:
            insert = '''INSERT INTO tb_corpo_celeste VALUES (?,?,?,?,?,?,?)'''
            cursor.execute(insert,(corpo.index(x)+1,x[0],x[1],x[2],x[3],x[4],x[5]))
        except:
          print("Algum erro de SQL impediu o cadastro da tabela tb_corpo_celeste")
        else:
          try:
            tabela = '''CREATE TABLE IF NOT EXISTS tb_estrela(
              id INT PRIMARY KEY,
              id_corpo INT NOT NULL,
              CONSTRAINT fk_id_corpo_estrela
              FOREIGN KEY (id_corpo) REFERENCES tb_corpo_celeste (id)
              )'''
            cursor.execute(tabela)
            for x in estrela:
              insert = '''INSERT INTO tb_estrela VALUES (?,?)'''
              cursor.execute(insert,(estrela.index(x)+1,x))
          except:
            print("Algum erro de SQL impediu o cadastro da tabela tb_estrela")
          else:
            try:
              tabela = '''CREATE TABLE IF NOT EXISTS tb_corpo_sistema(
                id INT PRIMARY KEY,
                periodo_ano FLOAT NOT NULL,
                perielio_km FLOAT NOT NULL,
                afelio_km FLOAT NOT NULL,
                id_corpo INT NOT NULL,
                id_estrela INT,
                CONSTRAINT fk_id_corpo_corpo_sistema
                FOREIGN KEY (id_corpo) REFERENCES tb_corpo_celeste (id),
                CONSTRAINT fk_id_estrela_corpo_sistema
                FOREIGN KEY (id_estrela) REFERENCES tb_estrela (id)
              )'''
              cursor.execute(tabela)
              for x in dados_orbitais:
                insert = '''INSERT INTO tb_corpo_sistema VALUES (?,?,?,?,?,?)'''
                cursor.execute(insert,(dados_orbitais.index(x)+1,x[0],x[1],x[2],x[3],x[4]))
            except:
              print("Algum erro de SQL impediu o cadastro da tabela tb_corpo_sistema")
            else:
              try:
                tabela = '''CREATE TABLE IF NOT EXISTS tb_planeta(
                  id INT PRIMARY KEY,
                  id_corpo INT NOT NULL,
                  CONSTRAINT fk_id_corpo_planeta
                  FOREIGN KEY (id_corpo) REFERENCES tb_corpo_sistema (id_corpo)
                )'''
                cursor.execute(tabela)
                for x in planeta:
                  insert = '''INSERT INTO tb_planeta VALUES (?,?)'''
                  cursor.execute(insert,(planeta.index(x)+1,x))
              except:
                print("Algum erro de SQL impediu o cadastro da tabela tb_planeta")
              else:
                try:
                  tabela = '''CREATE TABLE IF NOT EXISTS tb_nao_planeta(
                  id INT PRIMARY KEY,
                  id_corpo INT NOT NULL,
                  CONSTRAINT fk_id_corpo_nao_planeta
                  FOREIGN KEY (id_corpo) REFERENCES tb_corpo_sistema (id)
                  )'''
                  cursor.execute(tabela)
                  for x in nao_planeta:
                    insert = '''INSERT INTO tb_nao_planeta VALUES (?,?)'''
                    cursor.execute(insert,(nao_planeta.index(x)+1,x))
                except:
                  print("Algum erro de SQL impediu o cadastro da tabela tb_nao_planeta")
                else:
                  try:
                    tabela = '''CREATE TABLE IF NOT EXISTS tb_satelite(
                    id INT PRIMARY KEY,
                    distancia_km FLOAT NOT NULL,
                    id_planeta INT NOT NULL,
                    id_nao_planeta INT NOT NULL,
                    CONSTRAINT fk_id_planeta_satelite
                    FOREIGN KEY (id_planeta) REFERENCES tb_planeta,
                    CONSTRAINT fk_id_nao_planeta_satelite
                    FOREIGN KEY (id_nao_planeta) REFERENCES tb_nao_planeta
                    )'''
                    cursor.execute(tabela)
                    for x in satelite:
                      insert = '''INSERT INTO tb_satelite VALUES (?,?,?,?)'''
                      cursor.execute(insert,(satelite.index(x)+1,x[0],x[1],x[2]))
                  except:
                    print("Algum erro de SQL impediu o cadastro da tabela tb_satelite")
                  else:
                    try:
                      tabela = '''CREATE TABLE tb_planeta_anao(
                      id INT PRIMARY KEY,
                      id_nao_planeta INT NOT NULL,
                      CONSTRAINT fk_id_nao_planeta_planeta_anao
                      FOREIGN KEY (id_nao_planeta) REFERENCES tb_nao_planeta (id)
                      )'''
                      cursor.execute(tabela)
                      for x in planeta_anao:
                        insert = '''INSERT INTO tb_planeta_anao VALUES (?,?)'''
                        cursor.execute(insert,(planeta_anao.index(x)+1,x))
                    except:
                      print("Algum erro de SQL impediu o cadastro da tabela tb_planeta_anao")
                    else:
                      try:
                        tabela = '''CREATE TABLE tb_asteroide(
                        id INT PRIMARY KEY,
                        id_nao_planeta INT NOT NULL,
                        CONSTRAINT fk_id_nao_planeta_asteroide
                        FOREIGN KEY (id_nao_planeta) REFERENCES tb_nao_planeta (id)
                        )'''
                        cursor.execute(tabela)
                        for x in asteroide:
                          insert = '''INSERT INTO tb_asteroide VALUES (?,?)'''
                          cursor.execute(insert,(asteroide.index(x)+1,x))
                      except:
                        print("Algum erro de SQL impediu o cadastro da tabela tb_asteroide")
                      else:
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

#Assim que todos os cadastros do banco forem efetivados, se pode realizar consultas
#Caso necessário, é recomendável realizar tudo no dentro do último else, logo depois de conn.commit()

#Extração do valor de 1UA
cursor.execute('''SELECT (s.perielio_km + s.afelio_km)/2
                FROM tb_corpo_sistema AS s
                INNER JOIN tb_corpo_celeste AS c
                ON s.id_corpo = c.id
                WHERE c.nome = 'Terra' ''')
unid_astro = cursor.fetchone()[0]

#Consulta de dados físicos e orbitais dos planetas do Sistema Solar
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
colunas = ('nome','massa_kg','raio_medio_km','temperatura_k','t_ano','r_ua','trc_kepler')

#Converter a consulta para um arquivo CSV
import csv

a_csv = 'planetas.csv'

with open(a_csv, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(colunas)
    for x in query:
        escritor_csv.writerow(x)

cursor.close()
conn.close()

# Converter a consulta CSV em um DataFrame no Pandas
import pandas as pd

df = pd.read_csv(a_csv)
print(df)