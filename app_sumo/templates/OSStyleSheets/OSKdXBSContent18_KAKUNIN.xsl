<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・階級別成績上位力士 -->
  <!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--階級別成績上位力士編集-->
      <xsl:call-template name="jouirikisi_KAKUNIN" />
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
	<!--階級別成績上位力士テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="jouirikisi_KAKUNIN">
		<!--Title-->
		<table xsl:use-attribute-sets="table_attribute_set" width="650">
			<tr>
				<xsl:for-each select="Body">
					<td class="font_size_KAKUNIN" valign="top">
						<xsl:value-of select="./Head/Meta/Title" />
					</td>
				</xsl:for-each>
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
				<xsl:call-template name="TableMidashi_jouirikisi_KAKUNIN" />

				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="jouirikisi_KAKUNIN" />
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--階級別成績上位力士テーブル見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="TableMidashi_jouirikisi_KAKUNIN">
		<!--Title-->
		<xsl:for-each select="Meta/Title">
			<tr>
				<td class="font_size_KAKUNIN" valign="center" align="left" colspan="20">
						<xsl:value-of select="." />
				</td>
			</tr>
		</xsl:for-each>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--階級別成績上位力士選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="jouirikisi_KAKUNIN">
		<tr>
			<!--地位、力士名-->
			<xsl:if test="
				//Standing/Player/PlayerForSumo/SumoGrade[not(@*)]/Writing or 
				//Standing/Player/PlayerName/Formal[not(@*)]
			">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
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
				<td class="font_size_KAKUNIN" valign="bottom" align="left">
					<nobr>
						<xsl:text>（</xsl:text>
						<xsl:value-of select="Belong/Formal[not(@*)]" />
						<xsl:text>）</xsl:text>
					</nobr>
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
