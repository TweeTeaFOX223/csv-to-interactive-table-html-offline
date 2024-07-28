import polars as pl
from itables import options as it_opt, to_html_datatable


# ここが非常に重要
# 現時点のバージョン「itables==2.1.4」では
# 「./02_tmp_html/index.html」からみた時の、
# 「./node_modules/dt_for_itables/dt_bundle.js」のパス、
#  つまりは「../node_modules/dt_for_itables/dt_bundle.js」を指定する
#  「dt_bundle.css」は同じディレクトリにあるので自動的に読み込まれます。

# ソースコードの変数「UNPKG_DT_BUNDLE_URL」に注目
# https://github.com/mwouts/itables/blob/main/src/itables/utils.py
# https://github.com/mwouts/itables/blob/main/src/itables/options.py
# it_opt.dt_url = "../node_modules/dt_for_itables/dt_bundle.js"
it_opt.dt_url = "../node_modules/dt_for_itables/dt_bundle.js"

# 読み込みが軽いため取り敢えずpolars
df = pl.read_csv(
    # ここに変換したいcsvのパスを入力
    "./01_input_csv/sample.csv",
    separator=",",
)


# ここが重要：connectedにはFalseではなくTrueを指定する。
# 現時点のバージョン「itables==2.1.4」では、dt_urlを指定するとオフラインモードになる
tmp_html = to_html_datatable(
    df,
    connected=True,
)


# Vite用の微修正：node_modulesにあるcssファイルはlinkで読み込んでもバンドルされない。
# その対策でCSSの読み込み箇所をscriptタグの先頭に追加する
# https://stackoverflow.com/questions/68376035/how-to-include-css-from-node-modules-in-vite-in-production
css_pass = it_opt.dt_url.replace(".js", ".css")
tmp_html = tmp_html.replace(
    '<script type="module">', f'<script type="module">\nimport "{css_pass}";'
)

# Viteのエントリーポイントのhtmlとして保存する
with open("./02_tmp_html/index.html", mode="w") as f:
    f.write(tmp_html)
