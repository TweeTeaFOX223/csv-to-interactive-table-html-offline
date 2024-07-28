# csv-to-interactive-table-html-offline
![](https://raw.githubusercontent.com/TweeTeaFOX223/csv-to-interactive-table-html-offline/main/overview.PNG)

# 目次
- [csv-to-interactive-table-html-offline](#csv-to-interactive-table-html-offline)
- [目次](#目次)
- [概要と機能](#概要と機能)
- [プログラムの使用方法](#プログラムの使用方法)
  - [実行に必要となる環境](#実行に必要となる環境)
  - [プログラムの実行](#プログラムの実行)
    - [\[0\]：実行環境を準備する](#0実行環境を準備する)
    - [\[1\]：変換するCSVファイルを用意](#1変換するcsvファイルを用意)
    - [\[2\]：Pythonのプログラムを実行](#2pythonのプログラムを実行)
    - [\[3\]：ビルドで単一HTMLに変換](#3ビルドで単一htmlに変換)
- [余談：npm-scriptsとPython仮想環境(venv)](#余談npm-scriptsとpython仮想環境venv)

# 概要と機能

入力したCSVファイルを、`ITables`と`vite-plugin-singlefile`を使用して **『インタラクティブな表形式(`Jquery`の`DataTables`)で、CSVのデータを表示する、オフライン環境でも動作可能な単一HTMLファイル』**  に変換するプログラムです(node.jsとpythonを併用)。  

手持ちのCSVファイルをブラウザ上で表示可能なものに変換したい時、CSVファイルを軽量かつ見やすい形式で配布したい時などに使えます。  
  
DataTablesの公式サイトでインタラクティブな表のサンプルを見ることができます  
https://datatables.net/
  
ITablesの`to_html_datatable`で出力したhtmlをオフライン化する方法のサンプルという面が強いです。このプログラムは`itables==2.1.4`の使用を前提にしています。ITablesにバージョンアップが入り機能が変化したらお役御免になる可能性もあるので注意です。  
https://mwouts.github.io/itables/html_export.html  
  
<br>  
  
| 技術項目                          | 使用しているもの             |
| --------------------------------- | ---------------------------- |
| プログラミング言語                | JavaScript・Python           |
| パッケージ管理とタスク処理        | npm                          |
| Pythonの仮想環境                  | venv                         |
| CSVをDataTables使用の表HTMLに変換 | ITables                      |
| HTMLとCSSとJavaScriptのバンドル化 | vite・vite-plugin-singlefile |
  
<br>    
  
# プログラムの使用方法 
## 実行に必要となる環境
これらのインストールが必須です。動作確認はWindows10とPowerShellとFirefoxでやりました。おそらく他のOSやターミナルでも動くと思います。
  
| 事前インストールが必要 | 動作確認したver |
| ---------------------- | --------------- |
| npm                    | v10.7.0         |
| node.js                | v20.14.0        |
| Python                 | v3.11.0         |
  
<br>  

## プログラムの実行
### [0]：実行環境を準備する

ターミナルでリポジトリをクローンし、cdでディレクトリに入ってください。gitがない場合はZIPでダウンロードして解凍してください。
```
git clone https://github.com/TweeTeaFOX223/csv-to-interactive-table-html-offline.git
cd csv-to-interactive-table-html-offline
```
  
  <br>  
npmのスクリプトを実行して、JavaScriptのパッケージインストールとPythonの仮想環境作成とPythonのパッケージインストールを行ってください。

```
npm install
npm run create-venv
npm run install-pip-requirements
```
  
<br>  
  
### [1]：変換するCSVファイルを用意
`./01_input`に変換するCSVファイルを設置して、`./convert.py`のCSVファイルを読み込む部分に相対パスを入れてください。最初の時点では`sample.csv`が入っています。※`sample.csv`はこのサイトで生成しました。  
https://tm-webtools.com/Tools/TestData    
  
ITablesの初期設定によって、64KBを超えるCSVはデータがダウンサンプリングされるようになっています。制限を変更したい場合は、下記を参照して、`maxBytes`の値を書き換えてください。最終的なhtmlは元のCSVの2倍ぐらいのサイズになるので、100MBぐらいが限界かもしれないです(未検証)。  
https://mwouts.github.io/itables/downsampling.html
  
<br>  
  
### [2]：Pythonのプログラムを実行
npmのスクリプトを実行し、作成したPythonの仮想環境で`./convert.py`を実行します。`./02_tmp_html`にバンドルする前の一時HTMLファイルが生成されます。
```
npm run generate-tmp-html
```
  
<br>  
実行に成功したら、ViteのdevサーバーでHTMLを確認して、インタラクティブな表形式での表示が成功しているか確認してください。

```
npm run dev
```
  
<br>  
  
### [3]：ビルドで単一HTMLに変換
npmのスクリプトを実行して、一時HTMLファイルを単一HTMLファイルにバンドルします。`./03_output_html/index.html`として生成されます。previewのサーバーでHTMLを確認して問題がなければ成功です！この`index.html`は概要の説明にある通りで、オフライン環境でも動作可能かつブラウザから直接開くことが可能です。

```
npm run build
npm run preview
```
  
<br>  
  
# 余談：npm-scriptsとPython仮想環境(venv)

Pythonの部分は`poetry`と`taskipy`でやろうと思っていたのですが、1ファイルだけだったのと、下記のものを見て「npmでvenvのアレコレをしたら良さそう」と思って何となくで試してみました。  

- `poetry`のプロジェクトでnpm-scriptsを使用したら良かったという記事を見た。  
https://kimuson.dev/blog/python/python_with_npm_scripts/  
- VSCodeのPython拡張機能が、`.venv`のディレクトリ内にあるPython実行ファイルのパスを直接指定して動かすコマンドを打っているのを見た。  
https://zenn.dev/tweeteafox300/scraps/692ccfc673d496