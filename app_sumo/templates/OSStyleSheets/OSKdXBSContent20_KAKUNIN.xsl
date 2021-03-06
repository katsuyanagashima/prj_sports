<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕下以下全成績 -->
  <!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--幕下以下全成績編集-->
      <xsl:call-template name="makusitaikazenseiseki_KAKUNIN" />
      <!--本文内注釈編集-->
      <xsl:for-each select="Body/TextNote">
        <table xsl:use-attribute-sets="table_attribute_set">
          <tr>
            <td class="font_size_KAKUNIN">
              <xsl:value-of select="." />
            </td>
          </tr>
        </table>
      </xsl:for-each>
      <xsl:for-each select="TextNote">
        <table xsl:use-attribute-sets="table_attribute_set">
          <tr>
            <td class="font_size_KAKUNIN">
              <xsl:value-of select="." />
            </td>
          </tr>
        </table>
      </xsl:for-each>
      <!--字解-->
      <xsl:call-template name="Gaiji_KAKUNIN" />
    </div>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下全成績テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="makusitaikazenseiseki_KAKUNIN">
		<!--Title-->
		<table xsl:use-attribute-sets="table_attribute_set" width="650">
			<tr>
				<td class="font_size_KAKUNIN" valign="top">
					<xsl:value-of select="./Head/Meta/Title" />
				</td>
			</tr>
		</table>

		<table xsl:use-attribute-sets="table_attribute_set">
			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--空白行-->
				<xsl:if test="position()!=1">
					<tr><td><br/></td></tr>
				</xsl:if>
				<!--テーブル見出し-->
				<xsl:call-template name="TableMidashi_makusitaikazenseiseki_KAKUNIN" />

				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="makusitaikazenseiseki_KAKUNIN" />
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下全成績テーブル見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="TableMidashi_makusitaikazenseiseki_KAKUNIN">
		<tr>
			<!--Title-->
			<td class="font_size_KAKUNIN" valign="center" align="left">
				<xsl:value-of select="Meta/Title" />
			</td>
			<!--部屋-->
			<xsl:if test="//Standing/Player/Belong/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="left">　部屋</td>
			</xsl:if>
			<!--勝休負-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="left">勝休負</td>
			</xsl:if>
		</tr>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下全成績選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="makusitaikazenseiseki_KAKUNIN">
		<tr>
			<!--地位、力士名-->
			<xsl:if test="
				//Standing/Player/PlayerForSumo/SumoGrade[not(@*)]/Writing or 
				//Standing/Player/PlayerName/Formal[not(@*)]
			">
				<td class="font_size_KAKUNIN" valign="bottom">
					<!--新位置-->
					<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[not(@*)]/Writing">
						<xsl:value-of select="PlayerForSumo/SumoGrade[not(@*)]/Writing" />
					</xsl:if>
					<!--力士名-->
					<xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
						<nobr>
							<xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
							<xsl:text>改め</xsl:text>
						</nobr>
						<br/>
						<xsl:text>　</xsl:text>
					</xsl:if>
					<nobr>
						<xsl:value-of select="PlayerName/Formal[not(@*)]" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--部屋-->
			<xsl:if test="//Standing/Player/Belong/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="bottom">
					<nobr>
						<xsl:text>（</xsl:text>
						<xsl:value-of select="Belong/Formal[not(@*)]" />
						<xsl:text>）</xsl:text>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--場所成績-->
<!--			<xsl:if test="//Standing/Player/Result[not(@*)]/ResultForSumo/SumoOutcomeTotal[WinCount or LossCount or DrawCount or AbsenceCount]">-->
<!--				<td class="font_size_KAKUNIN" valign="bottom" align="left">-->
<!--					<nobr>-->
<!--						<xsl:if test="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/WinCount != '０'">-->
<!--							<xsl:call-template name="RensuuHenkan">-->
<!--								<xsl:with-param name="Sts" select="3"/>-->
<!--								<xsl:with-param name="Pdata" select="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/WinCount"/>-->
<!--							</xsl:call-template>-->
<!--							<xsl:text>勝</xsl:text>-->
<!--						</xsl:if>-->
<!--						<xsl:if test="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/LossCount != '０'">-->
<!--							<xsl:call-template name="RensuuHenkan">-->
<!--								<xsl:with-param name="Sts" select="3"/>-->
<!--								<xsl:with-param name="Pdata" select="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/LossCount"/>-->
<!--							</xsl:call-template>-->
<!--							<xsl:text>敗</xsl:text>-->
<!--						</xsl:if>-->
<!--						<xsl:if test="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/DrawCount != '０'">-->
<!--							<xsl:call-template name="RensuuHenkan">-->
<!--								<xsl:with-param name="Sts" select="3"/>-->
<!--								<xsl:with-param name="Pdata" select="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/DrawCount"/>-->
<!--							</xsl:call-template>-->
<!--							<xsl:text>分</xsl:text>-->
<!--						</xsl:if>-->
<!--						<xsl:if test="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/AbsenceCount != '０'">-->
<!--							<xsl:call-template name="RensuuHenkan">-->
<!--								<xsl:with-param name="Sts" select="3"/>-->
<!--								<xsl:with-param name="Pdata" select="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/AbsenceCount"/>-->
<!--							</xsl:call-template>-->
<!--							<xsl:text>休</xsl:text>-->
<!--						</xsl:if>-->
<!--					</nobr>-->
<!--					<br/>-->
<!--				</td>-->
<!--			</xsl:if>-->
			<xsl:if test="
				//Standing/Player/Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/Writing or 
				//Standing/Player/PlayerForSumo/Retirement/Writing
			">
				<td class="font_size_KAKUNIN" valign="bottom" align="left">
					<xsl:value-of select="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/Writing" />
					<xsl:value-of select="PlayerForSumo/Retirement/Writing" />
				</td>
			</xsl:if>

			<!--初土俵（付出）-->
			<xsl:if test="//Standing/Player/PlayerForSumo/Debut/Writing">
				<td class="font_size_KAKUNIN" valign="bottom" align="left">
					<nobr>
						<xsl:value-of select="PlayerForSumo/Debut/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
		</tr>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--Gaijiテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="Gaiji_KAKUNIN">

		<!-- 字解編集 -->
		<xsl:variable name="JIKAI_DATA">
			<xsl:for-each select=".//Body/TextNote">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Meta/Title">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[not(@*)]/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Belong/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/Retirement/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/Debut/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
		</xsl:variable>

		<xsl:if test="($JIKAI_DATA!='')">
			<!--字解が存在した場合-->
			<!--改ページ-->
			<p class="pb" />

			<!--字解見出し-->
			<div class="font_size_KAKUNIN">
				<xsl:text>字解情報</xsl:text>
			</div>

			<!--字解-->
			<xsl:value-of disable-output-escaping="yes" select="$JIKAI_DATA" />

			<!--改行-->
			<br />
		</xsl:if>

	</xsl:template>
</xsl:stylesheet>
