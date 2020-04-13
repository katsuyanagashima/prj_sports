
// 力士マスタメンテナンス作成と更新画面
// 日付は、年-月-日 の形式でお願いする。
$(function () {
  let dateFormat = 'yy-mm-dd';
  $('#id_Date_of_birth').datepicker({
      dateFormat: dateFormat
  });

  $('#age_calcu_reference_date').datepicker({
    dateFormat: dateFormat
  });  
});

// 対戦結果新規入力画面


$('#winlose1').change(function () {
  //勝敗ラジオボタン1
  const outcome1 = $("input[name='winlose1']:checked").val();

  $('#id_outcome1').val(outcome1);


  //勝敗1を入力したら自動で勝敗2が設定される
  // いったん全部クリアする
  $('#batsu2').removeClass('active');
  $('#sankaku2').removeClass('active');
  $('#maru2').removeClass('active');

  switch (outcome1) {
    case '1':
      $('#id_outcome2').val("3")
      $('#batsu2').addClass('active');
      break;
    case '2':
      $('#id_outcome2').val("2")
      $('#sankaku2').addClass('active');
      break;
    case '3':
      $('#id_outcome2').val("1")
      $('#maru2').addClass('active');
      break;
    default:
      $('#id_outcome2').val("")
  }
});


$('#winlose2').change(function () {
  //勝敗ラジオボタン2
  const outcome2 = $("input[name='winlose2']:checked").val();

  $('#id_outcome2').val(outcome2);

  //勝敗2を入力したら自動で勝敗2が設定される 
  // いったん全部クリアする
  $('#batsu1').removeClass('active');
  $('#sankaku1').removeClass('active');
  $('#maru1').removeClass('active');

  switch (outcome2) {
    case '1':
      $('#id_outcome1').val("3")
      $('#batsu1').addClass('active');
      break;
    case '2':
      $('#id_outcome1').val("2")
      $('#sankaku1').addClass('active');
      break;
    case '3':
      $('#id_outcome1').val("1")
      $('#maru1').addClass('active');
      break;
    default:
      $('#id_outcome1').val("")
  }
});


//力士1を入力したら自動で力士2の選択肢から力士1を省く
$('#id_player1').change(function () {
  const player1 = $(this).val();
  //作成中
})

// クリアボタン
$('#clear').click(function () {
  $('#batsu1').removeClass('active');
  $('#sankaku1').removeClass('active');
  $('#maru1').removeClass('active');
  $('#batsu2').removeClass('active');
  $('#sankaku2').removeClass('active');
  $('#maru2').removeClass('active');
  $('#id_outcome1').val("");
  $('#id_outcome2').val("");
  $('#id_player1').val("");
  $('#id_player2').val("");
  $('#id_waza').val("");
  $('#rikishi_label').val("");
  $('#rikishi_label2').val("");
  $('#kimarite_label').val("");
  $('#rikishi_sentaku_1').css("display", "none");
  $('#rikishi_sentaku_2').css("display", "none");
  $('#waza_sentaku').css("display", "none");
})



// 力士選択ボタン
$('#rikishiselect').click(function () { $('#rikishi_sentaku_1').css("display", "") });
$('#rikishiselect2').click(function () { $('#rikishi_sentaku_2').css("display", "") });

// 力士選択1
$('.selected_rikishi').click(function () {
  $('#id_player1').val($("option", this)[0].value);

  $('#rikishi_label').val($("option", this)[0].innerHTML);
  $('#rikishi_sentaku_1').css("display", "none")
});

// 力士選択2
$('.selected_rikishi2').click(function () {
  $('#id_player2').val($("option", this)[0].value);

  $('#rikishi_label2').val($("option", this)[0].innerHTML);
  $('#rikishi_sentaku_2').css("display", "none")
});

// 決まり手選択ボタン
$('#kimarite_select_btn').click(function () { $('#waza_sentaku').css("display", "") });

// 決まり手選択
$('.selected_waza').click(function () {
  $('#id_waza').val($("option", this)[0].value);

  $('#kimarite_label').val($("option", this)[0].innerHTML);
  $('#waza_sentaku').css("display", "none");
});


// 常時監視
window.addEventListener("load", function () {

  // フォームのバリデーションを解除
  // https://qiita.com/jkr_2255/items/c0bf1627a5bcdf4f8964
  $('form').find('input textarea select').removeAttr('required max min maxlength pattern');
  // ↑これじゃうまくいかない、、、


  // 初期表示
  // $('#id_outcome1 , #id_waza , #id_outcome2').attr('class', 'form-control');

  // いろいろと非表示にさせる
  $('#id_player1').css("display", "none");
  $('#id_player2').css("display", "none");
  $('#id_outcome1').css("display", "none");
  $('#id_outcome2').css("display", "none");
  $('#id_waza').css("display", "none");

  $('#rikishi_sentaku_1').css("display", "none");
  $('#rikishi_sentaku_2').css("display", "none");
  $('#waza_sentaku').css("display", "none");

});

 // 画面 SUMOUT02の種別チェックボックスをクリック時に電文種別のセレクトボックスを変更する
 $('input.group_code').on('click', function(){
  let json_data = $(this).data();
  let d = json_data["group"];
  let slct = $("select#NewsMLNo").empty();
  for(let i = 0; i < d.length; i++){
    dt = d[i]
    let opt = $('<option>').val(dt["NewsMLNo"]).text(dt["ContentName"]);
    slct.append(opt);
  }
 })

 // 画面 SUMUDY01(運用日設定)の勝負日目を変更したタイミングで発火
 $('select#shoubu').on('change', function(){
  let data = $(this).data();
  let val = parseInt($(this).val());
  let banzuke_date = data["banzukeDate"];
  let first_date = data["firstDate"];

  let change_date = "";
  if(!val) change_date = banzuke_date;
  else{
    //　YYYY-MM-DD形式の文字列をDATEオブジェクトに変換
    let arr = first_date.split('-');
    let date_obj = new Date(arr[0],arr[1]-1, arr[2]);

    // DATEオブジェクトに日数を加算
    let dt = date_obj.setDate(date_obj.getDate() + (val-1));
    dt = new Date(dt)

    // DATEオブジェクトからYYYY-MM-DD形式の文字列に戻す
    let y = dt.getFullYear();
    let m = ("00" + (dt.getMonth()+1)).slice(-2);
    let d = ("00" + dt.getDate()).slice(-2);
    first_date = y + "-" + m + "-" + d;
    change_date = first_date;
  }

  $("input#age_calcu_reference_date").val(change_date);

 })
