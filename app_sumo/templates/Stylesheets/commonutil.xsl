<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja">
  <!--=============================================================================
　プレーンテキスト・全スタイルシート共通処理用
4.0版　 2014.12.19 プレーンテキスト版として新規公開
4.01版　2015.02.27 PAGE_LINE_COUNT_START_UTLを削除（未使用のため）
                   WritingModeYoko_UTLに処理対象文字列定義を追加
                   空行に設定する空白文字に全角スペースを使用するよう訂正
                   内容情報部が長い場合に、一頁目に改行を挿入する処理を追加
                   以下のテンプレートを新規追加
                   ・Get_TextLineCount_UTL
                   ・TranslateToRensuuFromEnd_UTL
                   ・SubstringAfterLast_UTL
                   ・SubstringTargetLine_UTL
                   ・SplitText_UTL
                   ・TABLE_LAYOUT_LeftRight_UTIL  
4.02版　2015.03.31 改ページ用divの仕様変更。div（class="pageBreak"）内にpタグを設定
                   NAIYOU_LINE_COUNT_UTL、NAIYOU_LINE_SETの定義変更（variable→template）関連部分の処理変更
                   SplitTextForPTag_UTL呼び出し処理の記述変更（ネストを排除、行カウント不要な場合の処理スキップ）
                   NAIYOU_LINE_COUNT_UTLの内容情報部の要素に解禁日時を追加、および行数算出式修正
                   縦書き・横書き混在記事用の処理を追加
                   ルーラー表示を本文出力行のみに変更
                   テンプレートSplitText_NotFillSpace_UTLを新規追加
4.03版　2015.05.29 内容情報部が長い場合の１頁目改ページ挿入処理にて、判断条件をＡ４縦/横で分岐するよう修正
                   横書き・縦書き混在記事の編集処理を変更。横書きDivが連続する場合は間隔をあけない
                   テンプレートReplaceString_UTLを新規追加
                   テンプレートTranslateCharYOKO_UTLに処理対象文字を追加
                   テンプレートWritingModeTateYoko_UTLに処理対象文字を追加
                   改行コードをCRLFに統一
4.04版　2015.07.30 GetTagsMaxLength_UTL、GetTagsMaxLengthStirng_UTL、GetTagsMaxNum_UTLをソートを使用しない仕様に変更
                   上記仕様変更に伴いテンプレートGet_TagsMaxNumString_UTL、Get_TextMaxLengthString_UTLを追加
                   テンプレートTranslateCharYOKO_UTLに処理対象文字を追加
                   テンプレートWritingModeTateYoko_UTLに処理対象文字を追加
4.05版　2015.08.20 （IE7,8対応）ソートを廃止した処理にて改行定数が見えない現象のため再定義追加
4.06版  2015.●.● OikomiStartクラス付加機能を追加
================================================================================-->
  <!--#### 共通変数 #################################################################################-->
  <!--===============================================================================================-->
  <!--  分割処理用改行文字列 可変 -->
  <!--===============================================================================================-->
  <!-- 改行定数 -->
  <xsl:variable name="LineFeed_UTL">
    <xsl:text>LF</xsl:text>
  </xsl:variable>
  <!-- 改ページ定数(定義用) -->
  <xsl:variable name="PageBreakTeigi_UTL">
    <xsl:text>PB</xsl:text>
  </xsl:variable>
  <!-- 改ページ定数（各テンプレートではこちらを使用） -->
  <xsl:variable name="PageBreak_UTL">
    <xsl:value-of select="$LineFeed_UTL"/>
    <xsl:value-of select="$PageBreakTeigi_UTL"/>
  </xsl:variable>
  <!-- pタグclass設定用定数（対戦） -->
  <xsl:variable name="MatchClass_UTL">
    <xsl:text>¶</xsl:text>
  </xsl:variable>
  <!-- pタグclass設定用定数（追い込み行頭） -->
  <xsl:variable name="OikomiClass_UTL">
    <xsl:text>§</xsl:text>
  </xsl:variable>
  <!-- pタグclass排除用定数 -->
  <xsl:variable name="NoClass_UTL">
    <xsl:text>®</xsl:text>
  </xsl:variable>
  <!-- 横書き縦書き混在記事　切り替えポイント -->
  <xsl:variable name="YOKOTATEBreak_UTL">
    <xsl:text>⌘</xsl:text>
  </xsl:variable>
  <!--===============================================================================================-->
  <!--  字詰め用空白文字 固定 -->
  <!--===============================================================================================-->
  <xsl:variable name="WhiteSpaceZenkaku_UTL">
    <xsl:text>S</xsl:text>
    <!-- 必ず１文字にすること -->
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- １行最大折り返し文字数を取得（共通） -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXTEXT_DEFAULT_UTIL">
    <!-- 個別定義が無効な場合、共通定義を取得 -->
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$PTEXT_TATEYOKO_SET=1">
            <!-- 縦書き -->
            <xsl:value-of select="$PRINT_MAXTEXT_TATE_TATE_SET"/>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXTEXT_TATE_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:choose>
          <xsl:when test="$PTEXT_TATEYOKO_SET=1">
            <!-- 縦書き -->
            <xsl:value-of select="$PRINT_MAXTEXT_YOKO_TATE_SET"/>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXTEXT_YOKO_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- １ページ最大行数を取得（共通） -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXLINES_DEFAULT_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$PTEXT_TATEYOKO_SET=1">
            <!-- 縦書き -->
            <xsl:value-of select="$PRINT_MAXLINES_TATE_TATE_SET"/>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXLINES_TATE_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:choose>
          <xsl:when test="$PTEXT_TATEYOKO_SET=1">
            <!-- 縦書き -->
            <xsl:value-of select="$PRINT_MAXLINES_YOKO_TATE_SET"/>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXLINES_YOKO_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■横書き固定専用■１行最大折り返し文字数を取得（横のみ・共通） -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXYOKOTEXT_DEFAULT_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXTEXT_TATE_YOKO_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXTEXT_YOKO_YOKO_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■横書き固定専用■１ページ最大行数を取得（横のみ・共通）  -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXYOKOLINES_DEFAULT_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXLINES_TATE_YOKO_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXLINES_YOKO_YOKO_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■縦書き固定専用■１行最大折り返し文字数を取得（縦のみ・共通） -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXTATETEXT_DEFAULT_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXTEXT_TATE_TATE_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXTEXT_YOKO_TATE_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■縦書き固定専用■１ページ最大行数を取得（縦のみ・共通）  -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXTATELINES_DEFAULT_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXLINES_TATE_TATE_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXLINES_YOKO_TATE_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■横書き固定専用（Ａ４タテのみ9pt文字）■１行最大折り返し文字数を取得（横のみ・Ａ４タテ印刷の場合に9pt用の文字数を適用） -->
  <!-- ※Ａ４ヨコ印刷の場合は12pt -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXYOKOTEXT_FontSizeSmall_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXTEXT_FontSizeSmall_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXTEXT_YOKO_YOKO_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■横書き固定専用（Ａ４タテのみ9pt文字）■１ページ最大行数を取得（横のみ・Ａ４タテ印刷の場合に9pt用の文字数を適用）  -->
  <!-- ※Ａ４ヨコ印刷の場合は12pt -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXYOKOLINES_FontSizeSmall_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXLINES_FontSizeSmall_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXLINES_YOKO_YOKO_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■横書き固定専用（9pt文字）■１行最大折り返し文字数を取得（横のみ・9pt用の文字数を適用） -->
  <!-- ※Ａ４タテ印刷/Ａ４ヨコ印刷、いずれも9pt -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXYOKOTEXT_FontSizeSmall_2_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXTEXT_FontSizeSmall_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXTEXT_FontSizeSmall_A4YOKO_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■横書き固定専用（9pt文字）■１ページ最大行数を取得（横のみ・9pt用の文字数を適用）  -->
  <!-- ※Ａ４タテ印刷/Ａ４ヨコ印刷、いずれも9pt -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXYOKOLINES_FontSizeSmall_2_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXLINES_FontSizeSmall_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXLINES_FontSizeSmall_A4YOKO_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- ■縦書き固定専用（9pt文字）■１ページ最大行数を取得（縦のみ・9pt用の文字数を適用）  -->
  <!-- ※Ａ４タテ印刷/Ａ４ヨコ印刷、いずれも9pt -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <xsl:variable name="PRINT_MAXTATELINES_FontSizeSmall_UTIL">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:value-of select="$PRINT_MAXTATELINES_FontSizeSmall_SET"/>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:value-of select="$PRINT_MAXTATELINES_FontSizeSmall_A4YOKO_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!--=======================================================================================================-->
  <!-- １ページ最大行数のカウントをスタートする値（共通）-->
  <!-- 横書き表示、かつ内容情報部表示時に１ページ目の表示行数を少なくする -->
  <!-- テンプレート「SplitTextForPTag_UTL」のパラメータ｢PAGE_LINE_COUNT」に設定する -->
  <!-- ※個別設定を使用しない場合 -->
  <!--=======================================================================================================-->
  <!--<xsl:variable name="PAGE_LINE_COUNT_START_UTL">-->
  <!--<xsl:choose>-->
  <!--内容情報部あり-->
  <!--<xsl:when test="$NAIYOU_F_SET=1 and $PTEXT_TATEYOKO_SET=2">-->
  <!--<xsl:value-of select="$NAIYOU_LINE_SET"/>-->
  <!--</xsl:when>-->
  <!--内容情報部なし-->
  <!--<xsl:otherwise>-->
  <!--<xsl:value-of select="0"/>-->
  <!--</xsl:otherwise>-->
  <!--</xsl:choose>-->
  <!--</xsl:variable>-->
  <!--=======================================================================================================-->
  <!--内容情報部　可変要素の出力確認　内部共通処理-->
  <!--=======================================================================================================-->
  <xsl:template name="Edit_NAIYOU_LINE_COUNT_UTL">
    <xsl:param name="TargetPath"/>
    <xsl:param name="LfLength"/>
    <xsl:choose>
      <xsl:when test="$TargetPath">
        <xsl:variable name="DataLengthCheck">
          <xsl:for-each select="$TargetPath">
            <xsl:value-of select="."/>
            <xsl:text>、</xsl:text>
          </xsl:for-each>
        </xsl:variable>
        <xsl:value-of select="ceiling(string-length($DataLengthCheck) div $LfLength)"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="0"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--内容情報部　可変要素の出力確認-->
  <!--=======================================================================================================-->
  <xsl:template name="NAIYOU_LINE_COUNT_UTL">
    <xsl:variable name="LfLength" select="45"/>
    <xsl:variable name="LfLengthColspan" select="20"/>
    <!-- 副ヘッダ -->
    <xsl:variable name="InSendControlCount">
      <xsl:variable name="InSendControlString">
        <xsl:call-template name="CH_InSendControl"/>
      </xsl:variable>
      <xsl:value-of select="ceiling(string-length($InSendControlString) div $LfLength)"/>
    </xsl:variable>
    <!-- コメント -->
    <xsl:variable name="InCommentCount">
      <xsl:call-template name="Edit_NAIYOU_LINE_COUNT_UTL">
        <xsl:with-param name="TargetPath" select="//InNewsInfo/InSupportControl/InComment"/>
        <xsl:with-param name="LfLength" select="$LfLength"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 主見出し・脇見出し -->
    <xsl:variable name="InSubHeadLineCount">
      <xsl:choose>
        <xsl:when test="//InSubHeadLine">
          <xsl:variable name="InHeadLine">
            <xsl:call-template name="Edit_NAIYOU_LINE_COUNT_UTL">
              <xsl:with-param name="TargetPath" select="//InHeadLine"/>
              <xsl:with-param name="LfLength" select="$LfLengthColspan"/>
            </xsl:call-template>
          </xsl:variable>
          <xsl:variable name="InSubHeadLine">
            <xsl:call-template name="Edit_NAIYOU_LINE_COUNT_UTL">
              <xsl:with-param name="TargetPath" select="//InSubHeadLine"/>
              <xsl:with-param name="LfLength" select="$LfLengthColspan"/>
            </xsl:call-template>
          </xsl:variable>
          <xsl:choose>
            <xsl:when test="$InHeadLine > $InSubHeadLine">
              <xsl:value-of select="$InHeadLine"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$InSubHeadLine"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:otherwise>
          <xsl:call-template name="Edit_NAIYOU_LINE_COUNT_UTL">
            <xsl:with-param name="TargetPath" select="//InHeadLine"/>
            <xsl:with-param name="LfLength" select="$LfLength"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- 見出し編注 -->
    <xsl:variable name="InEditLineCount">
      <xsl:choose>
        <!--記事以外の編注=InEditLine出力-->
        <xsl:when test="not(substring(//InProductId,9,2)='ＤＨ')">
          <xsl:call-template name="Edit_NAIYOU_LINE_COUNT_UTL">
            <xsl:with-param name="TargetPath" select="//InEditLine"/>
            <xsl:with-param name="LfLength" select="$LfLength"/>
          </xsl:call-template>
        </xsl:when>
        <!--一般記事編注＝InNewsLineTextを編注とする-->
        <xsl:otherwise>
          <xsl:call-template name="Edit_NAIYOU_LINE_COUNT_UTL">
            <xsl:with-param name="TargetPath" select="//NewsComponent/NewsLines/NewsLine/NewsLineType[@FormalName='EditInfo']"/>
            <xsl:with-param name="LfLength" select="$LfLength"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- 部署＆ユーザ -->
    <xsl:variable name="InSendFromCount">
      <xsl:choose>
        <xsl:when test="not(substring(//InProductId,9,2)='ＤＨ')">
          <xsl:choose>
            <xsl:when test="//InNewsGenre='加盟' and (//InSendFrom or //ByLine)">
              <xsl:value-of select="1"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="0"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="0"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--末尾編注（記事以外のみ表示）-->
    <xsl:variable name="InEndLineCount">
      <xsl:choose>
        <xsl:when test="not(substring(//InProductId,9,2)='ＤＨ')">
          <xsl:call-template name="Edit_NAIYOU_LINE_COUNT_UTL">
            <xsl:with-param name="TargetPath" select="//InEndLine"/>
            <xsl:with-param name="LfLength" select="$LfLength"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="0"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- 解禁日時 -->
    <xsl:variable name="InLimitation">
      <xsl:call-template name="Edit_NAIYOU_LINE_COUNT_UTL">
        <xsl:with-param name="TargetPath" select="//InLimitation"/>
        <xsl:with-param name="LfLength" select="$LfLength"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 合計数 -->
    <!--<xsl:value-of select="ceiling(($InSendControlCount + $InCommentCount + $InSubHeadLineCount + $InEditLineCount + $InSendFromCount + $InEndLineCount + $InLimitation)*0.75)"/>-->
    <xsl:value-of select="($InSendControlCount + $InCommentCount + $InSubHeadLineCount + $InEditLineCount + $InSendFromCount + $InEndLineCount + $InLimitation)"/>
  </xsl:template>
  <!--#### 共通テンプレート #########################################################################-->
  <!--===============================================================================================-->
  <!--pタグを出力-->
  <!--===============================================================================================-->
  <!--■<p>を出力-->
  <xsl:template name="PTag_UTL">
    <xsl:param name="PTEXT"/>
    <xsl:param name="TateYoko" select="0"/>
    <xsl:choose>
      <xsl:when test="$TateYoko=1">
        <p>
          <!-- spanタグ挿入処理 -->
          <xsl:call-template name="WritingModeYoko_UTL">
            <xsl:with-param name="BeforeData">
              <xsl:value-of select="translate($PTEXT, $WhiteSpaceZenkaku_UTL, '　')"/>
            </xsl:with-param>
          </xsl:call-template>
        </p>
      </xsl:when>
      <xsl:otherwise>
        <p>
          <xsl:value-of select="translate($PTEXT, $WhiteSpaceZenkaku_UTL, '　')"/>
        </p>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--■<p>を出力（横書き／縦書き混在記事用）-->
  <xsl:template name="PTag_TATEYOKO_UTL">
    <xsl:param name="PTEXT"/>
    <p>
      <!-- spanタグ挿入処理 -->
      <xsl:call-template name="WritingModeTateYoko_UTL">
        <xsl:with-param name="BeforeData">
          <xsl:value-of select="translate($PTEXT, $WhiteSpaceZenkaku_UTL, '　')"/>
        </xsl:with-param>
      </xsl:call-template>
    </p>
  </xsl:template>
  <!--■<p class="MatchStart">を出力-->
  <xsl:template name="PTag_MatchClass_UTL">
    <xsl:param name="PTEXT"/>
    <xsl:param name="TateYoko" select="0"/>
    <xsl:choose>
      <xsl:when test="$TateYoko=1">
        <p class="MatchStart">
          <!-- spanタグ挿入処理 -->
          <xsl:call-template name="WritingModeYoko_UTL">
            <xsl:with-param name="BeforeData">
              <xsl:value-of select="translate($PTEXT, $WhiteSpaceZenkaku_UTL, '　')"/>
            </xsl:with-param>
          </xsl:call-template>
        </p>
      </xsl:when>
      <xsl:otherwise>
        <p class="MatchStart">
          <xsl:value-of select="translate($PTEXT, $WhiteSpaceZenkaku_UTL, '　')"/>
        </p>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--■<p class="OikomiStart">を出力-->
  <xsl:template name="PTag_OikomiClass_UTL">
    <xsl:param name="PTEXT"/>
    <xsl:param name="TateYoko" select="0"/>
    <xsl:choose>
      <xsl:when test="$TateYoko=1">
        <p class="OikomiStart">
          <!-- spanタグ挿入処理 -->
          <xsl:call-template name="WritingModeYoko_UTL">
            <xsl:with-param name="BeforeData">
              <xsl:value-of select="translate($PTEXT, $WhiteSpaceZenkaku_UTL, '　')"/>
            </xsl:with-param>
          </xsl:call-template>
        </p>
      </xsl:when>
      <xsl:otherwise>
        <p class="OikomiStart">
          <xsl:value-of select="translate($PTEXT, $WhiteSpaceZenkaku_UTL, '　')"/>
        </p>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!--縦書き内で個別の文字に横書きstyleを指定する（<span></span>使用）-->
  <!--※対象文字は$CharSetに定義 -->
  <!-- 【param】BeforeData ：処理対象文字列（一行分の文字列を想定） -->
  <!--===============================================================================================-->
  <xsl:template name="WritingModeYoko_UTL">
    <xsl:param name="BeforeData" select="''"/>
    <xsl:variable name="CharSet" select="'ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ½¼¾'"/>
    <xsl:choose>
      <xsl:when test="contains($BeforeData,'Ⅰ') 
                   or contains($BeforeData,'Ⅱ') 
                   or contains($BeforeData,'Ⅲ') 
                   or contains($BeforeData,'Ⅳ') 
                   or contains($BeforeData,'Ⅴ') 
                   or contains($BeforeData,'Ⅵ') 
                   or contains($BeforeData,'Ⅶ') 
                   or contains($BeforeData,'Ⅷ') 
                   or contains($BeforeData,'Ⅸ') 
                   or contains($BeforeData,'Ⅹ')
                   or contains($BeforeData,'½')
                   or contains($BeforeData,'¼')
                   or contains($BeforeData,'¾')">
        <xsl:variable name="CheckChar" select="substring($BeforeData,1,1)"/>
        <xsl:variable name="NextBeforeData" select="substring($BeforeData,2)"/>
        <xsl:choose>
          <xsl:when test="contains($CharSet,$CheckChar)">
            <span class="yoko">
              <xsl:value-of select="$CheckChar"/>
            </span>
            <xsl:call-template name="WritingModeYoko_UTL">
              <xsl:with-param name="BeforeData" select="$NextBeforeData"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$CheckChar"/>
            <xsl:call-template name="WritingModeYoko_UTL">
              <xsl:with-param name="BeforeData" select="$NextBeforeData"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$BeforeData"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!--縦書き内で個別の文字に横書きstyleを指定する（<span></span>使用）-->
  <!--★横書きレイアウトの本文を縦書き表示する場合に使用する★-->
  <!--※対象文字は$CharSetに定義 -->
  <!-- 【param】BeforeData ：処理対象文字列（一行分の文字列を想定） -->
  <!--===============================================================================================-->
  <xsl:template name="WritingModeTateYoko_UTL">
    <xsl:param name="BeforeData" select="''"/>
    <xsl:variable name="CharSet" select="'ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ½¼¾（）ー―ァィゥェォッャュョぁぃぅぇぉゃゅょ'"/>
    <xsl:choose>
      <xsl:when test="contains($BeforeData,'Ⅰ') 
                   or contains($BeforeData,'Ⅱ') 
                   or contains($BeforeData,'Ⅲ') 
                   or contains($BeforeData,'Ⅳ') 
                   or contains($BeforeData,'Ⅴ') 
                   or contains($BeforeData,'Ⅵ') 
                   or contains($BeforeData,'Ⅶ') 
                   or contains($BeforeData,'Ⅷ') 
                   or contains($BeforeData,'Ⅸ') 
                   or contains($BeforeData,'Ⅹ')
                   or contains($BeforeData,'½')
                   or contains($BeforeData,'¼')
                   or contains($BeforeData,'¾')
                   or contains($BeforeData,'（') 
                   or contains($BeforeData,'）') 
                   or contains($BeforeData,'ー') 
                   or contains($BeforeData,'―') 
                   or contains($BeforeData,'ァ') 
                   or contains($BeforeData,'ィ') 
                   or contains($BeforeData,'ゥ') 
                   or contains($BeforeData,'ェ') 
                   or contains($BeforeData,'ォ')
                   or contains($BeforeData,'ッ')
                   or contains($BeforeData,'ャ')
                   or contains($BeforeData,'ュ')
                   or contains($BeforeData,'ョ')
                   or contains($BeforeData,'ぁ')
                   or contains($BeforeData,'ぃ')
                   or contains($BeforeData,'ぅ')
                   or contains($BeforeData,'ぇ')
                   or contains($BeforeData,'ぉ')
                   or contains($BeforeData,'ゃ')
                   or contains($BeforeData,'ゅ')
                   or contains($BeforeData,'ょ') ">
        <xsl:variable name="CheckChar" select="substring($BeforeData,1,1)"/>
        <xsl:variable name="NextBeforeData" select="substring($BeforeData,2)"/>
        <xsl:choose>
          <xsl:when test="contains($CharSet,$CheckChar)">
            <span class="yoko">
              <xsl:value-of select="$CheckChar"/>
            </span>
            <xsl:call-template name="WritingModeTateYoko_UTL">
              <xsl:with-param name="BeforeData" select="$NextBeforeData"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$CheckChar"/>
            <xsl:call-template name="WritingModeTateYoko_UTL">
              <xsl:with-param name="BeforeData" select="$NextBeforeData"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$BeforeData"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!--指定数の全角スペースを出力-->
  <!-- 【param】count　：全角スペース出力個数 -->
  <!--===============================================================================================-->
  <xsl:template name="PrintSpaceZenkaku_UTL">
    <xsl:param name="count"/>
    <xsl:if test="$count > 0">
      <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$count - 1"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!--指定パスの要素から、最大長の文字数を取得-->
  <!-- 【param】TargetPath　：処理対象パス -->
  <!--===============================================================================================-->
  <xsl:template name="GetTagsMaxLength_UTL">
    <xsl:param name="TargetPath"/>
    <!-- 改行定数 -->
    <!--【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="LineFeed_UTL">
      <xsl:text>LF</xsl:text>
    </xsl:variable>
    <xsl:variable name="AllLines">
      <xsl:for-each select="$TargetPath">
        <xsl:value-of select="."/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:for-each>
    </xsl:variable>
    <xsl:choose>
      <xsl:when test="$AllLines!=''">
        <xsl:call-template name="Get_TextMaxLength_UTL">
          <xsl:with-param name="Data" select="$AllLines"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="0"/>
      </xsl:otherwise>
    </xsl:choose>
    <!--<xsl:choose>
      <xsl:when test="$TargetPath">
        <xsl:for-each select="$TargetPath">
          <xsl:sort select="string-length(.)" data-type="number" order="descending"/>
          <xsl:if test="position() = 1">
            <xsl:value-of select="string-length(.)"/>
          </xsl:if>
        </xsl:for-each>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="0"/>
      </xsl:otherwise>
    </xsl:choose>-->
  </xsl:template>
  <!--===============================================================================================-->
  <!--指定パスの要素から、最大長の文字列を取得-->
  <!-- 【param】TargetPath　：処理対象パス -->
  <!--===============================================================================================-->
  <xsl:template name="GetTagsMaxLengthStirng_UTL">
    <xsl:param name="TargetPath"/>
    <!-- 改行定数 -->
    <!--【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="LineFeed_UTL">
      <xsl:text>LF</xsl:text>
    </xsl:variable>
    <xsl:variable name="AllLines">
      <xsl:for-each select="$TargetPath">
        <xsl:value-of select="."/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:for-each>
    </xsl:variable>
    <xsl:choose>
      <xsl:when test="$AllLines!=''">
        <xsl:call-template name="Get_TextMaxLengthString_UTL">
          <xsl:with-param name="Data" select="$AllLines"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="''"/>
      </xsl:otherwise>
    </xsl:choose>
    <!--<xsl:choose>
      <xsl:when test="$TargetPath">
        <xsl:for-each select="$TargetPath">
          <xsl:sort select="string-length(.)" data-type="number" order="descending"/>
          <xsl:if test="position() = 1">
            <xsl:value-of select="."/>
          </xsl:if>
        </xsl:for-each>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="''"/>
      </xsl:otherwise>
    </xsl:choose>-->
  </xsl:template>
  <!--===============================================================================================-->
  <!--指定パスの数値要素から、最大の数値を取得-->
  <!-- 【param】TargetPath　：処理対象パス（要素が数値であることを想定） -->
  <!--===============================================================================================-->
  <xsl:template name="GetTagsMaxNum_UTL">
    <xsl:param name="TargetPath"/>
    <!-- 改行定数 -->
    <!--【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="LineFeed_UTL">
      <xsl:text>LF</xsl:text>
    </xsl:variable>
    <xsl:variable name="AllLines">
      <xsl:for-each select="$TargetPath">
        <xsl:value-of select="."/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:for-each>
    </xsl:variable>
    <xsl:choose>
      <xsl:when test="$AllLines!=''">
        <xsl:call-template name="Get_TagsMaxNumString_UTL">
          <xsl:with-param name="Data" select="$AllLines"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="0"/>
      </xsl:otherwise>
    </xsl:choose>
    <!--<xsl:for-each select="$TargetPath">
      <xsl:sort select="number(translate(.,'０１２３４５６７８９．','0123456789.'))" data-type="number" order="descending"/>
      <xsl:if test="position() = 1">
        <xsl:value-of select="number(translate(.,'０１２３４５６７８９．','0123456789.'))"/>
      </xsl:if>
    </xsl:for-each>-->
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 最大数値取得テンプレート -->
  <!-- 改行文字で区切られた複数の数値文字列の、最大を取得 -->
  <!-- （例）下記の文字列の場合「124」を返却 -->
  <!-- 『１LF２LF３LF１２３LF１２４LF０LF１２３LF１LF１２３LF』 -->
  <!-- 【param】Data：改行文字で区切られた文字列 -->
  <!-- 【param】Max ：最大数を保持(初回呼び出し時は0を設定) -->
  <!--=======================================================================================================-->
  <xsl:template name="Get_TagsMaxNumString_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="Max" select="0"/>
    <!-- 改行定数 -->
    <!--【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="LineFeed_UTL">
      <xsl:text>LF</xsl:text>
    </xsl:variable>
    <!--１つめの改行までの文字列-->
    <xsl:variable name="LfBefore">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$Data"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--残りの文字列-->
    <xsl:variable name="LfAfter">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
        </xsl:when>
        <xsl:otherwise>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--残りの文字列を数値化-->
    <xsl:variable name="LfBeforeNum">
      <xsl:value-of select="number(translate($LfBefore,'０１２３４５６７８９．','0123456789.'))"/>
    </xsl:variable>
    <!--これまでの最大長と比較し、長い方のlengthを取得-->
    <xsl:variable name="NewMax">
      <xsl:choose>
        <xsl:when test="$LfBeforeNum > $Max">
          <xsl:value-of select="$LfBeforeNum"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$Max"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:choose>
      <!--選手名が最後になるまで再帰呼び出し-->
      <xsl:when test="$LfAfter!='' and contains($LfAfter,$LineFeed_UTL)">
        <xsl:call-template name="Get_TagsMaxNumString_UTL">
          <xsl:with-param name="Data" select="$LfAfter"/>
          <xsl:with-param name="Max" select="$NewMax"/>
        </xsl:call-template>
      </xsl:when>
      <!--文字列が最後の場合は、最大を返却-->
      <xsl:otherwise>
        <xsl:value-of select="$NewMax"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!--全角数字を数値型に変換-->
  <!-- 【param】zenkakuNum　：全角数値文字列 -->
  <!--===============================================================================================-->
  <xsl:template name="TransrateNum_UTL">
    <xsl:param name="zenkakuNum"/>
    <xsl:value-of select="number(translate($zenkakuNum,'０１２３４５６７８９．','0123456789.'))"/>
  </xsl:template>
  <!--===============================================================================================-->
  <!--２つの数値を比較し、大きい数値を返却-->
  <!-- 【param】Num1　：比較対照数値１ -->
  <!-- 【param】Num2　：比較対照数値２ -->
  <!--===============================================================================================-->
  <xsl:template name="CompareNum_UTL">
    <xsl:param name="Num1"/>
    <xsl:param name="Num2"/>
    <xsl:choose>
      <xsl:when test="$Num1 > $Num2">
        <xsl:value-of select="$Num1"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$Num2"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!--ルーラーを出力-->
  <!--【param】LineBrake：改ページ行数定義-->
  <!--【param】CntBrake ：ルーラー表示最大数定義-->
  <!--【param】Cnt　　　：記事内のカウンタ(ルーラー表示を開始する数字)-->
  <!--【param】LCnt　　 ：ルーラー内のカウンタ(呼び出しは0を指定)-->
  <!--===============================================================================================-->
  <xsl:template name="LineRuler_UTL">
    <xsl:param name="LineBrake"/>
    <xsl:param name="CntBrake"/>
    <xsl:param name="Cnt"/>
    <xsl:param name="LCnt"/>
    <!--ルーラー出力処理-->
    <xsl:if test="($LineBrake - $LCnt) > 0">
      <!-- 行数表示する最大まで -->
      <xsl:if test="$CntBrake >= $Cnt">
        <xsl:call-template name="PTag_UTL">
          <xsl:with-param name="PTEXT">
            <xsl:choose>
              <xsl:when test="($Cnt mod 5)=0">
                <!--２桁以上の行数のとき末尾２桁のみ表示する-->
                <xsl:variable name="Cnt2Len" select="$Cnt mod 100"/>
                <xsl:call-template name="RensuuHenkan">
                  <xsl:with-param name="Sts" select="4"/>
                  <xsl:with-param name="Pdata" select="translate($Cnt mod 100,'0123456789','０１２３４５６７８９')"/>
                </xsl:call-template>
              </xsl:when>
              <xsl:otherwise>
                <xsl:text>・</xsl:text>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:with-param>
        </xsl:call-template>
      </xsl:if>
      <!--改行文字数分を出力するまで再帰呼び出し-->
      <xsl:call-template name="LineRuler_UTL">
        <xsl:with-param name="LineBrake" select="$LineBrake"/>
        <xsl:with-param name="CntBrake" select="$CntBrake"/>
        <xsl:with-param name="LCnt" select="$LCnt+1"/>
        <xsl:with-param name="Cnt" select="$Cnt+1"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!--ルーラーを出力（先頭に空白あり）-->
  <!--【param】LineBrake：改ページ行数定義-->
  <!--【param】CntBrake ：ルーラー表示最大数定義-->
  <!--【param】Cnt　　　：記事内のカウンタ(ルーラー表示を開始する数字)-->
  <!--【param】LCnt　　 ：ルーラー内のカウンタ(呼び出しは0を指定)-->
  <!--【param】PreSpace ：仮見出しを出力する場合に行数を指定(ルーラーを表示しないため) -->
  <!--===============================================================================================-->
  <xsl:template name="LineRulerPreSpace_UTL">
    <xsl:param name="LineBrake"/>
    <xsl:param name="CntBrake"/>
    <xsl:param name="Cnt"/>
    <xsl:param name="LCnt"/>
    <xsl:param name="PreSpace"/>
    <!--ルーラー出力処理-->
    <xsl:choose>
      <!--先頭を指定文字数分スペース埋め-->
      <xsl:when test="$PreSpace != '' and $PreSpace > 0">
        <xsl:call-template name="LineRulerSpace_UTL">
          <xsl:with-param name="LineBrake" select="$PreSpace"/>
          <xsl:with-param name="Cnt" select="0"/>
        </xsl:call-template>
        <!--空白をのぞいた分で通常のルーラー表示処理を呼び出し-->
        <xsl:call-template name="LineRuler_UTL">
          <xsl:with-param name="LineBrake" select="$LineBrake - $PreSpace"/>
          <xsl:with-param name="CntBrake" select="$CntBrake"/>
          <xsl:with-param name="LCnt" select="$LCnt"/>
          <xsl:with-param name="Cnt" select="$Cnt"/>
        </xsl:call-template>
      </xsl:when>
      <!--通常のルーラー表示処理を呼び出し-->
      <xsl:otherwise>
        <xsl:call-template name="LineRuler_UTL">
          <xsl:with-param name="LineBrake" select="$LineBrake"/>
          <xsl:with-param name="CntBrake" select="$CntBrake"/>
          <xsl:with-param name="LCnt" select="$LCnt"/>
          <xsl:with-param name="Cnt" select="$Cnt"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!--ルーラーに空白を出力-->
  <!--【param】LineBrake：スペース出力数-->
  <!--【param】LCnt　　 ：ルーラー内のカウンタ(呼び出しは0を指定)-->
  <!--===============================================================================================-->
  <xsl:template name="LineRulerSpace_UTL">
    <xsl:param name="LineBrake"/>
    <xsl:param name="Cnt"/>
    <!--ルーラー出力処理-->
    <xsl:if test="($LineBrake - $Cnt) > 0">
      <xsl:call-template name="PTag_UTL">
        <xsl:with-param name="PTEXT">
          <xsl:text>　</xsl:text>
        </xsl:with-param>
      </xsl:call-template>
      <!--文字数分を出力するまで再帰呼び出し-->
      <xsl:call-template name="LineRulerSpace_UTL">
        <xsl:with-param name="LineBrake" select="$LineBrake"/>
        <xsl:with-param name="Cnt" select="$Cnt+1"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Ｐタグ内整形処理　-->
  <!-- ★本テンプレートの結果をVariavleで取得し、KAKUNIN2_DIVS_UTLの引数に渡す★ -->
  <!-- 改行文字($LineFeed_UTL)、一行最大文字数を考慮した改行文字設定、改ページ文字設定、 -->
  <!-- 行数カウント を行う-->
  <!-- 【param】Data　　　　　　　：整形対象文字列 -->
  <!-- 【param】LINE_MAX_LENGTH 　：１行の折り返し最大文字数 -->
  <!-- 【param】LINE_COUNT　　　　：全体の行数カウント（呼び出し時は0を設定） -->
  <!-- 【param】PAGE_LINE_COUNT 　：処理中のページの行数カウント（呼び出し時は0を設定） -->
  <!-- 【param】PAGE_LINE_MAX　 　：１ページの最大行数定義 -->
  <!-- 【param】ADD_LINE_COUNT_FLG：行数カウント付加有無フラグ [0]なし、[1]文字列の末尾に行数カウントを追加-->
  <!-- 【param】TATEYOKO_FLG      ：縦横フラグ -->
  <!-- 【param】ADD_OIKOMI_CLASS_FLG ：OikomiStartクラス付加フラグ -->
  <!--===============================================================================================-->
  <xsl:template name="SplitTextForPTag_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="LINE_MAX_LENGTH"/>
    <xsl:param name="LINE_COUNT"/>
    <xsl:param name="PAGE_LINE_COUNT"/>
    <xsl:param name="PAGE_LINE_MAX"/>
    <xsl:param name="ADD_LINE_COUNT_FLG"/>
    <xsl:param name="TATEYOKO_FLG"/>
    <xsl:param name="ADD_OIKOMI_CLASS_FLG" select="0"/>
    <xsl:choose>
      <xsl:when test="($PAGE_LINE_COUNT=$PAGE_LINE_MAX) or (starts-with($Data,$PageBreak_UTL))">
        <xsl:value-of select="$PageBreak_UTL"/>
        <!--改ページ指定の場合は改ページを実施-->
        <xsl:variable name="Data_CutPB">
          <xsl:choose>
            <xsl:when test="starts-with($Data,$PageBreak_UTL)">
              <xsl:value-of select="substring-after($Data,$PageBreak_UTL)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$Data"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <!-- 再帰呼び出し -->
        <xsl:call-template name="SplitTextForPTag_UTL">
          <xsl:with-param name="Data" select="$Data_CutPB"/>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
          <xsl:with-param name="LINE_COUNT" select="$LINE_COUNT"/>
          <xsl:with-param name="PAGE_LINE_COUNT" select="0"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
          <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="$ADD_OIKOMI_CLASS_FLG"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:choose>
          <!--出力対象文字が''でない場合は処理を実施-->
          <xsl:when test="$Data!=''">
            <!-- 先頭のマッチスタート文字を除外 -->
            <xsl:variable name="Data_ExcludeMatchClass">
              <xsl:choose>
                <xsl:when test="starts-with($Data,$MatchClass_UTL)">
                  <xsl:value-of select="substring-after($Data,$MatchClass_UTL)"/>
                </xsl:when>
                <xsl:when test="starts-with($Data,$OikomiClass_UTL)">
                  <xsl:value-of select="substring-after($Data,$OikomiClass_UTL)"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="$Data"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:variable>
            <!--改行文字までの文字列を取得(マッチスタートclass設定を考慮)-->
            <xsl:variable name="Data_LineData">
              <xsl:choose>
                <xsl:when test="starts-with($Data_ExcludeMatchClass,$LineFeed_UTL)">
                  <xsl:text>　</xsl:text>
                </xsl:when>
                <xsl:when test="substring-before($Data_ExcludeMatchClass,$LineFeed_UTL)!= '' 
                                and $LINE_MAX_LENGTH >= string-length(substring-before($Data_ExcludeMatchClass,$LineFeed_UTL))">
                  <xsl:value-of select="substring-before($Data_ExcludeMatchClass,$LineFeed_UTL)"/>
                </xsl:when>
                <xsl:when test="string-length($Data_ExcludeMatchClass) > $LINE_MAX_LENGTH">
                  <xsl:value-of select="substring($Data_ExcludeMatchClass,1,$LINE_MAX_LENGTH)"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="$Data_ExcludeMatchClass"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:variable>
            <!-- 取り除いたマッチスタートを付加 -->
            <xsl:if test="starts-with($Data,$MatchClass_UTL)">
              <!-- マッチスタートを付加するか設定を確認 -->
              <xsl:if test="$ADD_MATCHSTART_CLASS_SET=3 or $ADD_MATCHSTART_CLASS_SET=$TATEYOKO_FLG">
                <xsl:value-of select="$MatchClass_UTL"/>
              </xsl:if>
            </xsl:if>
            <!-- 取り除いた追い込みスタートを付加 -->
            <xsl:if test="starts-with($Data,$OikomiClass_UTL)">
              <!-- 追い込みスタートを付加するか設定を確認 -->
              <xsl:if test="$ADD_OIKOMI_CLASS_SET=3 or $ADD_OIKOMI_CLASS_SET=$TATEYOKO_FLG">
                <xsl:value-of select="$OikomiClass_UTL"/>
              </xsl:if>
            </xsl:if>
            <!-- Ｐタグ１つ分の文字列を出力 -->
            <xsl:value-of select="$Data_LineData"/>
            <xsl:value-of select="$LineFeed_UTL"/>
            <!-- 出力済みの文字列の残り -->
            <xsl:variable name="Data_After">
              <xsl:choose>
                <xsl:when test="starts-with($Data,$LineFeed_UTL)">
                  <xsl:value-of select="$Data"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="substring-after($Data,$Data_LineData)"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:variable>
            <!-- 再帰呼び出し -->
            <xsl:call-template name="SplitTextForPTag_UTL">
              <xsl:with-param name="Data">
                <xsl:choose>
                  <xsl:when test="starts-with($Data_After, $LineFeed_UTL)">
                    <xsl:value-of select="substring-after($Data_After,$LineFeed_UTL)"/>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="$Data_After"/>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:with-param>
              <xsl:with-param name="LINE_COUNT" select="$LINE_COUNT +1"/>
              <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
              <xsl:with-param name="PAGE_LINE_COUNT" select="$PAGE_LINE_COUNT+1"/>
              <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
              <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG"/>
              <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
              <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="$ADD_OIKOMI_CLASS_FLG"/>
            </xsl:call-template>
          </xsl:when>
          <!-- 出力対象文字列が空の場合LINE_COUNTを出力 -->
          <xsl:otherwise>
            <!-- 出力有無フラグを確認 -->
            <xsl:if test="$ADD_LINE_COUNT_FLG=1">
              <!-- １ページ最大行数を超えた場合は改ページ -->
              <xsl:if test="$PAGE_LINE_COUNT+1 > $PAGE_LINE_MAX">
                <xsl:value-of select="$PageBreak_UTL"/>
              </xsl:if>
              <xsl:choose>
                <xsl:when test="$TATEYOKO_FLG=1">
                  <xsl:text>〈</xsl:text>
                </xsl:when>
                <xsl:when test="$TATEYOKO_FLG=2">
                  <xsl:text>＜</xsl:text>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="$LINE_COUNT > 99">
                  <xsl:value-of select="translate($LINE_COUNT,'0123456789','０１２３４５６７８９')"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:call-template name="RensuuHenkan">
                    <xsl:with-param name="Sts" select="3"/>
                    <xsl:with-param name="Pdata" select="translate($LINE_COUNT,'0123456789','０１２３４５６７８９')"/>
                  </xsl:call-template>
                </xsl:otherwise>
              </xsl:choose>
              <xsl:text>行</xsl:text>
              <xsl:choose>
                <xsl:when test="$TATEYOKO_FLG=1">
                  <xsl:text>〉</xsl:text>
                </xsl:when>
                <xsl:when test="$TATEYOKO_FLG=2">
                  <xsl:text>＞</xsl:text>
                </xsl:when>
              </xsl:choose>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:if>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Ｐタグ行数カウント（仮見出し出力共通処理にて使用）　-->
  <!-- 【param】Data　　　　　　　：整形対象文字列 -->
  <!-- 【param】LINE_MAX_LENGTH 　：１行の折り返し最大文字数 -->
  <!-- 【param】LINE_COUNT　　　　：全体の行数カウント（呼び出し時は0を設定） -->
  <!--===============================================================================================-->
  <xsl:template name="PTagCount_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="LINE_COUNT"/>
    <xsl:param name="LINE_MAX_LENGTH" select="0"/>
    <xsl:choose>
      <!--出力対象文字が''でない場合は処理を実施-->
      <xsl:when test="$Data!='' and $LINE_MAX_LENGTH > 0">
        <xsl:variable name="Data_After">
          <xsl:choose>
            <xsl:when test="starts-with($Data,$LineFeed_UTL)">
              <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:when test="substring-before($Data,$LineFeed_UTL)!= '' 
                                and $LINE_MAX_LENGTH >= string-length(substring-before($Data,$LineFeed_UTL))">
              <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:when test="string-length($Data) > $LINE_MAX_LENGTH">
              <xsl:value-of select="substring($Data,$LINE_MAX_LENGTH+1)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="''"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <!-- 再帰呼び出し -->
        <xsl:call-template name="PTagCount_UTL">
          <xsl:with-param name="Data" select="$Data_After"/>
          <xsl:with-param name="LINE_COUNT" select="$LINE_COUNT+1"/>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 出力対象文字列が空の場合LINE_COUNTを出力 -->
      <xsl:otherwise>
        <xsl:value-of select="$LINE_COUNT"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- Div生成 Div毎に再帰呼び出しを行う -->
  <!-- 【param】Data　　　 ：本文文字列（改ページ文字区切りでDivタグ,改行文字区切りでpタグに出力） -->
  <!-- 【param】DivCount　 ：Divタグが何番目のDivか(初回呼び出し時は0を設定) -->
  <!-- 【param】TateYoko　 ：縦書き[1]/横書き[2]/縦書きLONG[3](div毎に改ページ) 切り替え -->
  <!-- 【param】PageLineMax：ルーラー表示する桁数 -->
  <!-- 【param】PTateHeadLineLength：仮見出しを出力する場合に行数を指定(処理対象divのルーラー開始位置) -->
  <!-- 【param】PageBrakeFirstFlg  ：縦書きで、１つ目のdivの後に改ページするか -->
  <!-- 【param】RulerPTateHeadLineLength：ルーラーのカウント時に想定する仮見出しの行数 -->
  <!-- 【param】CntStart   ：出力対象Divのカウント開始 -->
  <!--=======================================================================================================-->
  <xsl:template name="KAKUNIN2_DIVS_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="DivCount"/>
    <xsl:param name="TateYoko"/>
    <xsl:param name="PageLineMax"/>
    <xsl:param name="PTateHeadLineLength"/>
    <xsl:param name="PageBrakeFirstFlg"/>
    <xsl:param name="RulerPTateHeadLineLength"/>
    <xsl:param name="CntStart" select="1"/>
    <xsl:if test="$Data!=''">
      <!--改ページ前を取得-->
      <xsl:variable name="PB_BEFORE">
        <xsl:choose>
          <xsl:when test="contains($Data,$PageBreak_UTL)">
            <xsl:value-of select="substring-before($Data,$PageBreak_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$Data"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!--改ページ後を取得-->
      <xsl:variable name="PB_AFTER">
        <xsl:choose>
          <xsl:when test="contains($Data,$PageBreak_UTL)">
            <xsl:value-of select="substring-after($Data,$PageBreak_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!-- 対象Divに出力する本文行数を取得 -->
      <xsl:variable name="PB_BEFORE_CNT">
        <!-- 出力行数を取得 -->
        <xsl:variable name="TempCnt">
          <xsl:choose>
            <xsl:when test="$PB_BEFORE!=''">
              <xsl:call-template name="Get_TextLineCount_UTL">
                <xsl:with-param name="Data" select="$PB_BEFORE"/>
              </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="0"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <xsl:choose>
          <!-- 縦書き１頁目の場合は仮見出し行数分をマイナス -->
          <xsl:when test="$PRINT_RULER_SET=1 and $PTateHeadLineLength != '' and $PTateHeadLineLength > 0">
            <xsl:value-of select="$TempCnt - $PTateHeadLineLength"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$TempCnt"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <xsl:if test="$PB_BEFORE!=''">
        <!-- Div１つを出力 -->
        <xsl:call-template name="KAKUNIN2_ONEDIV_UTL">
          <xsl:with-param name="Data" select="$PB_BEFORE"/>
          <xsl:with-param name="LulerMaxCount" select="$PageLineMax"/>
          <xsl:with-param name="DivCount" select="$DivCount"/>
          <xsl:with-param name="TateYoko" select="$TateYoko"/>
          <xsl:with-param name="PTateHeadLineLength" select="$PTateHeadLineLength"/>
          <xsl:with-param name="RulerPTateHeadLineLength" select="$RulerPTateHeadLineLength"/>
          <xsl:with-param name="PageBrakeFirstFlg" select="$PageBrakeFirstFlg"/>
          <xsl:with-param name="CntStart" select="$CntStart"/>
          <xsl:with-param name="CntBrake" select="$CntStart + $PB_BEFORE_CNT - 1"/>
        </xsl:call-template>
      </xsl:if>
      <xsl:if test="$PB_AFTER!=''">
        <!--  再帰呼び出し -->
        <xsl:call-template name="KAKUNIN2_DIVS_UTL">
          <xsl:with-param name="Data" select="$PB_AFTER"/>
          <xsl:with-param name="DivCount" select="$DivCount+1"/>
          <xsl:with-param name="TateYoko" select="$TateYoko"/>
          <xsl:with-param name="PageLineMax" select="$PageLineMax"/>
          <xsl:with-param name="PTateHeadLineLength" select="0"/>
          <xsl:with-param name="RulerPTateHeadLineLength" select="$RulerPTateHeadLineLength"/>
          <xsl:with-param name="PageBrakeFirstFlg" select="$PageBrakeFirstFlg"/>
          <xsl:with-param name="CntStart" select="$CntStart + $PB_BEFORE_CNT"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- Div出力 -->
  <!-- ルーラー表示ありの場合、ルーラーを出力する -->
  <!-- １ページにDivを２つ出力する用にPageBreakを行う -->
  <!-- 【param】Data　　　　 ：Divタグ１つに出力する文字列（改行文字区切りでPタグに分割します） -->
  <!-- 【param】LulerMaxCount：ルーラー表示の最大値(半角数値) -->
  <!-- 【param】DivCount　　 ：Divタグが何番目のDivか(半角数値) -->
  <!-- 【param】TateYoko　　 ：縦書き[1]/横書き[2]/縦書きLONG[3](div毎に改ページ)　切り替え -->
  <!-- 【param】PTateHeadLineLength：仮見出しを出力する場合に行数を指定(ルーラーを表示しないため) -->
  <!-- 【param】RulerPTateHeadLineLength：ルーラーのカウント時に想定する仮見出しの行数 -->
  <!-- 【param】PageBrakeFirstFlg  ：縦書きで、１つ目のdivの後に改ページするか -->
  <!-- 【param】CntStart   ：出力対象Divのカウント開始 -->
  <!-- 【param】CntBrake   ：出力対象Divのカウント終了 -->
  <!--=======================================================================================================-->
  <xsl:template name="KAKUNIN2_ONEDIV_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="LulerMaxCount"/>
    <xsl:param name="DivCount"/>
    <xsl:param name="TateYoko"/>
    <xsl:param name="PTateHeadLineLength"/>
    <xsl:param name="RulerPTateHeadLineLength"/>
    <xsl:param name="PageBrakeFirstFlg"/>
    <xsl:param name="CntStart"/>
    <xsl:param name="CntBrake"/>
    <!-- 内容情報部行数を取得 -->
    <xsl:variable name="NAIYOU_LINE_SET">
      <xsl:call-template name="NAIYOU_LINE_SET"/>
    </xsl:variable>
    <!-- １ページにDivを２つ出力する用にPageBreakを行う -->
    <!--
    <xsl:if test="$DivCount mod 2 = 1">
      <div class="pageBreak"><p>　</p></div>
    </xsl:if>
-->
    <xsl:choose>
      <!--横書き-->
      <xsl:when test="$TateYoko=2">
        <xsl:if test="$DivCount!=0">
          <div class="pageBreak"><p>　</p></div>
        </xsl:if>
        <div class="ptextYOKO">
          <xsl:call-template name="PRINT_P_UTL">
            <xsl:with-param name="Data" select="$Data"/>
          </xsl:call-template>
        </div>
      </xsl:when>
      <!--縦書き-->
      <xsl:otherwise>
        <xsl:choose>
          <!-- １ページにDivを１つ出力する用にPageBreakを行う -->
          <!--<xsl:when test="($TateYoko=3) and ($DivCount!=0) ">-->
          <!-- 内容情報部が長い場合は最初のページも改ページする -->
          <!--<xsl:when test="($TateYoko=3) and ($DivCount!=0 or ($DivCount=0 and $NAIYOU_LINE_SET > 12)) ">-->
          <!-- Ａ４横印刷時 -->
          <xsl:when test="($TateYoko=3) and ($DivCount!=0 or ($PRINT_F_SET=2 and $DivCount=0 and $NAIYOU_LINE_SET > 12)) ">
            <div class="pageBreak"><p>　</p></div>
            <!-- <br/>はIE8印刷不具合用に設定 -->
            <br/>
          </xsl:when>
          <!-- Ａ４縦印刷時 -->
          <xsl:when test="($TateYoko=3) and ($DivCount!=0 or ($PRINT_F_SET=1 and $DivCount=0 and $NAIYOU_LINE_SET > 32)) ">
            <div class="pageBreak"><p>　</p></div>
            <!-- <br/>はIE8印刷不具合用に設定 -->
            <br/>
          </xsl:when>
          <!-- １ページにDivを２つ（印刷方向による１頁目div数を考慮しない） -->
          <xsl:when test="$PageBrakeFirstFlg=1">
            <xsl:if test="($DivCount!=0) and ($DivCount mod 2 = 0)">
              <div class="pageBreak"><p>　</p></div>
              <br/>
            </xsl:if>
          </xsl:when>
          <!-- １ページにDivを２つ -->
          <xsl:when test="($PRINT_F_SET=1) and ($DivCount!=0) and ($DivCount mod 2 = 0)">
            <div class="pageBreak"><p>　</p></div>
            <br/>
          </xsl:when>
          <!-- １ページにDivを２つ(A4縦印刷は１頁目のみ１つ) -->
          <xsl:when test="($PRINT_F_SET=2) and ($DivCount mod 2 = 1)">
            <div class="pageBreak"><p>　</p></div>
            <br/>
          </xsl:when>
        </xsl:choose>
        <!-- ルーラー表示 -->
        <xsl:choose>
          <xsl:when test="$PRINT_RULER_SET=1 and $PTateHeadLineLength != '' and $PTateHeadLineLength > 0">
            <div class="pTATERuler">
              <xsl:call-template name="LineRulerPreSpace_UTL">
                <xsl:with-param name="LineBrake" select="$LulerMaxCount"/>
                <xsl:with-param name="CntBrake" select="$CntBrake"/>
                <!--<xsl:with-param name="Cnt" select="1"/>-->
                <xsl:with-param name="Cnt" select="$CntStart"/>
                <xsl:with-param name="LCnt" select="0"/>
                <xsl:with-param name="PreSpace" select="$PTateHeadLineLength"/>
              </xsl:call-template>
            </div>
          </xsl:when>
          <xsl:when test="$PRINT_RULER_SET=1">
            <div class="pTATERuler">
              <xsl:call-template name="LineRuler_UTL">
                <xsl:with-param name="LineBrake" select="$LulerMaxCount"/>
                <xsl:with-param name="CntBrake" select="$CntBrake"/>
                <!--<xsl:with-param name="Cnt" select="1"/>-->
                <!--<xsl:with-param name="Cnt" select="($LulerMaxCount * $DivCount) - $RulerPTateHeadLineLength + 1"/>-->
                <xsl:with-param name="Cnt" select="$CntStart"/>
                <xsl:with-param name="LCnt" select="0"/>
              </xsl:call-template>
            </div>
          </xsl:when>
        </xsl:choose>
        <!-- 本文表示 -->
        <xsl:choose>
          <xsl:when test="$TateYoko=3">
            <div class="ptextTATELONG">
              <xsl:call-template name="PRINT_P_UTL">
                <xsl:with-param name="Data" select="$Data"/>
                <xsl:with-param name="TateYoko" select="1"/>
              </xsl:call-template>
            </div>
          </xsl:when>
          <xsl:otherwise>
            <div class="ptextTATE">
              <xsl:call-template name="PRINT_P_UTL">
                <xsl:with-param name="Data" select="$Data"/>
                <xsl:with-param name="TateYoko" select="1"/>
              </xsl:call-template>
            </div>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- Div出力 -->
  <!-- 横書き・縦書き混在記事用 -->
  <!-- （ルーラーは出力しない） -->
  <!-- 【param】Data　　　　   ：Divタグに出力する文字列 -->
  <!-- 【param】DivCount       ：処理中のDivの数のカウンター -->
  <!-- 【param】TateContainsFlg：縦書き部編集中のフラグ -->
  <!-- 【param】DivModNum      ：１頁目表示div数の指定 -->
  <!--=======================================================================================================-->
  <xsl:template name="KAKUNIN2_DIVS_YOKOTATE_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="DivCount" select="0"/>
    <xsl:param name="TateContainsFlg" select="0"/>
    <xsl:param name="DivModNum"/>
    <xsl:if test="$Data!=''">
      <!--改ページ前を取得-->
      <xsl:variable name="PB_BEFORE">
        <xsl:choose>
          <xsl:when test="contains($Data,$PageBreak_UTL)">
            <xsl:value-of select="substring-before($Data,$PageBreak_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$Data"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!--改ページ後を取得-->
      <xsl:variable name="PB_AFTER">
        <xsl:choose>
          <xsl:when test="contains($Data,$PageBreak_UTL)">
            <xsl:value-of select="substring-after($Data,$PageBreak_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <xsl:if test="$PB_BEFORE!=''">
        <xsl:choose>
          <xsl:when test="contains($PB_BEFORE,$YOKOTATEBreak_UTL) or $TateContainsFlg=1">
            <!-- 縦書き用(Div間に間隔あり)Divを出力 -->
            <xsl:call-template name="KAKUNIN2_ONEDIV_YOKOTATE_TATE_UTL">
              <xsl:with-param name="Data" select="$PB_BEFORE"/>
              <xsl:with-param name="DivCount" select="$DivCount"/>
              <xsl:with-param name="TateContainsFlg" select="$TateContainsFlg"/>
              <xsl:with-param name="DivModNum" select="$DivModNum"/>
            </xsl:call-template>
            <xsl:if test="$PB_AFTER!=''">
              <!--  再帰呼び出し -->
              <xsl:call-template name="KAKUNIN2_DIVS_YOKOTATE_UTL">
                <xsl:with-param name="Data" select="$PB_AFTER"/>
                <xsl:with-param name="DivCount" select="$DivCount + 1"/>
                <xsl:with-param name="TateContainsFlg" select="1"/>
                <xsl:with-param name="DivModNum" select="$DivModNum"/>
              </xsl:call-template>
            </xsl:if>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き用(Div間に間隔なし)Divを出力 -->
            <xsl:call-template name="KAKUNIN2_ONEDIV_YOKOTATE_YOKO_UTL">
              <xsl:with-param name="Data" select="$PB_BEFORE"/>
              <xsl:with-param name="DivCount" select="$DivCount"/>
              <xsl:with-param name="TateContainsFlg" select="$TateContainsFlg"/>
              <xsl:with-param name="DivModNum" select="$DivModNum"/>
            </xsl:call-template>
            <xsl:if test="$PB_AFTER!=''">
              <!--  再帰呼び出し -->
              <xsl:call-template name="KAKUNIN2_DIVS_YOKOTATE_UTL">
                <xsl:with-param name="Data" select="$PB_AFTER"/>
                <xsl:with-param name="DivCount" select="$DivCount + 1"/>
                <xsl:with-param name="TateContainsFlg" select="0"/>
                <xsl:with-param name="DivModNum" select="$DivModNum"/>
              </xsl:call-template>
            </xsl:if>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:if>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Div出力（横書き・縦書き混在記事）内部処理　横書き部表示-->
  <!--===============================================================================================-->
  <xsl:template name="KAKUNIN2_ONEDIV_YOKOTATE_YOKO_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="DivCount"/>
    <xsl:param name="TateContainsFlg"/>
    <xsl:param name="DivModNum"/>
    <!-- 特定ページ単位で改行を挿入 -->
    <xsl:choose>
      <!--Ａ４縦：１ページにDivを３つ -->
      <xsl:when test="($PRINT_F_SET=1) and ($DivCount!=0) and ($DivCount mod 3 = $DivModNum)">
        <div class="pageBreak"><p>　</p></div>
        <br/>
      </xsl:when>
      <!-- Ａ４縦：１ページにDivを２つ -->
      <xsl:when test="($PRINT_F_SET=2) and ($DivCount!=0) and ($DivCount mod 2 = $DivModNum)">
        <div class="pageBreak"><p>　</p></div>
        <br/>
      </xsl:when>
    </xsl:choose>
    <!-- 本文表示 -->
    <div class="ptextYOKOTATE">
      <xsl:call-template name="PRINT_P_TATEYOKO_UTL">
        <xsl:with-param name="Data" select="$Data"/>
        <xsl:with-param name="TateContainsFlg" select="$TateContainsFlg"/>
      </xsl:call-template>
    </div>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Div出力（横書き・縦書き混在記事）内部処理　縦書き部表示-->
  <!--===============================================================================================-->
  <xsl:template name="KAKUNIN2_ONEDIV_YOKOTATE_TATE_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="DivCount"/>
    <xsl:param name="TateContainsFlg"/>
    <xsl:param name="DivModNum"/>
    <!-- 特定ページ単位で改行を挿入 -->
    <xsl:choose>
      <!--Ａ４縦：１ページにDivを３つ -->
      <xsl:when test="($PRINT_F_SET=1) and ($DivCount!=0) and ($DivCount mod 3 = $DivModNum)">
        <div class="pageBreak"><p>　</p></div>
        <br/>
      </xsl:when>
      <!-- Ａ４縦：１ページにDivを２つ -->
      <xsl:when test="($PRINT_F_SET=2) and ($DivCount!=0) and ($DivCount mod 2 = $DivModNum)">
        <div class="pageBreak"><p>　</p></div>
        <br/>
      </xsl:when>
    </xsl:choose>
    <div class="ptextTATE">
      <xsl:call-template name="PRINT_P_TATEYOKO_UTL">
        <xsl:with-param name="Data" select="$Data"/>
        <xsl:with-param name="TateContainsFlg" select="$TateContainsFlg"/>
      </xsl:call-template>
    </div>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- 強制改ページ -->
  <!-- 【param】TateYoko：縦書き[1]/横書き[2] -->
  <!--===============================================================================================-->
  <xsl:template name="KAKUNIN2_PRINT_PAGEBRAKE_DIV_UTL">
    <xsl:param name="TateYoko"/>
    <div class="pageBreak"><p>　</p></div>
    <xsl:if test="$TateYoko=1">
      <br/>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!--改行文字($LineFeed_UTL)区切りでpタグ出力-->
  <!-- ★改ページ処理は含まない。１つのDivタグの中に出力することを想定。★ -->
  <!-- 【param】Data ：出力対象文字列 -->
  <!-- 【param】TateYoko ：縦書き[1]/横書き[2] -->
  <!--===============================================================================================-->
  <xsl:template name="PRINT_P_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="TateYoko"/>
    <!--出力対象文字が''でない場合は処理を実施-->
    <xsl:if test="$Data!=''">
      <!--改行文字までの文字列を取得-->
      <xsl:variable name="Data_LineData">
        <xsl:choose>
          <xsl:when test="starts-with($Data,$LineFeed_UTL)">
            <xsl:text>　</xsl:text>
          </xsl:when>
          <xsl:when test="contains($Data,$LineFeed_UTL)">
            <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$Data"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!-- プレーンテキストをＰタグ出力 -->
      <!-- マッチクラスclass設定を考慮 -->
      <!--
      <xsl:call-template name="PTag_UTL">
        <xsl:with-param name="PTEXT">
          <xsl:value-of select="$Data_LineData"/>
        </xsl:with-param>
      </xsl:call-template>
      -->
      <xsl:choose>
        <xsl:when test="starts-with($Data_LineData,$MatchClass_UTL)">
          <xsl:call-template name="PTag_MatchClass_UTL">
            <xsl:with-param name="PTEXT">
              <xsl:value-of select="substring-after($Data_LineData,$MatchClass_UTL)"/>
            </xsl:with-param>
            <xsl:with-param name="TateYoko" select="$TateYoko"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:when test="starts-with($Data_LineData,$OikomiClass_UTL)">
          <xsl:call-template name="PTag_OikomiClass_UTL">
            <xsl:with-param name="PTEXT">
              <xsl:value-of select="substring-after($Data_LineData,$OikomiClass_UTL)"/>
            </xsl:with-param>
            <xsl:with-param name="TateYoko" select="$TateYoko"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:call-template name="PTag_UTL">
            <xsl:with-param name="PTEXT">
              <xsl:value-of select="$Data_LineData"/>
            </xsl:with-param>
            <xsl:with-param name="TateYoko" select="$TateYoko"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 出力済みの文字列の残りが存在する場合は再帰呼び出し -->
      <xsl:if test="contains($Data,$LineFeed_UTL)">
        <xsl:variable name="Data_After">
          <xsl:choose>
            <xsl:when test="starts-with($Data,$LineFeed_UTL)">
              <xsl:value-of select="$Data"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="substring-after($Data,$Data_LineData)"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <!-- 再帰呼び出し -->
        <xsl:call-template name="PRINT_P_UTL">
          <xsl:with-param name="Data">
            <xsl:choose>
              <xsl:when test="starts-with($Data_After, $LineFeed_UTL)">
                <xsl:value-of select="substring-after($Data_After,$LineFeed_UTL)"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="$Data_After"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:with-param>
          <xsl:with-param name="TateYoko" select="$TateYoko"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!--改行文字($LineFeed_UTL)区切りでpタグ出力-->
  <!-- ★縦書き横書き混在記事用★ -->
  <!-- 【param】Data ：出力対象文字列 -->
  <!-- 【param】TateContainsFlg ：縦書きを含むDivかどうか -->
  <!--===============================================================================================-->
  <xsl:template name="PRINT_P_TATEYOKO_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="TateContainsFlg"/>
    <!--出力対象文字が''でない場合は処理を実施-->
    <xsl:if test="$Data!=''">
      <!--改行文字までの文字列を取得-->
      <xsl:variable name="Data_LineData">
        <xsl:choose>
          <xsl:when test="starts-with($Data,$LineFeed_UTL)">
            <xsl:text>　</xsl:text>
          </xsl:when>
          <xsl:when test="contains($Data,$LineFeed_UTL)">
            <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$Data"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!-- プレーンテキストをＰタグ出力 -->
      <!-- マッチクラスclass設定、縦書き横書き混在記事を考慮 -->
      <xsl:choose>
        <xsl:when test="$TateContainsFlg=0">
          <xsl:call-template name="PTag_TATEYOKO_UTL">
            <xsl:with-param name="PTEXT">
              <xsl:value-of select="$Data_LineData"/>
            </xsl:with-param>
          </xsl:call-template>
        </xsl:when>
        <xsl:when test="starts-with($Data_LineData,$MatchClass_UTL)">
          <xsl:call-template name="PTag_MatchClass_UTL">
            <xsl:with-param name="PTEXT">
              <xsl:value-of select="substring-after($Data_LineData,$MatchClass_UTL)"/>
            </xsl:with-param>
            <xsl:with-param name="TateYoko" select="1"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:when test="starts-with($Data_LineData,$OikomiClass_UTL)">
          <xsl:call-template name="PTag_OikomiClass_UTL">
            <xsl:with-param name="PTEXT">
              <xsl:value-of select="substring-after($Data_LineData,$OikomiClass_UTL)"/>
            </xsl:with-param>
            <xsl:with-param name="TateYoko" select="1"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:call-template name="PTag_UTL">
            <xsl:with-param name="PTEXT">
              <xsl:value-of select="$Data_LineData"/>
            </xsl:with-param>
            <xsl:with-param name="TateYoko" select="1"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 出力済みの文字列の残りが存在する場合は再帰呼び出し -->
      <xsl:if test="contains($Data,$LineFeed_UTL)">
        <xsl:variable name="Data_After">
          <xsl:choose>
            <xsl:when test="starts-with($Data,$LineFeed_UTL)">
              <xsl:value-of select="$Data"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="substring-after($Data,$Data_LineData)"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <!-- 再帰呼び出し -->
        <xsl:choose>
          <xsl:when test="$TateContainsFlg=1 
                       or starts-with($Data_After,$YOKOTATEBreak_UTL)
                       or starts-with($Data_After,concat($LineFeed_UTL,$YOKOTATEBreak_UTL))">
            <xsl:call-template name="PRINT_P_UTL">
              <xsl:with-param name="Data">
                <xsl:choose>
                  <xsl:when test="starts-with($Data_After, concat($LineFeed_UTL,$YOKOTATEBreak_UTL))">
                    <xsl:value-of select="substring-after($Data_After,concat($LineFeed_UTL,$YOKOTATEBreak_UTL))"/>
                  </xsl:when>
                  <xsl:when test="starts-with($Data_After, $LineFeed_UTL)">
                    <xsl:value-of select="substring-after($Data_After,$LineFeed_UTL)"/>
                  </xsl:when>
                  <xsl:when test="starts-with($Data_After, $YOKOTATEBreak_UTL)">
                    <xsl:value-of select="substring-after($Data_After,$YOKOTATEBreak_UTL)"/>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="$Data_After"/>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:with-param>
              <xsl:with-param name="TateYoko" select="1"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <xsl:call-template name="PRINT_P_TATEYOKO_UTL">
              <xsl:with-param name="Data">
                <xsl:choose>
                  <xsl:when test="starts-with($Data_After, $LineFeed_UTL)">
                    <xsl:value-of select="substring-after($Data_After,$LineFeed_UTL)"/>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="$Data_After"/>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:with-param>
              <xsl:with-param name="TateContainsFlg" select="$TateContainsFlg"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:if>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Ｐタグ内整形処理とDiv生成処理をまとめて実施する　-->
  <!-- SplitTextForPTag_UTLとKAKUNIN2_DIVS_UTLを呼び出す。　-->
  <!-- 本文要素を『本文』と『字解』を別で受け取り、　-->
  <!-- 『本文』に対してのみフラグに応じた文字カウント処理を実施する　-->
  <!-- 【param】HONBUN_DATA     　：本文文字列（文字カウント対象） -->
  <!-- 【param】JIKAI_DATA　　　　：字解文字列（文字カウント対象外）-->
  <!-- 【param】LINE_MAX_LENGTH 　：１行の折り返し最大文字数 -->
  <!-- 【param】PAGE_LINE_MAX　 　：１ページの最大行数定義 -->
  <!-- 【param】ADD_LINE_COUNT_FLG：行数カウント付加有無フラグ [0]なし、[1]文字列の末尾に行数カウントを追加 -->
  <!-- 【param】TATEYOKO_FLG　　　：縦書き[1]/横書き[2]切り替え -->
  <!-- 【param】ADD_OIKOMI_CLASS_FLG ：OikomiStartクラス付加フラグ -->
  <!--===============================================================================================-->
  <xsl:template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
    <xsl:param name="HONBUN_DATA"/>
    <xsl:param name="JIKAI_DATA"/>
    <xsl:param name="LINE_MAX_LENGTH"/>
    <xsl:param name="PAGE_LINE_MAX"/>
    <xsl:param name="ADD_LINE_COUNT_FLG"/>
    <xsl:param name="TATEYOKO_FLG"/>
    <xsl:param name="ADD_OIKOMI_CLASS_FLG" select="0"/>
    <!-- 内容情報部行数を取得 -->
    <xsl:variable name="NAIYOU_LINE_SET">
      <xsl:call-template name="NAIYOU_LINE_SET"/>
    </xsl:variable>
    <!-- 仮見出しを取得　-->
    <xsl:variable name="PTate_HeadLine">
      <xsl:call-template name="PTateHeadLine_EDT"/>
    </xsl:variable>
    <!-- 仮見出しの行数を取得　-->
    <xsl:variable name="PTate_HeadLineCount">
      <xsl:call-template name="PTagCount_UTL">
        <xsl:with-param name="Data" select="$PTate_HeadLine"/>
        <xsl:with-param name="LINE_COUNT" select="0"/>
        <xsl:with-param name="LINE_MAX_LENGTH">
          <xsl:value-of select="$LINE_MAX_LENGTH"/>
        </xsl:with-param>
      </xsl:call-template>
    </xsl:variable>
    <!-- 本文文字列にclass="OikomiStart"用の定数を付加する -->
    <xsl:variable name="HONBUN_DATA_CLASS">
      <xsl:choose>
        <xsl:when test="$ADD_OIKOMI_CLASS_FLG=1">
          <xsl:call-template name="SetOikomiClass_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$HONBUN_DATA"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="P_DATA_TEMP">
      <xsl:choose>
        <xsl:when test="$ADD_LINE_COUNT_FLG=1">
          <!-- 行数カウントのために整形処理を呼び出す -->
          <xsl:call-template name="SplitTextForPTag_UTL">
            <xsl:with-param name="Data">
              <xsl:if test="$TATEYOKO_FLG=1">
                <xsl:value-of select="$PTate_HeadLine"/>
              </xsl:if>
              <xsl:value-of select="$HONBUN_DATA_CLASS"/>
            </xsl:with-param>
            <xsl:with-param name="LINE_COUNT">
              <xsl:choose>
                <xsl:when test="$TATEYOKO_FLG=1">
                  <!-- 仮見出しの行数分マイナスした数値から合計行数カウント開始 -->
                  <xsl:value-of select="0 - $PTate_HeadLineCount"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="0"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:with-param>
            <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
            <xsl:with-param name="PAGE_LINE_COUNT">
              <xsl:choose>
                <xsl:when test="$NAIYOU_F_SET=1 and $TATEYOKO_FLG=2">
                  <!-- 内容情報部あり、かつ横書きの場合 -->
                  <!-- 内容情報部の分だけ１ページ目の行数を減らす -->
                  <xsl:value-of select="$NAIYOU_LINE_SET"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="0"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:with-param>
            <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
            <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG"/>
            <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
            <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="$ADD_OIKOMI_CLASS_FLG"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <!-- 行数カウント非表示の場合、行数カウント表示のための整形処理は不要 -->
          <xsl:if test="$TATEYOKO_FLG=1">
            <xsl:value-of select="$PTate_HeadLine"/>
          </xsl:if>
          <!--<xsl:value-of select="$HONBUN_DATA"/>-->
          <!-- 本文末の改行文字の有無を統一 -->
          <xsl:call-template name="DeleteEndDelimiter_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA_CLASS"/>
            <xsl:with-param name="Delimiter" select="$LineFeed_UTL"/>
          </xsl:call-template>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 改行 -->
      <xsl:if test="$JIKAI_DATA!=''">
        <xsl:value-of select="$LineFeed_UTL"/>
        <!-- 字解情報 -->
        <xsl:value-of select="$JIKAI_DATA"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="P_DATA">
      <!-- 行数カウント以降を含めたの全文字列のために整形処理を呼び出す -->
      <xsl:call-template name="SplitTextForPTag_UTL">
        <xsl:with-param name="Data" select="$P_DATA_TEMP"/>
        <xsl:with-param name="LINE_COUNT">
          <xsl:choose>
            <xsl:when test="$TATEYOKO_FLG=1">
              <!-- 仮見出しの行数分マイナスした数値から合計行数カウント開始 -->
              <xsl:value-of select="0 - $PTate_HeadLineCount"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="0"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
        <xsl:with-param name="PAGE_LINE_COUNT">
          <xsl:choose>
            <xsl:when test="$NAIYOU_F_SET=1 and $TATEYOKO_FLG=2">
              <!-- 内容情報部あり、かつ横書きの場合 -->
              <!-- 内容情報部の分だけ１ページ目の行数を減らす -->
              <xsl:value-of select="$NAIYOU_LINE_SET"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="0"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
        <xsl:with-param name="ADD_LINE_COUNT_FLG" select="0"/>
        <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- タグを生成して出力 -->
    <xsl:call-template name="KAKUNIN2_DIVS_UTL">
      <xsl:with-param name="Data" select="$P_DATA"/>
      <xsl:with-param name="DivCount" select="0"/>
      <xsl:with-param name="TateYoko" select="$TATEYOKO_FLG"/>
      <xsl:with-param name="PageLineMax" select="$PAGE_LINE_MAX"/>
      <xsl:with-param name="PTateHeadLineLength" select="$PTate_HeadLineCount"/>
      <xsl:with-param name="RulerPTateHeadLineLength" select="$PTate_HeadLineCount"/>
      <xsl:with-param name="PageBrakeFirstFlg" select="0"/>
    </xsl:call-template>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Ｐタグ内整形処理とDiv生成処理をまとめて実施する　-->
  <!-- SplitTextForPTag_UTLとKAKUNIN2_DIVS_UTLを呼び出す。　-->
  <!-- 本文要素を『本文』と『字解』を別で受け取り、　-->
  <!-- 『本文』に対してのみフラグに応じた文字カウント処理を実施する　-->
  <!-- ★１頁目以降の処理で使用。仮見出し出力処理を実施しない★　-->
  <!-- 【param】HONBUN_DATA     　：本文文字列（文字カウント対象） -->
  <!-- 【param】JIKAI_DATA　　　　：字解文字列（文字カウント対象外）-->
  <!-- 【param】LINE_MAX_LENGTH 　：１行の折り返し最大文字数 -->
  <!-- 【param】PAGE_LINE_MAX　 　：１ページの最大行数定義 -->
  <!-- 【param】ADD_LINE_COUNT_FLG：行数カウント付加有無フラグ [0]なし、[1]文字列の末尾に行数カウントを追加 -->
  <!-- 【param】TATEYOKO_FLG　　　：縦書き[1]/横書き[2]切り替え -->
  <!-- 【param】ADD_OIKOMI_CLASS_FLG ：OikomiStartクラス付加フラグ -->
  <!--===============================================================================================-->
  <xsl:template name="KAKUNIN2_DIVS_NO_PTateHeadLine_UTL">
    <xsl:param name="HONBUN_DATA"/>
    <xsl:param name="JIKAI_DATA"/>
    <xsl:param name="LINE_MAX_LENGTH"/>
    <xsl:param name="PAGE_LINE_MAX"/>
    <xsl:param name="ADD_LINE_COUNT_FLG"/>
    <xsl:param name="TATEYOKO_FLG"/>
    <xsl:param name="ADD_OIKOMI_CLASS_FLG" select="0"/>
    <!-- 本文文字列にclass="OikomiStart"用の定数を付加する -->
    <xsl:variable name="HONBUN_DATA_CLASS">
      <xsl:choose>
        <xsl:when test="$ADD_OIKOMI_CLASS_FLG=1">
          <xsl:call-template name="SetOikomiClass_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$HONBUN_DATA"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="P_DATA_TEMP">
      <xsl:choose>
        <xsl:when test="$ADD_LINE_COUNT_FLG=1">
          <!-- 行数カウントのために整形処理を呼び出す -->
          <xsl:call-template name="SplitTextForPTag_UTL">
            <xsl:with-param name="Data">
              <xsl:value-of select="$HONBUN_DATA_CLASS"/>
            </xsl:with-param>
            <xsl:with-param name="LINE_COUNT" select="0"/>
            <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
            <xsl:with-param name="PAGE_LINE_COUNT" select="0"/>
            <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
            <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG"/>
            <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
            <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="$ADD_OIKOMI_CLASS_FLG"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <!-- 本文末の改行文字の有無を統一 -->
          <xsl:call-template name="DeleteEndDelimiter_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA_CLASS"/>
            <xsl:with-param name="Delimiter" select="$LineFeed_UTL"/>
          </xsl:call-template>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 改行 -->
      <xsl:if test="$JIKAI_DATA!=''">
        <xsl:value-of select="$LineFeed_UTL"/>
        <!-- 字解情報 -->
        <xsl:value-of select="$JIKAI_DATA"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="P_DATA">
      <!-- 行数カウント以降を含めたの全文字列のために整形処理を呼び出す -->
      <xsl:call-template name="SplitTextForPTag_UTL">
        <xsl:with-param name="Data" select="$P_DATA_TEMP"/>
        <xsl:with-param name="LINE_COUNT" select="0"/>
        <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
        <xsl:with-param name="PAGE_LINE_COUNT" select="0"/>
        <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
        <xsl:with-param name="ADD_LINE_COUNT_FLG" select="0"/>
        <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- タグを生成して出力 -->
    <xsl:call-template name="KAKUNIN2_DIVS_UTL">
      <xsl:with-param name="Data" select="$P_DATA"/>
      <xsl:with-param name="DivCount" select="0"/>
      <xsl:with-param name="TateYoko" select="$TATEYOKO_FLG"/>
      <xsl:with-param name="PageLineMax" select="$PAGE_LINE_MAX"/>
      <xsl:with-param name="PTateHeadLineLength" select="0"/>
      <xsl:with-param name="RulerPTateHeadLineLength" select="0"/>
      <xsl:with-param name="PageBrakeFirstFlg" select="1"/>
    </xsl:call-template>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Ｐタグ内整形処理とDiv生成処理をまとめて実施する　-->
  <!-- SplitTextForPTag_UTLとKAKUNIN2_DIVS_UTLを呼び出す。　-->
  <!-- 本文要素を『本文』と『字解』を別で受け取り、　-->
  <!-- 『本文』に対してのみフラグに応じた文字カウント処理を実施する　-->
  <!-- ★縦書き時に１ページ１divを表示する場合用　-->
  <!-- 【param】HONBUN_DATA     　：本文文字列（文字カウント対象） -->
  <!-- 【param】JIKAI_DATA　　　　：字解文字列（文字カウント対象外）-->
  <!-- 【param】LINE_MAX_LENGTH 　：１行の折り返し最大文字数 -->
  <!-- 【param】PAGE_LINE_MAX　 　：１ページの最大行数定義 -->
  <!-- 【param】ADD_LINE_COUNT_FLG：行数カウント付加有無フラグ [0]なし、[1]文字列の末尾に行数カウントを追加 -->
  <!-- 【param】TATEYOKO_FLG　　　：縦書き(１ページ１div)[1]/横書き[2]切り替え -->
  <!-- 【param】ADD_OIKOMI_CLASS_FLG ：OikomiStartクラス付加フラグ -->
  <!--===============================================================================================-->
  <xsl:template name="KAKUNIN2_DIVS_TATELONG_LAYOUT_UTL">
    <xsl:param name="HONBUN_DATA"/>
    <xsl:param name="JIKAI_DATA"/>
    <xsl:param name="LINE_MAX_LENGTH"/>
    <xsl:param name="PAGE_LINE_MAX"/>
    <xsl:param name="ADD_LINE_COUNT_FLG"/>
    <xsl:param name="TATEYOKO_FLG"/>
    <xsl:param name="ADD_OIKOMI_CLASS_FLG" select="0"/>
    <!-- 本文文字列にclass="OikomiStart"用の定数を付加する -->
    <xsl:variable name="HONBUN_DATA_CLASS">
      <xsl:choose>
        <xsl:when test="$ADD_OIKOMI_CLASS_FLG=1">
          <xsl:call-template name="SetOikomiClass_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$HONBUN_DATA"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- 内容情報部行数を取得 -->
    <xsl:variable name="NAIYOU_LINE_SET">
      <xsl:call-template name="NAIYOU_LINE_SET"/>
    </xsl:variable>
    <!-- 仮見出しを取得　-->
    <xsl:variable name="PTate_HeadLine">
      <xsl:call-template name="PTateHeadLine_EDT"/>
    </xsl:variable>
    <!-- 仮見出しの行数を取得　-->
    <xsl:variable name="PTate_HeadLineCount">
      <xsl:call-template name="PTagCount_UTL">
        <xsl:with-param name="Data" select="$PTate_HeadLine"/>
        <xsl:with-param name="LINE_COUNT" select="0"/>
        <xsl:with-param name="LINE_MAX_LENGTH">
          <xsl:value-of select="$LINE_MAX_LENGTH"/>
        </xsl:with-param>
      </xsl:call-template>
    </xsl:variable>
    <xsl:variable name="P_DATA_TEMP">
      <xsl:choose>
        <xsl:when test="$ADD_LINE_COUNT_FLG=1">
          <!-- 行数カウントのために整形処理を呼び出す -->
          <xsl:call-template name="SplitTextForPTag_UTL">
            <xsl:with-param name="Data">
              <xsl:if test="$TATEYOKO_FLG=1">
                <xsl:value-of select="$PTate_HeadLine"/>
              </xsl:if>
              <xsl:value-of select="$HONBUN_DATA_CLASS"/>
            </xsl:with-param>
            <xsl:with-param name="LINE_COUNT">
              <xsl:choose>
                <xsl:when test="$TATEYOKO_FLG=1">
                  <!-- 仮見出しの行数分マイナスした数値から合計行数カウント開始 -->
                  <xsl:value-of select="0 - $PTate_HeadLineCount"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="0"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:with-param>
            <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
            <xsl:with-param name="PAGE_LINE_COUNT">
              <xsl:choose>
                <xsl:when test="$NAIYOU_F_SET=1 and $TATEYOKO_FLG=2">
                  <!-- 内容情報部あり、かつ横書きの場合 -->
                  <!-- 内容情報部の分だけ１ページ目の行数を減らす -->
                  <xsl:value-of select="$NAIYOU_LINE_SET"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="0"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:with-param>
            <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
            <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG"/>
            <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
            <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="$ADD_OIKOMI_CLASS_FLG"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <!-- 行数カウント非表示の場合、行数カウント表示のための整形処理は不要 -->
          <xsl:if test="$TATEYOKO_FLG=1">
            <xsl:value-of select="$PTate_HeadLine"/>
          </xsl:if>
          <!--<xsl:value-of select="$HONBUN_DATA"/>-->
          <!-- 本文末の改行文字の有無を統一 -->
          <xsl:call-template name="DeleteEndDelimiter_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA_CLASS"/>
            <xsl:with-param name="Delimiter" select="$LineFeed_UTL"/>
          </xsl:call-template>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 改行 -->
      <xsl:if test="$JIKAI_DATA!=''">
        <xsl:value-of select="$LineFeed_UTL"/>
        <!-- 字解情報 -->
        <xsl:value-of select="$JIKAI_DATA"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="P_DATA">
      <!-- 行数カウント以降を含めたの全文字列のために整形処理を呼び出す -->
      <xsl:call-template name="SplitTextForPTag_UTL">
        <xsl:with-param name="Data" select="$P_DATA_TEMP"/>
        <xsl:with-param name="LINE_COUNT">
          <xsl:choose>
            <xsl:when test="$TATEYOKO_FLG=1">
              <!-- 仮見出しの行数分マイナスした数値から合計行数カウント開始 -->
              <xsl:value-of select="0 - $PTate_HeadLineCount"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="0"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
        <xsl:with-param name="PAGE_LINE_COUNT">
          <xsl:choose>
            <xsl:when test="$NAIYOU_F_SET=1 and $TATEYOKO_FLG=2">
              <!-- 内容情報部あり、かつ横書きの場合 -->
              <!-- 内容情報部の分だけ１ページ目の行数を減らす -->
              <xsl:value-of select="$NAIYOU_LINE_SET"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="0"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
        <xsl:with-param name="ADD_LINE_COUNT_FLG" select="0"/>
        <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- タグを生成して出力 -->
    <xsl:choose>
      <xsl:when test="$TATEYOKO_FLG=1">
        <xsl:call-template name="KAKUNIN2_DIVS_UTL">
          <xsl:with-param name="Data" select="$P_DATA"/>
          <xsl:with-param name="DivCount" select="0"/>
          <xsl:with-param name="TateYoko" select="3"/>
          <xsl:with-param name="PageLineMax" select="$PAGE_LINE_MAX"/>
          <xsl:with-param name="PTateHeadLineLength" select="$PTate_HeadLineCount"/>
          <xsl:with-param name="RulerPTateHeadLineLength" select="$PTate_HeadLineCount"/>
          <xsl:with-param name="PageBrakeFirstFlg" select="0"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:call-template name="KAKUNIN2_DIVS_UTL">
          <xsl:with-param name="Data" select="$P_DATA"/>
          <xsl:with-param name="DivCount" select="0"/>
          <xsl:with-param name="TateYoko" select="$TATEYOKO_FLG"/>
          <xsl:with-param name="PageLineMax" select="$PAGE_LINE_MAX"/>
          <xsl:with-param name="PTateHeadLineLength" select="$PTate_HeadLineCount"/>
          <xsl:with-param name="RulerPTateHeadLineLength" select="$PTate_HeadLineCount"/>
          <xsl:with-param name="PageBrakeFirstFlg" select="0"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Ｐタグ内整形処理とDiv生成処理をまとめて実施する　-->
  <!-- SplitTextForPTag_UTLとKAKUNIN2_DIVS_UTLを呼び出す。　-->
  <!-- 本文要素を『本文』と『字解』を別で受け取り、　-->
  <!-- 『本文』に対してのみフラグに応じた文字カウント処理を実施する　-->
  <!-- ★縦書き時に１ページ１divを表示する場合用　-->
  <!-- ★１頁目以降の処理で使用。仮見出し出力処理を実施しない★　-->
  <!-- 【param】HONBUN_DATA     　：本文文字列（文字カウント対象） -->
  <!-- 【param】JIKAI_DATA　　　　：字解文字列（文字カウント対象外）-->
  <!-- 【param】LINE_MAX_LENGTH 　：１行の折り返し最大文字数 -->
  <!-- 【param】PAGE_LINE_MAX　 　：１ページの最大行数定義 -->
  <!-- 【param】ADD_LINE_COUNT_FLG：行数カウント付加有無フラグ [0]なし、[1]文字列の末尾に行数カウントを追加 -->
  <!-- 【param】TATEYOKO_FLG　　　：縦書き(１ページ１div)[1]/横書き[2]切り替え -->
  <!-- 【param】ADD_OIKOMI_CLASS_FLG ：OikomiStartクラス付加フラグ -->
  <!--===============================================================================================-->
  <xsl:template name="KAKUNIN2_DIVS_TATELONG_NO_PTateHeadLine_UTL">
    <xsl:param name="HONBUN_DATA"/>
    <xsl:param name="JIKAI_DATA"/>
    <xsl:param name="LINE_MAX_LENGTH"/>
    <xsl:param name="PAGE_LINE_MAX"/>
    <xsl:param name="ADD_LINE_COUNT_FLG"/>
    <xsl:param name="TATEYOKO_FLG"/>
    <xsl:param name="ADD_OIKOMI_CLASS_FLG" select="0"/>
    <!-- 本文文字列にclass="OikomiStart"用の定数を付加する -->
    <xsl:variable name="HONBUN_DATA_CLASS">
      <xsl:choose>
        <xsl:when test="$ADD_OIKOMI_CLASS_FLG=1">
          <xsl:call-template name="SetOikomiClass_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$HONBUN_DATA"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="P_DATA_TEMP">
      <xsl:choose>
        <xsl:when test="$ADD_LINE_COUNT_FLG=1">
          <!-- 行数カウントのために整形処理を呼び出す -->
          <xsl:call-template name="SplitTextForPTag_UTL">
            <xsl:with-param name="Data">
              <xsl:value-of select="$HONBUN_DATA_CLASS"/>
            </xsl:with-param>
            <xsl:with-param name="LINE_COUNT" select="0"/>
            <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
            <xsl:with-param name="PAGE_LINE_COUNT" select="0"/>
            <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
            <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG"/>
            <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
            <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="$ADD_OIKOMI_CLASS_FLG"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <!-- 本文末の改行文字の有無を統一 -->
          <xsl:call-template name="DeleteEndDelimiter_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA_CLASS"/>
            <xsl:with-param name="Delimiter" select="$LineFeed_UTL"/>
          </xsl:call-template>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 改行 -->
      <xsl:if test="$JIKAI_DATA!=''">
        <xsl:value-of select="$LineFeed_UTL"/>
        <!-- 字解情報 -->
        <xsl:value-of select="$JIKAI_DATA"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="P_DATA">
      <!-- 行数カウント以降を含めたの全文字列のために整形処理を呼び出す -->
      <xsl:call-template name="SplitTextForPTag_UTL">
        <xsl:with-param name="Data" select="$P_DATA_TEMP"/>
        <xsl:with-param name="LINE_COUNT" select="0"/>
        <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
        <xsl:with-param name="PAGE_LINE_COUNT" select="0"/>
        <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
        <xsl:with-param name="ADD_LINE_COUNT_FLG" select="0"/>
        <xsl:with-param name="TATEYOKO_FLG" select="$TATEYOKO_FLG"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- タグを生成して出力 -->
    <xsl:choose>
      <xsl:when test="$TATEYOKO_FLG=1">
        <xsl:call-template name="KAKUNIN2_DIVS_UTL">
          <xsl:with-param name="Data" select="$P_DATA"/>
          <xsl:with-param name="DivCount" select="0"/>
          <xsl:with-param name="TateYoko" select="3"/>
          <xsl:with-param name="PageLineMax" select="$PAGE_LINE_MAX"/>
          <xsl:with-param name="PTateHeadLineLength" select="0"/>
          <xsl:with-param name="RulerPTateHeadLineLength" select="0"/>
          <xsl:with-param name="PageBrakeFirstFlg" select="1"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:call-template name="KAKUNIN2_DIVS_UTL">
          <xsl:with-param name="Data" select="$P_DATA"/>
          <xsl:with-param name="DivCount" select="0"/>
          <xsl:with-param name="TateYoko" select="$TATEYOKO_FLG"/>
          <xsl:with-param name="PageLineMax" select="$PAGE_LINE_MAX"/>
          <xsl:with-param name="PTateHeadLineLength" select="0"/>
          <xsl:with-param name="RulerPTateHeadLineLength" select="0"/>
          <xsl:with-param name="PageBrakeFirstFlg" select="1"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- Ｐタグ内整形処理とDiv生成処理をまとめて実施する　-->
  <!-- 本文要素を『本文（縦書き）』『本文（横書き）』と『字解』を別で受け取る　-->
  <!-- 文字カウント処理は　「横書き部分の１行の文字数＋縦書き部分の全行数」をカウント　-->
  <!-- ★縦書き／横書きの混在記事★　-->
  <!-- 【param】HONBUN_DATA_YOKO　：本文文字列（横書き） -->
  <!-- 【param】HONBUN_DATA_TATE  ：本文文字列（縦書き） -->
  <!-- 【param】JIKAI_DATA　　　　：字解文字列（文字カウント対象外）-->
  <!-- 【param】LINE_MAX_LENGTH 　：１行の折り返し最大文字数 -->
  <!-- 【param】PAGE_LINE_MAX　 　：１ページの最大行数定義 -->
  <!-- 【param】ADD_LINE_COUNT_FLG：行数カウント付加有無フラグ [0]なし、[1]文字列の末尾に行数カウントを追加 -->
  <!-- 【param】ADD_OIKOMI_CLASS_FLG ：OikomiStartクラス付加フラグ -->
  <!--===============================================================================================-->
  <xsl:template name="KAKUNIN2_DIVS_YOKOTATE_LAYOUT_UTL">
    <xsl:param name="HONBUN_DATA_YOKO"/>
    <xsl:param name="HONBUN_DATA_TATE"/>
    <xsl:param name="JIKAI_DATA"/>
    <xsl:param name="LINE_MAX_LENGTH"/>
    <xsl:param name="PAGE_LINE_MAX"/>
    <xsl:param name="ADD_LINE_COUNT_FLG"/>
    <xsl:param name="ADD_OIKOMI_CLASS_FLG" select="0"/>
    <!-- 横書きの行数を取得 -->
    <xsl:variable name="YokoLineCount">
      <xsl:value-of select="string-length(substring-before($HONBUN_DATA_YOKO, $LineFeed_UTL))"/>
    </xsl:variable>
    <!-- 横書きの文字列を縦書きに変換 -->
    <xsl:variable name="P_DATA_YOKO">
      <xsl:call-template name="TranslateVerticalWriting">
        <xsl:with-param name="Content">
          <xsl:call-template name="TranslateCharTATE_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA_YOKO"/>
          </xsl:call-template>
        </xsl:with-param>
        <xsl:with-param name="MaxCol" select="$YokoLineCount"/>
        <xsl:with-param name="MaxLine" select="$LINE_MAX_LENGTH"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 縦書き本文文字列にclass="OikomiStart"用の定数を付加する -->
    <xsl:variable name="HONBUN_DATA_TATE_CLASS">
      <xsl:choose>
        <xsl:when test="$ADD_OIKOMI_CLASS_FLG=1">
          <xsl:call-template name="SetOikomiClass_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA_TATE"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$HONBUN_DATA_TATE"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- 文字数カウントありの場合、整形処理を呼び出す -->
    <xsl:variable name="P_DATA_TATE">
      <xsl:choose>
        <xsl:when test="$ADD_LINE_COUNT_FLG_SET=1">
          <xsl:call-template name="SplitTextForPTag_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA_TATE_CLASS"/>
            <xsl:with-param name="LINE_COUNT" select="$YokoLineCount"/>
            <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
            <xsl:with-param name="PAGE_LINE_COUNT" select="$YokoLineCount"/>
            <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
            <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG"/>
            <xsl:with-param name="TATEYOKO_FLG" select="1"/>
            <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="$ADD_OIKOMI_CLASS_FLG"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <!-- 本文末の改行文字の有無を統一 -->
          <xsl:call-template name="DeleteEndDelimiter_UTL">
            <xsl:with-param name="Data" select="$HONBUN_DATA_TATE_CLASS"/>
            <xsl:with-param name="Delimiter" select="$LineFeed_UTL"/>
          </xsl:call-template>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 改行 -->
      <xsl:if test="$JIKAI_DATA!=''">
        <xsl:value-of select="$LineFeed_UTL"/>
        <!-- 字解情報 -->
        <xsl:value-of select="$JIKAI_DATA"/>
      </xsl:if>
    </xsl:variable>
    <!-- 縦書き部分整形 -->
    <xsl:variable name="P_DATA">
      <xsl:call-template name="SplitTextForPTag_UTL">
        <xsl:with-param name="Data">
          <xsl:value-of select="$P_DATA_TATE"/>
        </xsl:with-param>
        <xsl:with-param name="LINE_COUNT" select="$YokoLineCount"/>
        <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
        <xsl:with-param name="PAGE_LINE_COUNT" select="$YokoLineCount"/>
        <xsl:with-param name="PAGE_LINE_MAX" select="$PAGE_LINE_MAX"/>
        <xsl:with-param name="ADD_LINE_COUNT_FLG" select="0"/>
        <xsl:with-param name="TATEYOKO_FLG" select="1"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 引数用に内容情報部行数を取得 -->
    <xsl:variable name="NAIYOU_LINE_SET">
      <xsl:call-template name="NAIYOU_LINE_SET"/>
    </xsl:variable>
    <!-- １頁目表示div数の指定 -->
    <xsl:variable name="DivModNum">
      <xsl:choose>
        <!--Ａ４縦 -->
        <xsl:when test="$PRINT_F_SET=1 and $NAIYOU_LINE_SET > 14">
          <xsl:value-of select="2"/>
        </xsl:when>
        <xsl:when test="$PRINT_F_SET=1">
          <xsl:value-of select="0"/>
        </xsl:when>
        <!-- Ａ４横 -->
        <xsl:when test="$PRINT_F_SET=2 and $NAIYOU_LINE_SET > 8">
          <xsl:value-of select="1"/>
        </xsl:when>
        <xsl:when test="$PRINT_F_SET=2">
          <xsl:value-of select="0"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- タグを生成して出力 -->
    <xsl:call-template name="KAKUNIN2_DIVS_YOKOTATE_UTL">
      <xsl:with-param name="Data">
        <xsl:value-of select="$P_DATA_YOKO"/>
        <xsl:value-of select="$YOKOTATEBreak_UTL"/>
        <xsl:value-of select="$P_DATA"/>
      </xsl:with-param>
      <xsl:with-param name="DivModNum" select="$DivModNum"/>
    </xsl:call-template>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- （横書きの文字列を縦書きに変換：内部処理）起点　-->
  <!--===============================================================================================-->
  <!-- 1Div分ずつ処理 -->
  <xsl:template name="TranslateVerticalWriting">
    <xsl:param name="Content"/>
    <xsl:param name="MaxCol"/>
    <xsl:param name="MaxLine"/>
    <!-- 1Div分を取得 -->
    <xsl:variable name="DivContent">
      <xsl:call-template name="pullStringLine">
        <xsl:with-param name="Content" select="$Content"/>
        <xsl:with-param name="MaxLine" select="$MaxLine"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 1Div分を処理 -->
    <xsl:call-template name="TranslateVerticalWritingDiv">
      <xsl:with-param name="Content" select="$DivContent"/>
      <xsl:with-param name="MaxCol" select="$MaxCol"/>
    </xsl:call-template>
    <!-- 1Div分の残り取得 -->
    <xsl:variable name="DivContentAfter">
      <xsl:value-of select="substring-after($Content, $DivContent)"/>
    </xsl:variable>
    <!-- 再帰 -->
    <xsl:if test="$DivContentAfter!=''">
      <xsl:value-of select="$PageBreak_UTL"/>
      <xsl:call-template name="TranslateVerticalWriting">
        <xsl:with-param name="Content" select="$DivContentAfter"/>
        <xsl:with-param name="MaxCol" select="$MaxCol"/>
        <xsl:with-param name="MaxLine" select="$MaxLine"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- （横書きの文字列を縦書きに変換：内部処理）１Div分の本文を取得　-->
  <!--===============================================================================================-->
  <xsl:template name="pullStringLine">
    <xsl:param name="Content"/>
    <xsl:param name="MaxLine"/>
    <xsl:param name="LineCount" select="1"/>
    <!-- 改行有りは１行分取得 -->
    <xsl:if test="contains($Content, $LineFeed_UTL)">
      <xsl:value-of select="substring-before($Content, $LineFeed_UTL)"/>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 最大行取得まで再帰処理 -->
      <xsl:if test="$MaxLine > $LineCount">
        <xsl:call-template name="pullStringLine">
          <xsl:with-param name="Content" select="substring-after($Content, $LineFeed_UTL)"/>
          <xsl:with-param name="MaxLine" select="$MaxLine"/>
          <xsl:with-param name="LineCount" select="$LineCount + 1"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- （横書きの文字列を縦書きに変換：内部処理）１Div分を横縦変換処理　-->
  <!--===============================================================================================-->
  <xsl:template name="TranslateVerticalWritingDiv">
    <xsl:param name="Content"/>
    <xsl:param name="MaxCol"/>
    <xsl:param name="TargetCol" select="$MaxCol"/>
    <!-- 縦の１行を取得 -->
    <xsl:call-template name="pullStringColumn">
      <xsl:with-param name="Content" select="$Content"/>
      <xsl:with-param name="TargetIndex" select="$TargetCol"/>
    </xsl:call-template>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
    <!-- 先頭列まで繰り返し -->
    <xsl:if test="$TargetCol > 1">
      <xsl:call-template name="TranslateVerticalWritingDiv">
        <xsl:with-param name="Content" select="$Content"/>
        <xsl:with-param name="MaxCol" select="$MaxCol"/>
        <xsl:with-param name="TargetCol" select="$TargetCol - 1"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--===============================================================================================-->
  <!-- （横書きの文字列を縦書きに変換：内部処理）特定列抜き出し　-->
  <!--===============================================================================================-->
  <xsl:template name="pullStringColumn">
    <xsl:param name="Content"/>
    <xsl:param name="TargetIndex"/>
    <!-- 抜き出す文字列 -->
    <xsl:variable name="TargetStr">
      <xsl:choose>
        <!-- 改行有りは１行分取得 -->
        <xsl:when test="contains($Content, $LineFeed_UTL)">
          <xsl:value-of select="substring-before($Content, $LineFeed_UTL)"/>
        </xsl:when>
        <!-- 改行無し、最終行はそのまま -->
        <xsl:otherwise>
          <xsl:value-of select="$Content"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- 指定された位置の文字を抜き出す -->
    <xsl:choose>
      <xsl:when test="substring($TargetStr, $TargetIndex, 1)!=''">
        <xsl:value-of select="substring($TargetStr, $TargetIndex, 1)"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!-- 複数行なら再起呼び出し -->
    <xsl:if test="substring-after($Content, $LineFeed_UTL)!=''">
      <xsl:call-template name="pullStringColumn">
        <xsl:with-param name="Content" select="substring-after($Content, $LineFeed_UTL)"/>
        <xsl:with-param name="TargetIndex" select="$TargetIndex"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 最大長取得テンプレート -->
  <!-- 改行文字で区切られた複数の文字列の、最大長を取得 -->
  <!-- （例）下記の文字列の場合「5」を返却 -->
  <!-- 『１LF１２LF１２３LF１２３４LF１２３４５LF１２LF１２３LF１LF１２３LF』 -->
  <!-- 【param】Data：改行文字で区切られた文字列 -->
  <!-- 【param】Max ：最大長を保持(初回呼び出し時は0を設定) -->
  <!--=======================================================================================================-->
  <xsl:template name="Get_TextMaxLength_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="Max" select="0"/>
    <!-- 改行定数 -->
    <!--【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="LineFeed_UTL">
      <xsl:text>LF</xsl:text>
    </xsl:variable>
    <!--１つめの改行までの文字列-->
    <xsl:variable name="LfBefore">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$Data"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--残りの文字列-->
    <xsl:variable name="LfAfter">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
        </xsl:when>
        <xsl:otherwise>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--これまでの最大長と比較し、長い方のlengthを取得-->
    <xsl:variable name="NewMax">
      <xsl:choose>
        <xsl:when test="string-length($LfBefore) > $Max">
          <xsl:value-of select="string-length($LfBefore)"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$Max"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:choose>
      <!--選手名が最後になるまで再帰呼び出し-->
      <xsl:when test="$LfAfter!='' and contains($LfAfter,$LineFeed_UTL)">
        <xsl:call-template name="Get_TextMaxLength_UTL">
          <xsl:with-param name="Data" select="$LfAfter"/>
          <xsl:with-param name="Max" select="$NewMax"/>
        </xsl:call-template>
      </xsl:when>
      <!--文字列が最後の場合は、最大を返却-->
      <xsl:otherwise>
        <xsl:value-of select="$NewMax"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 最大長取得テンプレート -->
  <!-- 改行文字で区切られた複数の文字列の、最大長の文字列を取得 -->
  <!-- （例）下記の文字列の場合「１２３４５」を返却 -->
  <!-- 『１LF１２LF１２３LF１２３４LF１２３４５LF１２LF１２３LF１LF１２３LF』 -->
  <!-- 【param】Data：改行文字で区切られた文字列 -->
  <!-- 【param】Max ：最大長を保持(初回呼び出し時は0を設定) -->
  <!--=======================================================================================================-->
  <xsl:template name="Get_TextMaxLengthString_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="Max" select="0"/>
    <xsl:param name="MaxString"/>
    <!-- 改行定数 -->
    <!--【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="LineFeed_UTL">
      <xsl:text>LF</xsl:text>
    </xsl:variable>
    <!--１つめの改行までの文字列-->
    <xsl:variable name="LfBefore">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$Data"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--残りの文字列-->
    <xsl:variable name="LfAfter">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
        </xsl:when>
        <xsl:otherwise>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--これまでの最大長と比較し、長い方のlengthを取得-->
    <xsl:variable name="NewMax">
      <xsl:choose>
        <xsl:when test="string-length($LfBefore) > $Max">
          <xsl:value-of select="string-length($LfBefore)"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$Max"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--これまでの最大長と比較し、長い方の文字列を取得-->
    <xsl:variable name="NewMaxString">
      <xsl:choose>
        <xsl:when test="string-length($LfBefore) > $Max">
          <xsl:value-of select="$LfBefore"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$MaxString"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:choose>
      <!--選手名が最後になるまで再帰呼び出し-->
      <xsl:when test="$LfAfter!='' and contains($LfAfter,$LineFeed_UTL)">
        <xsl:call-template name="Get_TextMaxLengthString_UTL">
          <xsl:with-param name="Data" select="$LfAfter"/>
          <xsl:with-param name="Max" select="$NewMax"/>
          <xsl:with-param name="MaxString" select="$NewMaxString"/>
        </xsl:call-template>
      </xsl:when>
      <!--文字列が最後の場合は、最大長の文字列を返却-->
      <xsl:otherwise>
        <xsl:value-of select="$NewMaxString"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 行数取得テンプレート -->
  <!-- 改行文字で区切られた文字列の、行数を取得 -->
  <!-- （例）下記の文字列の場合「9」を返却 -->
  <!-- 『１LF１２LF１２３LF１２３４LF１２３４５LF１２LF１２３LF１LF１２３LF』 -->
  <!-- 【param】Data：改行文字で区切られた文字列 -->
  <!-- 【param】Count ：行数カウント(呼び出し時設定不要) -->
  <!--=======================================================================================================-->
  <xsl:template name="Get_TextLineCount_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="Count" select="1"/>
    <xsl:choose>
      <xsl:when test="$Count = 1 and $Data=''">
        <xsl:value-of select="0"/>
      </xsl:when>
      <xsl:otherwise>
        <!--１つめの改行までの文字列-->
        <xsl:variable name="LfBefore">
          <xsl:choose>
            <xsl:when test="contains($Data,$LineFeed_UTL)">
              <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$Data"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <!--残りの文字列-->
        <xsl:variable name="LfAfter">
          <xsl:choose>
            <xsl:when test="contains($Data,$LineFeed_UTL)">
              <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:otherwise>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <xsl:choose>
          <!--選手名が最後になるまで再帰呼び出し-->
          <xsl:when test="$LfAfter!='' and contains($LfAfter,$LineFeed_UTL)">
            <xsl:call-template name="Get_TextLineCount_UTL">
              <xsl:with-param name="Data" select="$LfAfter"/>
              <xsl:with-param name="Count" select="$Count+1"/>
            </xsl:call-template>
          </xsl:when>
          <!--文字列が最後の場合は、最大を返却-->
          <xsl:otherwise>
            <xsl:value-of select="$Count"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 対戦型ヘッダ取得テンプレート -->
  <!-- ヘッダの表示エリアのサイズに合わせてヘッダのレイアウトを返却する -->
  <!-- 【param】HeaderStr ：ヘッダ文字列 -->
  <!-- 【param】WidthSize ：ヘッダ表示エリアの横幅(横書き表示時の横桁数) -->
  <!-- 【param】HightSize ：ヘッダ表示エリアの縦幅(横書き表示時の縦桁数) -->
  <!-- 【param】TargetLine：取得したい行数(横書き表示時の縦何番目の行か) -->
  <!--=======================================================================================================-->
  <xsl:template name="Get_TableHeader_UTL">
    <xsl:param name="HeaderStr"/>
    <xsl:param name="WidthSize"/>
    <xsl:param name="HightSize"/>
    <xsl:param name="TargetLine"/>
    <!-- ヘッダ文字列が表示エリアの最大桁より長い場合カットする -->
    <xsl:variable name="HeaderSpaceFill">
      <xsl:choose>
        <xsl:when test="string-length($HeaderStr) > $WidthSize * $HightSize">
          <xsl:value-of select="substring($HeaderStr,1,$WidthSize * $HightSize)"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:variable name="HeaderLayout">
            <xsl:choose>
              <!-- ヘッダ文字列が１字、縦幅が３字以上の場合 -->
              <xsl:when test="string-length($HeaderStr) = 1 and $HightSize > 2">
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="floor(($HightSize - 1) div 2)"/>
                </xsl:call-template>
                <xsl:value-of select="$HeaderStr"/>
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="floor(($HightSize - 1) div 2) + (($HightSize - 1) mod 2)"/>
                </xsl:call-template>
              </xsl:when>
              <!-- ヘッダ文字列が２字、縦幅が３字以上の場合 -->
              <xsl:when test="string-length($HeaderStr) = 2 and $HightSize > 2">
                <xsl:value-of select="substring($HeaderStr,1,1)"/>
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="$HightSize - 2"/>
                </xsl:call-template>
                <xsl:value-of select="substring($HeaderStr,2,1)"/>
              </xsl:when>
              <!-- ヘッダ文字列が３字、縦幅が５字の場合 -->
              <xsl:when test="string-length($HeaderStr) = 3 and $HightSize = 5">
                <xsl:value-of select="substring($HeaderStr,1,1)"/>
                <xsl:text>　</xsl:text>
                <xsl:value-of select="substring($HeaderStr,2,1)"/>
                <xsl:text>　</xsl:text>
                <xsl:value-of select="substring($HeaderStr,3,1)"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="$HeaderStr"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>
          <xsl:value-of select="$HeaderLayout"/>
          <xsl:if test="(string-length($HeaderLayout) mod $HightSize) > 0">
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$HightSize - (string-length($HeaderLayout) mod $HightSize)"/>
            </xsl:call-template>
          </xsl:if>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="PrintLength">
      <xsl:value-of select="string-length($HeaderSpaceFill) div $HightSize"/>
    </xsl:variable>
    <xsl:variable name="BeforeSpaceLength">
      <xsl:value-of select="floor(($WidthSize - $PrintLength) div 2) + (($WidthSize - $PrintLength) mod 2)"/>
    </xsl:variable>
    <xsl:variable name="AfterSpaceLength">
      <xsl:value-of select="floor(($WidthSize - $PrintLength) div 2)"/>
    </xsl:variable>
    <!-- スペース埋め -->
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$BeforeSpaceLength"/>
    </xsl:call-template>
    <!-- ヘッダ文字を出力 -->
    <xsl:call-template name="Get_TableHeaderChar_UTL">
      <xsl:with-param name="HeaderStr" select="$HeaderSpaceFill"/>
      <xsl:with-param name="WidthSize" select="$PrintLength"/>
      <xsl:with-param name="HightSize" select="$HightSize"/>
      <xsl:with-param name="TargetLine" select="$TargetLine"/>
      <xsl:with-param name="Counter" select="0"/>
    </xsl:call-template>
    <!-- スペース埋め -->
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$AfterSpaceLength"/>
    </xsl:call-template>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 対戦型ヘッダ取得テンプレート（内部処理） -->
  <!-- 指定行に該当する文字列を取得する(再帰) -->
  <!--=======================================================================================================-->
  <xsl:template name="Get_TableHeaderChar_UTL">
    <xsl:param name="HeaderStr"/>
    <xsl:param name="WidthSize"/>
    <xsl:param name="HightSize"/>
    <xsl:param name="TargetLine"/>
    <xsl:param name="Counter"/>
    <xsl:value-of select="substring($HeaderStr,$TargetLine + ($HightSize * $Counter),1)"/>
    <xsl:if test="$WidthSize - 1 > $Counter">
      <xsl:call-template name="Get_TableHeaderChar_UTL">
        <xsl:with-param name="HeaderStr" select="$HeaderStr"/>
        <xsl:with-param name="WidthSize" select="$WidthSize"/>
        <xsl:with-param name="HightSize" select="$HightSize"/>
        <xsl:with-param name="TargetLine" select="$TargetLine"/>
        <xsl:with-param name="Counter" select="$Counter+1"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 区切り文字変換テンプレート -->
  <!-- 繰り返しや条件分岐などで、文末にも区切り文字がセットされてしまう場合に利用 -->
  <!-- デリミタ（$Delimiter_UTL）を途中に含む文を、指定された「、」などに置き換える -->
  <!-- 「、」などで文が終わらないように、文末のデリミタは無視する -->
  <!-- （例）下記の場合「タはタイ、ニはニュージーランド、印はインド」を返却（$Delimiterに「、」を指定）-->
  <!-- 『タはタイDLMニはニュージーランドDLM印はインドDLM』-->
  <!-- 【param】Data      ：デリミタを含んだ文字列 -->
  <!-- 【param】Delimiter ：変換後の文字を指定。「、」「／」など -->
  <!--=======================================================================================================-->
  <!--  デリミタ 可変 -->
  <xsl:variable name="Delimiter_UTL">
    <xsl:text>DLM</xsl:text>
  </xsl:variable>
  <xsl:template name="SplitTextByDelimiter_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="Delimiter"/>
    <xsl:choose>
      <!--文字列の先頭がデリミタの場合は表示しない-->
      <xsl:when test="starts-with($Data,$Delimiter_UTL)">
      </xsl:when>
      <!--デリミタを含む場合はその前の文字列を表示-->
      <xsl:when test="contains($Data,$Delimiter_UTL)">
        <xsl:value-of select="substring-before($Data,$Delimiter_UTL)"/>
      </xsl:when>
      <!--デリミタを含まない場合は全文字列を表示-->
      <xsl:otherwise>
        <xsl:value-of select="$Data"/>
      </xsl:otherwise>
    </xsl:choose>
    <!--デリミタの後に文字列が残っている場合、再帰呼び出し-->
    <!--渡す文字列の先頭に実際の読点記号を追加する-->
    <xsl:if test="substring-after($Data,$Delimiter_UTL)!=''">
      <xsl:call-template name="SplitTextByDelimiter_UTL">
        <xsl:with-param name="Data" select="concat($Delimiter, substring-after($Data,$Delimiter_UTL))"/>
        <xsl:with-param name="Delimiter" select="$Delimiter"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 末尾文字列削除テンプレート -->
  <!-- 繰り返しや条件分岐などで、文末にも区切り文字がセットされてしまう場合に利用 -->
  <!-- デリミタ（$Delimiter）が文章（$Data）の末尾に設定されている場合、削除した文字列を返却 -->
  <!-- 【param】Data      ：文字列 -->
  <!-- 【param】Delimiter ：末尾に存在した場合に削除したい文字を指定。「、」「／」など -->
  <!--=======================================================================================================-->
  <xsl:template name="DeleteEndDelimiter_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="Delimiter"/>
    <xsl:variable name="DataEnd">
      <xsl:if test="string-length($Data) > string-length($Delimiter)">
        <xsl:value-of select="substring($Data,(string-length($Data) - string-length($Delimiter) + 1))"/>
      </xsl:if>
    </xsl:variable>
    <xsl:choose>
      <xsl:when test="$DataEnd = $Delimiter">
        <xsl:value-of select="substring($Data,1,string-length($Data) - string-length($Delimiter))"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$Data"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 縦横文字変換（縦書き表示用） -->
  <!-- 【param】Data ：変換対象文字列 -->
  <!--=======================================================================================================-->
  <xsl:template name="TranslateCharTATE_UTL">
    <xsl:param name="Data"/>
    <!--translateの２，３番目の引数の同じ位置にある文字を置換-->
    <!--（例）以下の例は、大文字を小文字に変換する-->
    <!--<xsl:value-of select="translate($Data,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>-->
    <xsl:value-of select="translate($Data,'－','―')"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 縦横文字変換（横書き表示用） -->
  <!-- 【param】Data ：変換対象文字列 -->
  <!--=======================================================================================================-->
  <xsl:template name="TranslateCharYOKO_UTL">
    <xsl:param name="Data"/>
    <!--translateの２，３番目の引数の同じ位置にある文字を置換-->
    <!--<xsl:value-of select="translate($Data,'','')"/>-->
    <xsl:value-of select="translate($Data,'ー―【】＜＞','｜︻︼〈〉')"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 縦横文字変換（変換文字を個別指定したい場合用） -->
  <!-- ※変換する文字を引数で指定する -->
  <!-- 【param】Data 　：変換対象文字列 -->
  <!-- 【param】Before ：変換前文字 -->
  <!-- 【param】After  ：変換後文字 -->
  <!--=======================================================================================================-->
  <xsl:template name="TranslateChar_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="Before"/>
    <xsl:param name="After"/>
    <!--translateの２，３番目の引数の同じ位置にある文字を置換-->
    <xsl:value-of select="translate($Data,$Before,$After)"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 文字列置換テンプレート -->
  <!-- 【param】Data         ：処理対象文字列 -->
  <!-- 【param】ReplacedData ：内部処理用文字列（引数指定不要） -->
  <!-- 【param】StringBefore ：置換前文字列 -->
  <!-- 【param】StringAfter  ：置換後文字列 -->
  <!--=======================================================================================================-->
  <xsl:template name="ReplaceString_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="ReplacedData" select="''"/>
    <xsl:param name="StringBefore"/>
    <xsl:param name="StringAfter"/>
    <xsl:choose>
      <xsl:when test="contains($Data,$StringBefore)">
        <!-- 処理対象文字列内に置換前文字列が含まれる場合 -->
        <!-- 置換対象文字列より前を取得 -->
        <xsl:variable name="Split_Before">
          <xsl:value-of select="substring-before($Data,$StringBefore)"/>
        </xsl:variable>
        <!-- 置換対象文字列より後を取得 -->
        <xsl:variable name="Split_After">
          <xsl:value-of select="substring-after($Data,$StringBefore)"/>
        </xsl:variable>
        <!-- 再帰呼び出し -->
        <xsl:call-template name="ReplaceString_UTL">
          <xsl:with-param name="Data" select="$Split_After"/>
          <xsl:with-param name="ReplacedData" select="concat($ReplacedData,$Split_Before,$StringAfter)"/>
          <xsl:with-param name="StringBefore" select="$StringBefore"/>
          <xsl:with-param name="StringAfter" select="$StringAfter"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <!-- 処理対象文字列内に置換前文字列が含まれない場合、変換済み文字を出力 -->
        <xsl:value-of select="concat($ReplacedData,$Data)"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 文字列スペース埋めテンプレート -->
  <!-- 割付対象文字列が１，２，３桁の場合、表示エリアに対応して割付を行う -->
  <!-- ※表示エリアが５字以上の場合は５字に割り付ける -->
  <!-- 割付対象文字列が４桁以上の場合、処理を行わない -->
  <!-- 【param】Data      ：割付対象文字列 -->
  <!-- 【param】AreaLength：割付対象エリアのサイズ -->
  <!--=======================================================================================================-->
  <xsl:template name="FillSpace_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="AreaLength"/>
    <!-- 割付対象文字列の桁数 -->
    <xsl:variable name="DataLength">
      <xsl:value-of select="string-length($Data)"/>
    </xsl:variable>
    <xsl:choose>
      <!-- 割付エリアより割付対象文字列のほうが長い場合はそのまま返却 -->
      <xsl:when test="$DataLength >= $AreaLength">
        <xsl:value-of select="$Data"/>
      </xsl:when>
      <!-- 割付対象文字列が４桁以上の場合はそのまま返却（割付対象外） -->
      <xsl:when test="$DataLength >= 4">
        <xsl:value-of select="$Data"/>
      </xsl:when>
      <!-- 割付対象文字列が１桁の場合 -->
      <xsl:when test="($DataLength=1) and ($AreaLength=3 or $AreaLength=4)">
        <!-- ３、４桁エリアに割付「１」→「□１□」 -->
        <xsl:text>　</xsl:text>
        <xsl:value-of select="$Data"/>
        <xsl:text>　</xsl:text>
      </xsl:when>
      <xsl:when test="($DataLength=1) and ($AreaLength>=5)">
        <!-- ５桁以上のエリアに割付「１」→「□□１□□」 -->
        <xsl:text>　　</xsl:text>
        <xsl:value-of select="$Data"/>
        <xsl:text>　　</xsl:text>
      </xsl:when>
      <!-- 割付対象文字列が２桁の場合 -->
      <xsl:when test="($DataLength=2) and ($AreaLength=3)">
        <!-- ３桁エリアに割付「１２」→「１□２」 -->
        <xsl:value-of select="substring($Data,1,1)"/>
        <xsl:text>　</xsl:text>
        <xsl:value-of select="substring($Data,2,1)"/>
      </xsl:when>
      <xsl:when test="($DataLength=2) and ($AreaLength=4)">
        <!-- ４桁エリアに割付「１２」→「１□□２」 -->
        <xsl:value-of select="substring($Data,1,1)"/>
        <xsl:text>　　</xsl:text>
        <xsl:value-of select="substring($Data,2,1)"/>
      </xsl:when>
      <xsl:when test="($DataLength=2) and ($AreaLength>=5)">
        <!-- ５桁以上のエリアに割付「１２」→「１□□□２」 -->
        <xsl:value-of select="substring($Data,1,1)"/>
        <xsl:text>　　　</xsl:text>
        <xsl:value-of select="substring($Data,2,1)"/>
      </xsl:when>
      <!-- 割付対象文字列が３桁の場合 -->
      <xsl:when test="($DataLength=3) and ($AreaLength>=5)">
        <!-- ５桁以上のエリアに割付「１２３」→「１□２□３」 -->
        <xsl:value-of select="substring($Data,1,1)"/>
        <xsl:text>　</xsl:text>
        <xsl:value-of select="substring($Data,2,1)"/>
        <xsl:text>　</xsl:text>
        <xsl:value-of select="substring($Data,3,1)"/>
      </xsl:when>
      <!-- その他の場合、そのまま返却 -->
      <xsl:otherwise>
        <xsl:value-of select="$Data"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 文字列スペース埋めテンプレート(２桁の場合のみ) -->
  <!-- 割付対象文字列が２桁の場合、のみ間にスペースを追加する -->
  <!-- 割付対象文字列がその他の場合、処理を行わない -->
  <!-- 【param】Data      ：割付対象文字列 -->
  <!-- 【param】AreaLength：割付対象エリアのサイズ -->
  <!--=======================================================================================================-->
  <xsl:template name="FillSpace_Length2_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="AreaLength"/>
    <!-- 割付対象文字列の桁数 -->
    <xsl:variable name="DataLength">
      <xsl:value-of select="string-length($Data)"/>
    </xsl:variable>
    <xsl:choose>
      <!-- 割付エリアより割付対象文字列のほうが長い場合はそのまま返却 -->
      <xsl:when test="($DataLength=2) and ($AreaLength > $DataLength)">
        <!-- ３桁エリアに割付「１２」→「１□２」 -->
        <xsl:value-of select="substring($Data,1,1)"/>
        <xsl:text>　</xsl:text>
        <xsl:value-of select="substring($Data,2,1)"/>
      </xsl:when>
      <!-- その他の場合、そのまま返却 -->
      <xsl:otherwise>
        <xsl:value-of select="$Data"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 段組レイアウト -->
  <!-- $DATAの文字列を$PageBreak_UTL(PB)区切りで分割し、奇数番目を左、偶数番目を右に -->
  <!-- $LineFeed_UTL(LF)単位で割り付けて出力する。 -->
  <!-- 【データ成型イメージ】 -->
  <!-- 　　①LF　　　　　①③LF　　 -->
  <!-- 　　②LF　　→　　②④LF　　 -->
  <!-- 　　PB　　　→　　PB　　　　 -->
  <!-- 　　③LF　　→　　⑤LF　　　 -->
  <!-- 　　④LF　　　　　　　　　　 -->
  <!-- 　　PB　　　　　　　　　　　 -->
  <!-- 　　⑤LF　　　　　　　　　　 -->
  <!-- $SPACEに指定した文字数分スペースを左右に割り付ける文字列の間に出力する -->
  <!-- ※$LineFeed_UTL区切りの各行の文字列長は、すべて一律である前提 -->
  <!-- 【param】DATA   ：出力データ文字列 -->
  <!-- 【param】SPACE  ：左右割り付け時のスペース数 -->
  <!--=======================================================================================================-->
  <xsl:template name="TABLE_LAYOUT_UTIL">
    <xsl:param name="DATA"/>
    <xsl:param name="SPACE"/>
    <xsl:if test="contains($DATA,$PageBreak_UTL)">
      <xsl:variable name="DATA1">
        <xsl:value-of select="substring-before($DATA,$PageBreak_UTL)"/>
      </xsl:variable>
      <xsl:variable name="DATA1_AFTER">
        <xsl:value-of select="substring-after($DATA,$PageBreak_UTL)"/>
      </xsl:variable>
      <xsl:variable name="DATA2">
        <xsl:value-of select="substring-before($DATA1_AFTER,$PageBreak_UTL)"/>
      </xsl:variable>
      <xsl:variable name="DATA2_AFTER">
        <xsl:value-of select="substring-after($DATA1_AFTER,$PageBreak_UTL)"/>
      </xsl:variable>
      <xsl:call-template name="TABLE_LAYOUT_2DATA_UTIL">
        <xsl:with-param name="DATA1" select="$DATA1"/>
        <xsl:with-param name="DATA2" select="$DATA2"/>
        <xsl:with-param name="SPACE" select="$SPACE"/>
      </xsl:call-template>
      <xsl:if test="contains($DATA2_AFTER,$PageBreak_UTL)">
        <!-- 改ページ -->
        <xsl:value-of select="$PageBreak_UTL"/>
        <!-- 再帰呼び出し -->
        <xsl:call-template name="TABLE_LAYOUT_UTIL">
          <xsl:with-param name="DATA" select="$DATA2_AFTER"/>
          <xsl:with-param name="SPACE" select="$SPACE"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- ２データの割り付け処理 -->
  <!-- $DATA1および$DATA2の文字列を、$LineFeed_UTL区切りで連結し、一行のデータとして出力する -->
  <!-- $SPACEに指定した文字数分スペースを$DATA1および$DATA2の間に出力する -->
  <!-- ※$LineFeed_UTL区切りの各行の文字列長は、すべて一律である前提 -->
  <!-- 【param】DATA1   ：左側出力データ文字列 -->
  <!-- 【param】DATA2   ：右側出力データ文字列 -->
  <!-- 【param】SPACE   ：左右割り付け時のスペース数 -->
  <!--=======================================================================================================-->
  <xsl:template name="TABLE_LAYOUT_2DATA_UTIL">
    <xsl:param name="DATA1"/>
    <xsl:param name="DATA2"/>
    <xsl:param name="SPACE"/>
    <xsl:if test="$DATA1!=''">
      <!-- データ１出力 -->
      <xsl:value-of select="substring-before($DATA1,$LineFeed_UTL)"/>
      <!-- 空白埋め -->
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$SPACE"/>
      </xsl:call-template>
      <!-- データ２出力 -->
      <xsl:if test="contains($DATA2,$LineFeed_UTL)">
        <xsl:value-of select="substring-before($DATA2,$LineFeed_UTL)"/>
      </xsl:if>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 再帰呼び出し -->
      <xsl:call-template name="TABLE_LAYOUT_2DATA_UTIL">
        <xsl:with-param name="DATA1" select="substring-after($DATA1,$LineFeed_UTL)"/>
        <xsl:with-param name="DATA2" select="substring-after($DATA2,$LineFeed_UTL)"/>
        <xsl:with-param name="SPACE" select="$SPACE"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--====================================================================-->
  <!-- 柱行の連数字変換 -->
  <!-- 数値が２個連続している箇所のみを連数字に変換。３個以上数値が続く箇所は変換対象外 -->
  <!-- 【param】Data ：変換対象文字列 -->
  <!--====================================================================-->
  <xsl:template name="TranslateToRensuuText_UTL">
    <xsl:param name="Data"/>
    <!-- 直前に処理した１文字 -->
    <xsl:param name="OnePrevChar"/>
    <!-- 末尾の１文字の処理用に、ダミー記号１文字を付加する -->
    <xsl:param name="DataWithEOLChar" select="concat($Data,'＃')"/>
    <xsl:if test="string-length($Data) &gt; 0">
      <xsl:choose>
        <!--現在の位置が文字列の先頭　または　１文字前が数字でないとき
          かつ、現在の位置から１文字目と２文字目が数字、３文字目が数字でないときは、
          ２桁の連数字に変換-->
        <xsl:when test="($OnePrevChar='' or not(contains('０１２３４５６７６８９',$OnePrevChar)))
                  and contains('０１２３４５６７６８９',substring($DataWithEOLChar,1,1))
                  and contains('０１２３４５６７６８９',substring($DataWithEOLChar,2,1))
                  and not(contains('０１２３４５６７６８９',substring($DataWithEOLChar,3,1)))">
          <xsl:call-template name="RensuuHenkan">
            <xsl:with-param name="Sts" select="3"/>
            <xsl:with-param name="Pdata" select="substring($Data,1,2)"/>
          </xsl:call-template>
          <!-- 再帰呼び出し。３文字目以降の文字列と最後に処理した１文字を渡す -->
          <xsl:call-template name="TranslateToRensuuText_UTL">
            <xsl:with-param name="Data" select="substring($Data,3)"/>
            <xsl:with-param name="OnePrevChar" select="substring($Data,2,1)"/>
          </xsl:call-template>
        </xsl:when>
        <!--その他の文字は変換しない-->
        <xsl:otherwise>
          <xsl:value-of select="substring($Data,1,1)"/>
          <!-- 再帰呼び出し。２文字目以降の文字列と最後に処理した１文字を渡す -->
          <xsl:call-template name="TranslateToRensuuText_UTL">
            <xsl:with-param name="Data" select="substring($Data,2)"/>
            <xsl:with-param name="OnePrevChar" select="substring($Data,1,1)"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>
  <!--====================================================================-->
  <!-- 連数字変換 -->
  <!-- 文字列を後ろから捜索し、数値が２個以上連続している箇所を連数字に変換する -->
  <!-- 【param】Data     ：変換対象文字列 -->
  <!-- 【param】EndIndex ：処理対象Index -->
  <!-- 【param】EditFlg  ：前の文字の数値変換有無 -->
  <!--====================================================================-->
  <xsl:template name="TranslateToRensuuFromEnd_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="EndIndex" select="string-length($Data)"/>
    <xsl:param name="EditFlg" select="0"/>
    <xsl:choose>
      <xsl:when test=" 0 >= $EndIndex">
        <xsl:value-of select="$Data"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 対象Indexの文字を取得 -->
        <xsl:variable name="IndexChar" select="substring($Data,$EndIndex,1)"/>
        <xsl:choose>
          <!-- 数値の場合 -->
          <xsl:when test="contains('０１２３４５６７６８９',$IndexChar)">
            <!-- 一つ前の文字を取得 -->
            <xsl:variable name="PreChar" select="substring($Data,$EndIndex -1,1)"/>
            <xsl:choose>
              <!-- 一つ先の文字も数値の場合 -->
              <xsl:when test="$EndIndex!=1 and contains('０１２３４５６７６８９',$PreChar)">
                <!-- 連数字化 -->
                <xsl:variable name="TranslatedString">
                  <xsl:value-of select="substring($Data,1,$EndIndex -2)"/>
                  <xsl:call-template name="RensuuHenkan">
                    <xsl:with-param name="Sts" select="3"/>
                    <xsl:with-param name="Pdata" select="concat($PreChar,$IndexChar)"/>
                  </xsl:call-template>
                  <xsl:value-of select="substring($Data,$EndIndex+1)"/>
                </xsl:variable>
                <!-- 再帰呼び出し -->
                <xsl:call-template name="TranslateToRensuuFromEnd_UTL">
                  <xsl:with-param name="Data" select="$TranslatedString"/>
                  <xsl:with-param name="EndIndex" select="$EndIndex -2"/>
                  <xsl:with-param name="EditFlg" select="1"/>
                </xsl:call-template>
              </xsl:when>
              <!-- 一つ先の文字が数値以外の場合 -->
              <xsl:otherwise>
                <xsl:variable name="TranslatedString">
                  <xsl:choose>
                    <!-- 後ろが数値の場合 -->
                    <xsl:when test="$EditFlg=1">
                      <!-- 片寄せ連数字変換 -->
                      <xsl:value-of select="substring($Data,1,$EndIndex -1)"/>
                      <xsl:value-of select="translate($IndexChar,'０１２３４５６７８９','')"/>
                      <xsl:value-of select="substring($Data,$EndIndex +1)"/>
                    </xsl:when>
                    <!-- 後ろが数値以外の場合 -->
                    <xsl:otherwise>
                      <!-- そのまま出力 -->
                      <xsl:value-of select="$Data"/>
                    </xsl:otherwise>
                  </xsl:choose>
                </xsl:variable>
                <!-- 再帰呼び出し -->
                <xsl:call-template name="TranslateToRensuuFromEnd_UTL">
                  <xsl:with-param name="Data" select="$TranslatedString"/>
                  <xsl:with-param name="EndIndex" select="$EndIndex -2"/>
                  <xsl:with-param name="EditFlg" select="0"/>
                </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <!-- 数値以外の場合 -->
          <xsl:otherwise>
            <!-- 再帰呼び出し -->
            <xsl:call-template name="TranslateToRensuuFromEnd_UTL">
              <xsl:with-param name="Data" select="$Data"/>
              <xsl:with-param name="EndIndex" select="$EndIndex -1"/>
              <xsl:with-param name="EditFlg" select="0"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--====================================================================-->
  <!-- 処理対象文字列中に最後に出現する特定文字以降の文字列を取得する -->
  <!-- （例）Data「あいうえおあいうえおあいうえお」、TargetWord「あい」の場合「うえお」を返却する -->
  <!-- 【param】Data       ：処理対象文字列 -->
  <!-- 【param】TargetWord ：特定文字 -->
  <!--====================================================================-->
  <xsl:template name="SubstringAfterLast_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="TargetWord"/>
    <xsl:choose>
      <xsl:when test="contains($Data,$TargetWord)">
        <xsl:call-template name="SubstringAfterLast_UTL">
          <xsl:with-param name="Data" select="substring-after($Data,$TargetWord)"/>
          <xsl:with-param name="TargetWord" select="$TargetWord"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$Data"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--====================================================================-->
  <!-- 指定行データ取得テンプレート -->
  <!-- 改行文字で区切られた文字列の、指定行を取得 -->
  <!-- （例）下記の文字列の場合、TargetLine:3の場合「１２３」を返却 -->
  <!-- 『１LF１２LF１２３LF１２３４LF１２３４５LF１２LF１２３LF１LF１２３LF』 -->
  <!-- 【param】Data      ：改行文字で区切られた文字列 -->
  <!-- 【param】TargetLine：取得したい行の数 -->
  <!-- 【param】Count     ：行数カウント(呼び出し時設定不要) -->
  <!--====================================================================-->
  <xsl:template name="SubstringTargetLine_UTL">
    <xsl:param name="Data"/>
    <xsl:param name="TargetLine"/>
    <xsl:param name="Count" select="1"/>
    <xsl:if test="$Data!=''">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <xsl:variable name="FirstLine">
            <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
          </xsl:variable>
          <xsl:variable name="AfterLines">
            <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
          </xsl:variable>
          <xsl:choose>
            <xsl:when test="$TargetLine = $Count">
              <xsl:value-of select="$FirstLine"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:call-template name="SubstringTargetLine_UTL">
                <xsl:with-param name="Data" select="$AfterLines"/>
                <xsl:with-param name="TargetLine" select="$TargetLine"/>
                <xsl:with-param name="Count" select="$Count + 1"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:otherwise>
          <xsl:if test="$TargetLine = $Count">
            <xsl:value-of select="$Data"/>
          </xsl:if>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 固定文字数での改行追加処理 -->
  <!-- 文字列に対し固定文字数ごとに$LineFeed_UTLを設定する。-->
  <!-- 元から含まれている$LineFeed_UTLについては維持する。-->
  <!-- また、１行が固定文字数に満たない場合は空白埋めする。-->
  <!-- 【param】DATA              ：処理対象文字列 -->
  <!-- 【param】LINE_MAX_LENGTH   ：$LineFeed_UTLを設定する１行の文字数 -->
  <!--=======================================================================================================-->
  <xsl:template name="SplitText_UTL">
    <xsl:param name="DATA"/>
    <xsl:param name="LINE_MAX_LENGTH"/>
    <!--出力対象文字が''でない場合は処理を実施-->
    <xsl:if test="$DATA!=''">
      <!--改行文字までの文字列を取得-->
      <xsl:variable name="Data_LineData">
        <xsl:choose>
          <xsl:when test="starts-with($DATA,$LineFeed_UTL)">
            <xsl:text>　</xsl:text>
          </xsl:when>
          <xsl:when test="substring-before($DATA,$LineFeed_UTL)!= '' 
                          and $LINE_MAX_LENGTH >= string-length(substring-before($DATA,$LineFeed_UTL))">
            <xsl:value-of select="substring-before($DATA,$LineFeed_UTL)"/>
          </xsl:when>
          <xsl:when test="string-length($DATA) > $LINE_MAX_LENGTH">
            <xsl:value-of select="substring($DATA,1,$LINE_MAX_LENGTH)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$DATA"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!-- Ｐタグ１つ分の文字列を出力 -->
      <xsl:value-of select="$Data_LineData"/>
      <!-- 空白埋め -->
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$LINE_MAX_LENGTH - string-length($Data_LineData)"/>
      </xsl:call-template>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 出力済みの文字列の残り -->
      <xsl:variable name="Data_After">
        <xsl:choose>
          <xsl:when test="starts-with($DATA,$LineFeed_UTL)">
            <xsl:value-of select="$DATA"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="substring-after($DATA,$Data_LineData)"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!-- 再帰呼び出し -->
      <xsl:call-template name="SplitText_UTL">
        <xsl:with-param name="DATA">
          <xsl:choose>
            <xsl:when test="starts-with($Data_After, $LineFeed_UTL)">
              <xsl:value-of select="substring-after($Data_After,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$Data_After"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 固定文字数での改行追加処理 -->
  <!-- 文字列に対し固定文字数ごとに$LineFeed_UTLを設定する。-->
  <!-- 元から含まれている$LineFeed_UTLについては維持する。-->
  <!-- １行が固定文字数に満たない場合は空白埋めしない。-->
  <!-- 【param】DATA              ：処理対象文字列 -->
  <!-- 【param】LINE_MAX_LENGTH   ：$LineFeed_UTLを設定する１行の文字数 -->
  <!--=======================================================================================================-->
  <xsl:template name="SplitText_NotFillSpace_UTL">
    <xsl:param name="DATA"/>
    <xsl:param name="LINE_MAX_LENGTH"/>
    <!--出力対象文字が''でない場合は処理を実施-->
    <xsl:if test="$DATA!=''">
      <!--改行文字までの文字列を取得-->
      <xsl:variable name="Data_LineData">
        <xsl:choose>
          <xsl:when test="starts-with($DATA,$LineFeed_UTL)">
            <xsl:text>　</xsl:text>
          </xsl:when>
          <xsl:when test="substring-before($DATA,$LineFeed_UTL)!= '' 
                          and $LINE_MAX_LENGTH >= string-length(substring-before($DATA,$LineFeed_UTL))">
            <xsl:value-of select="substring-before($DATA,$LineFeed_UTL)"/>
          </xsl:when>
          <xsl:when test="string-length($DATA) > $LINE_MAX_LENGTH">
            <xsl:value-of select="substring($DATA,1,$LINE_MAX_LENGTH)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$DATA"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!-- Ｐタグ１つ分の文字列を出力 -->
      <xsl:value-of select="$Data_LineData"/>
      <!-- 空白埋め -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 出力済みの文字列の残り -->
      <xsl:variable name="Data_After">
        <xsl:choose>
          <xsl:when test="starts-with($DATA,$LineFeed_UTL)">
            <xsl:value-of select="$DATA"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="substring-after($DATA,$Data_LineData)"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!-- 再帰呼び出し -->
      <xsl:call-template name="SplitText_NotFillSpace_UTL">
        <xsl:with-param name="DATA">
          <xsl:choose>
            <xsl:when test="starts-with($Data_After, $LineFeed_UTL)">
              <xsl:value-of select="substring-after($Data_After,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$Data_After"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="LINE_MAX_LENGTH" select="$LINE_MAX_LENGTH"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- ２データの割り付け処理 -->
  <!-- $DATA1および$DATA2の文字列を、$LineFeed_UTL区切りで連結し、一行のデータとして出力する -->
  <!-- $DATA1または$DATA2が指定文字数に満たない場合は空白埋めする。 -->
  <!-- $SPACEに指定した文字数分スペースを$DATA1および$DATA2の間に出力する -->
  <!-- 【param】DATA1_AREA   ：DATA1のエリア文字数(スペース補完用) ※１行が当設定値より長い場合でも改行処理は行わない -->
  <!-- 【param】DATA2_AREA   ：DATA2のエリア文字数(スペース補完用) ※１行が当設定値より長い場合でも改行処理は行わない -->
  <!-- 【param】DATA1       ：左側出力データ文字列 -->
  <!-- 【param】DATA2       ：右側出力データ文字列 -->
  <!-- 【param】SPACE       ：左右割り付け時のスペース数 -->
  <!--=======================================================================================================-->
  <xsl:template name="TABLE_LAYOUT_LeftRight_UTIL">
    <xsl:param name="DATA1_AREA"/>
    <xsl:param name="DATA2_AREA"/>
    <xsl:param name="DATA1"/>
    <xsl:param name="DATA2"/>
    <xsl:param name="SPACE"/>
    <xsl:if test="$DATA1!='' or $DATA2!=''">
      <!-- データ１出力 -->
      <xsl:value-of select="substring-before($DATA1,$LineFeed_UTL)"/>
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$DATA1_AREA - string-length(substring-before($DATA1,$LineFeed_UTL))"/>
      </xsl:call-template>
      <!-- 空白埋め -->
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$SPACE"/>
      </xsl:call-template>
      <!-- データ２出力 -->
      <xsl:value-of select="substring-before($DATA2,$LineFeed_UTL)"/>
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$DATA2_AREA - string-length(substring-before($DATA2,$LineFeed_UTL))"/>
      </xsl:call-template>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 再帰呼び出し -->
      <xsl:call-template name="TABLE_LAYOUT_LeftRight_UTIL">
        <xsl:with-param name="DATA1_AREA" select="$DATA1_AREA"/>
        <xsl:with-param name="DATA2_AREA" select="$DATA2_AREA"/>
        <xsl:with-param name="DATA1" select="substring-after($DATA1,$LineFeed_UTL)"/>
        <xsl:with-param name="DATA2" select="substring-after($DATA2,$LineFeed_UTL)"/>
        <xsl:with-param name="SPACE" select="$SPACE"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--====================================================================-->
  <!-- pタグclass設定用定数（追い込み行頭）付加テンプレート -->
  <!-- 改行文字で区切られた各文字列の先頭に「pタグclass設定用定数（追い込み行頭）」を付加する -->
  <!-- 【param】Data      ：文字列 -->
  <!--====================================================================-->
  <xsl:template name="SetOikomiClass_UTL">
    <xsl:param name="Data"/>
    <xsl:if test="$Data!=''">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <!-- 先頭行 -->
          <xsl:variable name="FirstLine">
            <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
          </xsl:variable>
          <!-- 残り行 -->
          <xsl:variable name="AfterLines">
            <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
          </xsl:variable>
          <xsl:choose>
            <xsl:when test="starts-with($FirstLine, $MatchClass_UTL)">
              <!-- 先頭行に「pタグclass設定用定数（対戦）」が存在する場合（何も設定しない） -->
              <xsl:value-of select="$FirstLine"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:when test="starts-with($FirstLine, $OikomiClass_UTL)">
              <!-- 先頭行に「pタグclass設定用定数（追い込み）」が存在する場合（何も設定しない） -->
              <xsl:value-of select="$FirstLine"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:when test="starts-with($FirstLine, $NoClass_UTL)">
              <!-- 先頭行に「pタグclass排除用定数」が存在する場合、排除する -->
              <xsl:value-of select="substring-after($FirstLine,$NoClass_UTL)"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:when test="$FirstLine!=''">
              <!-- 先頭行に文字列が存在する場合（固定文字を付加する） -->
              <xsl:value-of select="$OikomiClass_UTL"/>
              <xsl:value-of select="$FirstLine"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:otherwise>
              <!-- 先頭行に文字列が存在しない場合（空行として「固定文字＋空白」を設定） -->
              <xsl:value-of select="$OikomiClass_UTL"/>
              <xsl:text>　</xsl:text>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:otherwise>
          </xsl:choose>
          <!-- 残り行が存在する場合は再帰呼び出し -->
          <xsl:if test="$AfterLines!=''">
            <xsl:choose>
              <xsl:when test="starts-with($AfterLines, $PageBreak_UTL)">
                <xsl:if test="$AfterLines!=$PageBreak_UTL">
                  <xsl:value-of select="$PageBreak_UTL"/>
                  <xsl:call-template name="SetOikomiClass_UTL">
                    <xsl:with-param name="Data" select="substring-after($AfterLines,$PageBreak_UTL)"/>
                  </xsl:call-template>
                </xsl:if>
              </xsl:when>
              <xsl:otherwise>
                <xsl:call-template name="SetOikomiClass_UTL">
                  <xsl:with-param name="Data" select="$AfterLines"/>
                </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:if>
        </xsl:when>
        <xsl:otherwise>
          <!-- 改行文字が含まれない場合は、引数全体を一行として扱う -->
          <!--<xsl:if test="not(starts-with($Data, $MatchClass_UTL))">-->
            <!-- 「pタグclass設定用定数（対戦）」が存在しない場合（固定文字を付加する） -->
            <!--<xsl:value-of select="$OikomiClass_UTL"/>
          </xsl:if>
          <xsl:value-of select="$Data"/>
          <xsl:value-of select="$LineFeed_UTL"/>-->

          <xsl:choose>
            <xsl:when test="starts-with($Data, $MatchClass_UTL)">
              <!-- 先頭行に「pタグclass設定用定数（対戦）」が存在する場合（何も設定しない） -->
              <xsl:value-of select="$Data"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:when test="starts-with($Data, $OikomiClass_UTL)">
              <!-- 先頭行に「pタグclass設定用定数（追い込み）」が存在する場合（何も設定しない） -->
              <xsl:value-of select="$Data"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:when test="starts-with($Data, $NoClass_UTL)">
              <!-- 先頭行に「pタグclass排除用定数」が存在する場合、排除する -->
              <xsl:value-of select="substring-after($Data,$NoClass_UTL)"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:otherwise>
              <!-- その他の場合（固定文字を付加する） -->
              <xsl:value-of select="$OikomiClass_UTL"/>
              <xsl:value-of select="$Data"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>
  <!--====================================================================-->
  <!-- 【対戦型内部処理専用】pタグclass排除用定数　付加テンプレート -->
  <!-- 改行文字で区切られた各文字列の先頭に「pタグclass排除用定数」を付加する -->
  <!-- 【param】Data      ：文字列 -->
  <!--====================================================================-->
  <xsl:template name="Taisen_SetNoClass_UTL">
    <xsl:param name="Data"/>
    <xsl:if test="$Data!=''">
      <xsl:choose>
        <xsl:when test="contains($Data,$LineFeed_UTL)">
          <!-- 先頭行 -->
          <xsl:variable name="FirstLine">
            <xsl:value-of select="substring-before($Data,$LineFeed_UTL)"/>
          </xsl:variable>
          <!-- 残り行 -->
          <xsl:variable name="AfterLines">
            <xsl:value-of select="substring-after($Data,$LineFeed_UTL)"/>
          </xsl:variable>
          <xsl:choose>
            <xsl:when test="starts-with($FirstLine, $MatchClass_UTL)">
              <!-- 先頭行に「pタグclass設定用定数（対戦）」が存在する場合（何も設定しない） -->
              <xsl:value-of select="$FirstLine"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:when test="starts-with($FirstLine, $OikomiClass_UTL)">
              <!-- 先頭行に「pタグclass設定用定数（追い込み）」が存在する場合（何も設定しない） -->
              <xsl:value-of select="$FirstLine"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:when>
            <xsl:otherwise>
              <!-- 固定文字を付加する -->
              <xsl:value-of select="$NoClass_UTL"/>
              <xsl:value-of select="$FirstLine"/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:otherwise>
          </xsl:choose>
          <!-- 残り行が存在する場合は再帰呼び出し -->
          <xsl:if test="$AfterLines!=''">
            <xsl:choose>
              <xsl:when test="starts-with($AfterLines, $PageBreak_UTL)">
                <xsl:if test="$AfterLines!=$PageBreak_UTL">
                  <xsl:value-of select="$PageBreak_UTL"/>
                  <xsl:call-template name="Taisen_SetNoClass_UTL">
                    <xsl:with-param name="Data" select="substring-after($AfterLines,$PageBreak_UTL)"/>
                  </xsl:call-template>
                </xsl:if>
              </xsl:when>
              <xsl:otherwise>
                <xsl:call-template name="Taisen_SetNoClass_UTL">
                  <xsl:with-param name="Data" select="$AfterLines"/>
                </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
            <!--<xsl:call-template name="Taisen_SetNoClass_UTL">
              <xsl:with-param name="Data" select="$AfterLines"/>
            </xsl:call-template>-->
          </xsl:if>
        </xsl:when>
        <xsl:otherwise>
          <!-- 改行文字が含まれない場合は、引数全体を一行として扱う -->
          <xsl:if test="not(starts-with($Data, $MatchClass_UTL)) and not(starts-with($Data, $OikomiClass_UTL))">
            <!-- 「pタグclass設定用定数（対戦）」が存在しない場合（固定文字を付加する） -->
            <xsl:value-of select="$NoClass_UTL"/>
          </xsl:if>
          <xsl:value-of select="$Data"/>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
