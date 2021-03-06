<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕下以下新番付 -->
	<!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--幕下以下新番付編集-->
      <xsl:call-template name="makusitaikasinbanduke_KAKUNIN" />
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
	<!--幕下以下新番付テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="makusitaikasinbanduke_KAKUNIN">
		<table xsl:use-attribute-sets="table_attribute_set">
			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--空白行-->
				<xsl:if test="position()!=1">
					<tr><td><br/></td></tr>
				</xsl:if>
				<!--テーブル見出し-->
				<xsl:call-template name="TableMidashi_makusitaikasinbanduke_KAKUNIN" />

				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="makusitaikasinbanduke_KAKUNIN" />
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下新番付テーブル見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="TableMidashi_makusitaikasinbanduke_KAKUNIN">
		<tr>
			<!--東西-->
			<td class="font_size_KAKUNIN" valign="center" align="left" colspan='20'>
				<xsl:for-each select="Meta/Title">
					<xsl:value-of select="." />
				</xsl:for-each>
			</td>
		</tr>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下新番付選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="makusitaikasinbanduke_KAKUNIN">
		<tr>
			<!--新位置-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
				<td class="font_size_KAKUNIN" valign="bottom" align="right">
					<nobr>
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--力士名-->
			<xsl:if test="//Standing/Player/PlayerName/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="bottom" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="bottom">
					<xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
						<nobr>
							<xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
							<xsl:text>改め</xsl:text>
						</nobr>
						<br/>
					</xsl:if>
					<nobr>
						<xsl:value-of select="PlayerName/Formal[not(@*)]" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--部屋-->
			<xsl:if test="//Standing/Player/Belong/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="bottom" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="bottom">
					<nobr>
						<xsl:value-of select="Belong/Formal[not(@*)]" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--出身地-->
			<xsl:if test="
				//Standing/Player/PlayerForSumo/NativeCountry/Formal[not(@*)] or 
				//Standing/Player/PlayerForSumo/NativeArea/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="bottom" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="bottom">
					<nobr>
						<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />
						<xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--初土俵-->
			<xsl:if test="//Standing/Player/PlayerForSumo/Debut/Writing">
				<td class="font_size_KAKUNIN" valign="bottom" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="bottom" align="left">
					<nobr>
						<xsl:value-of select="PlayerForSumo/Debut/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--昇降-->
			<xsl:if test="//Standing/Player/PlayerForSumo/RankShift/ShiftCount">
				<td class="font_size_KAKUNIN" valign="bottom" align="right">
					<nobr>
						<xsl:choose>
							<xsl:when test="PlayerForSumo/RankShift/ShiftCount = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="PlayerForSumo/RankShift/UpDown" />
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="PlayerForSumo/RankShift/ShiftCount"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
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
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
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
			<xsl:for-each select=".//PlayerForSumo/NativeCountry/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeArea/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/Debut/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/RankShift/UpDown">
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
