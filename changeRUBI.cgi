#!/usr/local/bin/python

html='''Context-Type: text/html
<head>
    <meta charset="UTF-8">
    <title>カクヨム，なろう，アルファのルビ一括変換ツール</title>
    <style type="text/css">
        <!--
        h1{
            font-size:20px;
        }
        div.sentence{
            display: inline-block;
        }
        -->
    </style>
</head>
<body>
<hr color="#FF8000" size="5">
<h1>カクヨム，なろう，アルファのルビ一括変換ツールver.1.0（べーた）</h1>
<p style="text-align: right">製作者：RealTakashi　ホームページ：<a href="https://pow6.net" target="_blank">最弱高専生の書きなぐり</a>　Twitter:<a href="https://twitter.com/simejiEgg" target="_blank">@simejiEgg</a></p>
<hr size="3">
<p>
    3大小説投稿サイト（カクヨム，小説家になろう，アルファポリス）のルビの形式が違うので，一括で変換できるツールを作成しました。
    <br>カクヨムで書いた小説をなろうとか，アルファに転載する時に使ってくれぇ。
    <br>一応，ミスの無いように作ったつもりですが，やらかしていたら教えてくだせぇ。（←べーた版だしね←べーたって書けば許されると思ってる奴）
</p>
<p>
    使い方：
    <br>　１．変換元の文章のサイトを選択
    <br>　２．変換する文章を入力
    <br>　３．『変換する』をクリックすると，それぞれのルビの形式に変換した文章を表示します
</p>

<div class="sentence">
    <h3>変換元サイト</h3>
    <form method="post" action="output">
        <input type="radio" name="mode" value="kaku" checked>カクヨム
        <input type="radio" name="mode" value="narou">なろう
        <input type="radio" name="mode" value="alpha">アルファポリス
        <h3>変換したい文章を入力</h3>
        <p>
            <button type="submit" name="action">変換する</button>
            <!--button type="button" onclick="paste()">貼り付け</button-->
            <button type="button" onclick="putSample()">変換サンプルを表示</button>
            <script>
                function  putSample() {
                    document.getElementById("originText").value = "カクヨム形式:\n\t漢字《かんじ》\n\t|テキスト《文章》\n\t《《強調するぜよ》》\nなろう形式：\n\t漢字(かんじ)\n\t|強調《・・》\nアルファ形式：\n\t#文字__テキスト__#\n\t#強調__・__#";
                }
            </script>
        </p>
        <textarea id="originText" cols="50" rows="10" name="input_str">変換したい文章を入力</textarea>
    </form>
    <h3>%s</h3>
    <p>%s</p>
    <p>%s</p>
</div>
</body>
</html>
'''
import cgi
form = cgi.FieldStorage()
text = form.getfirst("originText","")
radio = form.getfirst("mode","")
print("変換結果")
print(html % text)
print(html % radio)