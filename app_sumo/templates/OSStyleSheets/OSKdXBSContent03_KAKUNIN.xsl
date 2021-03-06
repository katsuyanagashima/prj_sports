<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・新番付 -->
	<!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--新番付編集-->
      <xsl:call-template name="sinbanduke_KAKUNIN" />
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
	<!--新番付テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="sinbanduke_KAKUNIN">
		<!--Title-->
		<table xsl:use-attribute-sets="table_attribute_set" width="650">
			<tr>
				<td class="font_size_KAKUNIN" valign="top">
					<xsl:value-of select="./Head/Meta/Title" />
				</td>
			</tr>
		</table>

		<!--Bodyタグを編集-->
		<table xsl:use-attribute-sets="table_attribute_set">
			<xsl:for-each select="Body">
				<!--改ページ-->
				<xsl:if test="position()!=1">
					<tr><td><p class="pb" /><br/></td></tr>
				</xsl:if>
				<!--テーブル見出し-->
				<xsl:call-template name="TableMidashi_sinbanduke_KAKUNIN" />

				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="sinbanduke_KAKUNIN" />
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--新番付テーブル見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="TableMidashi_sinbanduke_KAKUNIN">
		<tr>
			<!--東西-->
			<td class="font_size_KAKUNIN" valign="center" align="left" colspan='3'>
				<xsl:text>　　　　 　</xsl:text>
				<xsl:value-of select="Meta/Title" />
			</td>
		</tr>
		<tr>
			<!--新位置-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="left">新位置</td>
			</xsl:if>
			<!--新再-->
			<xsl:if test="//Standing/Player/PlayerForSumo/RankAttribute/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
			</xsl:if>
			<!--力士名-->
			<xsl:if test="//Standing/Player/PlayerName/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="left">力士名</td>
			</xsl:if>
			<!--年齢-->
			<xsl:if test="//Standing/Player/Age">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
			</xsl:if>
			<!--部屋-->
			<xsl:if test="//Standing/Player/Belong/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="left">部屋</td>
			</xsl:if>
			<!--出身地-->
			<xsl:if test="
				//Standing/Player/PlayerForSumo/NativeCountry/Formal[not(@*)] or 
				//Standing/Player/PlayerForSumo/NativeArea/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="left">出身地</td>
			</xsl:if>
			<!--旧位置-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='旧位置']/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="left">旧位置</td>
			</xsl:if>
			<!--昇降情報-->
			<xsl:if test="//Standing/Player/PlayerForSumo/RankShift">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="center">昇降</td>
			</xsl:if>
			<!--先場所成績-->
			<xsl:if test="//Standing/Player/Result[@Period='先場所']/ResultForSumo/SumoOutcomeTotal/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="left">先場所成績</td>
			</xsl:if>
			<!--初土俵-->
			<xsl:if test="//Standing/Player/PlayerForSumo/Debut/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="left">初土俵</td>
			</xsl:if>
			<!--身長(cm)-->
			<xsl:if test="//Standing/Player/Height">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="center">身長</td>
			</xsl:if>
			<!--体重(kg)-->
			<xsl:if test="//Standing/Player/Weight">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="center">体重</td>
			</xsl:if>
			<!--前回体重比-->
			<xsl:if test="//Standing/Player/PlayerForSumo/WeightDefference">
				<td class="font_size_KAKUNIN" valign="top" align="left">前比</td>
			</xsl:if>
		</tr>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--新番付選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="sinbanduke_KAKUNIN">
		<!--力士名（改め）-->
		<xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
			<tr>
				<!--新位置（間隔をあけるため）-->
				<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
					<td class="font_size_KAKUNIN" valign="top" align="right">
						<br/>
					</td>
				</xsl:if>
				<!--新再-->
				<xsl:if test="//Standing/Player/PlayerForSumo/RankAttribute/Writing">
					<td class="font_size_KAKUNIN" valign="top" align="right">
						<br/>
					</td>
				</xsl:if>
				<!--力士名（改め）-->
				<td class="font_size_KAKUNIN" align="left">
					<nobr>
						<xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
						<xsl:text>改め</xsl:text>
					</nobr>
					<br/>
				</td>
			</tr>
		</xsl:if>
		<tr>
			<!--新位置-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--新再-->
			<xsl:if test="//Standing/Player/PlayerForSumo/RankAttribute/Writing">
				<td class="font_size_KAKUNIN" valign="top">
					<nobr>
						<xsl:value-of select="PlayerForSumo/RankAttribute/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--力士名-->
			<xsl:if test="//Standing/Player/PlayerName/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top">
					<nobr>
						<xsl:value-of select="PlayerName/Formal[not(@*)]" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--年齢-->
			<xsl:if test="//Standing/Player/Age">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<xsl:call-template name="RensuuHenkan">
						<xsl:with-param name="Sts" select="3"/>
						<xsl:with-param name="Pdata" select="Age"/>
					</xsl:call-template>
				</td>
			</xsl:if>
			<!--部屋-->
			<xsl:if test="//Standing/Player/Belong/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top">
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
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top">
					<nobr>
						<xsl:call-template name="AddBR_KAKUNIN_OSCOM">
							<!--処理対象文字列-->
							<xsl:with-param name="Data">
								<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />
								<xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
							</xsl:with-param>
							<!--改行文字数-->
							<xsl:with-param name="Length" select="8" />
							<!--編集パターン-->
							<xsl:with-param name="EditPattern" select="3" />
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--旧位置-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='旧位置']/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="left">
					<nobr>
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='旧位置']/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--昇降-->
			<xsl:if test="//Standing/Player/PlayerForSumo/RankShift/ShiftCount">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="right">
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
			<!--先場所成績-->
			<xsl:if test="//Standing/Player/Result[@Period='先場所']/ResultForSumo/SumoOutcomeTotal/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="left">
					<nobr>
						<xsl:value-of select="Result[@Period='先場所']/ResultForSumo/SumoOutcomeTotal/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--初土俵-->
			<xsl:if test="//Standing/Player/PlayerForSumo/Debut/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="left">
					<nobr>
						<xsl:value-of select="PlayerForSumo/Debut/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--身長(cm)-->
			<xsl:if test="//Standing/Player/Height">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Height"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--体重(kg)-->
			<xsl:if test="//Standing/Player/Weight">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Weight"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--前回体重比-->
			<xsl:if test="//Standing/Player/PlayerForSumo/WeightDefference">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:choose>
							<xsl:when test="PlayerForSumo/WeightDefference = '０'">
								<xsl:value-of select="PlayerForSumo/WeightDefference" />
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="substring(PlayerForSumo/WeightDefference, 1, 1)" />
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="substring(PlayerForSumo/WeightDefference, 2)"/>
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
			<xsl:for-each select=".//Head/Meta/Title">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Meta/Title">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/RankAttribute/Writing">
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
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='旧位置']/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/RankShift/UpDown">
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
