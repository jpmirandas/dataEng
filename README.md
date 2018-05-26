https://github.com/lgaticaq/python-alpine/blob/master/3.6.3/Dockerfile


#Montando o ambiente

1. Buildar a imagem

  docker build -t python-data-science -f Dockerfile-LF .

2. Entrar no container
  
  docker run -v $PWD:/scripts -it python-data-science /bin/bash
  
  O diretorio local sera mapeado para o diretorio scripts dentro do container (seus scripts de python devem estar do diretorio atual)

3. Entrar na pasta dos scripts
  
  cd scripts

4. Executar o script python desejado
  
  python NOME_DO_SCRIPT.py
