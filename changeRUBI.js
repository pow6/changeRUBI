function  putSampleKaku() {
    document.getElementById("originText").value = "【カクヨム形式】\n\n漢字《かんじ》\n|テキスト《文章》\n《《強調するぜよ》》\n";
    var radio = document.getElementById("kaku");
    radio.checked = true;
}

function putSampleNarou() {
    document.getElementById("originText").value = "【なろう形式】\n\n漢字(かんじ)\n監事《かんじ》\n|強調するんだよぉ《・・・・・・・・》\n";
    var radio = document.getElementById("narou");
    radio.checked = true;
}

function putSampleAlpha() {
    document.getElementById("originText").value = "【アルファ形式】\n\n#文字__テキスト__#\n#強調するんご__・__#\n";
    var radio = document.getElementById("alpha");
    radio.checked = true;
}

function copy_kaku() {
    var t_kaku = document.getElementById("str_kaku");
    t_kaku.select();
    document.execCommand("Copy");
}
function copy_narou() {
    var t_narou = document.getElementById("str_narou");
    t_narou.select();
    document.execCommand("copy");
}
function copy_alpha() {
    var t_alpha = document.getElementById("str_alpha");
    t_alpha.select();
    document.execCommand("copy");
}

function paste() {
    var str = document.querySelector("#originText");
    str.focus();
    document.execCommand("paste");
}