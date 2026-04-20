# 入力画像を視覚暗号にする

## 概要
  * 入力画像から視覚暗号を用いた2枚のシェア画像を作成する
  * シェア画像の視覚的なピクセルのスケールが入力可能
  
## version
* python: 3.7.6
* numpy: 1.18.1
* opencv-python: 4.5.2.52

## 実行方法
* ライブラリのインストール\
'pip install -r requirements.txt'  
※ tkinterは環境によって別途インストールが必要です

* 実行\
'python main.py'

* 入力画像の選択\

* 出力画像のスケール入力\
    
## 結果
### 入力画像/設定値
* 入力画像

![input_image](./fig/input_image.png)

* スケール設定：0.5

### 出力結果
* share1

![share1](./fig/share1.png)

* share2

![share2](./fig/share2.png)

* share1とshare2を重ね合わせた画像

![overlay](./fig/overlay.png)

## 参考サイト
https://www.acompany.tech/privacytechlab/Visual-Secret-Sharing-Scheme