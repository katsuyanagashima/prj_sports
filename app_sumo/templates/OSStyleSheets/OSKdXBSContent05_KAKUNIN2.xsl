<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕下以下新番付 -->
	<!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
  
	<!--=======================================================================================================-->
	<!--【プレーンテキスト版】スポーツデータタグテンプレート -->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN2">
    <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
      <!-- 本文要素 -->
      <xsl:with-param name="HONBUN_DATA">
        <xsl:call-template name="honbun"/>
      </xsl:with-param>
      <!--字解-->
      <xsl:with-param name="JIKAI_DATA">
        <xsl:call-template name="Gaiji_KAKUNIN2"/>
      </xsl:with-param>
        <xsl:with-param name="LINE_MAX_LENGTH" select="$PRINT_MAXYOKOTEXT_DEFAULT_UTIL"/>
        <xsl:with-param name="PAGE_LINE_MAX" select="$PRINT_MAXYOKOLINES_DEFAULT_UTIL"/>
        <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
        <xsl:with-param name="TATEYOKO_FLG" select="2"/>
      </xsl:call-template>
  </xsl:template>
	
	<!--=======================================================================================================-->
	<!-- レイアウト調整用変数 -->
	<!--=======================================================================================================-->

  <!-- 表示タイプ切替 -->
  <xsl:variable name="OS05_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS05_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>	

	<!-- 力士名フルネームの最大文字数 -->
	<xsl:variable name="PlayerNameFormalMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/PlayerName/Formal[not(@*)]"/>
		</xsl:call-template>
	</xsl:variable>		
	
	<!-- 部屋名フルネームの最大文字数 -->
	<xsl:variable name="BelongFormalMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/Belong/Formal[not(@*)]"/>
		</xsl:call-template>
	</xsl:variable>
	
	<!-- 国の最大文字数 -->
	<xsl:variable name="NativeCountryFormalMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/PlayerForSumo/NativeCountry/Formal[not(@*)]"/>
		</xsl:call-template>
	</xsl:variable>	
	
	<!-- 出身地の最大文字数 -->
	<xsl:variable name="NativeAreaFormalMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/PlayerForSumo/NativeArea/Formal[not(@*)]"/>
		</xsl:call-template>
	</xsl:variable>
	
	<!-- 国と出身地で最大文字数 -->
	<xsl:variable name="NativeCountryAreaFormalMaxLength">
    <xsl:choose>
      <!--国の文字数＞＝出身地の文字数の場合-->
      <xsl:when test="$NativeCountryFormalMaxLength &gt;= $NativeAreaFormalMaxLength">	
        <xsl:value-of select="$NativeCountryFormalMaxLength" />
      </xsl:when>
      <!--国の文字数＜出身地の文字数の場合-->
      <xsl:otherwise>  	
        <xsl:value-of select="$NativeAreaFormalMaxLength" />
      </xsl:otherwise>
    </xsl:choose>		
	</xsl:variable>
	
	<!-- 先場所成績の最大文字数 -->
	<xsl:variable name="DebutWritingMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/PlayerForSumo/Debut/Writing"/>
		</xsl:call-template>
	</xsl:variable>
	
	<!--=======================================================================================================-->
	<!--幕下以下新番付表テンプレート　本文要素　テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="honbun">
      <!--幕下以下新番付編集-->
      <xsl:call-template name="makusitaikasinbanduke_KAKUNIN2" />
      <!--本文内注釈編集-->
      <xsl:for-each select="Body/TextNote">
              <xsl:value-of select="." />
              <!-- 改行 -->
              <xsl:value-of select="$LineFeed_UTL"/>		
      </xsl:for-each>
      <xsl:for-each select="TextNote">
              <xsl:value-of select="." />
              <!-- 改行 -->
              <xsl:value-of select="$LineFeed_UTL"/>	
      </xsl:for-each>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下新番付テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="makusitaikasinbanduke_KAKUNIN2">
			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--テーブル見出し-->
				<xsl:call-template name="TableMidashi_makusitaikasinbanduke_KAKUNIN2" />
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="makusitaikasinbanduke_KAKUNIN2" />
			</xsl:for-each>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下新番付テーブル見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="TableMidashi_makusitaikasinbanduke_KAKUNIN2">
	
				<xsl:for-each select="Meta/Title">
					<xsl:value-of select="." />
				</xsl:for-each>	
      
	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下新番付選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="makusitaikasinbanduke_KAKUNIN2">
			<!--新位置-->
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" />

			<!--力士名-->
            <xsl:text>　</xsl:text>
            <xsl:choose>
              <!--OS05_PLAYERNAME_DISPLAY_SETフラグが１の場合-->
              <xsl:when test="$OS05_PLAYERNAME_DISPLAY_SET = 1">	
                <xsl:value-of select="PlayerName/Formal[not(@*)]" />
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="$PlayerNameFormalMaxLength - string-length(PlayerName/Formal[not(@*)]) "/> 
                </xsl:call-template>
              </xsl:when>
              <!--OS05_PLAYERNAME_DISPLAY_SETフラグが０の場合-->
              <xsl:otherwise>  	
                <xsl:value-of select="PlayerName/Formal[@Display='3字']" />
						  </xsl:otherwise>
            </xsl:choose>
            
			<!--部屋-->
            <xsl:text>　</xsl:text>
            <xsl:choose>
              <!--OS05_PLAYERNAME_DISPLAY_SETフラグが１の場合-->
              <xsl:when test="$OS05_PLAYERNAME_DISPLAY_SET = 1">	
                <xsl:value-of select="Belong/Formal[not(@*)]" />
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="$BelongFormalMaxLength - string-length(Belong/Formal[not(@*)]) "/> 
                </xsl:call-template>
              </xsl:when>
              <!--OS05_PLAYERNAME_DISPLAY_SETフラグが０の場合-->
              <xsl:otherwise>  	
                <xsl:value-of select="Belong/Formal[@Display='2字']" />
						  </xsl:otherwise>
            </xsl:choose>
            

			<!--出身地-->
            <xsl:text>　</xsl:text>
            
            <xsl:choose>
              <!--OS05_PLAYERNAME_DISPLAY_SETフラグが１の場合-->
              <xsl:when test="$OS05_PLAYERNAME_DISPLAY_SET = 1">
                <xsl:choose>
                  <!--国の場合-->
                  <xsl:when test="PlayerForSumo/NativeCountry/Formal[not(@*)]">	              
                    <xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />
                    <xsl:call-template name="PrintSpaceZenkaku_UTL">
                      <xsl:with-param name="count" select="$NativeCountryAreaFormalMaxLength - string-length(PlayerForSumo/NativeCountry/Formal[not(@*)]) "/> 
                    </xsl:call-template>
                  </xsl:when>
                  <!--出身地の場合-->
                  <xsl:otherwise>
                    <xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
                    <xsl:call-template name="PrintSpaceZenkaku_UTL">
                      <xsl:with-param name="count" select="$NativeCountryAreaFormalMaxLength - string-length(PlayerForSumo/NativeArea/Formal[not(@*)]) "/> 
                    </xsl:call-template>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:when>
              <!--OS05_PLAYERNAME_DISPLAY_SETフラグが０の場合-->
              <xsl:otherwise>  	
                <xsl:value-of select="PlayerForSumo/NativeCountry/Formal[@Display='2字']" />
                <xsl:value-of select="PlayerForSumo/NativeArea/Formal[@Display='2字']" />
						  </xsl:otherwise>
            </xsl:choose>            

			<!--初土俵-->
            <xsl:text>　</xsl:text>
            <!--東西-->      
            <xsl:choose>
              <!--初土俵時期が５文字以上の場合-->
              <xsl:when test="$DebutWritingMaxLength &gt;= 5">	
                <xsl:value-of select="PlayerForSumo/Debut/Writing" />
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="$DebutWritingMaxLength - string-length(PlayerForSumo/Debut/Writing) "/> 
                </xsl:call-template>
              </xsl:when>
              <!--初土俵時期が５文字未満の場合-->
              <xsl:otherwise>  	
                <xsl:value-of select="PlayerForSumo/Debut/Writing" />
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="5 - string-length(PlayerForSumo/Debut/Writing) "/> 
                </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>	 

			<!--昇降-->
						<xsl:choose>
							<xsl:when test="PlayerForSumo/RankShift/Writing = '―'">
								<xsl:text>　</xsl:text>
								<xsl:value-of select="PlayerForSumo/RankShift/Writing" />
							</xsl:when>
							<xsl:otherwise>
								<xsl:value-of select="PlayerForSumo/RankShift/Writing" />
							</xsl:otherwise>
						</xsl:choose>
			
			<!--改め-->
            <xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
            
              <xsl:choose>
                <!--OS05_PLAYERNAME_DISPLAY_SETフラグが１の場合-->
                <xsl:when test="$OS05_PLAYERNAME_DISPLAY_SET = 1">	
                  <xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
                </xsl:when>
                <!--OS05_PLAYERNAME_DISPLAY_SETフラグが０の場合-->
                <xsl:otherwise>  	
                  <xsl:value-of select="PlayerForSumo/PreviousName/Formal[@Display='3字']" />
                </xsl:otherwise>
              </xsl:choose>            

							<xsl:text>改</xsl:text>
            </xsl:if>			
			
			  <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>			
			
	</xsl:template>

	<!--=======================================================================================================-->
	<!--Gaijiテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="Gaiji_KAKUNIN2">

		<!-- 字解編集 -->
		<xsl:variable name="JIKAI_DATA">
			<xsl:for-each select=".//Body/TextNote">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//Meta/Title">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//Belong/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeCountry/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeArea/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/Debut/Writing">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/RankShift/UpDown">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
		</xsl:variable>
		
    <xsl:if test="($JIKAI_DATA!='')">
      <!--字解見出し-->
      <xsl:text>字解情報</xsl:text>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <!--字解-->
      <xsl:value-of select="$JIKAI_DATA"/>
    </xsl:if>

	</xsl:template>
</xsl:stylesheet>
