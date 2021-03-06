<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">

<!-- 3.0版　2014.2.26 html関連タグの小文字化 -->

	<!--=======================================================================================================-->
	<!--テーブル属性-->
	<!--=======================================================================================================-->
	<xsl:attribute-set name="table_attribute_set">
		<xsl:attribute name="border">0</xsl:attribute>
		<xsl:attribute name="cellspacing">0</xsl:attribute>
		<xsl:attribute name="cellpadding">0</xsl:attribute>
	</xsl:attribute-set>

	<!--=======================================================================================================-->
	<!--文字列から指定された文字数ごとにBRタグを加えるテンプレート-->
	<!--=======================================================================================================-->

	<xsl:template name="AddBR_KAKUNIN_OSCOM">

		<!--処理対象文字列-->
		<xsl:param name="Data" />
		<!--改行文字数-->		
		<xsl:param name="Length" />
		<!--チームポジション（左チーム括弧付：１、右チーム括弧付：２、左チーム括弧無し：３、右チーム括弧無し：４）-->
		<xsl:param name="EditPattern" />
		
		<!--文字列の先頭からの指定文字数を変数Tipとする。-->
		<xsl:variable name="Tip">
			<xsl:choose>
				<xsl:when test="($EditPattern = 2) and (string-length($Data) mod $Length = 1)">

					<!--(右側への編集で)最終行が'）'のみの場合は、はみ出し処理を行う。
						予備エリアに'（'を編集するため、文字列の先頭からの指定文字数+1を変数Tipとする。-->
					<xsl:value-of select="substring($Data,1,$Length + 1)" />
				</xsl:when>
				<xsl:when test="($EditPattern = 1) and (string-length($Data) = $Length+1)">

					<!--(左側への編集で)最終行が'）'のみの場合は、はみ出し処理を行う。
						予備エリアに'）'を編集するため、文字列の先頭からの指定文字数+1を変数Tipとする。-->
					<xsl:value-of select="substring($Data,1,$Length + 1)" />
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="substring($Data,1,$Length)" />
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>

		<!--文字列の指定文字数目以降を変数Afterとする。-->
		<xsl:variable name="After" select="substring-after($Data,$Tip)" />

		<xsl:choose>
			<!--変数Afterが空の場合（次行の編集がない場合）-->
			<xsl:when test="string-length($After) = 0">
				<!--(右側への編集で)はみ出し処理でない場合は、予備スペースを追加-->
				<xsl:if test="(($EditPattern = 2) or ($EditPattern = 4)) and (string-length($Tip) &lt;= $Length)">
					<!--  予備スペース  -->
					<xsl:text>　</xsl:text>
				</xsl:if>
				<!--先頭からの指定文字数分を表示する-->
				<xsl:value-of select="$Tip" />
			</xsl:when>
			<xsl:otherwise>
				<!--(右側への編集で)はみ出し処理でない場合は、予備スペースを追加-->
				<xsl:if test="(($EditPattern = 2) or ($EditPattern = 4)) and (string-length($Tip) &lt;= $Length)">
					<!--  予備スペース  -->
					<xsl:text>　</xsl:text>
				</xsl:if>
				<!--先頭からの指定文字数分を表示する-->
				<xsl:value-of select="$Tip" />
				<br />

				<!--AddBR_KAKUNINテンプレートを再起呼び出し-->
				<xsl:call-template name="AddBR_KAKUNIN_OSCOM">
					<!--文字列の２文字目以降をセットする。-->
					<xsl:with-param name="Data" select="$After" />
					<xsl:with-param name="Length" select="$Length" />
					<xsl:with-param name="EditPattern" select="$EditPattern" />
				</xsl:call-template>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--確認用ページ　字解表示の共通処理用テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="Gaiji_com_KAKUNIN_OSCOM">
		<xsl:for-each select='KdGaiji'>
			<xsl:text>&lt;table xsl:use-attribute-sets='table_attribute_set' width='650'&gt;</xsl:text>
			<xsl:text>&lt;td width='25%' class="font_size_KAKUNIN" valign='top'&gt;</xsl:text>
			<xsl:value-of select='parent::*' />
			<xsl:text>&lt;/td&gt;</xsl:text>
			<xsl:text>&lt;td width='75%' class="font_size_KAKUNIN" valign='top'&gt;</xsl:text>
			<xsl:text>☆</xsl:text>
			<xsl:value-of select="@KdJikai" />
			<xsl:text>&lt;/td&gt;</xsl:text>
			<xsl:text>&lt;/table&gt;</xsl:text>
		</xsl:for-each>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--確認用ページ　文字列変換共通処理用テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="replace_KAKUNIN_OSCOM">
		<xsl:param name="str"/>
		<xsl:param name="match"/>
		<xsl:param name="replace"/>
		<xsl:choose>
			<xsl:when test="contains($str,$match)">
				<xsl:value-of select="substring-before($str,$match)"/>
				<xsl:value-of select="$replace"/>
				<xsl:call-template name="replace_KAKUNIN_OSCOM">
					<xsl:with-param name="str" select="substring-after($str,$match)"/>
					<xsl:with-param name="match" select="$match"/>
					<xsl:with-param name="replace" select="$replace"/>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$str"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--確認用ページ　連続数字連数字変換処理用テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="RensuuHenkan_KAKUNIN_OSCOM">
		<xsl:param name="str"/>
		<xsl:choose>
			<xsl:when test="
				contains($str,'０') or
				contains($str,'１') or
				contains($str,'２') or
				contains($str,'３') or
				contains($str,'４') or
				contains($str,'５') or
				contains($str,'６') or
				contains($str,'７') or
				contains($str,'８') or
				contains($str,'９')
			">
				<xsl:choose>
					<xsl:when test="
						starts-with($str, '０') or
						starts-with($str, '１') or
						starts-with($str, '２') or
						starts-with($str, '３') or
						starts-with($str, '４') or
						starts-with($str, '５') or
						starts-with($str, '６') or
						starts-with($str, '７') or
						starts-with($str, '８') or
						starts-with($str, '９')
					">
						<xsl:choose>
							<xsl:when test="
								substring($str,2,1) = '０' or
								substring($str,2,1) = '１' or
								substring($str,2,1) = '２' or
								substring($str,2,1) = '３' or
								substring($str,2,1) = '４' or
								substring($str,2,1) = '５' or
								substring($str,2,1) = '６' or
								substring($str,2,1) = '７' or
								substring($str,2,1) = '８' or
								substring($str,2,1) = '９'
							">
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="substring($str,1,2)"/>
								</xsl:call-template>
								<xsl:call-template name="RensuuHenkan_KAKUNIN_OSCOM">
									<xsl:with-param name="str" select="substring($str,3)"/>
								</xsl:call-template>
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="substring($str,1,1)"/>
								<xsl:call-template name="RensuuHenkan_KAKUNIN_OSCOM">
									<xsl:with-param name="str" select="substring($str,2)"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="substring($str,1,1)"/>
						<xsl:call-template name="RensuuHenkan_KAKUNIN_OSCOM">
							<xsl:with-param name="str" select="substring($str,2)"/>
						</xsl:call-template>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$str"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

</xsl:stylesheet>
