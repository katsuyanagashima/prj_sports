<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
<!--=============================================================================
　プレーンテキスト・全スタイルシート共通数値変換用
4.0版　 2014.12.19　プレーンテキスト版対応に伴い、以下の編集パターンを追加
　　　　　　　　　　パターン11：1桁、3桁以上はそのまま表示、2桁は連数字
　　　　　　　　　　パターン12：９まで全角、10～149まで一文字連数、150以上片寄せ連数字
　　　　　　　　　　パターン13：縦順位の表示用
　　　　　　　　　　パターン14：３桁毎に「、」切れ表示
4.01版  2014.02.27   以下の編集パターンを追加
　　　　　　　　　　パターン15：９まで全角、10～149まで一文字連数、150以上〓を表示
　　　　　　　　　　パターン16：①～まで丸数字、100以上片寄せ連数字
================================================================================-->
  <!-- 3.0版　2014.2.26 html関連タグの小文字化 -->
  <!--=======================================================
編集者「共通スタイルシート」
Ver1.0　2007.01.25 全角→連数字（複数種）変換の目的で、共有テンプレートとして新規作成
Ver1.1  2007.05.10 パターン２でデータがマイナス記号に加えて　　横棒「－」もチェック文字に追加した
Ver1.2  2007.05.21 パターン10変更 入力＝1-9は全角、10-149は全角or１字連数、１５０以上全角を条件に
　　　　出力＝1-9まで全角、10-99まで１文字連数、100以上を片寄せ連数変換に変更した（対戦型で使用）
		また、入力データが＊付きの場合は小数部と判断して奇数桁の右半角スペース文字に変換

===========================================================-->
  <xsl:variable name="Batsunum">
    <xsl:text></xsl:text>
  </xsl:variable>
  <xsl:variable name="Opnsuu">
    <xsl:text>０１２３４５６７８９</xsl:text>
  </xsl:variable>
  <xsl:variable name="Openren">
    <xsl:text>０１２３４５６７８９</xsl:text>
  </xsl:variable>
  <xsl:variable name="Sironuki">
    <xsl:text>❶❷❸❹❺❻❼❽❾❿</xsl:text>
  </xsl:variable>
  <xsl:variable name="Prespace">
    <xsl:text></xsl:text>
  </xsl:variable>
  <xsl:variable name="Afspace">
    <xsl:text></xsl:text>
  </xsl:variable>
  <xsl:variable name="Commanum">
    <xsl:text></xsl:text>
  </xsl:variable>
  <xsl:variable name="Piriodonum">
    <xsl:text></xsl:text>
  </xsl:variable>
  <xsl:variable name="Zerosuu">
    <xsl:text></xsl:text>
  </xsl:variable>
  <xsl:variable name="Bunsuu">
    <xsl:text>½⅓⅔¼¾⅕⅗⅘⅚⅛⅞</xsl:text>
  </xsl:variable>
  <!--=============================================-->
  <!--Sts:変換parameter Pdata：各業務からの元データ-->
  <!--=============================================-->
  <xsl:template name="RensuuHenkan">
    <xsl:param name="Sts"/>
    <xsl:param name="Pdata"/>
    <xsl:variable name="Marusuu">
      <xsl:text>①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳</xsl:text>
    </xsl:variable>
    <xsl:variable name="Opnsuu">
      <xsl:text>０１２３４５６７８９</xsl:text>
    </xsl:variable>
    <xsl:variable name="Openren">
      <xsl:text>０１２３４５６７８９</xsl:text>
    </xsl:variable>
    <xsl:variable name="Sironuki">
      <xsl:text>❶❷❸❹❺❻❼❽❾❿</xsl:text>
    </xsl:variable>
    <xsl:variable name="Prespace">
      <xsl:text></xsl:text>
    </xsl:variable>
    <xsl:variable name="Afspace">
      <xsl:text></xsl:text>
    </xsl:variable>
    <xsl:variable name="Commanum">
      <xsl:text></xsl:text>
    </xsl:variable>
    <xsl:variable name="Piriodonum">
      <xsl:text></xsl:text>
    </xsl:variable>
    <xsl:variable name="Zerosuu">
      <xsl:text></xsl:text>
    </xsl:variable>
    <xsl:variable name="Bunsuu">
      <xsl:text>½⅓⅔¼¾⅕⅗⅘⅚⅛⅞</xsl:text>
    </xsl:variable>
    <xsl:choose>
      <!--パターン１：率表示、小数点以下のみ表記-->
      <xsl:when test="$Sts = 1">
        <xsl:choose>
          <xsl:when test="contains($Pdata,'．') or contains($Pdata,'－')">
            <!--真：｢．｣or｢－]が含まれる場合のみチェック-->
            <xsl:choose>
              <!--率でマイナスのみそのまま表記-->
              <xsl:when test="substring($Pdata,1,1)= '－' and string-length($Pdata)=1">
                <xsl:value-of select="$Pdata"/>
              </xsl:when>
              <!--マイナス数値はそのまま表記-->
              <xsl:when test="substring($Pdata,1,1)= '－' and string-length($Pdata)!=1">
                <xsl:value-of select="$Pdata"/>
              </xsl:when>
              <!--率で横棒のみそのまま表記-->
              <xsl:when test="substring($Pdata,1,1)= '―' and string-length($Pdata)=1">
                <xsl:value-of select="$Pdata"/>
              </xsl:when>
              <!--10割りの場合は、1.000で表記のため整数部＋小数部SSF=2-->
              <xsl:when test="substring-before($Pdata,'．') = '１'">
                <xsl:call-template name="SeiShousuubu">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                  <xsl:with-param name="SeiData" select="'１'"/>
                  <xsl:with-param name="SSF" select="2"/>
                </xsl:call-template>
              </xsl:when>
              <!--小数点以下切り出しはサブで処理へ 小数部のみ処理SSF=1-->
              <!--整数部SeiDataはヌルに-->
              <xsl:otherwise>
                <xsl:call-template name="SeiShousuubu">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                  <xsl:with-param name="SeiData" select="''"/>
                  <xsl:with-param name="SSF" select="1"/>
                </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <!--対象外-->
          <xsl:otherwise>
            <xsl:value-of select="$Pdata"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン２：率、点数、オッズ、タイムなど整数部と小数部の両方を表示する-->
      <!--点数表示で整数部のときもある-->
      <xsl:when test="$Sts = 2">
        <xsl:choose>
          <!--偽：変換外-->
          <xsl:when test="contains($Pdata,'＋') or contains($Pdata,'／')  or contains($Pdata,'時') or contains($Pdata,'分') or contains($Pdata,'秒')">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <xsl:when test="contains($Pdata,'Ｒ') or contains($Pdata,'日') or contains($Pdata,'回') or contains($Pdata,'点')or contains($Pdata,'・')">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--マイナスのみそのまま表記-->
          <xsl:when test="substring($Pdata,1,1)= '－' and string-length($Pdata)=1">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--マイナス数値はそのまま表記-->
          <xsl:when test="contains($Pdata,'－') and string-length($Pdata)!=1">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--率で横棒のみそのまま表記-->
          <xsl:when test="contains($Pdata,'―') and string-length($Pdata)=1">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--真：変換対象Data-->
          <xsl:when test="contains($Pdata,'．')">
            <!--整数部and小数部あり,Seidata:整数部分代入 SSF=2-->
            <xsl:call-template name="SeiShousuubu">
              <xsl:with-param name="Pdata" select="$Pdata"/>
              <xsl:with-param name="SeiData" select="substring-before($Pdata,'．')"/>
              <xsl:with-param name="SSF" select="2"/>
            </xsl:call-template>
          </xsl:when>
          <!--パターン2で整数部のみのとき-->
          <xsl:otherwise>
            <!--SSF=3-->
            <xsl:call-template name="SeiShousuubu">
              <xsl:with-param name="Pdata" select="$Pdata"/>
              <xsl:with-param name="SeiData" select="$Pdata"/>
              <xsl:with-param name="SSF" select="3"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン2-->
      <!--パターン３：通常数字として表示、但し、10以下の数字は全角 例　５-->
      <!--パターン４：通常数字として表示、但し、10以下の数字は前半角スペース文字 ex 05-->
      <xsl:when test="$Sts = 3 or $Sts = 4">
        <xsl:choose>
          <!--偽：変換外-->
          <xsl:when test="contains($Pdata,'．') or contains($Pdata,'＋') or contains($Pdata,'時') or contains($Pdata,'分') or contains($Pdata,'秒')">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <xsl:when test="contains($Pdata,'／') or contains($Pdata,'Ｒ') or contains($Pdata,'日') or contains($Pdata,'回') or contains($Pdata,'点')or contains($Pdata,'・')">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--マイナスのみそのまま表記-->
          <xsl:when test="substring($Pdata,1,1)= '－' and string-length($Pdata)=1">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--マイナス数値はそのまま表記-->
          <xsl:when test="contains($Pdata,'－') and string-length($Pdata)!=1">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--率で横棒のみそのまま表記-->
          <xsl:when test="contains($Pdata,'―') and string-length($Pdata)=1">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--真：変換対象Data-->
          <xsl:otherwise>
            <xsl:variable name="Len3" select="string-length($Pdata)"/>
            <xsl:choose>
              <!--1桁：ステータスが３は、そのまま全角表記、ステータス４は、04のように表示-->
              <xsl:when test="$Len3 = 1">
                <xsl:choose>
                  <!--sts=3で、0～9まで、及びPdataが×の場合はそのまま-->
                  <xsl:when test="$Sts = 3 or contains($Pdata,'×')">
                    <xsl:value-of select="$Pdata"/>
                  </xsl:when>
                  <xsl:when test="$Sts = 4">
                    <xsl:variable name="Lhen1" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
                    <xsl:value-of select="substring($Zerosuu,$Lhen1+1,1)"/>
                  </xsl:when>
                  <!--sts=3でPdataが〓の場合はそのまま-->
                  <xsl:otherwise>
                    <xsl:value-of select="$Pdata"/>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:when>
              <!--2桁を連数に変換-->
              <xsl:when test="$Len3 = 2">
                <xsl:choose>
                  <!--sts=3で、かつPdataが０×～９×の場合-->
                  <xsl:when test="$Sts = 3 and contains($Pdata,'×')">
                    <xsl:variable name="Lhen0" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                    <xsl:value-of select="substring($Batsunum,$Lhen0+1,1)"/>
                  </xsl:when>
                  <!--suts=3で通常の数字２桁-->
                  <xsl:otherwise>
                    <xsl:variable name="Lhen2" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
                    <xsl:value-of select="substring($Zerosuu,$Lhen2+1,1)"/>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:when>
              <!--データ長が３桁以上のとき、３桁以上共有処理で連数変換して表示-->
              <xsl:when test="$Len3 &gt; 2">
                <xsl:choose>
                  <!--１０×など２桁に×がある場合、数値のみ連数変換して×は全角-->
                  <xsl:when test="$Sts = 3 and contains($Pdata,'×')">
                    <xsl:variable name="Lhen3_0" select="translate(substring-before($Pdata,'×'),'１２３４５６７８９０','1234567890')"/>
                    <xsl:value-of select="concat(substring($Zerosuu,$Lhen3_0+1,1),'×')"/>
                  </xsl:when>
                  <!--通常の３桁以上数値変換-->
                  <xsl:otherwise>
                    <xsl:call-template name="SeisuuOnly">
                      <xsl:with-param name="Pdata" select="$Pdata"/>
                    </xsl:call-template>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:when>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン５：金額数字として表示、３桁ごとにカンマ区切り挿入 ex 1,505-->
      <xsl:when test="$Sts = 5">
        <xsl:choose>
          <!--偽：変換外-->
          <xsl:when test="contains($Pdata,'．') or contains($Pdata,'＋') or contains($Pdata,'－') or contains($Pdata,'／') or contains($Pdata,'―')">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--真：変換対象Data-->
          <xsl:otherwise>
            <xsl:variable name="Len5" select="string-length($Pdata)"/>
            <xsl:choose>
              <!--1桁：そのまま全角表示-->
              <xsl:when test="$Len5 = 1">
                <xsl:value-of select="$Pdata"/>
              </xsl:when>
              <!--2桁を連数に変換-->
              <xsl:when test="$Len5 = 2">
                <xsl:variable name="Lhen2" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
                <xsl:value-of select="substring($Zerosuu,$Lhen2+1,1)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 3">
                <!--前１桁は前半角スペース文字、後ろ2桁は連数に変換-->
                <xsl:variable name="Lhen3_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen3_11" select="substring($Prespace,$Lhen3_1+1,1)"/>
                <xsl:variable name="Lhen3_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen3_21" select="substring($Zerosuu,$Lhen3_2+1,1)"/>
                <xsl:value-of select="concat($Lhen3_11,$Lhen3_21)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 4">
                <!--前2桁は前半角スペース文字、2桁目にカンマ付き、後2桁連数に変換-->
                <xsl:variable name="Lhen4_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen4_11" select="substring($Prespace,$Lhen4_1+1,1)"/>
                <xsl:variable name="Lhen4_2" select="translate(substring($Pdata,2,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen4_21" select="substring($Commanum,$Lhen4_2+1,1)"/>
                <xsl:variable name="Lhen4_3" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen4_31" select="substring($Zerosuu,$Lhen4_3+1,1)"/>
                <xsl:value-of select="concat($Lhen4_11,$Lhen4_21,$Lhen4_31)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 5">
                <!--前2桁連数字、3桁目にカンマ付き、後2桁連数に変換-->
                <xsl:variable name="Lhen5_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen5_11" select="substring($Zerosuu,$Lhen5_1+1,1)"/>
                <xsl:variable name="Lhen5_2" select="translate(substring($Pdata,3,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen5_21" select="substring($Commanum,$Lhen5_2+1,1)"/>
                <xsl:variable name="Lhen5_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen5_31" select="substring($Zerosuu,$Lhen5_3+1,1)"/>
                <xsl:value-of select="concat($Lhen5_11,$Lhen5_21,$Lhen5_31)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 6">
                <!--前1桁は前半角スペース文字、2,3桁目連数字、4桁目カンマ付き、後2桁を連数に変換-->
                <xsl:variable name="Lhen6_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen6_11" select="substring($Prespace,$Lhen6_1+1,1)"/>
                <xsl:variable name="Lhen6_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen6_21" select="substring($Zerosuu,$Lhen6_2+1,1)"/>
                <xsl:variable name="Lhen6_3" select="translate(substring($Pdata,4,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen6_31" select="substring($Commanum,$Lhen6_3+1,1)"/>
                <xsl:variable name="Lhen6_4" select="translate(substring($Pdata,5,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen6_41" select="substring($Zerosuu,$Lhen6_4+1,1)"/>
                <xsl:value-of select="concat($Lhen6_11,$Lhen6_21,$Lhen6_31,$Lhen6_41)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 7">
                <!--前1桁は前半角SP文字、2桁目カンマ付き、3,4桁連数、5桁目カンマ付き、後2桁連数に変換-->
                <xsl:variable name="Lhen7_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen7_11" select="substring($Prespace,$Lhen7_1+1,1)"/>
                <xsl:variable name="Lhen7_2" select="translate(substring($Pdata,2,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen7_21" select="substring($Commanum,$Lhen7_2+1,1)"/>
                <xsl:variable name="Lhen7_3" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen7_31" select="substring($Zerosuu,$Lhen7_3+1,1)"/>
                <xsl:variable name="Lhen7_4" select="translate(substring($Pdata,5,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen7_41" select="substring($Commanum,$Lhen7_4+1,1)"/>
                <xsl:variable name="Lhen7_5" select="translate(substring($Pdata,6,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen7_51" select="substring($Zerosuu,$Lhen7_5+1,1)"/>
                <xsl:value-of select="concat($Lhen7_11,$Lhen7_21,$Lhen7_31,$Lhen7_41,$Lhen7_51)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 8">
                <!--前2桁連数、3桁目カンマ付き、4,5桁連数、6桁目カンマ付き、後2桁連数に変換-->
                <xsl:variable name="Lhen8_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen8_11" select="substring($Zerosuu,$Lhen8_1+1,1)"/>
                <xsl:variable name="Lhen8_2" select="translate(substring($Pdata,3,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen8_21" select="substring($Commanum,$Lhen8_2+1,1)"/>
                <xsl:variable name="Lhen8_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen8_31" select="substring($Zerosuu,$Lhen8_3+1,1)"/>
                <xsl:variable name="Lhen8_4" select="translate(substring($Pdata,6,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen8_41" select="substring($Commanum,$Lhen8_4+1,1)"/>
                <xsl:variable name="Lhen8_5" select="translate(substring($Pdata,7,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen8_51" select="substring($Zerosuu,$Lhen8_5+1,1)"/>
                <xsl:value-of select="concat($Lhen8_11,$Lhen8_21,$Lhen8_31,$Lhen8_41,$Lhen8_51)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 9">
                <!--前1桁は前半角SP文字、2,3桁連数、4桁目カンマ付き、5,6桁連数、7桁目カンマ付き、後2桁連数に変換-->
                <xsl:variable name="Lhen9_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen9_11" select="substring($Prespace,$Lhen9_1+1,1)"/>
                <xsl:variable name="Lhen9_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen9_21" select="substring($Zerosuu,$Lhen9_2+1,1)"/>
                <xsl:variable name="Lhen9_3" select="translate(substring($Pdata,4,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen9_31" select="substring($Commanum,$Lhen9_3+1,1)"/>
                <xsl:variable name="Lhen9_4" select="translate(substring($Pdata,5,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen9_41" select="substring($Zerosuu,$Lhen9_4+1,1)"/>
                <xsl:variable name="Lhen9_5" select="translate(substring($Pdata,7,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen9_51" select="substring($Commanum,$Lhen9_5+1,1)"/>
                <xsl:variable name="Lhen9_6" select="translate(substring($Pdata,8,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen9_61" select="substring($Zerosuu,$Lhen9_6+1,1)"/>
                <xsl:value-of select="concat($Lhen9_11,$Lhen9_21,$Lhen9_31,$Lhen9_41,$Lhen9_51,$Lhen9_61)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 10">
                <!--前1桁は前半角SP文字、2桁目カンマ付き、3,4桁目連数、5桁目カンマ付き、6,7桁連数、8桁目カンマ付き、後2桁連数に変換-->
                <xsl:variable name="Lhen10_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen10_11" select="substring($Prespace,$Lhen10_1+1,1)"/>
                <xsl:variable name="Lhen10_2" select="translate(substring($Pdata,2,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen10_21" select="substring($Commanum,$Lhen10_2+1,1)"/>
                <xsl:variable name="Lhen10_3" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen10_31" select="substring($Zerosuu,$Lhen10_3+1,1)"/>
                <xsl:variable name="Lhen10_4" select="translate(substring($Pdata,5,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen10_41" select="substring($Commanum,$Lhen10_4+1,1)"/>
                <xsl:variable name="Lhen10_5" select="translate(substring($Pdata,6,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen10_51" select="substring($Zerosuu,$Lhen10_5+1,1)"/>
                <xsl:variable name="Lhen10_6" select="translate(substring($Pdata,8,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen10_61" select="substring($Commanum,$Lhen10_6+1,1)"/>
                <xsl:variable name="Lhen10_7" select="translate(substring($Pdata,9,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen10_71" select="substring($Zerosuu,$Lhen10_7+1,1)"/>
                <xsl:value-of select="concat($Lhen10_11,$Lhen10_21,$Lhen10_31,$Lhen10_41,$Lhen10_51,$Lhen10_61,$Lhen10_71)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 11">
                <!--前2桁連数、3桁目カンマ付き、4,5桁連数、6桁目カンマ付き、78桁連数、9桁カンマ、後2桁連数に変換-->
                <xsl:variable name="Lhen11_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen11_11" select="substring($Zerosuu,$Lhen11_1+1,1)"/>
                <xsl:variable name="Lhen11_2" select="translate(substring($Pdata,3,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen11_21" select="substring($Commanum,$Lhen11_2+1,1)"/>
                <xsl:variable name="Lhen11_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen11_31" select="substring($Zerosuu,$Lhen11_3+1,1)"/>
                <xsl:variable name="Lhen11_4" select="translate(substring($Pdata,6,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen11_41" select="substring($Commanum,$Lhen11_4+1,1)"/>
                <xsl:variable name="Lhen11_5" select="translate(substring($Pdata,7,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen11_51" select="substring($Zerosuu,$Lhen11_5+1,1)"/>
                <xsl:variable name="Lhen11_6" select="translate(substring($Pdata,9,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen11_61" select="substring($Commanum,$Lhen11_6+1,1)"/>
                <xsl:variable name="Lhen11_7" select="translate(substring($Pdata,10,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen11_71" select="substring($Zerosuu,$Lhen11_7+1,1)"/>
                <xsl:value-of select="concat($Lhen11_11,$Lhen11_21,$Lhen11_31,$Lhen11_41,$Lhen11_51,$Lhen11_61,$Lhen11_71)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 12">
                <!--前1桁は前半角SP文字、2,3桁連数、4桁目カンマ付き、5,6桁連数、7桁目カンマ付き、8,9桁連数、10桁カンマ、後2桁連数に変換-->
                <xsl:variable name="Lhen12_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen12_11" select="substring($Prespace,$Lhen12_1+1,1)"/>
                <xsl:variable name="Lhen12_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen12_21" select="substring($Zerosuu,$Lhen12_2+1,1)"/>
                <xsl:variable name="Lhen12_3" select="translate(substring($Pdata,4,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen12_31" select="substring($Commanum,$Lhen12_3+1,1)"/>
                <xsl:variable name="Lhen12_4" select="translate(substring($Pdata,5,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen12_41" select="substring($Zerosuu,$Lhen12_4+1,1)"/>
                <xsl:variable name="Lhen12_5" select="translate(substring($Pdata,7,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen12_51" select="substring($Commanum,$Lhen12_5+1,1)"/>
                <xsl:variable name="Lhen12_6" select="translate(substring($Pdata,8,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen12_61" select="substring($Zerosuu,$Lhen12_6+1,1)"/>
                <xsl:variable name="Lhen12_7" select="translate(substring($Pdata,10,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen12_71" select="substring($Commanum,$Lhen12_7+1,1)"/>
                <xsl:variable name="Lhen12_8" select="translate(substring($Pdata,11,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen12_81" select="substring($Zerosuu,$Lhen12_8+1,1)"/>
                <xsl:value-of select="concat($Lhen12_11,$Lhen12_21,$Lhen12_31,$Lhen12_41,$Lhen12_51,$Lhen12_61,$Lhen12_71,$Lhen12_81)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 13">
                <!--前1桁は前半角SP文字、2桁目カンマ付き、3,4桁目連数、5桁目カンマ、6,7桁連数、8桁目カンマ、9,10桁連数,11桁カンマ､12,13桁連数に変換-->
                <xsl:variable name="Lhen13_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_11" select="substring($Prespace,$Lhen13_1+1,1)"/>
                <xsl:variable name="Lhen13_2" select="translate(substring($Pdata,2,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_21" select="substring($Commanum,$Lhen13_2+1,1)"/>
                <xsl:variable name="Lhen13_3" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_31" select="substring($Zerosuu,$Lhen13_3+1,1)"/>
                <xsl:variable name="Lhen13_4" select="translate(substring($Pdata,5,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_41" select="substring($Commanum,$Lhen13_4+1,1)"/>
                <xsl:variable name="Lhen13_5" select="translate(substring($Pdata,6,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_51" select="substring($Zerosuu,$Lhen13_5+1,1)"/>
                <xsl:variable name="Lhen13_6" select="translate(substring($Pdata,8,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_61" select="substring($Commanum,$Lhen13_6+1,1)"/>
                <xsl:variable name="Lhen13_7" select="translate(substring($Pdata,9,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_71" select="substring($Zerosuu,$Lhen13_7+1,1)"/>
                <xsl:variable name="Lhen13_8" select="translate(substring($Pdata,11,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_81" select="substring($Commanum,$Lhen13_8+1,1)"/>
                <xsl:variable name="Lhen13_9" select="translate(substring($Pdata,12,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen13_91" select="substring($Zerosuu,$Lhen13_9+1,1)"/>
                <xsl:value-of select="concat($Lhen13_11,$Lhen13_21,$Lhen13_31,$Lhen13_41,$Lhen13_51,$Lhen13_61,$Lhen13_71,$Lhen13_81,$Lhen13_91)"/>
              </xsl:when>
              <xsl:when test="$Len5 = 14">
                <!--前2桁連数、3桁目カンマ、4,5桁連数、6桁目カンマ、78桁連数、9桁カンマ、10,11､12桁カンマ,13,14桁連数に変換-->
                <xsl:variable name="Lhen14_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_11" select="substring($Zerosuu,$Lhen14_1+1,1)"/>
                <xsl:variable name="Lhen14_2" select="translate(substring($Pdata,3,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_21" select="substring($Commanum,$Lhen14_2+1,1)"/>
                <xsl:variable name="Lhen14_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_31" select="substring($Zerosuu,$Lhen14_3+1,1)"/>
                <xsl:variable name="Lhen14_4" select="translate(substring($Pdata,6,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_41" select="substring($Commanum,$Lhen14_4+1,1)"/>
                <xsl:variable name="Lhen14_5" select="translate(substring($Pdata,7,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_51" select="substring($Zerosuu,$Lhen14_5+1,1)"/>
                <xsl:variable name="Lhen14_6" select="translate(substring($Pdata,9,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_61" select="substring($Commanum,$Lhen14_6+1,1)"/>
                <xsl:variable name="Lhen14_7" select="translate(substring($Pdata,10,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_71" select="substring($Zerosuu,$Lhen14_7+1,1)"/>
                <xsl:variable name="Lhen14_8" select="translate(substring($Pdata,12,1),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_81" select="substring($Commanum,$Lhen14_8+1,1)"/>
                <xsl:variable name="Lhen14_9" select="translate(substring($Pdata,13,2),'１２３４５６７８９０','1234567890')"/>
                <xsl:variable name="Lhen14_91" select="substring($Zerosuu,$Lhen14_9+1,1)"/>
                <xsl:value-of select="concat($Lhen14_11,$Lhen14_21,$Lhen14_31,$Lhen14_41,$Lhen14_51,$Lhen14_61,$Lhen14_71,$Lhen14_81,$Lhen14_91)"/>
              </xsl:when>
              <!--15桁以上は全角でそのまま-->
              <xsl:otherwise>
                <xsl:value-of select="$Pdata"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン６：白抜き❶数字として表示-->
      <xsl:when test="$Sts = 6">
        <xsl:variable name="Temp" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
        <xsl:choose>
          <xsl:when test="$Temp &lt; 31">
            <!--30以下のみ白抜き変換-->
            <xsl:value-of select="substring($Sironuki,$Temp,1)"/>
          </xsl:when>
          <xsl:when test="$Temp &gt; 30 and $Temp &lt; 150">
            <!--31-149は１文字連数変換-->
            <xsl:value-of select="substring($Openren,$Temp+1,1)"/>
          </xsl:when>
          <xsl:otherwise>
            <!--ー150以上、整数部の連数処理して表示-->
            <xsl:call-template name="SeisuuOnly">
              <xsl:with-param name="Pdata" select="$Pdata"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン７：丸数字①として表示-->
      <xsl:when test="$Sts = 7">
        <xsl:variable name="Temp" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
        <xsl:choose>
          <xsl:when test="$Temp &lt; 100">
            <!--99以下のみ白抜き変換-->
            <xsl:value-of select="substring($Marusuu,$Temp,1)"/>
          </xsl:when>
          <xsl:when test="$Temp &gt; 99 and $Temp &lt; 150">
            <!--100-149は１文字連数変換-->
            <xsl:value-of select="substring($Openren,$Temp+1,1)"/>
          </xsl:when>
          <xsl:otherwise>
            <!--ー150以上、整数部の連数処理して表示-->
            <xsl:call-template name="SeisuuOnly">
              <xsl:with-param name="Pdata" select="$Pdata"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン８：半角として表示-->
      <xsl:when test="$Sts = 8">
        <xsl:variable name="Temp" select="translate($Pdata,'１２３４５６７８９０＋－．／','1234567890+-./')"/>
        <xsl:choose>
          <xsl:when test="$Temp &lt; 100000000000">
            <!--数字のみ半角変換-->
            <xsl:value-of select="$Temp"/>
          </xsl:when>
          <xsl:otherwise>
            <!--対象外はそのまま-->
            <xsl:value-of select="$Pdata"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン９：分数を表示。全角の２／３のように分数で渡される-->
      <xsl:when test="$Sts = 9">
        <xsl:variable name="Bunsi" select="substring-before($Pdata,'／')"/>
        <xsl:variable name="Bunbo" select="substring-after($Pdata,'／')"/>
        <xsl:choose>
          <xsl:when test="$Bunsi = '１' and $Bunbo = '２'">
            <xsl:value-of select="substring($Bunsuu,1,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '０' and $Bunbo = '３'">
            <xsl:value-of select="substring($Bunsuu,2,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '１' and $Bunbo = '３'">
            <xsl:value-of select="substring($Bunsuu,3,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '２' and $Bunbo = '３'">
            <xsl:value-of select="substring($Bunsuu,4,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '１' and $Bunbo = '４'">
            <xsl:value-of select="substring($Bunsuu,5,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '３' and $Bunbo = '４'">
            <xsl:value-of select="substring($Bunsuu,6,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '１' and $Bunbo = '５'">
            <xsl:value-of select="substring($Bunsuu,7,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '３' and $Bunbo = '５'">
            <xsl:value-of select="substring($Bunsuu,8,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '４' and $Bunbo = '５'">
            <xsl:value-of select="substring($Bunsuu,9,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '５' and $Bunbo = '６'">
            <xsl:value-of select="substring($Bunsuu,10,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '１' and $Bunbo = '８'">
            <xsl:value-of select="substring($Bunsuu,11,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '７' and $Bunbo = '８'">
            <xsl:value-of select="substring($Bunsuu,12,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '１' and $Bunbo = '１０'">
            <xsl:value-of select="substring($Bunsuu,13,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '１' and $Bunbo = '１２'">
            <xsl:value-of select="substring($Bunsuu,14,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '７' and $Bunbo = '１２'">
            <xsl:value-of select="substring($Bunsuu,15,1)"/>
          </xsl:when>
          <xsl:when test="$Bunsi = '１' and $Bunbo = '１００'">
            <xsl:value-of select="substring($Bunsuu,16,1)"/>
          </xsl:when>
          <!--対象外はそのまま-->
          <xsl:otherwise>
            <xsl:value-of select="$Pdata"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン10：①（正数部）９まで全角、10～99まで一文字連数、100以上片寄せ連数字-->
      <!--②（小数部）＊付きは小数点以下の扱いで処理する-->
      <!--変換前データは、全角でも、連数字でもかまわない-->
      <xsl:when test="$Sts = 10">
        <xsl:choose>
          <xsl:when test="contains($Pdata,'＊')">
            <!--元データに＊があるものは小数部処理-->
            <xsl:variable name="P10data" select="substring-after($Pdata,'＊')"/>
            <xsl:call-template name="Shousuubu">
              <xsl:with-param name="Pdata" select="$P10data"/>
              <xsl:with-param name="Pdata_seisuu" select="''"/>
              <!--奇数桁末尾を後ろ半角スペースに変換させるフラグ-->
              <xsl:with-param name="Ptn" select="10"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <!--正数部処理-->
            <xsl:variable name="Len10" select="string-length($Pdata)"/>
            <xsl:choose>
              <!--入力データが1～9の全角か、10-149の１文字連数である-->
              <xsl:when test="$Len10 = 1">
                <!--連数字テーブルから入力データ値より前の文字列を抽出すると、その文字列長が入力された数値になる-->
                <xsl:variable name="Lhen10_1" select="string-length(substring-before($Openren,$Pdata))"/>
                <xsl:choose>
                  <!--1～9の数字である、そのまま全角で表記するタイプ-->
                  <xsl:when test="$Lhen10_1 &lt; 10">
                    <xsl:value-of select="$Pdata"/>
                  </xsl:when>
                  <!--10～99の数字である、１文字連数で表記-->
                  <xsl:when test="$Lhen10_1 &gt; 9 and $Lhen10_1 &lt; 100">
                    <xsl:value-of select="substring($Openren,$Lhen10_1+1,1)"/>
                  </xsl:when>
                  <!--100以上である、片寄せ連数処理して表示-->
                  <xsl:when test="$Lhen10_1 &gt; 99">
                    <xsl:variable name="Lhen10_11" select="translate($Lhen10_1,'1234567890','１２３４５６７８９０')"/>
                    <xsl:call-template name="SeisuuOnly">
                      <xsl:with-param name="Pdata" select="$Lhen10_11"/>
                    </xsl:call-template>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!--入力データが全角の2桁である、１文字連数で表記-->
              <xsl:when test="$Len10 = 2">
                <xsl:variable name="Lhen10_2" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
                <xsl:value-of select="substring($Zerosuu,$Lhen10_2+1,1)"/>
              </xsl:when>
              <!--入力データが全角３桁以上である、片寄せ連数処理して表示-->
              <xsl:otherwise>
                <xsl:call-template name="SeisuuOnly">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン10終了-->
      <!--パターン11：①（正数部）９まで全角、10～99まで一文字連数、100以上は全角-->
      <xsl:when test="$Sts = 11">
        <xsl:variable name="Len11" select="string-length($Pdata)"/>
        <xsl:choose>
          <!--入力データが１桁の場合、そのまま表示-->
          <xsl:when test="$Len11= 1">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!--入力データが2桁の場合、連数字で表示 -->
          <xsl:when test="$Len11 = 2">
            <xsl:variable name="Lhen11_2" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
            <xsl:value-of select="substring($Zerosuu,$Lhen11_2+1,1)"/>
          </xsl:when>
          <!--入力データが３桁以上の場合、そのまま表示-->
          <xsl:otherwise>
            <xsl:value-of select="$Pdata"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン12：①（正数部）９まで全角、10～149まで一文字連数、150以上片寄せ連数字-->
      <!--②（小数部）＊付きは小数点以下の扱いで処理する-->
      <!--変換前データは、全角でも、連数字でもかまわない-->
      <xsl:when test="$Sts = 12">
        <xsl:choose>
          <xsl:when test="contains($Pdata,'＊')">
            <!--元データに＊があるものは小数部処理-->
            <xsl:variable name="P10data" select="substring-after($Pdata,'＊')"/>
            <xsl:call-template name="Shousuubu">
              <xsl:with-param name="Pdata" select="$P10data"/>
              <xsl:with-param name="Pdata_seisuu" select="''"/>
              <!--奇数桁末尾を後ろ半角スペースに変換させるフラグ-->
              <xsl:with-param name="Ptn" select="10"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <!--正数部処理-->
            <xsl:variable name="Len10" select="string-length($Pdata)"/>
            <xsl:choose>
              <!--入力データが1～9の全角か、10-149の１文字連数である-->
              <xsl:when test="$Len10 = 1">
                <!--連数字テーブルから入力データ値より前の文字列を抽出すると、その文字列長が入力された数値になる-->
                <xsl:variable name="Lhen10_1" select="string-length(substring-before($Openren,$Pdata))"/>
                <xsl:choose>
                  <!--1～9の数字である、そのまま全角で表記するタイプ-->
                  <xsl:when test="$Lhen10_1 &lt; 10">
                    <xsl:value-of select="$Pdata"/>
                  </xsl:when>
                  <!--10～149の数字である、１文字連数で表記-->
                  <xsl:when test="$Lhen10_1 &gt; 9 and $Lhen10_1 &lt; 150">
                    <xsl:value-of select="substring($Openren,$Lhen10_1+1,1)"/>
                  </xsl:when>
                  <!--150以上である、片寄せ連数処理して表示-->
                  <xsl:when test="$Lhen10_1 &gt; 149">
                    <xsl:variable name="Lhen10_11" select="translate($Lhen10_1,'1234567890','１２３４５６７８９０')"/>
                    <xsl:call-template name="SeisuuOnly">
                      <xsl:with-param name="Pdata" select="$Lhen10_11"/>
                    </xsl:call-template>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!--入力データが全角の2桁である、１文字連数で表記-->
              <xsl:when test="$Len10 = 2">
                <xsl:variable name="Lhen10_2" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
                <xsl:value-of select="substring($Zerosuu,$Lhen10_2+1,1)"/>
              </xsl:when>
              <!--入力データが全角３桁以上である-->
              <xsl:otherwise>
                <xsl:variable name="Lhen10_3" select="number(translate($Pdata,'０１２３４５６７８９','0123456789'))"/>
                <xsl:choose>
                  <!--入力データが１５０未満である、１文字連数で表記-->
                  <xsl:when test="150 > $Lhen10_3">
                    <xsl:value-of select="substring($Openren,$Lhen10_3+1,1)"/>
                  </xsl:when>
                  <!--入力データが１５０以上である、片寄せ連数処理して表示-->
                  <xsl:otherwise>
                    <xsl:call-template name="SeisuuOnly">
                      <xsl:with-param name="Pdata" select="$Pdata"/>
                    </xsl:call-template>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン12終了-->
      <!--パターン13：丸数字①として表示-->
      <!--パターン７との違いは、3桁の表示。パターン７は横表示を想定して、3桁以上は連数字、片寄せ＋連数字で表示。
　　　　　パターン13では、3桁は（全角数字）で表示する -->
      <xsl:when test="$Sts = 13">
        <xsl:variable name="Temp" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
        <xsl:choose>
          <!--99以下のみ白抜き変換-->
          <xsl:when test="$Temp &lt; 100">
            <xsl:value-of select="substring($Marusuu,$Temp,1)"/>
          </xsl:when>
          <!--100-149はカッコで囲って１文字連数変換-->
          <xsl:when test="$Temp &gt; 99 and $Temp &lt; 150">
            <xsl:text>（</xsl:text>
            <xsl:value-of select="substring($Openren,$Temp+1,1)"/>
            <xsl:text>）</xsl:text>
          </xsl:when>
          <!-- 150以上はカッコで囲って元データを表示 -->
          <xsl:otherwise>
            <xsl:text>（</xsl:text>
            <xsl:value-of select="$Pdata"/>
            <xsl:text>）</xsl:text>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン13終了-->
      <!--パターン14：全角数字として表示、３桁ごとにカンマ区切り挿入 ex １，５０５-->
      <xsl:when test="$Sts = 14">
        <xsl:variable name="Length" select="string-length($Pdata)"/>
        <xsl:variable name="Hasuu" select="$Length mod 3"/>
        <xsl:choose>
          <!-- ４桁未満の場合はそのまま返却 -->
          <xsl:when test="3 >= $Length">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <!-- ４桁以上の場合はカンマ追加処理 -->
          <xsl:otherwise>
            <xsl:value-of select="substring($Pdata,1,$Hasuu)"/>
            <xsl:if test="$Hasuu!=0">
              <xsl:text>、</xsl:text>
            </xsl:if>
            <xsl:call-template name="ZenkakuComma">
              <xsl:with-param name="Data" select="substring($Pdata,$Hasuu + 1)"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン14終了-->
      <!--パターン15：①（正数部）９まで全角、10～149まで一文字連数、150以上〓を表示-->
      <!--②（小数部）＊付きは小数点以下の扱いで処理する-->
      <!--変換前データは、全角でも、連数字でもかまわない-->
      <xsl:when test="$Sts = 15">
        <xsl:choose>
          <xsl:when test="contains($Pdata,'＊')">
            <!--元データに＊があるものは小数部処理-->
            <xsl:variable name="P10data" select="substring-after($Pdata,'＊')"/>
            <xsl:call-template name="Shousuubu">
              <xsl:with-param name="Pdata" select="$P10data"/>
              <xsl:with-param name="Pdata_seisuu" select="''"/>
              <!--奇数桁末尾を後ろ半角スペースに変換させるフラグ-->
              <xsl:with-param name="Ptn" select="10"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <!--正数部処理-->
            <xsl:variable name="Len10" select="string-length($Pdata)"/>
            <xsl:choose>
              <!--入力データが1～9の全角か、10-149の１文字連数である-->
              <xsl:when test="$Len10 = 1">
                <!--連数字テーブルから入力データ値より前の文字列を抽出すると、その文字列長が入力された数値になる-->
                <xsl:variable name="Lhen10_1" select="string-length(substring-before($Openren,$Pdata))"/>
                <xsl:choose>
                  <!--1～9の数字である、そのまま全角で表記するタイプ-->
                  <xsl:when test="$Lhen10_1 &lt; 10">
                    <xsl:value-of select="$Pdata"/>
                  </xsl:when>
                  <!--10～149の数字である、１文字連数で表記-->
                  <xsl:when test="$Lhen10_1 &gt; 9 and $Lhen10_1 &lt; 150">
                    <xsl:value-of select="substring($Openren,$Lhen10_1+1,1)"/>
                  </xsl:when>
                  <!--150以上である、〓を表示-->
                  <xsl:when test="$Lhen10_1 &gt; 149">
                    <xsl:text>〓</xsl:text>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!--入力データが全角の2桁である、１文字連数で表記-->
              <xsl:when test="$Len10 = 2">
                <xsl:variable name="Lhen10_2" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
                <xsl:value-of select="substring($Zerosuu,$Lhen10_2+1,1)"/>
              </xsl:when>
              <!--入力データが全角３桁以上である-->
              <xsl:otherwise>
                <xsl:variable name="Lhen10_3" select="number(translate($Pdata,'０１２３４５６７８９','0123456789'))"/>
                <xsl:choose>
                  <!--入力データが１５０未満である、１文字連数で表記-->
                  <xsl:when test="150 > $Lhen10_3">
                    <xsl:value-of select="substring($Openren,$Lhen10_3+1,1)"/>
                  </xsl:when>
                  <!--入力データが１５０以上である、〓を表示-->
                  <xsl:otherwise>
                    <xsl:text>〓</xsl:text>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン15終了-->
      <!--パターン16：丸数字①として表示　100以上で片寄せ連数字-->
      <!--※パターン７は100～150は三連数字を使用-->
      <xsl:when test="$Sts = 16">
        <xsl:variable name="Temp" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
        <xsl:choose>
          <xsl:when test="$Temp &lt; 100">
            <!--99以下のみ白抜き変換-->
            <xsl:value-of select="substring($Marusuu,$Temp,1)"/>
          </xsl:when>
          <xsl:otherwise>
            <!--ー100以上、整数部の連数処理して表示-->
            <xsl:call-template name="SeisuuOnly">
              <xsl:with-param name="Pdata" select="$Pdata"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--パターン16終了-->
      <!--								
			</xsl:otherwise>
		</xsl:choose>
-->
      <!--パターン９９：元データそのまま表示-->
      <xsl:when test="$Sts = 99">
        <xsl:value-of select="$Pdata"/>
      </xsl:when>
      <!--パターン1～11＆９９以外、そのまま表示-->
      <xsl:otherwise>
        <xsl:value-of select="$Pdata"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--###############サブテンプレート郡###################-->
  <!--パターン３＆４＆６＆７、１０で共用。３桁以上正数を処理-->
  <!--####################################################-->
  <xsl:template name="SeisuuOnly">
    <xsl:param name="Pdata"/>
    <xsl:variable name="Len3" select="string-length($Pdata)"/>
    <!-- 【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="Prespace" select="''"/>
    <xsl:variable name="Zerosuu" select="''"/>
    <xsl:choose>
      <!--3桁を連数に変換-->
      <xsl:when test="$Len3 = 3">
        <xsl:variable name="Lhen3_0" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
        <!--Sts=3 or Sts=4:前1桁は前半角SP文字、後ろ2桁は連数に変換-->
        <xsl:variable name="Lhen3_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen3_11" select="substring($Prespace,$Lhen3_1+1,1)"/>
        <xsl:variable name="Lhen3_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen3_21" select="substring($Zerosuu,$Lhen3_2+1,1)"/>
        <xsl:value-of select="concat($Lhen3_11,$Lhen3_21)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 4">
        <!--前2桁、後2桁をそれぞれ連数に変換-->
        <xsl:variable name="Lhen4_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen4_11" select="substring($Zerosuu,$Lhen4_1+1,1)"/>
        <xsl:variable name="Lhen4_2" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen4_21" select="substring($Zerosuu,$Lhen4_2+1,1)"/>
        <xsl:value-of select="concat($Lhen4_11,$Lhen4_21)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 5">
        <!--前1桁は前半角SP文字、中2桁、後2桁をそれぞれ連数に変換-->
        <xsl:variable name="Lhen5_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen5_11" select="substring($Prespace,$Lhen5_1+1,1)"/>
        <xsl:variable name="Lhen5_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen5_21" select="substring($Zerosuu,$Lhen5_2+1,1)"/>
        <xsl:variable name="Lhen5_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen5_31" select="substring($Zerosuu,$Lhen5_3+1,1)"/>
        <xsl:value-of select="concat($Lhen5_11,$Lhen5_21,$Lhen5_31)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 6">
        <!--前2桁、中2桁、後2桁をそれぞれ連数に変換-->
        <xsl:variable name="Lhen6_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen6_11" select="substring($Zerosuu,$Lhen6_1+1,1)"/>
        <xsl:variable name="Lhen6_2" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen6_21" select="substring($Zerosuu,$Lhen6_2+1,1)"/>
        <xsl:variable name="Lhen6_3" select="translate(substring($Pdata,5,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen6_31" select="substring($Zerosuu,$Lhen6_3+1,1)"/>
        <xsl:value-of select="concat($Lhen6_11,$Lhen6_21,$Lhen6_31)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 7">
        <!--前1桁は前半角SP文字、後の6桁をそれぞれ2桁の連数に変換-->
        <xsl:variable name="Lhen7_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen7_11" select="substring($Prespace,$Lhen7_1+1,1)"/>
        <xsl:variable name="Lhen7_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen7_21" select="substring($Zerosuu,$Lhen7_2+1,1)"/>
        <xsl:variable name="Lhen7_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen7_31" select="substring($Zerosuu,$Lhen7_3+1,1)"/>
        <xsl:variable name="Lhen7_4" select="translate(substring($Pdata,6,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen7_41" select="substring($Zerosuu,$Lhen7_4+1,1)"/>
        <xsl:value-of select="concat($Lhen7_11,$Lhen7_21,$Lhen7_31,$Lhen7_41)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 8">
        <!--すべてを2桁の連数に変換-->
        <xsl:variable name="Lhen8_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen8_11" select="substring($Zerosuu,$Lhen8_1+1,1)"/>
        <xsl:variable name="Lhen8_2" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen8_21" select="substring($Zerosuu,$Lhen8_2+1,1)"/>
        <xsl:variable name="Lhen8_3" select="translate(substring($Pdata,5,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen8_31" select="substring($Zerosuu,$Lhen8_3+1,1)"/>
        <xsl:variable name="Lhen8_4" select="translate(substring($Pdata,7,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen8_41" select="substring($Zerosuu,$Lhen8_4+1,1)"/>
        <xsl:value-of select="concat($Lhen8_11,$Lhen8_21,$Lhen8_31,$Lhen8_41)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 9">
        <!--前1桁は前半角SP文字、後の8桁をそれぞれ2桁の連数に変換-->
        <xsl:variable name="Lhen9_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen9_11" select="substring($Prespace,$Lhen9_1+1,1)"/>
        <xsl:variable name="Lhen9_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen9_21" select="substring($Zerosuu,$Lhen9_2+1,1)"/>
        <xsl:variable name="Lhen9_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen9_31" select="substring($Zerosuu,$Lhen9_3+1,1)"/>
        <xsl:variable name="Lhen9_4" select="translate(substring($Pdata,6,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen9_41" select="substring($Zerosuu,$Lhen9_4+1,1)"/>
        <xsl:variable name="Lhen9_5" select="translate(substring($Pdata,8,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen9_51" select="substring($Zerosuu,$Lhen9_5+1,1)"/>
        <xsl:value-of select="concat($Lhen9_11,$Lhen9_21,$Lhen9_31,$Lhen9_41,$Lhen9_51)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 10">
        <!--すべてを2桁の連数に変換-->
        <xsl:variable name="Lhen10_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen10_11" select="substring($Zerosuu,$Lhen10_1+1,1)"/>
        <xsl:variable name="Lhen10_2" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen10_21" select="substring($Zerosuu,$Lhen10_2+1,1)"/>
        <xsl:variable name="Lhen10_3" select="translate(substring($Pdata,5,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen10_31" select="substring($Zerosuu,$Lhen10_3+1,1)"/>
        <xsl:variable name="Lhen10_4" select="translate(substring($Pdata,7,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen10_41" select="substring($Zerosuu,$Lhen10_4+1,1)"/>
        <xsl:variable name="Lhen10_5" select="translate(substring($Pdata,9,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen10_51" select="substring($Zerosuu,$Lhen10_5+1,1)"/>
        <xsl:value-of select="concat($Lhen10_11,$Lhen10_21,$Lhen10_31,$Lhen10_41,$Lhen10_51)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 11">
        <!--前1桁は前半角SP文字、後の10桁をそれぞれ2桁の連数に変換-->
        <xsl:variable name="Lhen11_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen11_11" select="substring($Prespace,$Lhen11_1+1,1)"/>
        <xsl:variable name="Lhen11_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen11_21" select="substring($Zerosuu,$Lhen11_2+1,1)"/>
        <xsl:variable name="Lhen11_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen11_31" select="substring($Zerosuu,$Lhen11_3+1,1)"/>
        <xsl:variable name="Lhen11_4" select="translate(substring($Pdata,6,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen11_41" select="substring($Zerosuu,$Lhen11_4+1,1)"/>
        <xsl:variable name="Lhen11_5" select="translate(substring($Pdata,8,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen11_51" select="substring($Zerosuu,$Lhen11_5+1,1)"/>
        <xsl:variable name="Lhen11_6" select="translate(substring($Pdata,10,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen11_61" select="substring($Zerosuu,$Lhen11_6+1,1)"/>
        <xsl:value-of select="concat($Lhen11_11,$Lhen11_21,$Lhen11_31,$Lhen11_41,$Lhen11_51,$Lhen11_61)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 12">
        <!--すべてを2桁の連数に変換-->
        <xsl:variable name="Lhen12_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen12_11" select="substring($Zerosuu,$Lhen12_1+1,1)"/>
        <xsl:variable name="Lhen12_2" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen12_21" select="substring($Zerosuu,$Lhen12_2+1,1)"/>
        <xsl:variable name="Lhen12_3" select="translate(substring($Pdata,5,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen12_31" select="substring($Zerosuu,$Lhen12_3+1,1)"/>
        <xsl:variable name="Lhen12_4" select="translate(substring($Pdata,7,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen12_41" select="substring($Zerosuu,$Lhen12_4+1,1)"/>
        <xsl:variable name="Lhen12_5" select="translate(substring($Pdata,9,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen12_51" select="substring($Zerosuu,$Lhen12_5+1,1)"/>
        <xsl:variable name="Lhen12_6" select="translate(substring($Pdata,11,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen12_61" select="substring($Zerosuu,$Lhen12_6+1,1)"/>
        <xsl:value-of select="concat($Lhen12_11,$Lhen12_21,$Lhen12_31,$Lhen12_41,$Lhen12_51,$Lhen12_61)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 13">
        <!--前1桁は前半角SP文字、後の12桁をそれぞれ2桁の連数に変換-->
        <xsl:variable name="Lhen13_1" select="translate(substring($Pdata,1,1),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen13_11" select="substring($Prespace,$Lhen13_1+1,1)"/>
        <xsl:variable name="Lhen13_2" select="translate(substring($Pdata,2,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen13_21" select="substring($Zerosuu,$Lhen13_2+1,1)"/>
        <xsl:variable name="Lhen13_3" select="translate(substring($Pdata,4,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen13_31" select="substring($Zerosuu,$Lhen13_3+1,1)"/>
        <xsl:variable name="Lhen13_4" select="translate(substring($Pdata,6,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen13_41" select="substring($Zerosuu,$Lhen13_4+1,1)"/>
        <xsl:variable name="Lhen13_5" select="translate(substring($Pdata,8,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen13_51" select="substring($Zerosuu,$Lhen13_5+1,1)"/>
        <xsl:variable name="Lhen13_6" select="translate(substring($Pdata,10,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen13_61" select="substring($Zerosuu,$Lhen13_6+1,1)"/>
        <xsl:variable name="Lhen13_7" select="translate(substring($Pdata,12,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen13_71" select="substring($Zerosuu,$Lhen13_7+1,1)"/>
        <xsl:value-of select="concat($Lhen13_11,$Lhen13_21,$Lhen13_31,$Lhen13_41,$Lhen13_51,$Lhen13_61,$Lhen13_71)"/>
      </xsl:when>
      <xsl:when test="$Len3 = 14">
        <!--すべてを2桁の連数に変換-->
        <xsl:variable name="Lhen14_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen14_11" select="substring($Zerosuu,$Lhen14_1+1,1)"/>
        <xsl:variable name="Lhen14_2" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen14_21" select="substring($Zerosuu,$Lhen14_2+1,1)"/>
        <xsl:variable name="Lhen14_3" select="translate(substring($Pdata,5,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen14_31" select="substring($Zerosuu,$Lhen14_3+1,1)"/>
        <xsl:variable name="Lhen14_4" select="translate(substring($Pdata,7,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen14_41" select="substring($Zerosuu,$Lhen14_4+1,1)"/>
        <xsl:variable name="Lhen14_5" select="translate(substring($Pdata,9,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen14_51" select="substring($Zerosuu,$Lhen14_5+1,1)"/>
        <xsl:variable name="Lhen14_6" select="translate(substring($Pdata,11,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen14_61" select="substring($Zerosuu,$Lhen14_6+1,1)"/>
        <xsl:variable name="Lhen14_7" select="translate(substring($Pdata,13,2),'１２３４５６７８９０','1234567890')"/>
        <xsl:variable name="Lhen14_71" select="substring($Zerosuu,$Lhen14_7+1,1)"/>
        <xsl:value-of select="concat($Lhen14_11,$Lhen14_21,$Lhen14_31,$Lhen14_41,$Lhen14_51,$Lhen14_61,$Lhen14_71)"/>
      </xsl:when>
      <!--15桁以上全角でそのまま-->
      <xsl:otherwise>
        <xsl:value-of select="$Pdata"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--パターン１＆２用：パラメータにより整数部、小数部を処理-->
  <xsl:template name="SeiShousuubu">
    <xsl:param name="Pdata"/>
    <!--各業務から渡されて元データ-->
    <xsl:param name="SeiData"/>
    <!--渡れた整数部のみ-->
    <xsl:param name="SSF"/>
    <!-- 【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="Prespace" select="''"/>
    <xsl:variable name="Zerosuu" select="''"/>
    <!--1:少数以下のみ 2:整数and小数部 3:整数部のみ-->
    <xsl:choose>
      <xsl:when test="$SSF=1">
        <xsl:call-template name="Shousuubu">
          <xsl:with-param name="Pdata" select="$Pdata"/>
          <xsl:with-param name="Pdata_seisuu" select="''"/>
          <!--カンマ付き小数点変換指定のフラグ-->
          <xsl:with-param name="Ptn" select="1"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:when test="$SSF=2 or $SSF=3">
        <xsl:variable name="SeiLen1" select="string-length($SeiData)"/>
        <xsl:choose>
          <!--整数部が1桁前半角スペース文字-->
          <xsl:when test="$SeiLen1 = 1">
            <xsl:variable name="SLhen1" select="translate($SeiData,'１２３４５６７８９０','1234567890')"/>
            <xsl:choose>
              <xsl:when test="$SSF=2">
                <!--小数点処理-->
                <xsl:call-template name="Shousuubu">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                  <xsl:with-param name="Pdata_seisuu" select="substring($Prespace,$SLhen1+1,1)"/>
                  <xsl:with-param name="Ptn" select="1"/>
                </xsl:call-template>
              </xsl:when>
              <!--整数のみ表記-->
              <xsl:when test="$SSF=3">
                <xsl:value-of select="substring($Prespace,$SLhen1+1,1)"/>
              </xsl:when>
            </xsl:choose>
          </xsl:when>
          <!--整数部2桁連数字-->
          <xsl:when test="$SeiLen1 = 2">
            <xsl:variable name="SLhen2" select="translate($SeiData,'１２３４５６７８９０','1234567890')"/>
            <xsl:choose>
              <xsl:when test="$SSF=2">
                <!--小数点処理-->
                <xsl:call-template name="Shousuubu">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                  <xsl:with-param name="Pdata_seisuu" select="substring($Zerosuu,$SLhen2+1,1)"/>
                  <xsl:with-param name="Ptn" select="1"/>
                </xsl:call-template>
              </xsl:when>
              <xsl:when test="$SSF=3">
                <xsl:value-of select="substring($Zerosuu,$SLhen2+1,1)"/>
              </xsl:when>
            </xsl:choose>
          </xsl:when>
          <!--整数部3桁-->
          <xsl:when test="$SeiLen1 = 3">
            <!--整数部3桁、先頭１桁は前半角スペース文字、後2桁は連数字-->
            <xsl:variable name="SLhen3_1" select="translate(substring($SeiData,1,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen3_11" select="substring($Prespace,$SLhen3_1+1,1)"/>
            <xsl:variable name="SLhen3_2" select="translate(substring($SeiData,2,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen3_21" select="substring($Zerosuu,$SLhen3_2+1,1)"/>
            <xsl:choose>
              <xsl:when test="$SSF=2">
                <!--小数点処理-->
                <xsl:call-template name="Shousuubu">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                  <xsl:with-param name="Pdata_seisuu" select="concat($SLhen3_11,$SLhen3_21)"/>
                  <xsl:with-param name="Ptn" select="1"/>
                </xsl:call-template>
              </xsl:when>
              <xsl:when test="$SSF=3">
                <xsl:value-of select="concat($SLhen3_11,$SLhen3_21)"/>
              </xsl:when>
            </xsl:choose>
          </xsl:when>
          <!--整数部4桁、先頭2桁、後2桁とも連数字-->
          <xsl:when test="$SeiLen1 = 4">
            <!--整数部4桁-->
            <xsl:variable name="SLhen4_1" select="translate(substring($SeiData,1,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen4_11" select="substring($Zerosuu,$SLhen4_1+1,1)"/>
            <xsl:variable name="SLhen4_2" select="translate(substring($SeiData,3,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen4_21" select="substring($Zerosuu,$SLhen4_2+1,1)"/>
            <xsl:choose>
              <xsl:when test="$SSF=2">
                <!--小数点処理-->
                <xsl:call-template name="Shousuubu">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                  <xsl:with-param name="Pdata_seisuu" select="concat($SLhen4_11,$SLhen4_21)"/>
                  <xsl:with-param name="Ptn" select="1"/>
                </xsl:call-template>
              </xsl:when>
              <xsl:when test="$SSF=3">
                <xsl:value-of select="concat($SLhen4_11,$SLhen4_21)"/>
              </xsl:when>
            </xsl:choose>
          </xsl:when>
          <!--整数部5桁、先頭1桁は前半角スペース文字、中、後2桁とも連数字-->
          <xsl:when test="$SeiLen1 = 5">
            <xsl:variable name="SLhen5_1" select="translate(substring($SeiData,1,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen5_11" select="substring($Prespace,$SLhen5_1+1,1)"/>
            <xsl:variable name="SLhen5_2" select="translate(substring($SeiData,2,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen5_21" select="substring($Zerosuu,$SLhen5_2+1,1)"/>
            <xsl:variable name="SLhen5_3" select="translate(substring($SeiData,4,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen5_31" select="substring($Zerosuu,$SLhen5_3+1,1)"/>
            <xsl:choose>
              <xsl:when test="$SSF=2">
                <!--小数点処理-->
                <xsl:call-template name="Shousuubu">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                  <xsl:with-param name="Pdata_seisuu" select="concat($SLhen5_11,$SLhen5_21,$SLhen5_31)"/>
                  <xsl:with-param name="Ptn" select="1"/>
                </xsl:call-template>
              </xsl:when>
              <xsl:when test="$SSF=3">
                <xsl:value-of select="concat($SLhen5_11,$SLhen5_21,$SLhen5_31)"/>
              </xsl:when>
            </xsl:choose>
          </xsl:when>
          <!--整数部6桁、2桁ごとに連数字-->
          <xsl:when test="$SeiLen1 = 6">
            <xsl:variable name="SLhen6_1" select="translate(substring($SeiData,1,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen6_11" select="substring($Zerosuu,$SLhen6_1+1,1)"/>
            <xsl:variable name="SLhen6_2" select="translate(substring($SeiData,3,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen6_21" select="substring($Zerosuu,$SLhen6_2+1,1)"/>
            <xsl:variable name="SLhen6_3" select="translate(substring($SeiData,5,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="SLhen6_31" select="substring($Zerosuu,$SLhen6_3+1,1)"/>
            <xsl:choose>
              <xsl:when test="$SSF=2">
                <!--小数点処理-->
                <xsl:call-template name="Shousuubu">
                  <xsl:with-param name="Pdata" select="$Pdata"/>
                  <xsl:with-param name="Pdata_seisuu" select="concat($SLhen6_11,$SLhen6_21,$SLhen6_31)"/>
                  <xsl:with-param name="Ptn" select="1"/>
                </xsl:call-template>
              </xsl:when>
              <xsl:when test="$SSF=3">
                <xsl:value-of select="concat($SLhen6_11,$SLhen6_21,$SLhen6_31)"/>
              </xsl:when>
            </xsl:choose>
          </xsl:when>
          <!--整数7以上はそのまま表示-->
          <xsl:otherwise>
            <xsl:value-of select="$Pdata"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
    </xsl:choose>
  </xsl:template>
  <!--小数部のみ処理する。Pdata_seisuuはSSFの値が1＝ヌル 2＝処理された整数部が渡されてくる-->
  <!--Ptn=1はピリオド付き小数点変換させる変換パターン、Ptn=10はピリオドなしで奇数桁末尾を後ろ半角スペースに変換-->
  <xsl:template name="Shousuubu">
    <xsl:param name="Pdata"/>
    <xsl:param name="Pdata_seisuu"/>
    <xsl:param name="Ptn"/>
    <!-- 【再定義】IE8以下で定義が消える現象に対応 -->
    <xsl:variable name="Afspace" select="''"/>
    <xsl:variable name="Piriodonum" select="''"/>
    <xsl:variable name="Zerosuu" select="''"/>
    <xsl:choose>
      <!--パターン１&２で、カンマ付きの小数点変換-->
      <xsl:when test="$Ptn = 1">
        <xsl:variable name="Pdata_shousuu" select="substring-after($Pdata,'．')"/>
        <xsl:variable name="Len1" select="string-length($Pdata_shousuu)"/>
        <xsl:choose>
          <xsl:when test="$Len1 = 1">
            <xsl:variable name="Lhen1" select="translate($Pdata_shousuu,'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen1_1" select="substring($Piriodonum,$Lhen1+1,1)"/>
            <xsl:value-of select="concat($Pdata_seisuu,$Lhen1_1)"/>
          </xsl:when>
          <xsl:when test="$Len1 = 2">
            <!--下１桁目は点付き数字、後ろ１桁は後半角SP文字に変換-->
            <xsl:variable name="Lhen2_1" select="translate(substring($Pdata_shousuu,1,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen2_11" select="substring($Piriodonum,$Lhen2_1+1,1)"/>
            <xsl:variable name="Lhen2_2" select="translate(substring($Pdata_shousuu,2,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen2_21" select="substring($Afspace,$Lhen2_2+1,1)"/>
            <xsl:value-of select="concat($Pdata_seisuu,$Lhen2_11,$Lhen2_21)"/>
          </xsl:when>
          <xsl:when test="$Len1 = 3">
            <!--下１桁目は点付き数字、後ろ２桁は連数字に変換-->
            <xsl:variable name="Lhen3_1" select="translate(substring($Pdata_shousuu,1,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen3_11" select="substring($Piriodonum,$Lhen3_1+1,1)"/>
            <xsl:variable name="Lhen3_2" select="translate(substring($Pdata_shousuu,2,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen3_21" select="substring($Zerosuu,$Lhen3_2+1,1)"/>
            <xsl:value-of select="concat($Pdata_seisuu,$Lhen3_11,$Lhen3_21)"/>
          </xsl:when>
          <xsl:when test="$Len1 = 4">
            <!--下1桁目は点付き数字、中2桁は連数字、4桁目は後半角SP文字に変換-->
            <xsl:variable name="Lhen4_1" select="translate(substring($Pdata_shousuu,1,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen4_11" select="substring($Piriodonum,$Lhen4_1+1,1)"/>
            <xsl:variable name="Lhen4_2" select="translate(substring($Pdata_shousuu,2,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen4_21" select="substring($Zerosuu,$Lhen4_2+1,1)"/>
            <xsl:variable name="Lhen4_3" select="translate(substring($Pdata_shousuu,4,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen4_31" select="substring($Afspace,$Lhen4_3+1,1)"/>
            <xsl:value-of select="concat($Pdata_seisuu,$Lhen4_11,$Lhen4_21,$Lhen4_31)"/>
          </xsl:when>
          <xsl:when test="$Len1 = 5">
            <!--下1桁目は点付き数字、中2桁、後2桁それぞれを連数字に変換-->
            <xsl:variable name="Lhen5_1" select="translate(substring($Pdata_shousuu,1,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen5_11" select="substring($Piriodonum,$Lhen5_1+1,1)"/>
            <xsl:variable name="Lhen5_2" select="translate(substring($Pdata_shousuu,2,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen5_21" select="substring($Zerosuu,$Lhen5_2+1,1)"/>
            <xsl:variable name="Lhen5_3" select="translate(substring($Pdata_shousuu,4,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen5_31" select="substring($Zerosuu,$Lhen5_3+1,1)"/>
            <xsl:value-of select="concat($Pdata_seisuu,$Lhen5_11,$Lhen5_21,$Lhen5_31)"/>
          </xsl:when>
          <!--下6桁以降はそのまま表示-->
          <xsl:otherwise>
            <xsl:value-of select="$Pdata"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <xsl:when test="$Ptn = 10">
        <!--パターン１０で小数点処理、奇数桁時の末尾を後ろ半角スペース文字に変換-->
        <xsl:variable name="Len1" select="string-length($Pdata)"/>
        <xsl:choose>
          <xsl:when test="$Len1 = 1">
            <xsl:value-of select="$Pdata"/>
          </xsl:when>
          <xsl:when test="$Len1 = 2">
            <!--１文字連数字に変換-->
            <xsl:variable name="Lhen112_2" select="translate($Pdata,'１２３４５６７８９０','1234567890')"/>
            <xsl:value-of select="substring($Zerosuu,$Lhen112_2+1,1)"/>
          </xsl:when>
          <xsl:when test="$Len1 = 3">
            <!--下２桁は１字連数、末尾１桁は後ろ半角スペース連数に変換-->
            <xsl:variable name="Lhen113_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen113_11" select="substring($Zerosuu,$Lhen113_1+1,1)"/>
            <xsl:variable name="Lhen113_2" select="translate(substring($Pdata,3,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen113_21" select="substring($Afspace,$Lhen113_2+1,1)"/>
            <xsl:value-of select="concat($Lhen113_11,$Lhen113_21)"/>
          </xsl:when>
          <xsl:when test="$Len1 = 4">
            <!--各２桁ごと、１字連数に変換-->
            <xsl:variable name="Lhen114_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen114_11" select="substring($Zerosuu,$Lhen114_1+1,1)"/>
            <xsl:variable name="Lhen114_2" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen114_21" select="substring($Zerosuu,$Lhen114_2+1,1)"/>
            <xsl:value-of select="concat($Lhen114_11,$Lhen114_21)"/>
          </xsl:when>
          <xsl:when test="$Len1 = 5">
            <!--下２桁、４桁目は１字連数、末尾１桁は後ろ半角スペース連数に変換-->
            <xsl:variable name="Lhen115_1" select="translate(substring($Pdata,1,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen115_11" select="substring($Zerosuu,$Lhen115_1+1,1)"/>
            <xsl:variable name="Lhen115_2" select="translate(substring($Pdata,3,2),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen115_21" select="substring($Zerosuu,$Lhen115_2+1,1)"/>
            <xsl:variable name="Lhen115_3" select="translate(substring($Pdata,5,1),'１２３４５６７８９０','1234567890')"/>
            <xsl:variable name="Lhen115_31" select="substring($Afspace,$Lhen115_3+1,1)"/>
            <xsl:value-of select="concat($Lhen115_11,$Lhen115_21,$Lhen115_31)"/>
          </xsl:when>
          <!--下6桁以降はそのまま表示-->
          <xsl:otherwise>
            <xsl:value-of select="$Pdata"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
    </xsl:choose>
  </xsl:template>
  <!--パターン14用：パラメータに３桁ごとに、を付加-->
  <xsl:template name="ZenkakuComma">
    <xsl:param name="Data"/>
    <xsl:if test="$Data!='' and string-length($Data) >= 3">
      <xsl:value-of select="substring($Data,1,3)"/>
      <xsl:if test="string-length($Data) >= 4">
        <xsl:text>、</xsl:text>
        <xsl:call-template name="ZenkakuComma">
          <xsl:with-param name="Data" select="substring($Data,4)"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
