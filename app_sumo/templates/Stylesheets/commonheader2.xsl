<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
<!--=============================================================================
　プレーンテキスト・全スタイルシート共通ヘッダー用
4.0版　 2014.12.19 プレーンテキスト版として新規公開
4.01版　2015.03.31 解禁日時を追加
4.02版　2015.05.29 改行コードをCRLFに統一
================================================================================-->
  <!--ProductID-->
  <xsl:variable name="PID">
    <xsl:text>　製品ＩＤ：</xsl:text>
  </xsl:variable>
  <!--Test区分-->
  <xsl:variable name="TKubun">
    <xsl:text>　Test区分：</xsl:text>
  </xsl:variable>
  <!--日・時間-->
  <xsl:variable name="CDate">
    <xsl:text>　配信日時：</xsl:text>
  </xsl:variable>
  <!--修正区分-->
  <xsl:variable name="SKubun">
    <xsl:text>　修正区分：</xsl:text>
  </xsl:variable>
  <!--主ヘッダ-->
  <xsl:variable name="Kijishu">
    <xsl:text>　記事種別：</xsl:text>
  </xsl:variable>
  <!--副ヘッダ-->
  <xsl:variable name="SubH">
    <xsl:text>　副ヘッダ：</xsl:text>
  </xsl:variable>
  <!--コメント部-->
  <xsl:variable name="Comt">
    <xsl:text>コメント部：</xsl:text>
  </xsl:variable>
  <!--主見出し-->
  <xsl:variable name="MainM">
    <xsl:text>　　見出し：</xsl:text>
  </xsl:variable>
  <!--脇見出し-->
  <xsl:variable name="SubM">
    <xsl:text>　脇見出し：</xsl:text>
  </xsl:variable>
  <!--編注-->
  <xsl:variable name="Hen">
    <xsl:text>　【編注】：</xsl:text>
  </xsl:variable>
  <!--末尾編注-->
  <xsl:variable name="EHen">
    <xsl:text>　末尾編注：</xsl:text>
  </xsl:variable>
  <!--解禁日時 2015.3.31改修-->
  <xsl:variable name="Opn">
    <xsl:text>　解禁日時：</xsl:text>
  </xsl:variable>
  <!--部署 2013.4.4改修-->
  <xsl:variable name="Busho">
    <xsl:text>　　部署名：</xsl:text>
  </xsl:variable>
  <!--ユーザー 2013.4.4改修　-->
  <xsl:variable name="User">
    <xsl:text>　ユーザー：</xsl:text>
  </xsl:variable>
  <!--修正区分の折り返し字数-->
  <xsl:variable name="Shujisuu">
    <xsl:text>24</xsl:text>
  </xsl:variable>
  <!--編注部など折り返し字数-->
  <xsl:variable name="Rtnjisuu">
    <xsl:text>45</xsl:text>
  </xsl:variable>
  <!--１行２カラム表示(見出し・脇見出し)折り返し字数-->
  <xsl:variable name="Rtnjisuu_Colspan">
    <xsl:text>20</xsl:text>
  </xsl:variable>
  <!--内容情報部ヘッダ-->
  <xsl:template name="InContent_InMetadata">
    <style type="text/css">
      <!--.font_1{font-size:10.5pt;}-->
      <!--.font_2{font-size:12pt;}-->
				.font_1{font-size:9pt;
                background-color: #dcdcdc;
                color: brown;
                width: 6em;
                }
				.font_2{font-size:9pt;}
			</style>
    <xsl:for-each select="//InContent/InMetadata">
      <!--<div style="width:720pt;">-->
      <table class="commonHeader">
        <tr>
          <!--製品ＩＤ-->
          <td class="font_1" align="left">
            <nobr>
              <font color="brown">
                <xsl:value-of select="$PID"/>
              </font>
            </nobr>
          </td>
          <td class="font_2">
            <nobr>
              <xsl:choose>
                <xsl:when test="//InProductId">
                  <xsl:value-of select="//InProductId"/>
                </xsl:when>
              </xsl:choose>
            </nobr>
          </td>
          <!--記事種別-->
          <td class="font_1">
            <nobr>
              <font color="brown">
                <xsl:value-of select="$Kijishu"/>
              </font>
            </nobr>
          </td>
          <td class="font_2" align="left" colspan="3">
            <nobr>
              <xsl:choose>
                <xsl:when test="//InMainHeader/InMainRank[not(.='')]">
                  <xsl:text>(格)</xsl:text>
                  <xsl:value-of select="//InMainHeader/InMainRank"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InMainHeader/InPriority[not(.='')]">
                  <xsl:text>(優)</xsl:text>
                  <xsl:value-of select="//InMainHeader/InPriority"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InMainHeader/InOfficeId[not(.='')]">
                  <xsl:text>　</xsl:text>
                  <xsl:value-of select="//InMainHeader/InOfficeId"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InMainHeader/InTotalNo[not(.='')]">
                  <xsl:value-of select="//InMainHeader/InTotalNo"/>
                </xsl:when>
              </xsl:choose>
              <!--記事種別、記事番号-->
              <xsl:choose>
                <xsl:when test="//InNewsGenre">
                  <xsl:text>　</xsl:text>
                  <xsl:value-of select="//InNewsGenre"/>
                  <xsl:value-of select="//InNewsNo"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InSubRank  and not(//InNewsNo)">
                  <xsl:text>　　　</xsl:text>
                  <xsl:value-of select="//InSubRank"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InSubRank  and //InNewsNo">
                  <xsl:value-of select="//InSubRank"/>
                </xsl:when>
              </xsl:choose>
              <!--続き指定-->
              <xsl:choose>
                <xsl:when test="//InSendSeq">
                  <xsl:value-of select="concat('　',//InSendSeqTotal,//@InSendSeqKind,//InSendSeqNo)"/>
                </xsl:when>
              </xsl:choose>
            </nobr>
          </td>
        </tr>
        <tr>
          <!--配信日時-->
          <td class="font_1">
            <nobr>
              <font color="brown">
                <xsl:value-of select="$CDate"/>
              </font>
            </nobr>
          </td>
          <td class="font_2">
            <nobr>
              <xsl:choose>
                <xsl:when test="//InDateTime">
                  <xsl:value-of select="//InDateTime"/>
                </xsl:when>
              </xsl:choose>
            </nobr>
          </td>
          <!--Test区分-->
          <td class="font_1">
            <nobr>
              <font color="brown">
                <xsl:value-of select="$TKubun"/>
              </font>
            </nobr>
          </td>
          <td class="font_2" align="left" style="width:4em">
            <nobr>
              <xsl:choose>
                <xsl:when test="//InTestClass">
                  <xsl:value-of select="//InTestClass"/>
                </xsl:when>
              </xsl:choose>
            </nobr>
          </td>
          <!--修正区分-->
          <td class="font_1">
            <nobr>
              <font color="brown">
                <xsl:value-of select="$SKubun"/>
              </font>
            </nobr>
          </td>
          <td class="font_2" align="left">
            <nobr>
              <xsl:choose>
                <xsl:when test="//InModifyInfo">
                  <xsl:call-template name="AddTagsHL">
                    <xsl:with-param name="HData">
                      <xsl:for-each select="//InModifyInfo">
                        <xsl:value-of select="."/>
                        <xsl:if test="not(position() = last())">
                          <xsl:value-of select="'。'"/>
                        </xsl:if>
                      </xsl:for-each>
                    </xsl:with-param>
                    <xsl:with-param name="LLB" select="$Shujisuu"/>
                  </xsl:call-template>
                </xsl:when>
              </xsl:choose>
            </nobr>
          </td>
        </tr>
      </table>
      <table class="commonHeader">
        <!--
        <tr>
        -->
        <!--主ヘッダー行-->
        <!--
          <td class="font_1">
            <nobr>
              <font color="brown">
                <xsl:value-of select="$Kijishu"/>
              </font>
            </nobr>
          </td>
          <td class="font_2" align="left">
            <nobr>
              <xsl:choose>
                <xsl:when test="//InMainHeader/InMainRank[not(.='')]">
                  <xsl:text>(格)</xsl:text>
                  <xsl:value-of select="//InMainHeader/InMainRank"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InMainHeader/InPriority[not(.='')]">
                  <xsl:text>(優)</xsl:text>
                  <xsl:value-of select="//InMainHeader/InPriority"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InMainHeader/InOfficeId[not(.='')]">
                  <xsl:text>　</xsl:text>
                  <xsl:value-of select="//InMainHeader/InOfficeId"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InMainHeader/InTotalNo[not(.='')]">
                  <xsl:value-of select="//InMainHeader/InTotalNo"/>
                </xsl:when>
              </xsl:choose>
              -->
        <!--記事種別、記事番号-->
        <!--
              <xsl:choose>
                <xsl:when test="//InNewsGenre">
                  <xsl:text>　</xsl:text>
                  <xsl:value-of select="//InNewsGenre"/>
                  <xsl:value-of select="//InNewsNo"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InSubRank  and not(//InNewsNo)">
                  <xsl:text>　　　</xsl:text>
                  <xsl:value-of select="//InSubRank"/>
                </xsl:when>
              </xsl:choose>
              <xsl:choose>
                <xsl:when test="//InSubRank  and //InNewsNo">
                  <xsl:value-of select="//InSubRank"/>
                </xsl:when>
              </xsl:choose>
              -->
        <!--続き指定-->
        <!--
              <xsl:choose>
                <xsl:when test="//InSendSeq">
                  <xsl:value-of select="concat('　',//InSendSeqTotal,//@InSendSeqKind,//InSendSeqNo)"/>
                </xsl:when>
              </xsl:choose>
            </nobr>
          </td>
        </tr>
        -->
        <!--副ヘッダ-->
        <xsl:choose>
          <xsl:when test="//InSendControl">
            <tr>
              <td class="font_1" valign="top">
                <nobr>
                  <font color="brown">
                    <xsl:value-of select="$SubH"/>
                  </font>
                </nobr>
              </td>
              <td class="font_2" colspan="3">
                <nobr>
                  <xsl:call-template name="AddTagsHL">
                    <xsl:with-param name="HData">
                      <xsl:call-template name="CH_InSendControl"/>
                    </xsl:with-param>
                    <xsl:with-param name="LLB" select="$Rtnjisuu"/>
                  </xsl:call-template>
                </nobr>
              </td>
            </tr>
          </xsl:when>
        </xsl:choose>
        <!--コメント-->
        <xsl:choose>
          <xsl:when test="//InNewsInfo/InSupportControl/InComment">
            <tr align="left">
              <td class="font_1" valign="top">
                <font color="brown">
                  <xsl:value-of select="$Comt"/>
                </font>
              </td>
              <td class="font_2" colspan="3">
                <nobr>
                  <xsl:call-template name="AddTagsHL">
                    <xsl:with-param name="HData">
                      <xsl:value-of select="//InComment"/>
                    </xsl:with-param>
                    <xsl:with-param name="LLB" select="$Rtnjisuu"/>
                  </xsl:call-template>
                </nobr>
              </td>
            </tr>
          </xsl:when>
        </xsl:choose>
        <!--主見出し-->
        <xsl:if test="//InHeadLine or //InSubHeadLine">
          <tr>
            <xsl:choose>
              <xsl:when test="//InHeadLine">
                <!--<tr>-->
                <td class="font_1" valign="top">
                  <nobr>
                    <font color="brown">
                      <xsl:value-of select="$MainM"/>
                    </font>
                  </nobr>
                </td>
                <xsl:choose>
                  <xsl:when test="//InSubHeadLine">
                    <td class="font_2" style="width: 20em;">
                      <nobr>
                        <xsl:call-template name="AddTagsHL">
                          <xsl:with-param name="HData">
                            <xsl:for-each select="//InHeadLine">
                              <xsl:text>◎</xsl:text>
                              <xsl:value-of select="."/>
                              <xsl:if test="not(position() = last())">
                                <xsl:value-of select="'。'"/>
                              </xsl:if>
                            </xsl:for-each>
                          </xsl:with-param>
                          <xsl:with-param name="LLB" select="$Rtnjisuu_Colspan"/>
                        </xsl:call-template>
                      </nobr>
                    </td>
                  </xsl:when>
                  <xsl:otherwise>
                    <td class="font_2" colspan="3">
                      <nobr>
                        <xsl:call-template name="AddTagsHL">
                          <xsl:with-param name="HData">
                            <xsl:for-each select="//InHeadLine">
                              <xsl:text>◎</xsl:text>
                              <xsl:value-of select="."/>
                              <xsl:if test="not(position() = last())">
                                <xsl:value-of select="'。'"/>
                              </xsl:if>
                            </xsl:for-each>
                          </xsl:with-param>
                          <xsl:with-param name="LLB" select="$Rtnjisuu"/>
                        </xsl:call-template>
                      </nobr>
                    </td>
                  </xsl:otherwise>
                </xsl:choose>
                <!--</tr>-->
              </xsl:when>
            </xsl:choose>
            <!--脇見出し-->
            <xsl:choose>
              <xsl:when test="//InSubHeadLine">
                <!--<tr>-->
                <td class="font_1" valign="top">
                  <nobr>
                    <font color="brown">
                      <xsl:value-of select="$SubM"/>
                    </font>
                  </nobr>
                </td>
                <td class="font_2">
                  <nobr>
                    <xsl:call-template name="AddTagsHL">
                      <xsl:with-param name="HData">
                        <xsl:for-each select="//InSubHeadLine">
                          <xsl:value-of select="."/>
                          <xsl:if test="not(position() = last())">
                            <xsl:value-of select="'。'"/>
                          </xsl:if>
                        </xsl:for-each>
                      </xsl:with-param>
                      <xsl:with-param name="LLB" select="$Rtnjisuu_Colspan"/>
                    </xsl:call-template>
                  </nobr>
                </td>
                <!--</tr>-->
              </xsl:when>
            </xsl:choose>
          </tr>
        </xsl:if>
        <!--編注-->
        <xsl:choose>
          <!--記事以外の編注=InEditLine出力-->
          <xsl:when test="not(substring(//InProductId,9,2)='ＤＨ')">
            <xsl:choose>
              <xsl:when test="//InEditLine">
                <tr>
                  <td class="font_1" valign="top">
                    <nobr>
                      <font color="brown">
                        <xsl:value-of select="$Hen"/>
                      </font>
                    </nobr>
                  </td>
                  <td class="font_2" colspan="3">
                    <nobr>
                      <xsl:call-template name="AddTagsHL">
                        <xsl:with-param name="HData">
                          <xsl:for-each select="//InEditLine">
                            <xsl:value-of select="."/>
                            <xsl:if test="not(position() = last())">
                              <xsl:value-of select="'、'"/>
                            </xsl:if>
                          </xsl:for-each>
                        </xsl:with-param>
                        <xsl:with-param name="LLB" select="$Rtnjisuu"/>
                      </xsl:call-template>
                    </nobr>
                  </td>
                </tr>
              </xsl:when>
            </xsl:choose>
            <!-- 部署・ユーザー情報追加　改修2013.4.4　-->
            <xsl:choose>
              <xsl:when test="//InNewsGenre='加盟'">
                <xsl:if test="//InSendFrom or //ByLine">
                  <tr>
                    <!--<xsl:if test="//InSendFrom">-->
                      <!--<tr>-->
                      <td class="font_1" valign="top">
                        <nobr>
                          <font color="brown">
                            <xsl:value-of select="$Busho"/>
                          </font>
                        </nobr>
                      </td>
                      <td class="font_2" style="width: 20em;">
                        <nobr>
                          <xsl:if test="//InSendFrom">
                          <xsl:call-template name="AddTagsHL">
                            <xsl:with-param name="HData">
                              <xsl:value-of select="//InSendFrom"/>
                            </xsl:with-param>
                            <xsl:with-param name="LLB" select="$Rtnjisuu"/>
                          </xsl:call-template>
                          </xsl:if>
                        </nobr>
                      </td>
                      <!--</tr>-->
                    <!--</xsl:if>-->
                    <!--<xsl:if test="//ByLine">-->
                      <!--<tr>-->
                      <td class="font_1" valign="top">
                        <nobr>
                          <font color="brown">
                            <xsl:value-of select="$User"/>
                          </font>
                        </nobr>
                      </td>
                      <td class="font_2" style="width: 20em;">
                        <nobr>
                          <xsl:if test="//ByLine">
                          <xsl:call-template name="AddTagsHL">
                            <xsl:with-param name="HData">
                              <xsl:value-of select="//ByLine"/>
                            </xsl:with-param>
                            <xsl:with-param name="LLB" select="$Rtnjisuu"/>
                          </xsl:call-template>
                          </xsl:if>
                        </nobr>
                      </td>
                      <!--</tr>-->
                    <!--</xsl:if>-->
                  </tr>
                </xsl:if>
              </xsl:when>
            </xsl:choose>
          </xsl:when>
          <!--一般記事編注＝InNewsLineTextを編注とする-->
          <xsl:otherwise>
            <xsl:choose>
              <!--        <xsl:when test="//NewsComponent/NewsLines/NewsLine">   -->
              <xsl:when test="//NewsComponent/NewsLines/NewsLine/NewsLineType[@FormalName='EditInfo']">
                <tr>
                  <td class="font_1" valign="top">
                    <font color="brown">
                      <xsl:value-of select="$Hen"/>
                    </font>
                  </td>
                  <td class="font_2" colspan="3">
                    <nobr>
                      <xsl:call-template name="AddTagsHL">
                        <xsl:with-param name="HData">
                          <!--2012.06.27 変数EditCnt追加。EditInfoの個数を退避し、最後の文章の後のみ「。」を編集-->
                          <xsl:variable name="EditCnt" select="count(//NewsLineType[@FormalName='EditInfo'])"/>
                          <xsl:for-each select="//NewsComponent/NewsLines/NewsLine">
                            <xsl:if test="NewsLineType[@FormalName='EditInfo']">
                              <xsl:value-of select="."/>
                              <!--2012.06.25 最後の見出しのみ末尾に区切りの「。」を表示-->
                              <xsl:if test="not($EditCnt = position())">
                                <xsl:value-of select="'。'"/>
                              </xsl:if>
                            </xsl:if>
                          </xsl:for-each>
                        </xsl:with-param>
                        <xsl:with-param name="LLB" select="$Rtnjisuu"/>
                      </xsl:call-template>
                    </nobr>
                  </td>
                </tr>
              </xsl:when>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
        <!--共通ヘッダに表示する末尾編注は記事以外のみ-->
        <xsl:choose>
          <xsl:when test="not(substring(//InProductId,9,2)='ＤＨ')">
            <xsl:choose>
              <xsl:when test="//InEndLine">
                <tr>
                  <td class="font_1" valign="top">
                    <nobr>
                      <font color="brown">
                        <xsl:value-of select="$EHen"/>
                      </font>
                    </nobr>
                  </td>
                  <td class="font_2" colspan="3">
                    <nobr>
                      <xsl:call-template name="AddTagsHL">
                        <xsl:with-param name="HData">
                          <xsl:for-each select="//InEndLine">
                            <xsl:value-of select="."/>
                            <xsl:if test="not(position() = last())">
                              <xsl:value-of select="'、'"/>
                            </xsl:if>
                          </xsl:for-each>
                        </xsl:with-param>
                        <xsl:with-param name="LLB" select="$Rtnjisuu"/>
                      </xsl:call-template>
                    </nobr>
                  </td>
                </tr>
              </xsl:when>
            </xsl:choose>
          </xsl:when>
        </xsl:choose>
        <!--解禁情報-->
         <xsl:choose>
          <xsl:when test="//InLimitation">
            <tr>
              <td class="font_1" valign="top">
                <font color="brown">
                  <xsl:value-of select="$Opn"/>
                </font>
              </td>
              <td class="font_2" colspan="3">
                <xsl:value-of select="//InLimitation"/>
              </td>
            </tr>
          </xsl:when>
        </xsl:choose>
      </table>
      <!--</div>-->
    </xsl:for-each>
    <br/>
  </xsl:template>
  <!--40行で折り返し-->
  <xsl:template name="AddTagsHL">
    <!--処理対象文字列-->
    <xsl:param name="HData"/>
    <!--改行文字数-->
    <xsl:param name="LLB"/>
    <!--文字長得る-->
    <xsl:variable name="HLen">
      <xsl:value-of select="string-length($HData)"/>
    </xsl:variable>
    <xsl:choose>
      <!--①文字数が改行文字数よりも大きい場合改行文字数分表示-->
      <xsl:when test="$HLen &gt; $LLB">
        <!--改行文字数分表示-->
        <xsl:value-of select="substring($HData,1, $LLB)"/>
        <br/>
        <!--AddTagsHテンプレートを再起呼び出し-->
        <xsl:call-template name="AddTagsHL">
          <xsl:with-param name="HData" select="substring($HData,$LLB+1,string-length($HData)-$LLB)"/>
          <xsl:with-param name="LLB" select="$LLB"/>
        </xsl:call-template>
      </xsl:when>
      <!--②文字数が改行文字数よりも小さい場合⌘の前までを表示-->
      <xsl:otherwise>
        <xsl:value-of select="substring($HData,1,$HLen)"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--******************************************-->
  <!--haisin block1-->
  <!--******************************************-->
  <xsl:template name="CH_InSendControl">
    <xsl:for-each select="//InSendControl">
      <nobr>
        <xsl:choose>
          <!--ブロック、個別、解禁-->
          <xsl:when test="//InSendBlkInfo and //InSendIndInfo and //InSendRestrict">
            <xsl:text>【</xsl:text>
            <xsl:call-template name="CH_InSendBlkInfo"/>
            <xsl:call-template name="CH_InSendIndInfo"/>
            <xsl:text>、</xsl:text>
            <xsl:value-of select="//InSendRestrict"/>
            <xsl:text>】</xsl:text>
          </xsl:when>
          <!--ブロック、個別-->
          <xsl:when test="//InSendBlkInfo and //InSendIndInfo">
            <xsl:text>【</xsl:text>
            <xsl:call-template name="CH_InSendBlkInfo"/>
            <xsl:call-template name="CH_InSendIndInfo"/>
            <xsl:text>】</xsl:text>
          </xsl:when>
          <!--ブロック、解禁-->
          <xsl:when test="//InSendBlkInfo and //InSendRestrict">
            <xsl:text>【</xsl:text>
            <xsl:call-template name="CH_InSendBlkInfo"/>
            <xsl:text>●</xsl:text>
            <xsl:value-of select="//InSendRestrict"/>
            <xsl:text>】</xsl:text>
          </xsl:when>
          <!--個別、解禁-->
          <xsl:when test="//InSendIndInfo and //InSendRestrict">
            <xsl:text>【</xsl:text>
            <xsl:call-template name="CH_InSendIndInfo"/>
            <xsl:text>、</xsl:text>
            <xsl:value-of select="//InSendRestrict"/>
            <xsl:text>】</xsl:text>
          </xsl:when>
          <!--ブロック-->
          <xsl:when test="//InSendBlkInfo">
            <xsl:text>【</xsl:text>
            <xsl:call-template name="CH_InSendBlkInfo"/>
            <xsl:text>】</xsl:text>
          </xsl:when>
          <!--個別-->
          <xsl:when test="//InSendIndInfo">
            <xsl:text>【</xsl:text>
            <xsl:call-template name="CH_InSendIndInfo"/>
            <xsl:text>】</xsl:text>
          </xsl:when>
          <!--解禁-->
          <xsl:when test="//InSendRestrict">
            <xsl:text>【●</xsl:text>
            <xsl:value-of select="//InSendRestrict"/>
            <xsl:text>】</xsl:text>
          </xsl:when>
        </xsl:choose>
      </nobr>
    </xsl:for-each>
  </xsl:template>
  <!--******************************************-->
  <!--haisin block wo matomeru-->
  <!--******************************************-->
  <xsl:template name="CH_InSendBlkInfo">
    <xsl:for-each select="//InSendBlkInfo">
      <xsl:for-each select="InSendBlk">
        <nobr>
          <xsl:value-of select="."/>
        </nobr>
        <xsl:if test="not(position()=last())">
          <nobr>
            <xsl:text>、</xsl:text>
          </nobr>
        </xsl:if>
      </xsl:for-each>
    </xsl:for-each>
  </xsl:template>
  <!--******************************************-->
  <!--haisin kobetu wo matomeru-->
  <!--******************************************-->
  <xsl:template name="CH_InSendIndInfo">
    <xsl:for-each select="//InSendIndInfo">
      <xsl:for-each select="InSendInd">
        <xsl:if test="(position()=1) and (substring(.,1,1) != '●')">
          <xsl:text>●</xsl:text>
        </xsl:if>
        <nobr>
          <xsl:choose>
            <xsl:when test="substring(.,1,1) = '●'">
              <xsl:if test="position()=1">
                <xsl:text>●</xsl:text>
              </xsl:if>
              <xsl:value-of select="substring-after(.,'●')"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="."/>
            </xsl:otherwise>
          </xsl:choose>
          <!--
          <xsl:value-of select="."/>
-->
        </nobr>
        <xsl:if test="not(position()=last())">
          <nobr>
            <xsl:text>、</xsl:text>
          </nobr>
        </xsl:if>
      </xsl:for-each>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
