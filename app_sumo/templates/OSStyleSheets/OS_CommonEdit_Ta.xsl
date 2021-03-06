<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!--=======================================================================================================-->
  <!--文字列から指定された文字数ごとにBRタグを挿入する-->
  <!--=======================================================================================================-->
  <xsl:template name="AddBR_KAKUNIN_OSCOM2">
    <!--処理対象文字列-->
    <xsl:param name="Data"/>
    <!--改行文字数-->
    <xsl:param name="Length"/>
    <!--力士ポジション[1:上段（左）、2:下段（右）]-->
    <xsl:param name="LeftOrRight" select="1"/>
    <!--括弧有無[0:なし、1:あり] -->
    <xsl:param name="KakkoHamidashiFlg" select="0"/>
    <!--変換パターン（左力士括弧付：１、右力士括弧付：２、左力士括弧無し：３、右力士括弧無し：４）-->
    <!--成績情報部の編集時は[左力士括弧無し：３]を指定する（はみ出し処理、スペース保管処理等行わない）-->
    <xsl:if test="$Data!=''">
      <xsl:variable name="EditPattern">
        <xsl:choose>
          <xsl:when test="$LeftOrRight=1 and $KakkoHamidashiFlg=1">
            <xsl:value-of select="1"/>
          </xsl:when>
          <xsl:when test="$LeftOrRight=2 and $KakkoHamidashiFlg=1">
            <xsl:value-of select="2"/>
          </xsl:when>
          <xsl:when test="$LeftOrRight=1 and $KakkoHamidashiFlg=0">
            <xsl:value-of select="3"/>
          </xsl:when>
          <xsl:when test="$LeftOrRight=2 and $KakkoHamidashiFlg=0">
            <xsl:value-of select="4"/>
          </xsl:when>
        </xsl:choose>
      </xsl:variable>
      <!--文字列の先頭からの指定文字数を変数Tipとする-->
      <xsl:variable name="Tip">
        <xsl:choose>
          <!--(左側への編集で)最終行が'）'のみの場合は、はみ出し処理を行う。
            予備エリアに'）'を編集するため、文字列の先頭からの指定文字数+1を変数Tipとする-->
          <xsl:when test="($EditPattern = 1) and (string-length($Data) = $Length+1) and substring($Data,string-length($Data),1)='）'">
            <xsl:value-of select="substring($Data,1,$Length + 1)"/>
          </xsl:when>
          <!--(右側への編集で)最終行が'）'のみの場合は、はみ出し処理を行う。
            予備エリアに'）'を編集するため、文字列の先頭からの指定文字数を変数Tipとする-->
          <xsl:when test="($EditPattern = 2) and (string-length($Data) mod $Length = 1) and substring($Data,string-length($Data),1)='）'">
            <xsl:value-of select="substring($Data,1,$Length)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="substring($Data,1,$Length)"/>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$Length - string-length($Data)"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!--文字列の指定文字数目以降を変数Afterとする-->
      <xsl:variable name="After" select="substring-after($Data,$Tip)"/>
      <xsl:choose>
        <!--右側の編集で１行が'）'のみの場合に置き換える-->
        <xsl:when test="($EditPattern = 2) and (string-length($After) = 1)">
          <xsl:value-of select="$Tip"/>
          <xsl:value-of select="$KakkoR"/>
        </xsl:when>
        <!--変数Afterが空の場合（次行の編集がない場合）-->
        <xsl:when test="string-length($After) = 0">
          <!--先頭からの指定文字数分を表示する-->
          <xsl:value-of select="$Tip"/>
          <!--右力士括弧付で、折り返し文字数に満たない場合は、予備スペースを追加-->
          <xsl:if test="(($EditPattern = 2) or ($EditPattern = 4)) and $Length > string-length($Tip)">
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$Length - string-length($Tip)"/>
            </xsl:call-template>
          </xsl:if>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:when>
        <xsl:otherwise>
          <!--先頭からの指定文字数分を表示する-->
          <xsl:value-of select="$Tip"/>
          <!--右力士括弧なしで、折り返し文字数に満たない場合は、予備スペースを追加-->
          <xsl:if test="(($EditPattern = 2) or ($EditPattern = 4)) and $Length > string-length($Tip)">
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$Length - string-length($Tip)"/>
            </xsl:call-template>
          </xsl:if>
          <xsl:value-of select="$LineFeed_UTL"/>
          <!--AddBR_KAKUNINテンプレートを再起呼び出し-->
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <!--文字列の２文字目以降をセットする-->
            <xsl:with-param name="Data" select="$After"/>
            <xsl:with-param name="Length" select="$Length"/>
            <xsl:with-param name="LeftOrRight" select="$LeftOrRight"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="$KakkoHamidashiFlg"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--規定の文字数ごとに空白を挿入する-->
  <!--上段（左）の力士名または出身地について（折り返す場合は各行の）先頭１文字を字下げするために使用-->
  <!--=======================================================================================================-->
  <xsl:template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
    <!--上段（左）力士名の前に付加する１文字（勝敗、勝ち越し／負け越し、対戦成績など）-->
    <xsl:param name="Outcome"/>
    <!--処理対象文字列-->
    <xsl:param name="Data"/>
    <!--１行文字数-->
    <xsl:param name="Length"/>
    <xsl:choose>
      <!--上段（左）力士名の前に勝敗、勝ち越し／負け越し、対戦成績など付加する場合は字下げしない-->
      <xsl:when test="string-length($Outcome) != 0">
        <xsl:value-of select="$Outcome"/>
        <xsl:value-of select="substring($Data, 1, $Length -1)"/>
        <xsl:if test="substring($Data, $Length) != ''">
          <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="substring($Data, $Length)"/>
            <xsl:with-param name="Length" select="$Length"/>
          </xsl:call-template>
        </xsl:if>
      </xsl:when>
      <!--１文字目が閉じ括弧の場合は字下げしない（後からはみ出し処理するのでそのまま１文字目に閉じ括弧を表示）-->
      <xsl:when test="starts-with($Data, '）') and string-length($Data) = 1">
        <xsl:text>）</xsl:text>
      </xsl:when>
      <!--１文字目が開き括弧の場合は字下げしない（出身地の１行目）-->
      <xsl:when test="starts-with($Data, '（')">
        <xsl:value-of select="substring($Data, 1, $Length)"/>
        <xsl:if test="substring($Data, $Length +1) != ''">
          <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="substring($Data, $Length +1)"/>
            <xsl:with-param name="Length" select="$Length"/>
          </xsl:call-template>
        </xsl:if>
      </xsl:when>
      <!--上記以外は字下げ-->
      <xsl:otherwise>
        <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
        <xsl:value-of select="substring($Data, 1, $Length -1)"/>
        <xsl:if test="substring($Data, $Length) != ''">
          <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="substring($Data, $Length)"/>
            <xsl:with-param name="Length" select="$Length"/>
          </xsl:call-template>
        </xsl:if>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 対戦型（取組）レイアウト整形処理             -->
  <!--=======================================================================================================-->
  <xsl:template name="TaisenLayout_TORIKUMI_OSCOM">
    <!--上段（左）力士名-->
    <xsl:param name="PLAYER_INFO_1"/>
    <!--下段（右）力士名-->
    <xsl:param name="PLAYER_INFO_2"/>
    <!--上段（左）力士名エリアにはみ出す決まり手などの１字-->
    <xsl:param name="RESULT_AREA_OVERFLOWED"/>
    <!--決まり手-->
    <xsl:param name="RESULT_AREA_INFO"/>
    <!--上段（左）力士名の文字数-->
    <xsl:param name="PLAYER1_AREA_LENGTH"/>
    <!--下段（右）力士名の文字数-->
    <xsl:param name="PLAYER2_AREA_LENGTH"/>
    <!--決まり手の文字数-->
    <xsl:param name="RESULT_AREA_LENGTH"/>
    <!--出力対象が空文字でない場合のみ処理を実施-->
    <xsl:if test="$PLAYER_INFO_1!='' or $PLAYER_INFO_2!='' or $RESULT_AREA_INFO!=''">
      <!--===================-->
      <!-- 出力文字列取得    -->
      <!--===================-->
      <!--改行文字までの文字列を取得：上段（左）-->
      <xsl:variable name="PLAYER_INFO_1_LineData">
        <xsl:choose>
          <xsl:when test="$PLAYER_INFO_1='' or starts-with($PLAYER_INFO_1,$LineFeed_UTL)">
            </xsl:when>
          <xsl:when test="substring-before($PLAYER_INFO_1,$LineFeed_UTL)!= ''">
            <xsl:value-of select="substring-before($PLAYER_INFO_1,$LineFeed_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$PLAYER_INFO_1"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!--改行文字までの文字列を取得：下段（右）-->
      <xsl:variable name="PLAYER_INFO_2_LineData">
        <xsl:choose>
          <xsl:when test="$PLAYER_INFO_2='' or starts-with($PLAYER_INFO_2,$LineFeed_UTL)">
            </xsl:when>
          <xsl:when test="substring-before($PLAYER_INFO_2,$LineFeed_UTL)!= ''">
            <xsl:value-of select="substring-before($PLAYER_INFO_2,$LineFeed_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$PLAYER_INFO_2"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!--改行文字までの文字列を取得：対戦成績-->
      <xsl:variable name="RESULT_AREA_INFO_LineData">
        <xsl:choose>
          <xsl:when test="$RESULT_AREA_INFO='' or starts-with($RESULT_AREA_INFO,$LineFeed_UTL)">
          </xsl:when>
          <xsl:when test="substring-before($RESULT_AREA_INFO,$LineFeed_UTL)!= ''">
            <xsl:value-of select="substring-before($RESULT_AREA_INFO,$LineFeed_UTL)"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$RESULT_AREA_INFO"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!--===================-->
      <!-- 出力処理          -->
      <!--===================-->
      <!-- 上段（左）-->
      <xsl:choose>
        <!--決まり手の１字を上段エリアにはみ出し表示-->
        <xsl:when test="$RESULT_AREA_OVERFLOWED != ''">
          <xsl:value-of select="substring($PLAYER_INFO_1_LineData, 1, string-length($PLAYER_INFO_1_LineData)-1)"/>
          <xsl:value-of select="$RESULT_AREA_OVERFLOWED"/>
        </xsl:when>
        <!--決まり手エリアの括弧付きの時間（○分○秒○）が１文字多く、かつ上段（左）がNULLまたは最後の文字が空白の場合、開き括弧をはみ出し表示-->
        <xsl:when test="string-length($RESULT_AREA_INFO_LineData) = $RESULT_AREA_LENGTH +1 and starts-with($RESULT_AREA_INFO_LineData, '（')
                      and (substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) = $WhiteSpaceZenkaku_UTL
                        or substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) = '　'
                        or $PLAYER_INFO_1_LineData = '')">
          <xsl:value-of select="substring($PLAYER_INFO_1_LineData, 1, string-length($PLAYER_INFO_1_LineData)-1)"/>
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$PLAYER1_AREA_LENGTH - string-length(substring($PLAYER_INFO_1_LineData, 1, string-length($PLAYER_INFO_1_LineData)-1)) -1"/>
          </xsl:call-template>
          <xsl:text>（</xsl:text>
        </xsl:when>
        <xsl:when test="$PLAYER_INFO_1_LineData=''">
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$PLAYER1_AREA_LENGTH"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$PLAYER_INFO_1_LineData"/>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 結果 -->
      <xsl:choose>
        <!--括弧付きの時間（○分○秒○）が１文字多く、かつ上段（左）がNULLまたは最後の文字が空白の場合、
          先頭の開き括弧を上段（左）にはみ出し表示するので、決まり手エリアには２文字目以降を表示-->
        <xsl:when test="string-length($RESULT_AREA_INFO_LineData) = $RESULT_AREA_LENGTH +1 and starts-with($RESULT_AREA_INFO_LineData, '（')
                      and (substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) = $WhiteSpaceZenkaku_UTL
                        or substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) = '　'
                        or $PLAYER_INFO_1_LineData = '')">
          <xsl:value-of select="substring($RESULT_AREA_INFO_LineData, 2)"/>
        </xsl:when>
        <!--括弧付きの時間（○分○秒○）が１文字多く、かつ上段（左）の最後の文字が空白でない場合、当該行は空白とし、次行にはみ出し表示する-->
        <xsl:when test="string-length($RESULT_AREA_INFO_LineData) = $RESULT_AREA_LENGTH +1 and starts-with($RESULT_AREA_INFO_LineData, '（')
                      and (substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) != $WhiteSpaceZenkaku_UTL
                       and substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) != '　')">
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$RESULT_AREA_LENGTH"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <!--スペース埋め（上段（左）の閉じ括弧のはみ出しがある場合は、その分の文字数を減らす）-->
          <xsl:variable name="lengthOverflowedChar_PLAYER_INFO_1">
            <xsl:value-of select="string-length($PLAYER_INFO_1_LineData) - $PLAYER1_AREA_LENGTH"/>
          </xsl:variable>
          <xsl:value-of select="$RESULT_AREA_INFO_LineData"/>
          <xsl:choose>
            <xsl:when test="$lengthOverflowedChar_PLAYER_INFO_1 &gt; 0">
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$RESULT_AREA_LENGTH - string-length($RESULT_AREA_INFO_LineData)
                                                    - $lengthOverflowedChar_PLAYER_INFO_1"/>
              </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$RESULT_AREA_LENGTH - string-length($RESULT_AREA_INFO_LineData)"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 下段（右） -->
      <xsl:choose>
        <!--行末に閉じ括弧用記号がある場合は'）'に置き換える-->
        <xsl:when test="contains($PLAYER_INFO_2_LineData,$KakkoR)">
          <xsl:value-of select="translate($PLAYER_INFO_2_LineData, $KakkoR, '）')"/>
        </xsl:when>
        <xsl:when test="$PLAYER_INFO_2_LineData=''">
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$PLAYER2_AREA_LENGTH"/>
          </xsl:call-template>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$PLAYER_INFO_2_LineData"/>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!--===================-->
      <!-- 残り文字列取得    -->
      <!--===================-->
      <xsl:variable name="PLAYER_INFO_1_After">
        <xsl:choose>
          <xsl:when test="$PLAYER_INFO_1_LineData=''">
            <xsl:value-of select="$PLAYER_INFO_1"/>
          </xsl:when>
          <!--括弧付きの時間（○分○秒○）が１文字多く、かつ上段（左）の最後の文字が空白でない場合、次行の上段（左）エリアに開き括弧をはみ出し表示する-->
          <xsl:when test="string-length($RESULT_AREA_INFO_LineData) = $RESULT_AREA_LENGTH +1 and starts-with($RESULT_AREA_INFO_LineData, '（')
                        and (substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) != $WhiteSpaceZenkaku_UTL
                         and substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) != '　')">
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$PLAYER1_AREA_LENGTH -1"/>
            </xsl:call-template>
            <xsl:text>（</xsl:text>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="substring-after($PLAYER_INFO_1,$PLAYER_INFO_1_LineData)"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <xsl:variable name="PLAYER_INFO_2_After">
        <xsl:choose>
          <xsl:when test="$PLAYER_INFO_2_LineData=''">
            <xsl:value-of select="$PLAYER_INFO_2"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="substring-after($PLAYER_INFO_2,$PLAYER_INFO_2_LineData)"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <xsl:variable name="RESULT_AREA_INFO_After">
        <!--括弧付きの時間（○分○秒○）が１文字多く、かつ上段（左）がNULLでないまたは最後の文字が空白でない場合、次行にはみ出し表示する-->
        <xsl:if test="string-length($RESULT_AREA_INFO_LineData) = $RESULT_AREA_LENGTH +1 and starts-with($RESULT_AREA_INFO_LineData, '（')
                      and (substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) != $WhiteSpaceZenkaku_UTL
                       and substring($PLAYER_INFO_1_LineData, $PLAYER1_AREA_LENGTH) != '　'
                       and $PLAYER_INFO_1_LineData != '')">
          <xsl:value-of select="substring($RESULT_AREA_INFO_LineData, 2)"/>
        </xsl:if>
        <xsl:choose>
          <xsl:when test="$RESULT_AREA_INFO_LineData=''">
            <xsl:value-of select="$RESULT_AREA_INFO"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="substring-after($RESULT_AREA_INFO,$RESULT_AREA_INFO_LineData)"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!--===================-->
      <!-- 再帰呼び出し      -->
      <!--===================-->
      <xsl:call-template name="TaisenLayout_TORIKUMI_OSCOM">
        <xsl:with-param name="PLAYER_INFO_1">
          <xsl:choose>
            <xsl:when test="starts-with($PLAYER_INFO_1_After, $LineFeed_UTL)">
              <xsl:value-of select="substring-after($PLAYER_INFO_1_After,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$PLAYER_INFO_1_After"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="PLAYER_INFO_2">
          <xsl:choose>
            <xsl:when test="starts-with($PLAYER_INFO_2_After, $LineFeed_UTL)">
              <xsl:value-of select="substring-after($PLAYER_INFO_2_After,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$PLAYER_INFO_2_After"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="RESULT_AREA_INFO">
          <xsl:choose>
            <xsl:when test="starts-with($RESULT_AREA_INFO_After,$LineFeed_UTL)">
              <xsl:value-of select="substring-after($RESULT_AREA_INFO_After,$LineFeed_UTL)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$RESULT_AREA_INFO_After"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:with-param>
        <xsl:with-param name="PLAYER1_AREA_LENGTH" select="$PLAYER1_AREA_LENGTH"/>
        <xsl:with-param name="PLAYER2_AREA_LENGTH" select="$PLAYER2_AREA_LENGTH"/>
        <xsl:with-param name="RESULT_AREA_LENGTH" select="$RESULT_AREA_LENGTH"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 対戦型レイアウト整形処理で内部的に使用する置き換え記号 -->
  <!--=======================================================================================================-->
  <xsl:variable name="KakkoR">
    <xsl:text>＄</xsl:text>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 決まり手の７字取り処理。実際には１行６字で出力する。郷土力士勝負、幕下以下勝負、勝負などで使用-->
  <!--・１行が６字未満でも、スペースで補填する必要はないが、改行コードで終えること-->
  <!--・８字以上の決まり手は、５字で改行　　　　　　　　　　　　「がっしょう□」「LF」「ひねり」「LF」-->
  <!--・７字の決まり手は、１文字を上段にはみ出し表示　　　「う」「わてだしなげ」「LF」-->
  <!--　　ただし、はみ出し可能な空白が上段になければ５字で改行　「うわてだし□」「LF」「なげ」「LF」-->
  <!--・３字の決まり手は、５字取り　　　　　　　　　　　　　　　「不□戦□勝」「LF」-->
  <!--・２字の決まり手は、３字取り　　　　　　　　　　　　　　　「反□則」「LF」-->
  <!--・その他はそのまま出力　　　　　　　　　　　　　　　　　　「よりきり」「LF」-->
  <!-- ================================================================================= -->
  <xsl:template name="AddBRandSpaceToWinningTrick_OSCOM2">
    <!--上段（左）の力士名-->
    <xsl:param name="PLAYER_INFO_1"/>
    <!--決まり手（字取り加工前）-->
    <xsl:param name="WINNING_TRICK"/>
    <!--上段（左）力士名の文字数-->
    <xsl:param name="PLAYER1_AREA_LENGTH"/>
    <!--決まり手の文字数（字取り加工前）-->
    <xsl:param name="WINNING_TRICK_LENGTH"/>
    <!--決まり手エリアの文字数-->
    <xsl:param name="RESULT_AREA_LENGTH"/>
    <!--上段（左）へのはみ出し文字-->
    <xsl:param name="RESULT_AREA_OVERFLOWED"/>
    <xsl:choose>
      <!--８字以上の決まり手は、５字で改行-->
      <xsl:when test="$WINNING_TRICK_LENGTH &gt;= $RESULT_AREA_LENGTH +2">
        <xsl:variable name="tmpWinningTrickPlusSpace">
          <xsl:value-of select="substring($WINNING_TRICK, 1, $RESULT_AREA_LENGTH -1)"/>
          <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
          <xsl:value-of select="substring($WINNING_TRICK, $RESULT_AREA_LENGTH)"/>
        </xsl:variable>
        <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
          <xsl:with-param name="Data" select="$tmpWinningTrickPlusSpace"/>
          <xsl:with-param name="Length" select="$RESULT_AREA_LENGTH"/>
          <xsl:with-param name="LeftOrRight" select="1"/>
          <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
        </xsl:call-template>
      </xsl:when>
      <!--７字の決まり手は、上段の１行目の最後の文字が空白の場合は、１字をはみ出し処理-->
      <xsl:when test="$RESULT_AREA_OVERFLOWED != ''">
        <xsl:value-of select="substring($WINNING_TRICK, 2)"/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:when>
      <!--７字の決まり手は、上段の１行目の最後の文字が空白でない場合は、５字で改行-->
      <xsl:when test="$WINNING_TRICK_LENGTH = $RESULT_AREA_LENGTH +1
                        and substring($PLAYER_INFO_1, $PLAYER1_AREA_LENGTH, 1) != '　'">
        <xsl:variable name="tmpWinningTrickPlusSpace">
          <xsl:value-of select="substring($WINNING_TRICK, 1, $RESULT_AREA_LENGTH -1)"/>
          <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
          <xsl:value-of select="substring($WINNING_TRICK, $RESULT_AREA_LENGTH)"/>
        </xsl:variable>
        <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
          <xsl:with-param name="Data" select="$tmpWinningTrickPlusSpace"/>
          <xsl:with-param name="Length" select="$RESULT_AREA_LENGTH"/>
          <xsl:with-param name="LeftOrRight" select="1"/>
          <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
        </xsl:call-template>
      </xsl:when>
      <!--３字の決まり手は、５字取り-->
      <xsl:when test="$WINNING_TRICK_LENGTH = 3">
        <xsl:call-template name="FillSpace_UTL">
          <xsl:with-param name="Data" select="$WINNING_TRICK"/>
          <xsl:with-param name="AreaLength" select="5"/>
        </xsl:call-template>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:when>
      <!--２字の決まり手は、３字取り-->
      <xsl:when test="$WINNING_TRICK_LENGTH = 2">
        <xsl:call-template name="FillSpace_UTL">
          <xsl:with-param name="Data" select="$WINNING_TRICK"/>
          <xsl:with-param name="AreaLength" select="3"/>
        </xsl:call-template>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:when>
      <!--その他はそのまま出力-->
      <xsl:otherwise>
        <xsl:value-of select="$WINNING_TRICK"/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
</xsl:stylesheet>
