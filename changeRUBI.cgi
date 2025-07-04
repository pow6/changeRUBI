#!/usr/local/bin/python
# -*- coding: utf-8 -*-
html='''Content-Type: text/html

<html>
  <head>
    <meta charset="UTF-8">
    <script data-ad-client="ca-pub-8903128356077453" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-125324142-2"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-125324142-2');
    </script>
    <title>カクヨム，なろう，アルファのルビ一括変換ツール</title>
    <meta content="3大小説投稿サイト（カクヨム，小説家になろう，アルファポリス）のルビの形式が違うので，一括で変換できるツール（非公式）。自分の小説を他サイトに転載するときなどに使ってください" name="description">
    
    <link rel="stylesheet" href="./changeRUBI.css">
    <link rel="shortcut icon" href="./changeRUBI_icon.png">
    <script type="text/javascript" src="./changeRUBI.js"></script>
  </head>
  <body>
    <hr color="#FF8000" size="5">
    <h1>カクヨム，なろう，アルファのルビ一括変換ツールver.1.1</h1>
    <p style="text-align: right">製作者：Arutaka　ホームページ：
      <a href="https://pow6.net" target="_blank">https://pow6.net</a></p>
    <hr size="3">
    <div class="intro">
    <p>　3大小説投稿サイト（カクヨム，小説家になろう，アルファポリス）のルビの形式が違うので，一括で変換できるツールを作成しました。 
      <br>　カクヨムで書いた小説をなろうとか，アルファに転載する時に使ってくれぇ。 
      <br>　一応，ミスの無いように作ったつもりですが，やらかしていたら教えてくだせぇ。 
    </p>
    </div>
    <div class="box">使い方：
      <br>　１．変換元の文章のサイトを選択 
      <br>　２．変換したい文章を入力 
      <br>　３．『変換する』をクリックすると，それぞれのルビの形式に変換した文章を表示します 
      <br>※変換サンプル⇒
      <a onclick="putSampleKaku()" class="likeButton">カクヨム</a>
      <a onclick="putSampleNarou()" class="likeButton">なろう</a>
      <a onclick="putSampleAlpha()" class="likeButton">アルファポリス</a>
    </div>
      <h3>変換元サイト</h3>
      <form method="post" action="changeRUBI.cgi">
        <div class="sentence">
          <div class="radio">
            <input type="radio" name="mode" value="kaku" id="kaku" checked/><label for="kaku">カクヨム</label>
            <input type="radio" name="mode" value="narou" id="narou"/><label for="narou">なろう</label> 
            <input type="radio" name="mode" value="alpha" id="alpha"/><label for="alpha">アルファポリス</label>
          </div>
          
          <!--button type="button" onclick="paste()">貼り付け</button-->
          </div>
          <p><button type="submit" class="square_btn">変換する</button></p>
          <p>
          <textarea class="ef" name="originText" id="originText" cols="100" rows="12" name="input_str" placeholder="変換したい文章を入力"></textarea>
          </p>
          <span class="focus_bg"></span>
      </form>
  </body>
</html>
'''

result='''
<head>
    <link rel="stylesheet" href="./changeRUBI.css">
    <script type="text/javascript" src="./changeRUBI.js"></script>
</head>
<hr color="#FF8000" size="5">
<h3>変換モード【%s】</h3>
<br>
<div class="sentence">
    <h3>カクヨム</h3>
    <button id="button_kaku" onclick="copy_kaku()" class="square_btn">コピー</button>
    <div class="enclosure"><textarea cols="50" rows="10" id="str_kaku" class="ef">%s</textarea></div>
</div>
<div class="sentence">
    <h3>なろう</h3>
    <button id="button_narou" onclick="copy_narou()" class="square_btn">コピー</button>
    <div class="enclosure"><textarea cols="50" rows="10" id="str_narou" class="ef">%s</textarea></div>
</div>
<div class="sentence">
    <h3>アルファポリス</h3>
    <button id="button_alpha" onclick="copy_alpha()" class="square_btn">コピー</button>
    <div class="enclosure"><textarea cols="50" rows="10" id="str_alpha" class="ef">%s</textarea></div>
</div>
<br>変換したルビ：%s
<br>変換後全ルビ：カクヨム %s
<br>　　　　　　　なろう　 %s
<br>　　　　　　　アルファ %s
'''

import sys
import cgi
import re
form = cgi.FieldStorage()
mode = form.getvalue("mode")
src = form.getvalue("originText")

#入力が何もない時のエラー処理（←エラーじゃなく例外処理的な）
if not src:
    print(html)
else:
    output_kaku = src
    output_narou = src
    output_alpha = src
    ptrnSt_kaku = r"(《《.*》》)"              #《《テキスト》》：カクヨムの強調機能
    ptrnNo_kaku = r"(\|?[一-龥]*《.*》)"    #テキスト《ルビ》：カクヨムのルビ機能
    ptrnFin_kaku = r"(\|.*《.*》)"          #|テキスト《ルビ》：カクヨム変換後形式
    ptrn_narou = r"(\|?[一-龥]*\(.*\))"        #テキスト（ルビ）：なろうのルビ機能
    ptrn_alpha = r"(#.*__.*__#)"           ##テキスト__ルビ__#：アルファポリスのルビ機能
    if mode == "kaku":
        mode = "カクヨム"
        changed_list = re.findall(ptrnNo_kaku, src)
        for word in changed_list:
            #changed_list から　《《》》の形式を|テキスト《ルビ》の形式にする処理
            if re.match(ptrnSt_kaku, word):
                pt = "・" * (len(word) - 4)
                dst = word.replace("《《", "|").replace("》》", "《" + pt + "》")
                output_kaku = output_kaku.replace(word, dst)
            else:
                #変換後の文字列を作成 | を追加し，《》を（）にする(なろう形式) ←なろうは，《》でもOkなので，《》に統一
                if (not word.startswith("|")) and (not word.startswith("《")):
                    dst = "|" + word
                    output_kaku = output_kaku.replace(word, dst)
            #|テキスト《ルビ》の形式になっているので，そこから，なろう，アルファ形式を作成
            output_narou = output_kaku
            #カクヨム，なろう互換形式から，アルファ形式を作成
            output_alpha = output_kaku.replace("|", "#").replace("《", "__").replace("》", "__#")
    elif mode == "narou":
        mode = "なろう"
        changed_list = re.findall(ptrn_narou, src)
        for word in changed_list:
            if (not word.startswith("|")) and (not word.startswith("《")):
                dst = "|" + word
                output_narou = output_narou.replace(word, dst)
        output_kaku = output_narou.replace("(", "《").replace(")", "》")
        output_alpha = output_kaku.replace("|", "#").replace("《", "__").replace("》", "__#")
    elif mode == "alpha":
        mode = "アルファポリス"
        changed_list = re.findall(ptrn_alpha, src)
        output_narou = output_alpha.replace("__#", "》").replace("__", "《").replace("#", "|")
        output_kaku = output_narou
        for word in changed_list:
            # changed_list から　|〇〇《・》の形式で，・の個数を調整する
            if re.search("・", word):
                pt = "・" * (len(word) - 3)
                dst = re.sub("・+", "・", pt)
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
    mode = mode
    changed_list = changed_list
    changed_kaku = re.findall(ptrnFin_kaku, output_kaku) + re.findall(ptrnSt_kaku, output_kaku)
    changed_narou = re.findall(ptrnFin_kaku, output_narou)
    changed_alpha = re.findall(ptrn_alpha, output_alpha)

    #リスト型を文字列に変換
    changed_list = '  '.join(changed_list)
    changed_kaku = '  '.join(changed_kaku)
    changed_narou = '  '.join(changed_narou)
    changed_alpha = '  '.join(changed_alpha)

    print(html)
    print(result % (mode, output_kaku, output_narou, output_alpha, changed_list, changed_kaku, changed_narou, changed_alpha))
