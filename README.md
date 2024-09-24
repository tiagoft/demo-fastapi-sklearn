# ⚡FastAPI Sentiment Analysis

Este repositório contém um exemplo de como organizar um projeto de análise de sentimentos utilizando FastAPI para criar uma API de predição. O objetivo é demonstrar como fazer o deploy de um modelo de machine learning treinado para análise de sentimentos em reviews de filmes.

## 📌Visão Geral

O projeto utiliza o dataset "IMDB dataset of 50k movie reviews" disponível no Kaggle. A aplicação é construída em Python utilizando a biblioteca FastAPI para criar endpoints que permitem a predição de sentimentos (positivo ou negativo) de textos fornecidos.

## 📐Estrutura do Projeto

1. **FastAPI**: Utilizada para criar a API que expõe o modelo de predição.
2. **Scikit-learn**: Usada para criar um pipeline de machine learning que transforma texto em vetores e realiza a classificação.
3. **Joblib**: Para salvar e carregar o modelo treinado.

## ✏️Requisitos

- Python 3.7+
- Bibliotecas: FastAPI, Uvicorn, Scikit-learn, Pandas, Numpy, Joblib

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/tiagoft/demo-fastapi-sklearn
   cd demo-fastapi-sklearn
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Use o dataset do próprio repositório para treinar o modelo.

## Como Executar

1. **Treinamento do Modelo**: Execute o script de treinamento para criar e salvar o modelo.

2. **Iniciar a API**: Execute o servidor FastAPI.
   ```bash
   uvicorn app:app --reload
   ```

3. **Testar a API**: Acesse `http://127.0.0.1:8000` no seu navegador ou use ferramentas como Postman para enviar requisições.

## 📢Importante

O professor Tiago Tavares destacou um ponto crucial: **nunca faça o `.fit()` do modelo diretamente na função das queries**. Isso gera um problema de performance, pois o modelo será treinado a cada requisição, tornando o processo extremamente lento. Em vez disso, treine o modelo uma vez e salve-o. Carregue o modelo salvo quando iniciar a API.

## ✨Disclaimer

**Este README foi gerado com IA**, o template básico da produção consta no notebook ``get_readme_from_video.ipynb``. Além disso, o embasamento para gerar o README foi tomado pela transcrição do vídeo referente a esse repositório, no qual você pode acessar aqui: [FastAPI Sentiment Analysis](https://www.youtube.com/watch?v=0NBL7sNOLoM)
