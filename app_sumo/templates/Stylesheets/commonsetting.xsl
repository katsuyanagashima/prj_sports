<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja">
	<!--=============================================================================
全スタイルシート共通設定
4.0版　 2014.12.19 プレーンテキスト版として新規公開
4.01版　2015.02.06 独自テンプレートimport時の不具合を解消
4.02版　2015.02.27 エンコードをUTF-16LEからUTF-16BEに訂正
                   Pタグの高さを1.0から1.1に訂正
                   横書き表示　１ページ最大行数の設定値を訂正
                   中央競馬の成績Ｃに、縦・横表示の切り替えを追加
                   地方競馬、オートレースの設定を追加
                   空行設定文字定義を削除（全角スペースを固定で使用する仕様としたため）
4.03版　2015.03.31 改ページ用divの仕様変更（commonutil）に伴い、CSS定義に「.pageBreak p」を追加
                   NAIYOU_LINE_SETの定義変更（variable→template）
                   横書きDiv(ptextYOKO)のmarginを変更
                   横書き表示　１ページ最大行数の設定値を訂正
                   K-LOT、地価、名簿の設定を追加
4.04版　2015.05.29 総合大会、K-MASTERの設定を追加 
                   空白文字削除定義を追加
                   縦書き・横書き混在記事用divの高さ指定を変更
4.05版　2015.06.30 大相撲の設定を追加
4.06版　2015.07.30 五輪・アジア大会の設定を追加
                   横書きのみ9pt表示するスタイル指定テンプレートCommonCSS_YokoSmall_SETを追加
4.07版　2015.09.30 中央競馬の成績Ｃに、騎手名情報の表示切り替えを追加
                   CSSの記述を更新（縦書き、フォント指定）
4.08版　2015.●.● OikomiStartクラス設定を追加
================================================================================-->
	<!--===============================================================================================-->
	<!-- 独自スタイルシートインポートエリア                                                            -->
	<!-- 以下に加盟社独自のimport定義を記載                                                            -->
	<!-- 以下<xsl:import href･･･>のコメントアウト部分を変更してご使用ください                          -->
	<!-- ==================== ##EXT_IMPORT_START## ==== ※この行は削除不可※ ==========================-->
	<!-- <xsl:import href="../Stylesheets/commonTest.xsl"/> -->
	<!-- ==================== ##EXT_IMPORT_END## ====== ※この行は削除不可※ ==========================-->
	<!--===============================================================================================-->
	<!--独自テンプレート追加エリア　                                                                   -->
	<!-- 以下に加盟社独自のテンプレートを記載してください。共通ヘッダーの上に挿入します                -->
	<!-- コメントアウト部分を変更してご使用ください                                                    -->
	<!--===============================================================================================-->
	<xsl:template name="commonTemplate_SET">
		<!-- <xsl:call-template name="TestTemplate"/>   -->
		<xsl:text>独自テンプレートエリア</xsl:text><br/>
		<xsl:text>独自テンプレートエリア</xsl:text><br/>
		<xsl:text>独自テンプレートエリア</xsl:text><br/>
		<xsl:text>独自テンプレートエリア</xsl:text><br/>
		<xsl:text>独自テンプレートエリア</xsl:text><br/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 独自テンプレートエリア使用時、追加分の想定行数を設定する。                                    -->
	<!-- 素材ＩＤ、バーコードなどを表示する場合には5（推奨値）を設定ください                           -->
	<!-- ※指定行数分、一頁目の本文行数を減らします                                                    -->
	<!--===============================================================================================-->
	<xsl:variable name="COMMON_TEMPLATE_LINE_SET">
		<xsl:value-of select="5"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 表示切替（可変）-->
	<!--===============================================================================================-->
	<!-- SHORI_F_SETの設定に応じて表示する-->
	<!-- SHORI_F_SET「1」：「プレーンテキスト」　　　　　　　　　 -->
	<!-- SHORI_F_SET「2」：「プレーンテキスト」＋「一覧」　　　　 -->
	<!-- SHORI_F_SET「3」：「一覧」※3を指定した場合、次項目「共通ヘッダー表示切替」を「0」にしてください。-->
	<!-- SHORI_F_SET「7」：「確認」　　　　　　　　　　　　　　　 -->
	<!-- SHORI_F_SET「8」：「縦追い込み」　　 　　　　   ※「縦追い込み」が存在しない記事では「確認」を表示-->
	<!-- SHORI_F_SET「9」： 検証用「プレーンテキスト」＋「確認」＋「一覧」-->
	<xsl:variable name="SHORI_F_SET">
		<!-- ここを変更する（半角） -->
		<xsl:value-of select="1"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 共通ヘッダー表示切替-->
	<!--===============================================================================================-->
	<!-- SHORI_F_SETによって内容情報部の表示を切り替える-->
	<!-- NAIYOU_F_SET「0」：共通ヘッダーを非表示　-->
	<!-- NAIYOU_F_SET「1」：共通ヘッダーを表示　-->
	<xsl:variable name="NAIYOU_F_SET">
		<xsl:value-of select="1"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 表示フォント-->
	<!--===============================================================================================-->
	<!-- 縦表示用フォント -->
	<xsl:template name="CommonFONT_KAKUNIN2_TATE_SET">
		<xsl:value-of select="'U-PRESS, &quot;U-PRESS 標準&quot;'"/>
	</xsl:template>
	<!-- 横表示用フォント -->
	<xsl:template name="CommonFONT_KAKUNIN2_YOKO_SET">
		<xsl:value-of select="'U-PRESS, &quot;U-PRESS 標準&quot;'"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 印刷方向定義-->
	<!--===============================================================================================-->
	<xsl:variable name="PRINT_F_SET">
		<!-- PRINT_F_SET「1」：Ａ４縦方向  -->
		<!-- PRINT_F_SET「2」：Ａ４横方向　-->
		<xsl:value-of select="2"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 縦書き/横書き設定（共通） -->
	<!--===============================================================================================-->
	<xsl:variable name="PTEXT_TATEYOKO_SET">
		<!-- PTEXT_TATEYOKO_SET「1」：縦書き -->
		<!-- PTEXT_TATEYOKO_SET「2」：横書き -->
		<xsl:value-of select="1"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 縦書き １行最大折り返し文字数（Ａ４タテ印刷／Ａ４ヨコ印刷共通） -->
	<!-- ※「9」～「15」を設定して下さい -->
	<!--===============================================================================================-->
	<!-- ============= 縦フォーマット表示 ================= -->
	<xsl:variable name="PRINT_MAXTEXT_TATE_FORMAT_SET">
		<xsl:value-of select="15"/>
	</xsl:variable>
	<!-- ============= 縦追い込み表示 ================= -->
	<xsl:variable name="PRINT_MAXTEXT_OIKOMI_SET">
		<xsl:value-of select="11"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 縦書きルーラー表示有無-->
	<!--===============================================================================================-->
	<xsl:variable name="PRINT_RULER_SET">
		<!-- PRINT_RULER_SET「0」：ルーラー表示なし  -->
		<!-- PRINT_RULER_SET「1」：ルーラー表示あり　-->
		<xsl:value-of select="1"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 行数カウント表示有無-->
	<!--===============================================================================================-->
	<xsl:variable name="ADD_LINE_COUNT_FLG_SET">
		<!-- ADD_LINE_COUNT_FLG_SET「0」：行数表示なし  -->
		<!-- ADD_LINE_COUNT_FLG_SET「1」：行数表示あり　-->
		<xsl:value-of select="1"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- Pタグ"MatchStart"class設定有無-->
	<!--===============================================================================================-->
	<xsl:variable name="ADD_MATCHSTART_CLASS_SET">
		<!-- ADD_MATCHSTART_CLASS_SET「0」：class設定なし  -->
		<!-- ADD_MATCHSTART_CLASS_SET「1」：縦書き時のみclass設定あり　-->
		<!-- ADD_MATCHSTART_CLASS_SET「2」：横書き時のみclass設定あり　-->
		<!-- ADD_MATCHSTART_CLASS_SET「3」：class設定あり　-->
		<xsl:value-of select="0"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- Pタグ"OikomiStart"class設定有無-->
	<!--===============================================================================================-->
	<xsl:variable name="ADD_OIKOMI_CLASS_SET">
		<!-- ADD_OIKOMI_CLASS_SET「0」：class設定なし  -->
		<!-- ADD_OIKOMI_CLASS_SET「1」：縦書き時のみclass設定あり　-->
		<!-- ADD_OIKOMI_CLASS_SET「2」：横書き時のみclass設定あり　-->
		<!-- ADD_OIKOMI_CLASS_SET「3」：class設定あり　-->
		<xsl:value-of select="0"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- １行最大折り返し文字数／１ページ最大行数定義（共通） -->
	<!-- ※個別指定が無い場合、本設定が適用されます。  -->
	<!--===============================================================================================-->
	<!-- ============= Ａ４タテ印刷の場合の設定 ================= -->
	<!-- 縦書き表示　１行最大折り返し文字数 -->
	<xsl:variable name="PRINT_MAXTEXT_TATE_TATE_SET">
		<xsl:value-of select="$PRINT_MAXTEXT_TATE_FORMAT_SET"/>
	</xsl:variable>
	<!-- 縦書き表示　１ページ最大行数 -->
	<xsl:variable name="PRINT_MAXLINES_TATE_TATE_SET">
		<xsl:value-of select="34"/>
	</xsl:variable>
	<!-- 横書き表示　１行最大折り返し文字数 -->
	<xsl:variable name="PRINT_MAXTEXT_TATE_YOKO_SET">
		<xsl:value-of select="38"/>
	</xsl:variable>
	<!-- 横書き表示　１ページ最大行数 -->
	<xsl:variable name="PRINT_MAXLINES_TATE_YOKO_SET">
		<xsl:value-of select="50"/>
	</xsl:variable>
	<!-- ============= Ａ４ヨコ印刷の場合の設定 ================= -->
	<!-- 縦書き表示　１行最大折り返し文字数 -->
	<xsl:variable name="PRINT_MAXTEXT_YOKO_TATE_SET">
		<xsl:value-of select="$PRINT_MAXTEXT_TATE_FORMAT_SET"/>
	</xsl:variable>
	<!-- 縦書き表示　１ページ最大行数 -->
	<xsl:variable name="PRINT_MAXLINES_YOKO_TATE_SET">
		<xsl:value-of select="52"/>
	</xsl:variable>
	<!-- 横書き表示　１行最大折り返し文字数 -->
	<xsl:variable name="PRINT_MAXTEXT_YOKO_YOKO_SET">
		<xsl:value-of select="58"/>
	</xsl:variable>
	<!-- 横書き表示　１ページ最大行数 -->
	<xsl:variable name="PRINT_MAXLINES_YOKO_YOKO_SET">
		<xsl:value-of select="33"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 文字サイズ9ptの場合の１行最大折り返し文字数／１ページ最大行数定義（共通） -->
	<!-- CommonCSS_FontSizeSmall_SETで使用。Ａ４タテで横表の１行に表示可能な最大文字数 -->
	<!--===============================================================================================-->
	<!-- ======================== 横書き ======================== -->
	<!-- ============= Ａ４タテ印刷の場合の設定 ================= -->
	<!-- 横書き9pt表示　１行最大折り返し文字数 -->
	<xsl:variable name="PRINT_MAXTEXT_FontSizeSmall_SET">
		<xsl:value-of select="55"/>
	</xsl:variable>
	<!-- 横書き9pt表示　１ページ最大行数 -->
	<xsl:variable name="PRINT_MAXLINES_FontSizeSmall_SET">
		<xsl:value-of select="66"/>
	</xsl:variable>
	<!-- ============= Ａ４ヨコ印刷の場合の設定 ================= -->
	<!-- 横書き9pt表示　１行最大折り返し文字数 -->
	<xsl:variable name="PRINT_MAXTEXT_FontSizeSmall_A4YOKO_SET">
		<xsl:value-of select="80"/>
	</xsl:variable>
	<!-- 横書き9pt表示　１ページ最大行数 -->
	<xsl:variable name="PRINT_MAXLINES_FontSizeSmall_A4YOKO_SET">
		<xsl:value-of select="43"/>
	</xsl:variable>
	<!-- ======================== 縦書き ======================== -->
	<!-- ============= Ａ４タテ印刷の場合の設定 ================= -->
	<!-- 縦書き9pt表示　１ページ最大行数 -->
	<xsl:variable name="PRINT_MAXTATELINES_FontSizeSmall_SET">
		<xsl:value-of select="47"/>
	</xsl:variable>
	<!-- ============= Ａ４ヨコ印刷の場合の設定 ================= -->
	<!-- 縦書き9pt表示　１ページ最大行数 -->
	<xsl:variable name="PRINT_MAXTATELINES_FontSizeSmall_A4YOKO_SET">
		<xsl:value-of select="72"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 縦書きのdivを１頁に１つ割り付ける場合の１行最大折り返し文字数（共通） -->
	<!-- １行最大折り返し文字数が18文字を超える場合に使用する。 -->
	<!--===============================================================================================-->
	<!-- ============= Ａ４タテ/Ａ４ヨコ共通の設定 ================= -->
	<!-- 縦書き(行長)12pt表示　１行最大折り返し文字数 -->
	<xsl:variable name="PRINT_MAXTATETEXT_Long_SET">
		<xsl:value-of select="25"/>
	</xsl:variable>
	<!-- 縦書き(行長)9pt表示　１行最大折り返し文字数 -->
	<xsl:variable name="PRINT_MAXTATETEXT_Long_FontSizeSmall_SET">
		<xsl:value-of select="27"/>
	</xsl:variable>
	<!--===============================================================================================-->
	<!-- 共通ヘッダーを表示する場合に、横書きの場合の１ページ目行数を短くする行数を取得 -->
	<!--===============================================================================================-->
	<!--<xsl:variable name="NAIYOU_LINE_SET">
    <xsl:value-of select="3 + $NAIYOU_LINE_COUNT_UTL + $COMMON_TEMPLATE_LINE_SET"/>
  </xsl:variable>-->
	<xsl:template name="NAIYOU_LINE_SET">
		<xsl:variable name="NAIYOU_LINE_COUNT_UTL">
			<xsl:call-template name="NAIYOU_LINE_COUNT_UTL"/>
		</xsl:variable>
		<xsl:value-of select="3 + $NAIYOU_LINE_COUNT_UTL + $COMMON_TEMPLATE_LINE_SET"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!--共通で使用するスタイルを定義-->
	<!--===============================================================================================-->
	<xsl:template name="CommonCSS_SET">
    .ptextYOKO p{
                      margin-top: 0.1em;
                      margin-bottom: 0.1em;
                      margin-left: 0;
                      margin-right: 0;
                      line-height: 1.1em;
                      height: 1.1em;
                      }
    .ptextTATE p,.pTATERuler p,.ptextTATELONG p,.ptextYOKOTATE p{
                      margin-top: 0;
                      margin-bottom: 0;
                      margin-left: 0.1em;
                      margin-right: 0.1em;
                      line-height: 1em;
                      width: 1em;
                      }
    table.commonheader{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_YOKO_SET"/>;
                      }
    div.pageBreak{
                      page-break-after: always;
                      }
    .pageBreak p{
                      display:none;
                      }
    hr.pageBreakAfter{
                      page-break-after: always;
                      margin-top: 1.0em;
                      margin-bottom: 1.0em;
                      }
    div.ptextYOKO{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_YOKO_SET"/>;
                      font-size: 12pt;
                      margin-top: 0.5em;
                      margin-bottom: 0em;
                      }
    div.ptextTATE{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 12pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 16em; <!-- PRINT_MAXTEXTに対応した設定が必要-->
		<xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 39em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 59em;
      </xsl:otherwise>
		</xsl:choose>
                      }
    div.pTATERuler{
                      page-break-after: avoid;
                      page-break-inside: avoid;  
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 12pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 1.5em;
    <xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 39em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 59em;
      </xsl:otherwise>
		</xsl:choose> 
                      }
    div.ptextTATELONG{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 12pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 25em; <!-- PRINT_MAXTEXTに対応した設定が必要-->
		<xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 39em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 59em;
      </xsl:otherwise>
		</xsl:choose>
                      }
    div.ptextYOKOTATE{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 12pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      <!-- height: 15em; -->
                      height: <xsl:value-of select="$PRINT_MAXTEXT_TATE_FORMAT_SET"/>em;
		<xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 39em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 59em;
      </xsl:otherwise>
		</xsl:choose>
                      }
    span.yoko{
                      margin: 0em;
                      writing-mode: horizontal-tb;
                      writing-mode: lr-tb;
                      -webkit-writing-mode: horizontal-tb;
                      -ms-writing-mode: lr-tb;
                      width: 1em;
                      line-height: 1em;
                      }
  </xsl:template>
	<xsl:template name="CommonCSS_FontSizeSmall_SET">
    .ptextYOKO p{
                      margin-top: 0.1em;
                      margin-bottom: 0.1em;
                      margin-left: 0;
                      margin-right: 0;
                      line-height: 1.1em;
                      height: 1.1em;
                      }
    .ptextTATE p,.pTATERuler p,.ptextTATELONG p{
                      margin-top: 0;
                      margin-bottom: 0;
                      margin-left: 0.1em;
                      margin-right: 0.1em;
                      line-height: 1em;
                      width: 1em;
                      }
    table.commonheader{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_YOKO_SET"/>;
                      }
    div.pageBreak{
                      page-break-after: always;
                      }
    .pageBreak p{
                      display:none;
                      }
    hr.pageBreakAfter{
                      page-break-after: always;
                      margin-top: 1.0em;
                      margin-bottom: 1.0em;
                      }
    div.ptextYOKO{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_YOKO_SET"/>;
                      font-size: 9pt;
                      margin-top: 0.5em;
                      margin-bottom: 0em;
                      letter-spacing: -0.05em; /*文字間隔*/
                      }
    div.ptextTATE{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 9pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 18em; <!-- PRINT_MAXTEXTに対応した設定が必要-->
		<xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 53em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 80em;
      </xsl:otherwise>
		</xsl:choose>
                      }
    div.pTATERuler{
                      page-break-after: avoid;
                      page-break-inside: avoid;  
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 9pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 1.5em;
    <xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 53em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 80em;
        </xsl:otherwise>
		</xsl:choose> 
                      }
    div.ptextTATELONG{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 9pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 27em; <!-- PRINT_MAXTEXTに対応した設定が必要-->
		<xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 53em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 80em;
      </xsl:otherwise>
		</xsl:choose>
                      }
    span.yoko{
                      margin: 0em;
                      writing-mode: horizontal-tb;
                      writing-mode: lr-tb;
                      -webkit-writing-mode: horizontal-tb;
                      -ms-writing-mode: lr-tb;
                      width: 1em;
                      line-height: 1em;
                      }
  </xsl:template>
	<xsl:template name="CommonCSS_YokoSmall_SET">
    .ptextYOKO p{
                      margin-top: 0.1em;
                      margin-bottom: 0.1em;
                      margin-left: 0;
                      margin-right: 0;
                      line-height: 1.1em;
                      height: 1.1em;
                      }
    .ptextTATE p,.pTATERuler p,.ptextTATELONG p,.ptextYOKOTATE p{
                      margin-top: 0;
                      margin-bottom: 0;
                      margin-left: 0.1em;
                      margin-right: 0.1em;
                      line-height: 1em;
                      width: 1em;
                      }
    table.commonheader{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_YOKO_SET"/>;
                      }
    div.pageBreak{
                      page-break-after: always;
                      }
    .pageBreak p{
                      display:none;
                      }
    hr.pageBreakAfter{
                      page-break-after: always;
                      margin-top: 1.0em;
                      margin-bottom: 1.0em;
                      }
    div.ptextYOKO{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_YOKO_SET"/>;
                      font-size: 9pt;
                      margin-top: 0.5em;
                      margin-bottom: 0em;
                      letter-spacing: -0.05em; /*文字間隔*/
                      }
    div.ptextTATE{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 12pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 16em; <!-- PRINT_MAXTEXTに対応した設定が必要-->
		<xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 39em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 59em;
      </xsl:otherwise>
		</xsl:choose>
                      }
    div.pTATERuler{
                      page-break-after: avoid;
                      page-break-inside: avoid;  
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 12pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 1.5em;
    <xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 39em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 59em;
      </xsl:otherwise>
		</xsl:choose> 
                      }
    div.ptextTATELONG{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 12pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      height: 25em; <!-- PRINT_MAXTEXTに対応した設定が必要-->
		<xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 39em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 59em;
      </xsl:otherwise>
		</xsl:choose>
                      }
    div.ptextYOKOTATE{
                      font-family: <xsl:call-template name="CommonFONT_KAKUNIN2_TATE_SET"/>;
                      font-size: 12pt;
                      writing-mode: vertical-rl;
                      writing-mode: tb-rl;
                      -webkit-writing-mode: vertical-rl;
                      -ms-writing-mode: tb-rl;
                      <!-- height: 15em; -->
                      height: <xsl:value-of select="$PRINT_MAXTEXT_TATE_FORMAT_SET"/>em;
		<xsl:choose>
			<xsl:when test="$PRINT_F_SET=1">
				<!-- 印刷方向：Ａ４縦方向の場合 -->
                      width: 39em;
      </xsl:when>
			<xsl:otherwise>
				<!-- 印刷方向：Ａ４横方向の場合 -->
                      width: 59em;
      </xsl:otherwise>
		</xsl:choose>
                      }
    span.yoko{
                      margin: 0em;
                      writing-mode: horizontal-tb;
                      writing-mode: lr-tb;
                      -webkit-writing-mode: horizontal-tb;
                      -ms-writing-mode: lr-tb;
                      width: 1em;
                      line-height: 1em;
                      }
  </xsl:template>
	<!--###############################################################################################-->
	<!--■縦書き/横書き設定（個別）■-->
	<!--※ PTEXT_TATEYOKO_SETに「0」を設定した場合、共通設定の設定が有効になります-->
	<!-- 「0」：共通設定を使用 -->
	<!-- 「1」：縦書き -->
	<!-- 「2」：横書き -->
	<!--###############################################################################################-->
	<!-- ========================================================== -->
	<!-- 野球                                                       -->
	<!-- ========================================================== -->
	<!-- 野球：個人テーブル【補足記録】-->
	<xsl:template name="PTEXT_TATEYOKO_SPYKT_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 野球：イニング-->
	<xsl:template name="PTEXT_TATEYOKO_SPYIN1_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- ゴルフ                                                     -->
	<!-- ========================================================== -->
	<!-- ゴルフ：アマ成績-->
	<xsl:template name="PTEXT_TATEYOKO_SPGPGA_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ゴルフ：バイホール-->
	<xsl:template name="PTEXT_TATEYOKO_SPGBH_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ゴルフ：マッチプレー-->
	<xsl:template name="PTEXT_TATEYOKO_SPGPM_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ゴルフ：都道府県対抗アマ個人成績-->
	<xsl:template name="PTEXT_TATEYOKO_SPGPGK_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ゴルフ：都道府県対抗アマ団体成績-->
	<xsl:template name="PTEXT_TATEYOKO_SPGAD_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ゴルフ：プロ成績-->
	<xsl:template name="PTEXT_TATEYOKO_SPGPGS_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 競馬                                                       -->
	<!-- ========================================================== -->
	<!-- 競馬：馬別上がりタイム　-->
	<xsl:template name="PTEXT_TATEYOKO_SPUAT_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競馬：出馬表　-->
	<xsl:template name="PTEXT_TATEYOKO_SPUFP_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競馬：事故情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPUJJ_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競馬：頭数表　-->
	<xsl:template name="PTEXT_TATEYOKO_SPUNH_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競馬：入場・人員　-->
	<xsl:template name="PTEXT_TATEYOKO_SPUNN_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競馬：終了通知　-->
	<xsl:template name="PTEXT_TATEYOKO_SPUOW_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競馬：成績表Ｃ　-->
	<xsl:template name="PTEXT_TATEYOKO_SPUSZ_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競馬：通信文　-->
	<xsl:template name="PTEXT_TATEYOKO_SPUTS_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 競艇                                                       -->
	<!-- ========================================================== -->
	<!-- 競艇：事故情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPBJJ_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競艇：終了通知　-->
	<xsl:template name="PTEXT_TATEYOKO_SPBOW_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競艇：競走変更情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPBPC_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競艇：選手欠場情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPBSC_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競艇：出走表　-->
	<xsl:template name="PTEXT_TATEYOKO_SPBFP_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 競輪                                                       -->
	<!-- ========================================================== -->
	<!-- 競輪：事故情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPVJJ_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競輪：終了通知　-->
	<xsl:template name="PTEXT_TATEYOKO_SPVOW_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競輪：競走変更情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPVPC_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競輪：選手欠場情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPVSC_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競輪：場外発売情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPVUJ_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競輪：誘導員情報　-->
	<xsl:template name="PTEXT_TATEYOKO_SPVYJ_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 競輪：出走表　-->
	<xsl:template name="PTEXT_TATEYOKO_SPVFP_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- Ｊリーグ                                                   -->
	<!-- ========================================================== -->
	<!-- ＪＬ組別最終順位-->
	<xsl:template name="PTEXT_TATEYOKO_JL_MainTeamRanking_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ＪＬスコア-->
	<xsl:template name="PTEXT_TATEYOKO_JL_MainOfficial_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ＪＬ試合結果Ａタイプ-->
	<xsl:template name="PTEXT_TATEYOKO_JL_MainMatchResultA_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ＪＬ試合結果Bタイプ（一部横書き固定）-->
	<xsl:template name="PTEXT_TATEYOKO_JL_MainMatchResultB_Score_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ＪＬ速報全試合分、ＪＬ本日の予定、ＪＬ○日の結果-->
	<xsl:template name="PTEXT_TATEYOKO_JL_MainNewsFlashMatchAll_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ＪＬ速報（試合単位）-->
	<xsl:template name="PTEXT_TATEYOKO_JL_MainNewsFlashMatch_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 地方競馬                                                   -->
	<!-- ========================================================== -->
	<!-- 地方競馬：馬別上がりタイム　-->
	<xsl:template name="PTEXT_TATEYOKO_CKUAT_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 地方競馬：通信文Ａ　-->
	<xsl:template name="PTEXT_TATEYOKO_CKUTA_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 地方競馬：通信文Ｃ　-->
	<xsl:template name="PTEXT_TATEYOKO_CKUTC_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 地方競馬：成績表Ｃ　-->
	<xsl:template name="PTEXT_TATEYOKO_CKUSZ_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 地方競馬：出馬表　-->
	<xsl:template name="PTEXT_TATEYOKO_CKUFP_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- オートレース                                               -->
	<!-- ========================================================== -->
	<!-- オートレース：通信文　-->
	<xsl:template name="PTEXT_TATEYOKO_ARAJJ_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- オートレース：出走表　-->
	<xsl:template name="PTEXT_TATEYOKO_ARAFP_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- Ｋ－ＬＯＴ                                                 -->
	<!-- ========================================================== -->
	<!-- サッカーくじ（トト指定試合、トトゴール指定試合）　-->
	<xsl:template name="PTEXT_TATEYOKO_KL_DOPEN_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 宝くじ　-->
	<xsl:template name="PTEXT_TATEYOKO_KL_PublicLottery_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 名簿                                                       -->
	<!-- ========================================================== -->
	<!-- 名簿 -->
	<xsl:template name="PTEXT_TATEYOKO_CM_NAMELIST_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 総体                                                       -->
	<!-- ========================================================== -->
	<!-- 順位型 -->
	<xsl:template name="PTEXT_TATEYOKO_SS_OI_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 終番通知 -->
	<xsl:template name="PTEXT_TATEYOKO_SS_SH_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 対戦型 -->
	<xsl:template name="PTEXT_TATEYOKO_SS_TA_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 天皇杯・皇后杯 -->
	<xsl:template name="PTEXT_TATEYOKO_SS_TE_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- イニング型 -->
	<xsl:template name="PTEXT_TATEYOKO_SS_YA_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 野球テーブル -->
	<xsl:template name="PTEXT_TATEYOKO_SS_MB_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 新総体                                                       -->
	<!-- ========================================================== -->
	<!-- 順位型 -->
	<!--<xsl:template name="PTEXT_TATEYOKO_KM_V10_TS_SET">-->
	<xsl:template name="PTEXT_TATEYOKO_ST_CS_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 記事形式（終番通知・ローカル一括該当なし） -->
	<!--<xsl:template name="PTEXT_TATEYOKO_KM_V10_TX_SET">-->
	<xsl:template name="PTEXT_TATEYOKO_ST_CX_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 対戦型 -->
	<!--<xsl:template name="PTEXT_TATEYOKO_KM_V10_TM_SET">-->
	<xsl:template name="PTEXT_TATEYOKO_ST_CM_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 天皇杯・皇后杯 -->
	<!--<xsl:template name="PTEXT_TATEYOKO_KM_V10_TS_TE_SET">-->
	<xsl:template name="PTEXT_TATEYOKO_ST_TE_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- イニング型 -->
	<!--<xsl:template name="PTEXT_TATEYOKO_KM_V10_TM070T_SET">-->
	<xsl:template name="PTEXT_TATEYOKO_ST_CM702T_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 野球テーブル -->
	<xsl:template name="PTEXT_TATEYOKO_ST_MB_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- K-MASTER                                                   -->
	<!-- ========================================================== -->
	<!-- 日常記録・順位型 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V12_NS_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 日常記録・対戦型 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V12_NM_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 日常記録・イニング -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V12_NM070_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 日常記録・MLB打席別結果 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V12_NO001_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 日常記録・テーブル -->
	<xsl:template name="PTEXT_TATEYOKO_KM_Table_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 大会記録・順位型 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V10_TS_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 大会記録・対戦型 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V10_TM_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 大会記録・イニング -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V10_TM070T_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 大会記録・天皇杯・皇后杯 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V10_TS_TE_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 大会記録・記事形式（終番通知・ローカル一括該当なし） -->
	<xsl:template name="PTEXT_TATEYOKO_KM_V10_TX_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- Ｗ杯サッカー記録・スコア -->
	<xsl:template name="PTEXT_TATEYOKO_KM_WCUP_WM903_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- Ｗ杯サッカー記録・テーブル -->
	<xsl:template name="PTEXT_TATEYOKO_KM_WCUP_MT906_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- Ｗ杯サッカー記録・組別最終順位 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_WCUP_MH908_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- Ｗ杯サッカー記録・○日の結果 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_WCUP_WM901_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- Ｗ杯サッカー記録・日程 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_WCUP_WO912_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- Ｗ杯サッカー記録・速報 -->
	<xsl:template name="PTEXT_TATEYOKO_KM_WCUP_WM904_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 五輪・アジア大会                                           -->
	<!-- ========================================================== -->
	<!-- 順位型 -->
	<xsl:template name="PTEXT_TATEYOKO_OL_OI_SET">
		<!-- 「0」：共通設定を使用 -->
		<!-- 「1」：紙面レイアウト　※縦表示+横表示（横表示レイアウトが存在する記事のみ） -->
		<!-- 「2」：校閲用横表示 -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 対戦型 -->
	<xsl:template name="PTEXT_TATEYOKO_OL_TA_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- イニング型 -->
	<xsl:template name="PTEXT_TATEYOKO_OL_YA_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 記事形式（終番通知） -->
	<xsl:template name="PTEXT_TATEYOKO_OL_SH_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- テーブル型 -->
	<xsl:template name="PTEXT_TATEYOKO_OL_TABLE_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- ========================================================== -->
	<!-- 大相撲                                                     -->
	<!-- ========================================================== -->
	<!-- 郷土力士取組（04．郷土力士新番付） -->
	<xsl:template name="PTEXT_TATEYOKO_OS04_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 郷土力士取組（06．対戦型） -->
	<xsl:template name="PTEXT_TATEYOKO_OS06_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 幕下以下取組（07．対戦型） -->
	<xsl:template name="PTEXT_TATEYOKO_OS07_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 十両取組（08．対戦型） -->
	<xsl:template name="PTEXT_TATEYOKO_OS08_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 中入り取組（09．対戦型） -->
	<xsl:template name="PTEXT_TATEYOKO_OS09_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 郷土力士勝負（階級別）、郷土力士勝負（まとめ）（10、11．対戦型） -->
	<xsl:template name="PTEXT_TATEYOKO_OS10_OS11_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 幕下以下勝負（12．対戦型） -->
	<xsl:template name="PTEXT_TATEYOKO_OS12_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 勝負、まとめ勝負（13、14．対戦型） -->
	<xsl:template name="PTEXT_TATEYOKO_OS13_OS14_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 外国力士成績表（16．その他） -->
	<xsl:template name="PTEXT_TATEYOKO_OS16_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 優勝三賞受賞力士（17．その他） -->
	<xsl:template name="PTEXT_TATEYOKO_OS17_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 階級別成績上位力士（18．その他） -->
	<xsl:template name="PTEXT_TATEYOKO_OS18_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 幕下以下全成績（20．その他） -->
	<xsl:template name="PTEXT_TATEYOKO_OS20_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■ＪＬ定義■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- ＪＬスコア　「スコア」　最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_JL_MainOfficial_SET">
		<!-- 「0」： JL個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： JL個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_JL_MainOfficial_SET">
		<!-- PRINT_MAXTEXT_FLG_JL_MainOfficial_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_JL_MainOfficial_SET =「0」の場合は共通定義を使用する -->
		<!-- ※「9」～「15」の奇数を設定して下さい -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--=======================================================================================================-->
	<!--ＪＬ試合結果Ａタイプ・ＪＬ試合結果Ｂタイプ・メンバー表・速報（試合単位）共通　選手名表記-->
	<!-- 「1」：３字表記  -->
	<!-- 「2」：５字表記  -->
	<!-- 「3」：フル表記（横書きは姓＋名を使用、縦書き時はFormalを使用し追い込み表示する）      -->
	<!--   ※「得点者」は本設定によらず常に追い込み表示する。                                   -->
	<!-- 　※フル表記を指定した場合の、「テーブル」「ＰＫ戦」「メンバー表」については、         -->
	<!--     表示する最大長を定義する[テーブルレイアウト選手名最大長]の設定を参照する。         -->
	<!-- 　　最大長を超える場合は、テーブルには最大長までの文字を表示し、注釈表記する。         -->
	<!--=======================================================================================================-->
	<!-- 下記（メンバー表、テーブル）以外の選手名表記 -->
	<xsl:template name="JL_PlayerName_Display_SET">
		<xsl:value-of select="1"/>
	</xsl:template>
	<!-- メンバー表、テーブルの選手名表記 -->
	<xsl:template name="JL_MemberTable_PlayerName_Display_SET">
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--【「3（フル表記）」指定時のみ有効】テーブルレイアウト選手名最大長-->
	<!-- 「テーブル」「ＰＫ戦」「メンバー表」での選手名最大長（超えた場合は注釈表記）-->
	<xsl:template name="JL_PlayerNameMaxLength_SET">
		<xsl:value-of select="10"/>
	</xsl:template>
	<!--=======================================================================================================-->
	<!--ＪＬ試合結果Ａタイプ・ＪＬ試合結果Ｂタイプ共通　「テーブル」控え選手表示／非表示-->
	<!-- 「0」：控え選手非表示 -->
	<!-- 「1」：控え選手表示   -->
	<!--=======================================================================================================-->
	<xsl:template name="JL_TableHikae_Display_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--=======================================================================================================-->
	<!--ＪＬ試合結果Ａタイプ・ＪＬ試合結果Ｂタイプ・速報（試合単位）共通　時間表記（通算表記／前後半表記）-->
	<!-- 「1」：通算表記  -->
	<!-- 「2」：前後半表記  -->
	<!--=======================================================================================================-->
	<xsl:template name="JL_RecordTime_Display_SET">
		<xsl:value-of select="2"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- ＪＬ試合結果Ｂタイプ　「スコア」　最大折り返し文字数定義-->
	<!-- 縦書き表示の場合は、以下にも折り返し文字数設定が適用されます-->
	<!-- ・スコアと同一ページに表示する得点者・観衆・天気 -->
	<!-- ・[選手名表記：フル]の場合の交代・警告・退場・審判 -->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_JL_MainMatchResultB_Score_SET">
		<!-- 「0」： 下記の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： 下記の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_JL_MainMatchResultB_Score_SET">
		<!-- PRINT_MAXTEXT_FLG_JL_MainMatchResultB_Score_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_JL_MainMatchResultB_Score_SET =「0」の場合は共通定義を使用する -->
		<!--※「9」～「15」の奇数を設定して下さい -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- ＪＬ速報全試合分、ＪＬ本日の予定、ＪＬ○日の結果　最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_JL_MainNewsFlashMatchAll_SET">
		<!-- 「0」： JL個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： JL個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_JL_MainNewsFlashMatchAll_SET">
		<!-- PRINT_MAXTEXT_FLG_JL_MainNewsFlashMatchAll_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_JL_MainNewsFlashMatchAll_SET =「0」の場合は共通定義を使用する -->
		<!-- ※「9」～「15」の奇数を設定して下さい -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 速報（試合単位）　「スコア」　最大折り返し文字数定義-->
	<!-- 縦書き表示の場合は、以下にも折り返し文字数設定が適用されます-->
	<!-- ・スコアと同一ページに表示する得点者・観衆・天気 -->
	<!-- ・[選手名表記：フル]の場合の交代・警告・退場 -->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_JL_JLMainNewsFlashMatch_Score_SET">
		<!-- 「0」： 下記の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： 下記の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_JL_JLMainNewsFlashMatch_Score_SET">
		<!-- PRINT_MAXTEXT_FLG_JL_JLMainNewsFlashMatch_Score_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_JL_JLMainNewsFlashMatch_Score_SET =「0」の場合は共通定義を使用する -->
		<!-- ※「9」～「15」の奇数を設定して下さい -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--=======================================================================================================-->
	<!--得点ランキング　選手名表記-->
	<!-- 「1」：３字表記  -->
	<!-- 「2」：５字表記  -->
	<!-- 「3」：フル表記（横書きは姓＋名、縦書き時はFormalを使用）  -->
	<!-- 　※フル表記を指定した場合、テーブルにて表示する最大長を定義する次項目の設定を参照する。  -->
	<!-- 　　最大長を超える場合は、テーブルには最大長までの文字を表示し、注釈表記する。  -->
	<!--=======================================================================================================-->
	<xsl:template name="JL_MainRanking_PlayerName_Display_SET">
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--【「3（フル表記）」指定時のみ有効】-->
	<!-- 得点ランキング　選手名最大長（超えた場合は注釈表記）-->
	<xsl:template name="JL_MainRanking_PlayerNameMaxLength_SET">
		<xsl:value-of select="10"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■野球定義■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- イニング（SPKdSPYIN1_KAKUNIN2.xsl）四死球・安打の表示・非表示を定義　-->
	<!--===============================================================================================-->
	<xsl:template name="editBalls">
		<!-- １：「球」を表示
         ２：「球」を非表示    -->
		<xsl:value-of select="2"/>
	</xsl:template>
	<xsl:template name="editHits">
		<!-- １：「安打」を表示
         ２：「安打」を非表示    -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 個人テーブル（SPKdSPYKT_KAKUNIN2.xsl）表示項目制御　-->
	<!-- 「1」 ：Ａ１　（３項目） -->
	<!-- 「2」 ：Ａ１Ｓ（３項目）＋学年（高校）、出身校（社会人）、学年・出身校（大学） -->
	<!-- 「3」 ：Ａ２　（３項目＋本塁打、打率、防御率） -->
	<!-- 「4」 ：Ａ３Ｓ（３項目＋本塁打、打率、防御率）＋学年（高校）、出身校（社会人）、学年・出身校（大学） -->
	<!-- 「5」 ：Ｂ１　（５項目） -->
	<!-- 「6」 ：Ｂ１Ｓ（５項目）＋学年（高校）、出身校（社会人） -->
	<!-- 「7」 ：Ｂ２　（５項目＋本塁打、打率、防御率） -->
	<!-- 「8」 ：Ｂ３Ｓ（５項目＋本塁打、打率、防御率）＋学年（高校）、出身校（社会人）-->
	<!-- 「9」 ：Ｃ１  （９項目）-->
	<!-- 「10」：Ｃ２  （９項目＋本塁打、打率、防御率）-->
	<!-- 「11」：Ｃ３Ｓ（９項目＋本塁打、打率、防御率）＋学年（高校）、出身校（社会人）-->
	<!-- 「12」：全表示 -->
	<!-- ※ただし、試合区分によりデータ有無に差違があるため、表示されない項目が存在する -->
	<!--===============================================================================================-->
	<!-- 試合区分：プロ -->
	<xsl:template name="SPYKT_PRO_SET">
		<xsl:value-of select="12"/>
	</xsl:template>
	<!-- 試合区分：高校 -->
	<xsl:template name="SPYKT_KOUKOU_SET">
		<xsl:value-of select="12"/>
	</xsl:template>
	<!-- 試合区分：社会人 -->
	<xsl:template name="SPYKT_TOSHI_SET">
		<xsl:value-of select="12"/>
	</xsl:template>
	<!-- 試合区分：大学 -->
	<xsl:template name="SPYKT_DAIGAKU_SET">
		<xsl:value-of select="12"/>
	</xsl:template>
	<!--===【試合区分：高校の場合のみ】===============================================================-->
	<!-- 条件によって前項目で設定した表示項目制御パターンと異なる表示を行う場合に以下の設定を行う -->
	<!-- 例えば、通常は上記設定で、決勝と指定したチームコードのみ表示形式を変更したい場合に下記の指定を行う -->
	<xsl:template name="SPYKT_KOUKOU_REFINE_SET">
		<!-- 「1」 ：Ａ１　（３項目） -->
		<!-- 「2」 ：Ａ１Ｓ（３項目）＋学年 -->
		<!-- 「4」 ：Ａ３Ｓ（３項目＋本塁打、打率、防御率）＋学年 -->
		<!-- 「5」 ：Ｂ１　（５項目） -->
		<!-- 「6」 ：Ｂ１Ｓ（５項目）＋学年） -->
		<!-- 「8」 ：Ｂ３Ｓ（５項目＋本塁打、打率、防御率）＋学年-->
		<!-- 「9」 ：Ｃ１  （９項目）-->
		<!-- 「11」：Ｃ３Ｓ（９項目＋本塁打、打率、防御率）＋学年-->
		<!-- 「12」：全表示 -->
		<xsl:value-of select="12"/>
	</xsl:template>
	<!-- ===== フェーズ文字列（完全一致）での絞り込み ===== -->
	<!-- 有効無効フラグ -->
	<xsl:template name="SPYKT_KOUKOU_REFINE_FEZU_FLG_SET">
		<!-- 「0」：無効 -->
		<!-- 「1」：有効 -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 絞込み対象文字列 -->
	<xsl:template name="SPYKT_KOUKOU_REFINE_FEZU_DIFINE_SET">
		<!-- 例：<xsl:value-of select="'決勝,準決勝'"/> -->
		<!-- ※複数設定する場合は「,」(半角カンマ)区切り -->
		<xsl:value-of select="'決勝'"/>
	</xsl:template>
	<!-- =========== チームコードでの絞り込み =========== -->
	<!-- 有効無効フラグ -->
	<xsl:template name="SPYKT_KOUKOU_REFINE_CHICODE_FLG_SET">
		<!-- 「0」：無効 -->
		<!-- 「1」：有効 -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!-- 絞込み対象チームコード -->
	<xsl:template name="SPYKT_KOUKOU_REFINE_CHICODE_DIFINE_SET">
		<!-- 例：<xsl:value-of select="'０１,０２,０３'"/> -->
		<!-- ※複数設定する場合は「,」(半角カンマ)区切り -->
		<xsl:value-of select="'０１,０２'"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■ゴルフ定義■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- プロゴルフ成績（SPKdSPGPGS_KAKUNIN2_TATE.xsl）縦・表示順位                                  　-->
	<!-- 「0」の場合は全件表示 -->
	<!--===============================================================================================-->
	<xsl:template name="SPGPGS_JUNI_SET">
		<xsl:value-of select="10"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- アマゴルフ成績（SPKdSPGPGA_KAKUNIN2_TATE.xsl）縦・表示順位                                  　-->
	<!-- 「0」の場合は全件表示 -->
	<!--===============================================================================================-->
	<xsl:template name="SPGPGA_JUNI_SET">
		<xsl:value-of select="10"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 都道府県対抗アマ個人成績（SPKdSPGPGK_KAKUNIN2.xsl）縦・表示順位　-->
	<!-- 「0」の場合は全件表示 -->
	<!--===============================================================================================-->
	<xsl:template name="SPGPGK_JUNI_SET">
		<xsl:value-of select="10"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 都道府県対抗アマ団体成績（SPKdSPGAD_KAKUNIN2_TATE.xsl）縦・表示順位　-->
	<!-- 「0」の場合は全件表示（参考記録、棄権、失格は「0」の場合のみ表示） -->
	<!--===============================================================================================-->
	<xsl:template name="SPGAD_JUNI_SET">
		<xsl:value-of select="10"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 賞金ランキング（SPKdSPGRG_KAKUNIN2.xsl）表示順位　-->
	<!-- 「0」の場合は全件表示 -->
	<!--===============================================================================================-->
	<xsl:template name="SPGRG_JUNI_SET">
		<xsl:value-of select="10"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- マッチプレー（SPKdSPGPM_KAKUNIN2.xsl）（対戦型）最大折り返し文字数定義-->
	<!-- 横書表示の場合、対戦成績以外（見出し行、字解）は共通設定を適用する -->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_SPGPM_SET">
		<!-- 「0」： JL個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： JL個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_SPGPM_SET">
		<!-- PRINT_MAXTEXT_FLG_SPGPM_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_SPGPM_SET =「0」の場合は共通定義を使用する -->
		<!-- ※「9」～「15」の奇数を設定して下さい -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■中央競馬定義■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- 成績表Ｃ（SPKdSPUSZ_KAKUNIN2_TATE.xsl）成績縦・表示順位                                     　-->
	<!-- 「0」の場合は全件表示 -->
	<!--===============================================================================================-->
	<xsl:template name="SPUSZ_JUNI_SET">
		<xsl:value-of select="5"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 成績表Ｃ（SPKdSPUSZ_KAKUNIN2_TATE.xsl）成績縦・騎手名情報の表示設定                         　-->
	<!-- 「0」： 非表示 -->
	<!-- 「1」： 外国人騎手のみ表示 -->
	<!-- 「2」： 全て表示 -->
	<!--===============================================================================================-->
	<xsl:template name="SPUSZ_KIMEI_NOTE_DISPLAY_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■競輪定義■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- 場外発売情報（SPKdSPVUJ_KAKUNIN2.xsl）エリア別発売情報 -->
	<!-- 「0」： ”全て”のエリアを表示 -->
	<!-- 「1」： ”東日本”を表示 -->
	<!-- 「2」： ”中部”を表示 -->
	<!-- 「3」： ”関西”を表示 -->
	<!-- 「4」： ”中四国”を表示 -->
	<!-- 「5」： ”九州”を表示 -->
	<!--===============================================================================================-->
	<xsl:template name="SPVUJ_AREA_SET">
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■地方競馬定義■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- 成績表Ｃ（SPKdCKUSZ_KAKUNIN2_TATE.xsl）成績縦・表示順位                                     　-->
	<!-- 「0」の場合は全件表示 -->
	<!--===============================================================================================-->
	<xsl:template name="CKUSZ_JUNI_SET">
		<xsl:value-of select="5"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■総体定義■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- 順位型　選手情報エリア文字数 -->
	<!-- 選手情報エリアの文字数を定義（初期値は20） -->
	<!--===============================================================================================-->
	<xsl:template name="SS_OI_YOKO_NAME_AREA_LENGTH_SET">
		<xsl:value-of select="20"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型　選手名・チーム名・所属　表示切替 -->
	<!-- 【横書きのみ設定変更有効】※縦書きはWriting固定 -->
	<!--===============================================================================================-->
	<xsl:template name="SS_OI_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型　記録　表示切替 -->
	<!-- 【横書きのみ設定変更有効】※縦書きはWriting固定 -->
	<!--===============================================================================================-->
	<xsl:template name="SS_OI_RESULT_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="2"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 対戦型　選手名表示切替 -->
	<!-- 【横書きのみ設定変更有効】※縦書きは　選手名＝Formal固定、チーム名・所属＝Writing固定 -->
	<!--===============================================================================================-->
	<xsl:template name="SS_TA_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="2"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 対戦型　最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_SS_TA_SET">
		<!-- 「0」： JL個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： JL個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_SS_TA_SET">
		<!-- PRINT_MAXTEXT_FLG_SS_TA_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_SS_TA_SET =「0」の場合は共通定義を使用する -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 野球テーブル　選手名・所属表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="SS_MB_PLAYER_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■新総体■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- 順位型/横書き　選手情報エリア文字数 -->
	<!-- 選手情報エリアの文字数を定義（初期値は20） -->
	<!--===============================================================================================-->
	<!--<xsl:template name="KM_V10_Standing_NAME_AREA_LENGTH_SET">-->
	<xsl:template name="ST_Standing_NAME_AREA_LENGTH_SET">
		<xsl:value-of select="20"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型　選手名・チーム名・所属　表示切替 -->
	<!-- 【横書きのみ設定変更有効】※縦書きはWriting固定 -->
	<!--===============================================================================================-->
	<!--<xsl:template name="KM_V10_Standing_PLAYERNAME_DISPLAY_SET">-->
	<xsl:template name="ST_Standing_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型　記録　表示切替 -->
<!-- 【横書きのみ設定変更有効】※縦書きはWriting固定 -->
	<!--===============================================================================================-->
	<!--<xsl:template name="KM_V10_Standing_RESULT_DISPLAY_SET">-->
	<xsl:template name="ST_Standing_RESULT_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 対戦型　選手名・チーム名・所属　表示切替 -->
	<!-- 【横書きのみ設定変更有効】※縦書きは　選手名＝Formal固定、チーム名・所属＝Writing固定 -->
	<!--===============================================================================================-->
	<!--<xsl:template name="KM_V10_Match_PLAYERNAME_DISPLAY_SET">-->
	<xsl:template name="ST_Match_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 対戦型　最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<!--<xsl:template name="KM_V10_Match_PRINT_MAXTEXT_FLG_SET">-->
	<xsl:template name="ST_Match_PRINT_MAXTEXT_FLG_SET">
		<!-- 「0」： 個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： 個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--<xsl:template name="KM_V10_Match_PRINT_MAXTEXT_SET">-->
	<xsl:template name="ST_Match_PRINT_MAXTEXT_SET">
		<!-- ST_Match_PRINT_MAXTEXT_FLG_SET =「1」の場合のみ下記有効 -->
		<!-- ST_Match_PRINT_MAXTEXT_FLG_SET =「0」の場合は共通定義を使用する -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 野球テーブル　選手名・所属表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="ST_MB_PLAYER_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■K-MASTER■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- 日常記録（順位型/横書き）　選手情報エリア文字数 -->
	<!-- 選手情報エリアの文字数を定義（初期値は20） -->
	<!--===============================================================================================-->
	<xsl:template name="KM_V12_Standing_NAME_AREA_LENGTH_SET">
		<xsl:value-of select="20"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 日常記録（対戦型）　最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="KM_V12_Match_PRINT_MAXTEXT_FLG_SET">
		<!-- 「0」： JL個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： JL個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="KM_V12_Match_PRINT_MAXTEXT_SET">
		<!-- KM_V12_Match_PRINT_MAXTEXT_FLG_SET =「1」の場合のみ下記有効 -->
		<!-- KM_V12_Match_PRINT_MAXTEXT_FLG_SET =「0」の場合は共通定義を使用する -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 日常記録（MLB打席別結果/MLB投球結果）リーグ・チーム・地区　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_V12_MLBLeagueInfo_DISPLAY_SET">
		<!-- 「0」：（リーグ・チーム・地区）を非表示 -->
		<!-- 「1」：（リーグ・チーム・地区）を表示 -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 日常記録（テーブル型）　選手名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_TABLE_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 日常記録（テーブル型）　所属　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_TABLE_PLAYERBELONG_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 日常記録（勝敗表型）　チーム名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WINLOSS_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 大会記録（順位型/横書き）　選手情報エリア文字数 -->
	<!-- 選手情報エリアの文字数を定義（初期値は20） -->
	<!--===============================================================================================-->
	<xsl:template name="KM_V10_Standing_NAME_AREA_LENGTH_SET">
		<xsl:value-of select="20"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 大会記録（順位型）　選手名・チーム名・所属　表示切替 -->
	<!-- 【横書きのみ設定変更有効】※縦書きはWriting固定 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_V10_Standing_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 大会記録（順位型）　記録　表示切替 -->
	<!-- 【横書きのみ設定変更有効】※縦書きはWriting固定 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_V10_Standing_RESULT_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="2"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 大会記録（対戦型）　選手名・チーム名・所属　表示切替 -->
	<!-- 【横書きのみ設定変更有効】※縦書きは　選手名＝Formal固定、チーム名・所属＝Writing固定 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_V10_Match_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="2"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 大会記録（対戦型）　最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="KM_V10_Match_PRINT_MAXTEXT_FLG_SET">
		<!-- 「0」： JL個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： JL個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="KM_V10_Match_PRINT_MAXTEXT_SET">
		<!-- KM_V10_Match_PRINT_MAXTEXT_FLG_SET =「1」の場合のみ下記有効 -->
		<!-- KM_V10_Match_PRINT_MAXTEXT_FLG_SET =「0」の場合は共通定義を使用する -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　テーブル型（スタメン・テーブル）　選手名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_TABLE_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　テーブル型（スタメン・テーブル）　所属　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_TABLE_BELONG_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　スコア　チーム名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_SCORE_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　スコア　最大折り返し文字数定義 -->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_KM_WCUP_SCORE_SET">
		<!-- 「0」： 個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： 個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_KM_WCUP_SCORE_SET">
		<!-- PRINT_MAXTEXT_FLG_KM_WCUP_SCORE_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_KM_WCUP_SCORE_SET =「0」の場合は共通定義を使用する -->
		<!-- ※「9」～「15」の奇数を設定して下さい -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　得点経過　選手名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_SCOREPROCESS_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing ※日本選手は3字表記 -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　ＰＫ戦　選手名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_PK_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing ※日本選手は3字表記 -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　勝敗表　チーム名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_WINLOSS_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　組別最終順位　チーム名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_RANKING_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　得点ランキング　選手名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_SCORERANKING_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　得点ランキング　所属　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_SCORERANKING_BELONG_DISPLAY_SET">
		<!-- 「1」： Writing ※日本選手は3字表記 -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　○日の結果　チーム名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_RESULT_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　○日の結果　最大折り返し文字数定義 -->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_KM_WCUP_RESULT_SET">
		<!-- 「0」： 個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： 個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_KM_WCUP_RESULT_SET">
		<!-- PRINT_MAXTEXT_KM_WCUP_RESULT_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_KM_WCUP_RESULT_SET =「0」の場合は共通定義を使用する -->
		<!-- ※「9」～「15」の奇数を設定して下さい -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　日程　チーム名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_SCHEDULE_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　速報　チーム名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="KM_WCUP_FLASH_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- Ｗ杯サッカー記録　速報　最大折り返し文字数定義 -->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_KM_WCUP_FLASH_SET">
		<!-- 「0」： 個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： 個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_KM_WCUP_FLASH_SET">
		<!-- PRINT_MAXTEXT_FLG_KM_WCUP_MTDD_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_KM_WCUP_MTDD_SET =「0」の場合は共通定義を使用する -->
		<!-- ※「9」～「15」の奇数を設定して下さい -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■五輪・アジア大会■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- 順位型　選手名・チーム名・所属　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_OI_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型　記録表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_OI_RESULT_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal  -->
		<xsl:value-of select="2"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型【紙面レイアウト縦表示】内訳記録　紙面イメージ絞込み -->
	<!--===============================================================================================-->
	<xsl:template name="OL_OI_YOKO_UCHIWAKE_DISPLAY_FLG_SET">
		<!-- 「0」： 絞込みなし -->
		<!-- 「1」： 絞込みあり（紙面イメージ）  -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型【紙面レイアウト横表示】　名前＋記録エリア文字数 -->
	<!-- 名前＋１つ目の記録を表記するエリアの文字数(固定)を定義（初期値は20） -->
	<!--===============================================================================================-->
	<xsl:template name="OL_OI_YOKO_NAME_AREA_LENGTH_SET">
		<xsl:value-of select="20"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型【紙面レイアウト横表示】世界記録・大会記録・日本記録の所属　表示切り替え -->
	<!--===============================================================================================-->
	<xsl:template name="OL_OI_YOKO_KIROKU_DISPLAY_SET">
		<!-- 「0」： 所属表示なし -->
		<!-- 「1」： 所属表示あり  -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 順位型【校閲用横表示】　選手情報エリア文字数 -->
	<!-- 選手情報エリアの最大文字数を定義（初期値は20） -->
	<!--===============================================================================================-->
	<xsl:template name="OL_OI_READING_NAME_AREA_LENGTH_SET">
		<xsl:value-of select="20"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 総集編型　折り返し文字数定義 -->
	<!-- 「25」以下の整数を指定してください（初期値は15） -->
	<!--===============================================================================================-->
	<xsl:template name="OL_OI_SOUSYUHEN_PRINT_MAXTEXT_SET">
		<xsl:value-of select="25"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 対戦型　選手名・チーム名・所属　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TA_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（姓＋名） -->
		<!-- 「3」： Formal（姓＋名）※一字略＜＞編集あり -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 対戦型　最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="OL_TA_PRINT_MAXTEXT_FLG_SET">
		<!-- 「0」： JL個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： JL個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="OL_TA_PRINT_MAXTEXT_SET">
		<!-- OL_TA_PRINT_MAXTEXT_FLG_SET =「1」の場合のみ下記有効 -->
		<!-- OL_TA_PRINT_MAXTEXT_FLG_SET =「0」の場合は共通定義を使用する -->
		<xsl:value-of select="15"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- テーブル型　選手名（所属） 表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TABLE_PLAYER_DISPLAY_SET">
		<!-- 「1」： 紙面表記 選手名（表記）　　　所属（Writing）-->
		<!-- 「2」： フル表記 選手名（姓＋名）　　所属（Formal）-->
		<!-- 「3」： 校閲表記 選手名（姓＋名＋略）所属（Formal）-->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- テーブル型　ポジション 表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TABLE_POSITION_DISPLAY_SET">
		<!-- 「1」： 紙面表記（片チームのWriting）-->
		<!-- 「2」： 校閲表記（両チームのFormal）-->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- テーブル型　選手エリアの最大長  フル・校閲表記　チーム並び【並列】、選手記録【無し】 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TABLE_P_AREA_LEN_FORMAL_HOR">
		<!-- 24（初期値）※A4横印刷用。A4縦の場合は"15"を推奨 -->
		<xsl:value-of select="24"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- テーブル型　選手エリアの最大長  フル・校閲表記　チーム並び【並列】、選手記録【有り】 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TABLE_P_AREA_LEN_FORMAL_HOR_RESULT">
		<!-- 20（初期値）※A4横印刷用。A4縦の場合は"11"を推奨 -->
		<xsl:value-of select="20"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- テーブル型　選手エリアの最大長  フル・校閲表記　チーム並び【直列】、選手記録【無し】 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TABLE_P_AREA_LEN_FORMAL_VER">
		<!-- 45（初期値）※A4横印刷用。A4縦の場合は"35"を推奨 -->
		<xsl:value-of select="45"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- テーブル型　選手エリアの最大長  フル・校閲表記　チーム並び【直列】、選手記録【有り】 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TABLE_P_AREA_LEN_FORMAL_VER_RESULT">
		<!-- 40（初期値）※A4横印刷用。A4縦の場合は"25"を推奨 -->
		<xsl:value-of select="40"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 国別メダル表　国名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_MK_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（正式名） -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- サッカー得点経過型　選手名（所属） 表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TO_PLAYER_DISPLAY_SET">
		<!-- 「1」： 紙面表記 選手名（表記）　　　所属（Writing）-->
		<!-- 「2」： フル表記 選手名（姓＋名）　　所属（Formal）-->
		<!-- 「3」： 校閲表記 選手名（姓＋名＋略）所属（Formal）-->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- サッカー得点経過型　選手エリアの最大長  フル・校閲表記 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_TO_P_AREA_LEN_FORMAL">
		<!-- 35（初期値）※A4横印刷用。A4縦の場合は"25"を推奨 -->
		<xsl:value-of select="35"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- サッカーＰＫ戦型　選手名（所属） 表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_PK_PLAYER_DISPLAY_SET">
		<!-- 「1」： 紙面表記 選手名（表記）　　　所属（Writing）-->
		<!-- 「2」： フル表記 選手名（姓＋名）　　所属（Formal）-->
		<!-- 「3」： 校閲表記 選手名（姓＋名＋略）所属（Formal）-->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- サッカーＰＫ戦型　選手エリアの最大長  フル・校閲表記 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_PK_P_AREA_LEN_FORMAL">
		<!-- 25（初期値）※A4横印刷用。A4縦の場合は"15"を推奨 -->
		<xsl:value-of select="25"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 勝敗表型　国名　表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OL_HY_TEAMNAME_DISPLAY_SET">
		<!-- 「1」： Writing -->
		<!-- 「2」： Formal（正式名） -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■大相撲定義■-->
	<!--###############################################################################################-->
	<!--===============================================================================================-->
	<!-- 新番付資料（01.新番付資料）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS01_PLAYERNAME_DISPLAY_SET">
		<!-- 「0」力士名は４字、部屋は３字、出身地は３字 -->
		<!-- 「1」力士名、部屋、出身地はフルネーム -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 新番付資料（補正）（02.新番付資料（補正））選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS02_PLAYERNAME_DISPLAY_SET">
		<!-- 「0」力士名は４字、部屋は３字、出身地は３字 -->
		<!-- 「1」力士名、部屋、出身地はフルネーム -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 新番付（03.新番付）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS03_PLAYERNAME_DISPLAY_SET">
		<!-- 「0」力士名は４字、部屋は３字、出身地は３字 -->
		<!-- 「1」力士名、部屋、出身地はフルネーム -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 新番付（03.新番付）Ａ・Ｂタイプ表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS03_TYPE_DISPLAY_SET">
		<!-- 「0」新番付（Ａタイプ） -->
		<!-- 「1」新番付（Ｂタイプ） -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士新番付（04 ．郷土力士新番付）力士名、部屋、出身地表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS04_PLAYERNAME_DISPLAY_SET">
		<!-- 「0」紙面表記（力士名は４字、出身地は３字、部屋は３字） -->
		<!-- 「1」フル表記（力士名、出身地、部屋はフルネーム） -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 幕下以下新番付（05 ．幕下以下新番付）力士名、部屋、出身地・国表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS05_PLAYERNAME_DISPLAY_SET">
		<!-- 「0」紙面表記（力士名は３字、部屋は２字、出身地・国は２字） -->
		<!-- 「1」フル表記（力士名、部屋、出身地・国はフルネーム） -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士取組（06．対戦型）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS06_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」上段の力士名は３字、　出身地なし。　　下段の力士名は３字、　出身地は２字 -->
		<!-- 「2」上段の力士名は４字、　出身地は３字。　下段の力士名は３字、　出身地は２字 -->
		<!-- 「3」上段の力士名は正式名、出身地は正式名。下段の力士名は正式名、出身地は正式名 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士取組（06．対戦型）最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_OS06_SET">
		<!-- 「0」： OS個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： OS個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_OS06_SET">
		<!-- PRINT_MAXTEXT_FLG_OS06_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_OS06_SET =「0」の場合は共通定義を使用する -->
		<xsl:value-of select="17"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 幕下以下取組（07．対戦型）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS07_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」力士名は３字、出身地は２字 -->
		<!-- 「2」力士名は正式名、出身地は正式名 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 幕下以下取組（07．対戦型）最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_OS07_SET">
		<!-- 「0」： OS個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： OS個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_OS07_SET">
		<!-- PRINT_MAXTEXT_FLG_OS07_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_OS07_SET =「0」の場合は共通定義を使用する -->
		<xsl:value-of select="18"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 十両取組（08．対戦型）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS08_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」力士名　紙面表記（３字） -->
		<!-- 「2」力士名　フル表記        -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 中入り取組（09．対戦型）過去の取組結果表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS09_RESULT_DISPLAY_SET">
		<!-- 「0」非表示 -->
		<!-- 「1」表示 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 中入り取組（09．対戦型）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS09_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」力士名　紙面表記（２字） -->
		<!-- 「2」力士名　フル表記        -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士勝負、郷土力士勝負まとめ（10、11．対戦型）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS10_OS11_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」上段の力士名は３字、　出身地なし。　　下段の力士名は３字、　出身地は２字 -->
		<!-- 「2」上段の力士名は４字、　出身地は３字。　下段の力士名は３字、　出身地は２字 -->
		<!-- 「3」上段の力士名は正式名、出身地は正式名。下段の力士名は正式名、出身地は正式名 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士勝負、郷土力士勝負まとめ（10、11．対戦型）最大折り返し文字数定義-->
	<!--===============================================================================================-->
	<xsl:template name="PRINT_MAXTEXT_FLG_OS10_OS11_SET">
		<!-- 「0」： OS個別の最大折り返し文字数定義を無効にする -->
		<!-- 「1」： OS個別の最大折り返し文字数定義を有効にする -->
		<xsl:value-of select="0"/>
	</xsl:template>
	<xsl:template name="PRINT_MAXTEXT_OS10_OS11_SET">
		<!-- PRINT_MAXTEXT_FLG_OS06_SET =「1」の場合のみ下記有効 -->
		<!-- PRINT_MAXTEXT_FLG_OS06_SET =「0」の場合は共通定義を使用する -->
		<xsl:value-of select="21"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士勝負、郷土力士勝負まとめ（10、11．対戦型）決まり手表示切替-->
	<!--===============================================================================================-->
	<xsl:template name="OS10_OS11_WINNINGTRICK_DISPLAY_SET">
		<!-- 「0」非表示 -->
		<!-- 「1」表示 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 幕下以下勝負（12．対戦型）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS12_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」力士名は３字 -->
		<!-- 「2」力士名は正式名 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 幕下以下勝負（12．対戦型）決まり手表示切替-->
	<!--===============================================================================================-->
	<xsl:template name="OS12_WINNINGTRICK_DISPLAY_SET">
		<!-- 「0」非表示 -->
		<!-- 「1」表示 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 勝負、まとめ勝負（13、14．対戦型）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS13_OS14_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」力士名は３字 -->
		<!-- 「2」力士名は正式名 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 勝負、まとめ勝負（13、14．対戦型）対戦成績表示切替-->
	<!--===============================================================================================-->
	<xsl:template name="OS13_OS14_OUTCOME_TSUSAN_DISPLAY_SET">
		<!-- 「0」非表示 -->
		<!-- 「1」表示 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 勝負、まとめ勝負（13、14．対戦型）今場所成績表示切替-->
	<!--===============================================================================================-->
	<xsl:template name="OS13_OS14_OUTCOME_KONBASHO_DISPLAY_SET">
		<!-- 「0」非表示 -->
		<!-- 「1」表示 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 勝負、まとめ勝負（13、14．対戦型）時間表示切替-->
	<!--===============================================================================================-->
	<xsl:template name="OS13_OS14_CLOSINGTIME_DISPLAY_SET">
		<!-- 「0」非表示 -->
		<!-- 「1」表示 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士星取表（15．星取り表）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS15_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」力士名　Writing（４字） -->
		<!-- 「2」力士名　フル表記        -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士星取表（15．星取り表）出身地表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS15_CITY_DISPLAY_SET">
		<!-- 「1」出身地　Writing（３字） -->
		<!-- 「2」出身地　フル表記        -->
		<!-- 「3」出身地　市町村付き      -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 郷土力士星取表（15．星取り表）部屋表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS15_BELONG_DISPLAY_SET">
		<!-- 「1」部屋　Writing（２字） -->
		<!-- 「2」部屋　フル表記        -->
		<!-- 「3」部屋　３字            -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 外国力士成績表（16．その他）力士名の表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS16_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」紙面表記 -->
		<!-- 「2」フル表記 -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 外国力士成績表（16．その他）出身全般の表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS16_BELONG_DISPLAY_SET">
		<!-- 「1」紙面表記 -->
		<!-- 「2」フル表記 -->
		<!-- 表示が切り替わる要素は以下のとおり -->
		<!-- ● 両力士の部屋名（紙面表記：２字）-->
		<!-- ● 上段力士の出身国（紙面表記：フル表記の空白埋め） -->
		<!-- ● 上段力士の出身市町村（紙面表記：フル表記の市町村名無し） -->
		<!-- ● 下段力士の出身都道府県（紙面表記：２字）※日本力士で出現-->
		<!-- ● 下段力士の出身国（紙面表記：２字）※外国力士で出現-->
		<!-- ● 下段力士の出身市町村（紙面表記：非表示） -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 優勝三賞受賞力士（17．その他）部屋、出身地・国表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS17_BELONG_DISPLAY_SET">
		<!-- 「1」紙面表記（部屋は３字、出身地・国は２字） -->
		<!-- 「2」フル表記（部屋は正式名、出身地・国は正式名） -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 階級別成績上位力士（18．その他）部屋表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS18_BELONG_DISPLAY_SET">
		<!-- 「1」部屋　紙面表記（３字の空白除外） -->
		<!-- 「2」部屋　フル表記        -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 幕下以下全成績（20．その他）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS20_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」力士名　紙面表記（３字） -->
		<!-- 「2」力士名　フル表記        -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 幕下以下全成績（20．その他）出身部屋表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS20_BELONG_DISPLAY_SET">
		<!-- 「1」部屋　紙面表記（２字）-->
		<!-- 「2」部屋　フル表記        -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 十両星取表（21．星取り表）選手名表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS21_PLAYERNAME_DISPLAY_SET">
		<!-- 「1」力士名　Writing（３字） -->
		<!-- 「2」力士名　フル表記        -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 十両星取表（21．星取り表）出身地表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS21_CITY_DISPLAY_SET">
		<!-- 「1」出身地Writing（２字） -->
		<!-- 「2」出身地フル表記  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--===============================================================================================-->
	<!-- 十両星取表（21．星取り表）部屋表示切替 -->
	<!--===============================================================================================-->
	<xsl:template name="OS21_BELONG_DISPLAY_SET">
		<!-- 「1」部屋Writing（２字） -->
		<!-- 「2」部屋フル表記  -->
		<xsl:value-of select="1"/>
	</xsl:template>
	<!--###############################################################################################-->
	<!--■空白文字削除定義■-->
	<!--###############################################################################################-->
	<xsl:strip-space elements="*"/>
	<!--###############################################################################################-->
	<!--■設定ツール定義■-->
	<!--###############################################################################################-->
	<!-- commonsettingのバージョンと設定ツールのバージョンを合わせる -->
	<xsl:template name="version">
		<xsl:value-of select="1.07"/>
	</xsl:template>
</xsl:stylesheet>
