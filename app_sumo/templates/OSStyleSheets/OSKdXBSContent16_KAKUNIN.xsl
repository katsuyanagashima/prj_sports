<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・外国力士成績表 -->
  <!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--勝負編集-->
      <xsl:call-template name="syobu_KAKUNIN" />
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
	<!--勝負テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="syobu_KAKUNIN">
		<table xsl:use-attribute-sets="table_attribute_set">
			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--Title-->
				<tr>
					<td class="font_size_KAKUNIN" colspan="20">
						<xsl:for-each select="Meta/Title">
							<xsl:value-of select="." />
							<br/>
						</xsl:for-each>
					</td>
				</tr>

				<!--Article-->
				<xsl:if test="Article/Paragraph">
					<tr>
						<td class="font_size_KAKUNIN" colspan="20">
							<xsl:text>　</xsl:text>
							<xsl:value-of select="Article/Paragraph" />
						</td>
					</tr>
				</xsl:if>

				<!--Match-->
				<xsl:for-each select="Match">
						<xsl:call-template name="Player_syobu_KAKUNIN" />
				</xsl:for-each>
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--勝負選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="Player_syobu_KAKUNIN">
		<tr>
			<td class="font_size_KAKUNIN" valign="top">
				<!--MatchDetail配下の勝敗結果-->
				<xsl:if test="MatchDetail/MatchResult/Outcome/Writing">
					<xsl:value-of select="MatchDetail/MatchResult/Outcome/Writing" />
				</xsl:if>
				<!--選手配下の勝敗結果-->
				<xsl:if test="Player/Result/Outcome/Writing">
					<xsl:value-of select="Player/Result/Outcome/Writing" />
				</xsl:if>
			</td>

			<td class="font_size_KAKUNIN" valign="top">
				<xsl:for-each select="Player">
					<!--「―」-->
					<xsl:if test="position() != 1">
						<xsl:text>　―　</xsl:text>
					</xsl:if>

					<!--力士名-->
					<xsl:value-of select="PlayerName/Formal[not(@*)]" />

					<xsl:if test="position() = 2">
						<!--出身地・出身市町村-->
						<xsl:if test="
							PlayerForSumo/NativeCountry/Formal[not(@*)] or 
							PlayerForSumo/NativeArea/Formal[not(@*)] or 
							PlayerForSumo/NativeCity/Formal[not(@*)]">
							<xsl:text>（</xsl:text>
							<!--部屋-->
							<xsl:if test="Belong/Formal[not(@*)]">
								<xsl:value-of select="Belong/Formal[not(@*)]" />
							</xsl:if>
							<xsl:if test="Belong/Formal[not(@*)] and (PlayerForSumo/NativeCountry/Formal[not(@*)] or PlayerForSumo/NativeArea/Formal[not(@*)])">
								<xsl:text>・</xsl:text>
							</xsl:if>
							<!--出身地-->
							<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />
							<xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
							<xsl:text>）</xsl:text>
						</xsl:if>
					</xsl:if>

					<!--今場所成績-->
					<xsl:if test="Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing">
						<br/>
						<xsl:value-of select="Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing" />
					</xsl:if>
				</xsl:for-each>
			</td>
		</tr>

		<tr>
			<xsl:for-each select="Player[1]">
				<!--対戦の一人目の選手のみ以下の処理を行う。-->
				<td class="font_size_KAKUNIN" valign="top">
					<br/>
				</td>
				<td class="font_size_KAKUNIN" valign="bottom" colspan="20">
					<!--今場所成績-->
					<xsl:if test="Result/ResultForSumo/SumoOutcomeTotal/Writing">
						<xsl:value-of select="Result/ResultForSumo/SumoOutcomeTotal/Writing" />
						<xsl:text>　</xsl:text>
					</xsl:if>
					<!--地位-->
					<xsl:if test="PlayerForSumo/SumoGrade/Writing">
						<xsl:value-of select="PlayerForSumo/SumoGrade/Writing" />
					</xsl:if>
					<!--部屋-->
					<xsl:if test="Belong/Formal[not(@*)]">
						<xsl:text>　</xsl:text>
						<xsl:value-of select="Belong/Formal[not(@*)]" />
					</xsl:if>
				</td>
			</xsl:for-each>
		</tr>

		<tr>
			<xsl:for-each select="Player[1]">
				<!--対戦の一人目の選手のみ以下の処理を行う。-->
				<td class="font_size_KAKUNIN" valign="top">
					<br/>
				</td>
				<td class="font_size_KAKUNIN" valign="bottom" colspan="20">
					<!--出身地・出身市町村-->
					<xsl:if test="
						PlayerForSumo/NativeCountry/Formal[not(@*)] or 
						PlayerForSumo/NativeArea/Formal[not(@*)] or 
						PlayerForSumo/NativeCity/Formal[not(@*)]">
						<!--出身地-->
						<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />
						<xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
						<!--出身市町村-->
						<xsl:if test="
							(PlayerForSumo/NativeCountry/Formal[not(@*)] or 
							 PlayerForSumo/NativeArea/Formal[not(@*)]) and 
							PlayerForSumo/NativeCity/Formal[not(@*)]">
							<xsl:text>・</xsl:text>
						</xsl:if>
						<xsl:value-of select="PlayerForSumo/NativeCity/Formal[not(@*)]" />
					</xsl:if>
				</td>
			</xsl:for-each>
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
			<xsl:for-each select=".//Article/Paragraph">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//MatchDetail/MatchResult/Outcome/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Result/Outcome/Writing">
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
			<xsl:for-each select=".//Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Result/ResultForSumo/SumoOutcomeTotal/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade/Writing">
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
			<xsl:for-each select=".//PlayerForSumo/NativeCity/Formal[not(@*)]">
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
