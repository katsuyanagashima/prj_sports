// 優勝・三賞入力画面
var oTable = null;
$(function () {
    var myTable = $("#tbl_SUMYUS01").DataTable({
        language: {
            search: '',
            lengthMenu: '_MENU_',
            searchPlaceholder: '検索',
            paginate: {next: '次', previous: '前',},
            zeroRecords: "データはありません。",
        },
        order: [[2, 'asc'], [4, 'asc'], [0, 'asc']], // 並び順
        columnDefs: [
            <!-- [0]東西コード -->
            <!-- [1]東西 -->
            <!-- [2]階級コード -->
            <!-- [3]階級 -->
            <!-- [4]番付順位 -->
            <!-- [5]力士名 -->
            <!-- [6] -->
            {orderable: false, targets: [0, 1, 2, 3, 4, 5, 6]}, // 利用者による並べ替えの禁止
            {targets: [0, 2], visible: false}, // 非表示の列
            {targets: 3, width: '110px'},
            {targets: 5, width: '110px'},
        ],
        paginate: false, // ページング
        info: false, // 件数情報
        //lengthChange: false, // 件数切替プルダウン
        //lengthMenu: [ [5, 15, -1], [5, 15, 'All'] ],
        scrollY: '40vh', // 縦方向のスクロールバー
        stateSave: true, // 表示条件の保存
        initComplete: function () { // プルダウンで階級を選択
            this.api().columns([3]).every(function () {
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
    // 選択した行の背景色を変更、ラジオボタンにチェック、優勝・三賞の指定ボタンの切り替え
    $('#tbl_SUMYUS01 tbody').on('click', 'tr', function () {
        if ($(this).hasClass('selected')) {
            $(this).removeClass('selected');
            $(this).children('.selectedRikishi').children('input').prop('checked', false);
        } else {
            myTable.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
            $(this).children('.selectedRikishi').children('input').prop('checked', true);
        }
        // 優勝・三賞の指定ボタンの切り替え
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
        var val_init = state['columns'][3]['search']['search'].replace(/\^|\$/g, '');
        $('#class_code_menu').val(val_init);
    }
});
