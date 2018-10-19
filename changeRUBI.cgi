#!/usr/local/bin/python
# -*- coding: utf-8 -*-
html='''Content-Type: text/html

<html>
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
    <p style="text-align: right">製作者：RealTakashi　ホームページ：
      <a href="https://pow6.net" target="_blank">最弱高専生の書きなぐり</a>　Twitter:
      <a href="https://twitter.com/simejiEgg" target="_blank">@simejiEgg</a>
    </p>
    <hr size="3">
    <p>3大小説投稿サイト（カクヨム，小説家になろう，アルファポリス）のルビの形式が違うので，一括で変換できるツールを作成しました。 
      <br>カクヨムで書いた小説をなろうとか，アルファに転載する時に使ってくれぇ。 
      <br>一応，ミスの無いように作ったつもりですが，やらかしていたら教えてくだせぇ。（←べーた版だしね←べーたって書けば許されると思ってる奴） 
    </p>
    <p>使い方： 
      <br>　１．変換元の文章のサイトを選択 
      <br>　２．変換する文章を入力 
      <br>　３．『変換する』をクリックすると，それぞれのルビの形式に変換した文章を表示します 
    </p>
    <div class="sentence">
      <h3>変換元サイト</h3>
      <form method="post" action="changeRUBI.cgi">
        <input type="radio" name="mode" value="kaku" checked/>カクヨム 
        <input type="radio" name="mode" value="narou"/>なろう 
        <input type="radio" name="mode" value="alpha"/>アルファポリス 
        <h3>変換したい文章を入力</h3>
        <textarea name="originText" id="originText" cols="50" rows="10" name="input_str" placeholder="変換したい文章を入力"></textarea>
        <p>
          <input type="submit" value="変換する">
          <!--button type="button" onclick="paste()">貼り付け</button-->
          <script>
                function  putSample() {
                    document.getElementById("originText").value = "カクヨム形式:\n\t漢字《かんじ》\n\t|テキスト《文章》\n\t《《強調するぜよ》》\nなろう形式：\n\t漢字(かんじ)\n\t|強調《・・》\nアルファ形式：\n\t#文字__テキスト__#\n\t#強調__・__#";
                }
          </script>
        </p>
      </form>
     </div>
  </body>
</html>
'''

result='''
<h1>変換結果</h1>
<h3>変換モード【%s】</h3>
<br>変換したルビ：%s
<br>変換後全ルビ：カクヨム %s
<br>　　　　　　　なろう　 %s
<br>　　　　　　　アルファ %s
<br>
<div class="sentence">
    <h3>カクヨム</h3>
    <button id="button_kaku">クリップボードにコピー</button>
    <div class="enclosure"><textarea cols="50" rows="10" id="str_kaku">%s</textarea></div>
</div>
<div class="sentence">
    <h3>なろう</h3>
    <button id="button_narou">クリップボードにコピー</button>
    <div class="enclosure"><textarea cols="50" rows="10" id="str_narou">%s</textarea></div>
</div>
<div class="sentence">
    <h3>アルファポリス</h3>
    <button id="button_alpha">クリップボードにコピー</button>
    <div class="enclosure"><textarea cols="50" rows="10" id="str_alpha">%s</textarea></div>
</div>
'''

js ='''Content-Type: application/x-javascript
<button type="button" onclick="putSample()">変換サンプルを表示</button>
<script>
    function  putSample() {
            document.getElementById("originText").value = "カクヨム形式:\n\t漢字《かんじ》\n\t|テキスト《文章》\n\t《《強調するぜよ》》\nなろう形式：\n\t漢字(かんじ)\n\t|強調《・・》\nアルファ形式：\n\t#文字__テキスト__#\n\t#強調__・__#";
        }
</script>
'''

import cgi
import re
import regex #regex モジュールでの\p{Han}が上手く動かないので，あんま意味ない
form = cgi.FieldStorage()
mode = form.getvalue("mode")
src = form.getvalue("originText")

#入力が何もない時のエラー処理
if not src:
    print(html)
else:

    output_kaku = src
    output_narou = src
    output_alpha = src
    ptrnSt_kaku = "(《《.*》》)"              #《《テキスト》》：カクヨムの強調機能
    #ptrnNo_kaku = "(\|?\p{Han}*《.*》)"    #テキスト《ルビ》：カクヨムのルビ機能
    ptrnNo_kaku = "(\|?[一-龥]*《.*》)"    #テキスト《ルビ》：カクヨムのルビ機能
    ptrnFin_kaku = "(\|.*《.*》)"          #|テキスト《ルビ》：カクヨム変換後形式
    #ptrn_narou = "(\|?\p{Han}*\(.*\))"        #テキスト（ルビ）：なろうのルビ機能
    ptrn_narou = "(\|?[一-龥]*\(.*\))"        #テキスト（ルビ）：なろうのルビ機能
    ptrn_alpha = "(#.*__.*__#)"           ##テキスト__ルビ__#：アルファポリスのルビ機能
    if mode == "kaku":
        mode = "カクヨム"
        changed_list = regex.findall(ptrnNo_kaku, src)
        for word in changed_list:
            #changed_list から　《《》》の形式を|テキスト《ルビ》の形式にする処理
            if regex.match(ptrnSt_kaku, word):
                pt = "・" * (len(word)-4)
                dst = word.replace("《《", "|").replace("》》", "《"+pt+"》")
                output_kaku = output_kaku.replace(word, dst)
            else:
                #変換後の文字列を作成 | を追加し，《》を（）にする(なろう形式) ←なろうは，《》でもOkなので，《》に統一
                #if regex.match("|.*", word):
                if (not word.startswith("|")) and (not word.startswith("《")):
                    dst = "|"+word
                    output_kaku = output_kaku.replace(word, dst)
            #|テキスト《ルビ》の形式になっているので，そこから，なろう，アルファ形式を作成
            #output_narou = output_kaku.replace("《", "(").replace("》", ")")
            output_narou = output_kaku
            #カクヨム，なろう互換形式から，アルファ形式を作成
            output_alpha = output_kaku.replace("|", "#").replace("《", "__").replace("》", "__#")
    elif mode == "narou":
        mode = "なろう"
        changed_list = regex.findall(ptrn_narou, src)
        for word in changed_list:
            if (not word.startswith("|")) and (not word.startswith("《")):
                dst = "|"+word
                output_narou = output_narou.replace(word, dst)
        output_kaku = output_narou.replace("(", "《").replace(")", "》")
        output_alpha = output_kaku.replace("|", "#").replace("《", "__").replace("》", "__#")
    elif mode == "alpha":
        mode = "アルファポリス"
        changed_list = regex.findall(ptrn_alpha, src)
        output_narou = output_alpha.replace("__#", "》").replace("__", "《").replace("#", "|")
        output_kaku = output_narou
        for word in changed_list:
            # changed_list から　|〇〇《・》の形式で，・の個数を調整する
            if regex.search("・", word):
                pt = "・" * (len(word) - 3)
                dst = regex.sub("・+", "・",pt)
                output_kaku = output_kaku.replace(word, dst)
    else:
        changed_list = "エラー"

    #最終調整：正規表現はグループ化しておかないと，・・・の連続を・にすることがうまくできない（注意）
    output_alpha = re.sub(r"(・)+", "・", output_alpha)
    #\2 は第二引数，つまり，(.*)の部分のこと【python 正規表現　後方参照】【python re.sub 後方参照】とかでググる
    #rは必ずつけること！　\使うと，エスケープされる
    output_kaku = re.sub(r"(\|)(.*)(《)(・)*(》)", r"《《\2》》", output_kaku)
    changed_kaku = re.sub(r"(\|)(.*)(《)(・)*(》)", r"《《\2》》", output_kaku)

    #調整
    #output_kaku = output_kaku
    #output_narou = output_narou
    #output_alpha = output_alpha
    mode = mode
    changed_list = changed_list
    changed_kaku = regex.findall(ptrnFin_kaku, output_kaku)+regex.findall(ptrnSt_kaku, output_kaku)
    changed_narou = regex.findall(ptrnFin_kaku, output_narou)
    changed_alpha = regex.findall(ptrn_alpha, output_alpha)

    #リスト型を文字列に変換
    changed_list = ','.join(changed_list)
    changed_kaku = ','.join(changed_kaku)
    changed_narou = ','.join(changed_narou)
    changed_alpha = ','.join(changed_alpha)

    print(html)
    #print(js)
    print(result % (mode,changed_list,changed_kaku,changed_narou,changed_alpha,output_kaku,output_narou,output_alpha))
