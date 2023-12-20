-- Exemplo da criação do banco sem o uso do Python

CREATE DATABASE IF NOT EXISTS db_astro;

CREATE TABLE IF NOT EXISTS tb_galaxia(
    id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_sistema_solar(
    id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    id_galaxia INT NOT NULL,
    CONSTRAINT fk_id_galaxia_sistema_solar
    FOREIGN KEY (id_galaxia) REFERENCES tb_galaxia (id)
    );

CREATE TABLE IF NOT EXISTS tb_substancia(
        id INT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL
        );

CREATE TABLE IF NOT EXISTS tb_classificacao(
          id INT PRIMARY KEY,
          classificacao VARCHAR(50)
          );

CREATE TABLE IF NOT EXISTS tb_corpo_celeste(
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
          );

CREATE TABLE IF NOT EXISTS tb_estrela(
              id INT PRIMARY KEY,
              id_corpo INT NOT NULL,
              CONSTRAINT fk_id_corpo_estrela
              FOREIGN KEY (id_corpo) REFERENCES tb_corpo_celeste (id)
              );

CREATE TABLE IF NOT EXISTS tb_corpo_sistema(
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
              );

CREATE TABLE IF NOT EXISTS tb_planeta(
                  id INT PRIMARY KEY,
                  id_corpo INT NOT NULL,
                  CONSTRAINT fk_id_corpo_planeta
                  FOREIGN KEY (id_corpo) REFERENCES tb_corpo_sistema (id_corpo)
                );

CREATE TABLE IF NOT EXISTS tb_nao_planeta(
                  id INT PRIMARY KEY,
                  id_corpo INT NOT NULL,
                  CONSTRAINT fk_id_corpo_nao_planeta
                  FOREIGN KEY (id_corpo) REFERENCES tb_corpo_sistema (id)
                  );

CREATE TABLE IF NOT EXISTS tb_satelite(
                    id INT PRIMARY KEY,
                    distancia_km FLOAT NOT NULL,
                    id_planeta INT NOT NULL,
                    id_nao_planeta INT NOT NULL,
                    CONSTRAINT fk_id_planeta_satelite
                    FOREIGN KEY (id_planeta) REFERENCES tb_planeta,
                    CONSTRAINT fk_id_nao_planeta_satelite
                    FOREIGN KEY (id_nao_planeta) REFERENCES tb_nao_planeta
                    );

CREATE TABLE IF NOT EXISTS tb_planeta_anao(
                      id INT PRIMARY KEY,
                      id_nao_planeta INT NOT NULL,
                      CONSTRAINT fk_id_nao_planeta_planeta_anao
                      FOREIGN KEY (id_nao_planeta) REFERENCES tb_nao_planeta (id)
                      );

CREATE TABLE IF NOT EXISTS tb_asteroide(
                        id INT PRIMARY KEY,
                        id_nao_planeta INT NOT NULL,
                        CONSTRAINT fk_id_nao_planeta_asteroide
                        FOREIGN KEY (id_nao_planeta) REFERENCES tb_nao_planeta (id)
                        );

CREATE TABLE IF NOT EXISTS tb_corpo_celeste_substancia(
                          id_corpo INT,
                          id_substancia INT,
                          PRIMARY KEY (id_corpo,id_substancia),
                          CONSTRAINT fk_id_corpo_corpo_celeste_substancia
                          FOREIGN KEY (id_corpo) REFERENCES tb_corpo_celeste (id),
                          CONSTRAINT fk_id_substancia_corpo_celeste_substancia
                          FOREIGN KEY (id_substancia) REFERENCES tb_substancia (id)
                          );