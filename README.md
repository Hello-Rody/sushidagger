# Sushidagger
寿司打のチート

速さは使ってるPCの性能依存

## 使い方
### 必要なパッケージのインストール
`$ pip install -r requirements.txt`

文字認識にはGoogle様のTesseractを使ってるのでそれのインストール

### WindowsかLinuxかによってファイルのPATHが変わってくるのでそれの変更
・ Linux
> デフォルトでOK

・Windows
> main.pyの10~13行目のスラッシュをバックスラッシュにする
18行目を`pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`に書き換える

### 実行
ブラウザのウィンドウと実行するターミナルのウィンドウは被せないように

あとはプログラムの指示に従うだけ
