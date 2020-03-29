(function($) {

 // 画面SUMOUT02の種別チェックボックスをクリック時に電文種別のセレクトボックスを変更する
 $('input.group_code').on('click', function(){
  let json_data = $(this).data();
  let d = JSON.parse(json_data);
  let slct = $("select#Input_status");
  for(let i = 0; i < d.length; i++){
    dt = d[i]
    let opt = $('<option>').val(dt["NewsMLNo"]).text(dt["ContentName"]);
    slct.append(opt);
  }
 })

})(django.jQuery);
