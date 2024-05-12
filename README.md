# Projeto Univesp - Projeto Integrador 1 Turma 001

## Descrição
Este repositório contém o código-fonte de um projeto acadêmico desenvolvido pelo Grupo Seis do Eixo de Computação da Universidade Virtual do Estado de São Paulo (Univesp), como parte do Projeto Integrador 1 da Turma 001. O projeto está em fase inicial de desenvolvimento e seu objetivo é puramente acadêmico. Visa criar uma aplicação web para armazenar leis municipais em um banco de dados e facilitar a busca no mesmo.

## Sobre a Aplicação
A aplicação web desenvolvida neste projeto permite aos usuários armazenar, pesquisar e visualizar leis municipais em um banco de dados. Ela oferece uma interface intuitiva para facilitar a busca e navegação pelas leis cadastradas.

### Tecnologias Utilizadas
- Framework: Django
- Servidor: Ubuntu Server (executando em um contêiner Proxmox)
- Servidor Web: Nginx

## Como Contribuir
Se você deseja contribuir para o desenvolvimento deste projeto, siga as etapas abaixo:

1. **Clone o repositório:**
   ```
   git clone https://github.com/seu-usuario/univesp_projeto.git
   ```

2. **Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```

3. **Faça suas alterações:**
   Faça as alterações desejadas no código-fonte.

4. **Envie suas alterações:**
   ```
   git add .
   git commit -m "Descrição das alterações"
   git push origin main
   ```

5. **Solicite um Pull Request:**
   Abra uma solicitação de pull request para que suas alterações sejam revisadas e mescladas à branch principal.

## Configuração do Ambiente de Desenvolvimento
Para configurar o ambiente de desenvolvimento localmente, siga as instruções abaixo:

1. **Instale o Python:**
   Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

2. **Instale o Django:**
   ```
   pip install django
   ```

3. **Configurações do Banco de Dados:**
   Certifique-se de configurar corretamente o banco de dados de acordo com as configurações do projeto.

4. **Executar o Servidor Localmente:**
   ```
   python manage.py runserver
   ```
   Acesse a aplicação em seu navegador através do endereço `http://localhost:8000`.

## Hospedagem
A aplicação está hospedada em [tiagomanoel.com.br](https://tiagomanoel.com.br), que está executando em um servidor Proxmox com Ubuntu Server configurado e Nginx como servidor web. Para mais informações sobre a configuração do ambiente de produção, consulte a documentação do Proxmox, Ubuntu Server e Nginx.

## Autores
- Wanderson Barbosa
- Nicole Calegari de Lima
- Celio Edgar Rebechi
- Paulo Eduardo Baroni
- Carlos Eduardo Cioffi Reigota
- Tiago Giglia Manoel
- Sergio Rebechi
- Jose Roberto de Andrade Salgueiro

## Licença
Este projeto está licenciado pela GPT-3.
