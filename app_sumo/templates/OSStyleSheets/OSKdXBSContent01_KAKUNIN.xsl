<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・新番付資料 -->
	<!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--新番付資料編集-->
      <xsl:call-template name="sinbandukesiryou_KAKUNIN" />
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
	<!--新番付資料テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="sinbandukesiryou_KAKUNIN">
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
				<xsl:call-template name="TableMidashi_sinbandukesiryou_KAKUNIN" />

				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="sinbandukesiryou_KAKUNIN" />
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--新番付資料テーブル見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="TableMidashi_sinbandukesiryou_KAKUNIN">
		<tr>
			<!--新位置-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
				<td class="font_size_KAKUNIN" valign="center" align="right">
					<xsl:value-of select="Meta/Title" />
				</td>
			</xsl:if>
			<!--力士名-->
			<xsl:if test="//Standing/Player/PlayerName/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="center">力<br/>士<br/>名</td>
			</xsl:if>
			<!--年齢-->
			<xsl:if test="//Standing/Player/Age">
				<td class="font_size_KAKUNIN" valign="top" align="center">年<br/>齢<br/></td>
			</xsl:if>
			<!--部屋-->
			<xsl:if test="//Standing/Player/Belong/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="center">部<br/>屋<br/></td>
			</xsl:if>
			<!--出身地-->
			<xsl:if test="
				//Standing/Player/PlayerForSumo/NativeCountry/Formal[not(@*)] or 
				//Standing/Player/PlayerForSumo/NativeArea/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="center">出<br/>身<br/>地</td>
			</xsl:if>
			<!--最高位-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='最高位']/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="left">最<br/>高<br/>位</td>
			</xsl:if>
			<!--場所数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/BashoCount">
				<td class="font_size_KAKUNIN" valign="top" align="right">場<br/>所<br/>数<table xsl:use-attribute-sets="table_attribute_set" width="32"><td/></table></td>
			</xsl:if>
			<!--勝ち数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/WinCount">
				<td class="font_size_KAKUNIN" valign="top" align="right">勝<br/>ち<br/>数<table xsl:use-attribute-sets="table_attribute_set" width="32"><td/></table></td>
			</xsl:if>
			<!--負け数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/LossCount">
				<td class="font_size_KAKUNIN" valign="top" align="right">負<br/>け<br/>数<table xsl:use-attribute-sets="table_attribute_set" width="32"><td/></table></td>
			</xsl:if>
			<!--分け数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/DrawCount != '０'">
				<td class="font_size_KAKUNIN" valign="top" align="right">分<br/>け<br/>数</td>
			</xsl:if>
			<!--休場数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount">
				<td class="font_size_KAKUNIN" valign="top" align="right">休<br/>場<br/>数<table xsl:use-attribute-sets="table_attribute_set" width="32"><td/></table></td>
			</xsl:if>
			<!--勝率-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/WinningPercentage[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="center">勝<br/>率<br/></td>
			</xsl:if>
			<!--休を負とした勝率-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/WinningPercentage[@Kind='休みを負とした']">
				<td class="font_size_KAKUNIN" valign="top" align="left">休と勝<br/>をし率<br/>負た</td>
			</xsl:if>
			<!--優勝-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='優勝']/Count/CountValue">
				<td class="font_size_KAKUNIN" valign="top" align="center">優<br/>勝<br/></td>
			</xsl:if>
			<!--殊勲賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='殊勲賞']/Count/CountValue">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="center">殊<br/>勲<br/>賞</td>
			</xsl:if>
			<!--敢闘賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='敢闘賞']/Count/CountValue">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="center">敢<br/>闘<br/>賞</td>
			</xsl:if>
			<!--技能賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='技能賞']/Count/CountValue">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="center">技<br/>能<br/>賞</td>
			</xsl:if>
			<!--与金星-->
			<xsl:if test="//Standing/Player/Result/Record[@Kind='与金星']/IntegerPart">
				<td class="font_size_KAKUNIN" valign="top" align="center">与<br/>金<br/>星</td>
			</xsl:if>
			<!--奪金星-->
			<xsl:if test="//Standing/Player/Result/Record[@Kind='奪金星']/IntegerPart">
				<td class="font_size_KAKUNIN" valign="top" align="center">奪<br/>金<br/>星</td>
			</xsl:if>
			<!--身長-->
			<xsl:if test="//Standing/Player/Height">
				<td class="font_size_KAKUNIN" valign="top" align="center">身<br/>長<br/></td>
			</xsl:if>
			<!--体重-->
			<xsl:if test="//Standing/Player/Weight">
				<td class="font_size_KAKUNIN" valign="top" align="center">体<br/>重<br/></td>
			</xsl:if>
			<!--前回体重比-->
			<xsl:if test="//Standing/Player/PlayerForSumo/WeightDefference">
				<td class="font_size_KAKUNIN" valign="top" align="left">前重<br/>回比<br/>体</td>
			</xsl:if>
		</tr>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--新番付資料選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="sinbandukesiryou_KAKUNIN">
		<!--力士名（改め）-->
		<xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
			<tr>
				<!--新位置（間隔をあけるため）-->
				<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
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
			<!--最高位-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='最高位']/Writing">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top">
					<nobr>
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='最高位']/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--場所数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/BashoCount">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/BashoCount"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--勝ち数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/WinCount">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/WinCount"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--負け数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/LossCount">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/LossCount"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--分け数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/DrawCount != '０'">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="7"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/DrawCount"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--休場数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--勝率-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/WinningPercentage[not(@*)]">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:text>　</xsl:text>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="1"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/WinningPercentage[not(@*)]"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--休を負とした勝率-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/WinningPercentage[@Kind='休みを負とした']">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<xsl:if test="Result/ResultForSumo/WinningPercentage[@Kind='休みを負とした']">
						<nobr>
							<xsl:text>（</xsl:text>
							<xsl:call-template name="RensuuHenkan">
								<xsl:with-param name="Sts" select="1"/>
								<xsl:with-param name="Pdata" select="Result/ResultForSumo/WinningPercentage[@Kind='休みを負とした']"/>
							</xsl:call-template>
							<xsl:text>）</xsl:text>
						</nobr>
					</xsl:if>
					<br/>
				</td>
			</xsl:if>
			<!--優勝-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='優勝']/Count/CountValue">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:choose>
							<xsl:when test="Result/Award[@Kind='優勝']/Count/CountValue = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="Result/Award[@Kind='優勝']/Count/CountValue"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--殊勲賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='殊勲賞']/Count/CountValue">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:choose>
							<xsl:when test="Result/Award[@Kind='殊勲賞']/Count/CountValue = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="Result/Award[@Kind='殊勲賞']/Count/CountValue"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--敢闘賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='敢闘賞']/Count/CountValue">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:choose>
							<xsl:when test="Result/Award[@Kind='敢闘賞']/Count/CountValue = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="Result/Award[@Kind='敢闘賞']/Count/CountValue"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--技能賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='技能賞']/Count/CountValue">
				<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:choose>
							<xsl:when test="Result/Award[@Kind='技能賞']/Count/CountValue = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							<xsl:otherwise>
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="Result/Award[@Kind='技能賞']/Count/CountValue"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--与金星-->
			<xsl:if test="//Standing/Player/Result/Record[@Kind='与金星']/IntegerPart">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="6"/>
							<xsl:with-param name="Pdata" select="Result/Record[@Kind='与金星']/IntegerPart"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--奪金星-->
			<xsl:if test="//Standing/Player/Result/Record[@Kind='奪金星']/IntegerPart">
				<td class="font_size_KAKUNIN" valign="top" align="right">
					<nobr>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="7"/>
							<xsl:with-param name="Pdata" select="Result/Record[@Kind='奪金星']/IntegerPart"/>
						</xsl:call-template>
					</nobr>
					<br/>
				</td>
			</xsl:if>
			<!--身長-->
			<xsl:if test="//Standing/Player/Height">
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
			<!--体重-->
			<xsl:if test="//Standing/Player/Weight">
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
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='最高位']/Writing">
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
