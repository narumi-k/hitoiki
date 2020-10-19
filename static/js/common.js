
$(function () {

    $('.container').on("load", function() {
        var imgpass = "../images/";
        // 表示させたい画像のファイル名＋拡張子を配列に格納
        var imgfile = [];
        imgfile[0] = 'bolivia-1802042_1920.jpg';
        imgfile[1] = 'forest-5179110_1920.jpg';
        imgfile[2] = 'japanese-cherry-trees-3063992_1920.jpg';
        // 画像の数を元に、ランダムな数値を算出
        var n = Math.floor(Math.random() * imgfile.length);
        // 算出したランダムな数値の順番にいるファイル情報をbackground-imageに設定する
        $('.container').css('background-image', 'url(' + imgpass + imgfile[n] + ')');
    })

})