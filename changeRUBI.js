function  putSample() {
    document.getElementById("originText").value = "カクヨム形式:\n\t漢字《かんじ》\n\t|テキスト《文章》\n\t《《強調するぜよ》》\nなろう形式：\n\t漢字(かんじ)\n\t|強調《・・》\nアルファ形式：\n\t#文字__テキスト__#\n\t#強調__・__#";
}

var t_kaku = document.getElementById("str_kaku");
var b_kaku = document.getElementById("button_kaku");
var t_narou = document.getElementById("str_narou");
var b_narou = document.getElementById("button_narou");
var t_alpha = document.getElementById("str_alpha");
var b_alpha = document.getElementById("button_alpha");
var result;
function copy_kaku() {
    t_kaku.select();
    result = document.execCommand("copy");
    console.log(result);
}
function copy_narou() {
    t_narou.select();
    result = document.execCommand("copy");
    console.log(result);
}
function copy_alpha() {
    t_alpha.select();
    result = document.execCommand("copy");
    console.log(result);
}
