# keiba-dicord-bot

## pythonファイルの実行方法
1. venvで仮想環境を作成
```python -m venv venv```
2. 実行環境を仮想環境に変更
```source venv/bin/activate```
3. パッケージのインストール
```pip install -r requirements.txt```
4. 仮想環境から抜ける
```deactivate```
5. detect.pyを実行する場合はtesseractをインストール
```brew install tesseract```
6. 日本語の学習済みモデルを以下のURLからインストール
```https://github.com/tesseract-ocr/tessdata/blob/master/jpn.traineddata```
7. 以下のディレクトリに配置
```/usr/local/Cellar/tesseract/tesseractのバージョン名/share/tessdata/```

## webhookの登録の仕方
1. bot起動させたいサーバのルームの設定ボタンからウェブフックを探す
2. ウェブフックURLをコピーし、.envファイルを作成し、WEB_HOOK="コピーしたウェブフックURL"を追記
3. python scrape.pyで起動
