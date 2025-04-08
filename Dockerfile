# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なツールのインストール
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gcc \
    g++ \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    zlib1g-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Node.js (npm) のインストール
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# プロジェクトのファイルをコピー
COPY . .

# Pythonの依存関係をインストール
RUN pip install --upgrade pip && pip install \
    --no-cache-dir -r scatter/requirements.txt

# JavaScriptの依存関係をインストール
RUN cd scatter/next-app && npm install

# NLTKのデータをダウンロード
RUN python -c "import nltk; nltk.download('stopwords')"

# pipeline ディレクトリに戻す（ENTRYPOINT用）
WORKDIR /app/scatter/pipeline

CMD ["bash"]
