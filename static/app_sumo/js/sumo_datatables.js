// 優勝・三賞入力画面
var oTable = null;
$(function () {
    var myTable = $("#tbl_SUMYUS01_banzuke").DataTable({
        language: {
            search: '',
            lengthMenu: '_MENU_',
            searchPlaceholder: '検索',
            paginate: {next: '次', previous: '前',},
            zeroRecords: "データはありません。",
        },
        order: [[7, 'asc'], [8, 'asc'], [6, 'asc']], // 並び順
        columnDefs: [
            //<!-- [0]東西 -->
            //<!-- [1]階級 -->
            //<!-- [2]地位 -->
            //<!-- [3]番付順位 -->
            //<!-- [4]力士名 -->
            //<!-- [5]ラジオボタン -->
            //<!-- [6]東西コード -->
            //<!-- [7]階級コード -->
            //<!-- [8]番付順位 -->
            {orderable: false, targets: [0, 1, 2, 3, 4, 5, 6, 7, 8]}, // 利用者による並べ替えの禁止
            {targets: [6, 7, 8], visible: false}, // 非表示の列
        ],
        autowidth: false,
        paginate: false, // ページング
        info: false, // 件数情報
        //lengthChange: false, // 件数切替プルダウン
        //lengthMenu: [ [5, 15, -1], [5, 15, 'All'] ],
        scrollX: true, // ヘッダーがずれるので使用しない
        scrollY: '40vh', // 縦方向のスクロールバー
        stateSave: true, // 表示条件の保存
        initComplete: function () { // プルダウンで階級を選択
            this.api().columns([1]).every(function () {
                var column = this;
                var select = $('<select><option value="">−−−</option></select>')
                    .appendTo($(column.header()).empty())
                    .attr('id', 'class_code_menu')
                    .addClass('form-control input-sm')
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
                select.append('<option value="幕内">幕内</option>');
                select.append('<option value="十両">十両</option>');
                select.append('<option value="幕下">幕下</option>');
                select.append('<option value="三段目">三段目</option>');
                select.append('<option value="序二段">序二段</option>');
                select.append('<option value="序ノ口">序ノ口</option>');
            });
        },
        dom: '<<t>f>\'', // 検索ボックスの位置
    });
    // ヘッダーとボディの位置ずれを解消
    $('#tbl_SUMYUS01_banzuke').css('margin-left', '0px');
    // 選択した行の背景色を変更、ラジオボタンにチェック、優勝・三賞の指定ボタンの有効／無効
    $('#tbl_SUMYUS01_banzuke tbody').on('click', 'tr', function () {
        if ($(this).hasClass('selected')) {
            $(this).removeClass('selected');
            $(this).find('input').prop('checked', false);
        } else {
            $('tr.selected').removeClass('selected');
            $(this).addClass('selected');
            $(this).find('input').prop('checked', true);
        }
        // ボタンの有効／無効
        var my_class_code = myTable.$('tr.selected').children('td.class_code').text();
        if (my_class_code == '幕内') {
            $('.btn-yusho').prop("disabled", false);
            $('.btn-3sho').prop("disabled", false);
        } else if (my_class_code != '') { // 幕内以外
            $('.btn-yusho').prop("disabled", false);
            $('.btn-3sho').prop("disabled", true);
        } else { // 未選択
            $('.btn-yusho').prop("disabled", true);
            $('.btn-3sho').prop("disabled", true);
        }
    });
});

// 優勝・三賞入力画面の階級プルダウンメニュー前回の値を呼び出し
$(document).on('init.dt', function (e, settings) {
    var api = new $.fn.dataTable.Api(settings);
    var state = api.state.loaded();
    if (state) {
        var val_init = state['columns'][1]['search']['search'].replace(/\^|\$/g, '');
        $('#class_code_menu').val(val_init);
    }
    //階級別の場合、ボディ部に階級を表示しない
    if ($('#class_code_menu option:selected').text() == '−−−')
        $('td.class_code').removeClass('hidden');
    else
        $('td.class_code').hide();
});

//階級別に番付を表示する場合、ボディの各行に階級を表示しない
$(function () {
    // セレクトボックスが切り替わったら発動
    $('select#class_code_menu').change(function () {
        if ($('#class_code_menu option:selected').text() == '−−−')
            $('td.class_code').show();
        else
            $('td.class_code').hide();
    });
});

// 優勝・三賞画面の指定済みテーブル
// 　選択した行の背景色を変更、ラジオボタンにチェック、取消ボタンの有効／無効
$('#tbl_SUMYUS01_yusho tbody, #tbl_SUMYUS01_3sho tbody').on('click', 'tr', function () {
    if ($(this).hasClass('selected')) {
        $(this).removeClass('selected');
        $(this).find('input').prop('checked', false);
        $('.btn-torikeshi').prop("disabled", true);
    } else {
        $('tr.selected').removeClass('selected');
        $(this).addClass('selected');
        $(this).find('input').prop('checked', true);
        $('.btn-torikeshi').prop("disabled", false);
    }
});
