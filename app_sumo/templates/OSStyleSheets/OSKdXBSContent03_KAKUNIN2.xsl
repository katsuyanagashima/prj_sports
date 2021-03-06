<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・新番付　　　DTD=KdCMNameListv1.0.dtd -->
	<!--  4.0版 2015.06.● プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->

	<!--=======================================================================================================-->
	<!--【プレーンテキスト版】スポーツデータタグテンプレート用文字数・行数変数-->
	<!--=======================================================================================================-->
    
    <!--文字数用数-->
  	<xsl:variable name="PRINT_MAXYOKOTEXT_OS04">
       <xsl:choose>
      <!--Ａ４タテ印刷andＢタイプの場合：文字サイズ9pt-->
        <xsl:when test="$PRINT_F_SET=1 and $OS03_TYPE_DISPLAY_SET = 1">
          <xsl:value-of select="$PRINT_MAXYOKOTEXT_FontSizeSmall_UTIL"/>
        </xsl:when>
        <!--Ａ４ヨコ印刷の場合：文字サイズ12pt-->
        <xsl:otherwise>
          <xsl:value-of select="$PRINT_MAXYOKOTEXT_DEFAULT_UTIL"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    	      
    <!--文字数用数-->
    <xsl:variable name="PRINT_MAXYOKOLINES_OS04">
      <xsl:choose>
      <!--Ａ４タテ印刷andＢタイプの場合：文字サイズ9pt-->
        <xsl:when test="$PRINT_F_SET=1 and $OS03_TYPE_DISPLAY_SET = 1">
          <xsl:value-of select="$PRINT_MAXYOKOLINES_FontSizeSmall_UTIL"/>
        </xsl:when>
        <!--Ａ４ヨコ印刷の場合：文字サイズ12pt-->
        <xsl:otherwise>
          <xsl:value-of select="$PRINT_MAXYOKOLINES_DEFAULT_UTIL"/>
        </xsl:otherwise>
      </xsl:choose>  
    </xsl:variable>
  
	<!--=======================================================================================================-->
	<!--【プレーンテキスト版】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN2">
    <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
      <!-- 本文要素 -->
      <xsl:with-param name="HONBUN_DATA">
        <xsl:call-template name="KAKUNIN2_TEXT"/>
      </xsl:with-param>
      <!--字解-->
      <xsl:with-param name="JIKAI_DATA">
        <xsl:call-template name="Gaiji_KAKUNIN2"/>
      </xsl:with-param>
      <xsl:with-param name="LINE_MAX_LENGTH" select="$PRINT_MAXYOKOTEXT_OS04"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$PRINT_MAXYOKOLINES_OS04"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="2"/>
    </xsl:call-template>
	</xsl:template>
	
	<!--=======================================================================================================-->
	<!-- レイアウト調整用変数 -->
	<!--=======================================================================================================-->
	
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

  <!-- 選手名表示切替 -->
  <xsl:variable name="OS03_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS03_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  
  <!-- 表示タイプ切替 -->
  <xsl:variable name="OS03_TYPE_DISPLAY_SET">
    <xsl:call-template name="OS03_TYPE_DISPLAY_SET"/>
  </xsl:variable>	

	<!-- 先場所成績の最大文字数 -->
	<xsl:variable name="SumoOutcomeTotalWritingMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
		</xsl:call-template>
	</xsl:variable>
	
	<!--=======================================================================================================-->
	<!--新番付テンプレート　本文要素　テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="KAKUNIN2_TEXT">
          <!--新番付資料編集-->
          <xsl:call-template name="sinbanduke_KAKUNIN2" />
      
					<!--本文内注釈編集-->
					<xsl:for-each select="Body/TextNote">
									<!-- 改行 -->
                  <xsl:value-of select="$LineFeed_UTL"/>
                  <!-- TextNote -->
									<xsl:value-of select="." />
					</xsl:for-each>

					<xsl:for-each select="TextNote">
									<!-- 改行 -->
                  <xsl:value-of select="$LineFeed_UTL"/>
                  <!-- TextNote -->				
									<xsl:value-of select="." />
					</xsl:for-each>

	</xsl:template>	

	<!--=======================================================================================================-->
	<!--新番付テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="sinbanduke_KAKUNIN2">

		<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
			
        <!--２回目以降のTableMidashiの前で改ページする-->
        <xsl:if test="position() &gt;= 2">
          <!-- 改ページ -->
          <xsl:value-of select="$PageBreak_UTL"/>	
        </xsl:if>			
			
				<!--テーブル見出し-->
				<xsl:call-template name="TableMidashi_sinbanduke_KAKUNIN2" />

				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="sinbanduke_KAKUNIN2" />
				
				<!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
        				
			</xsl:for-each>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--新番付テーブル見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="TableMidashi_sinbanduke_KAKUNIN2">
	
      <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>		
	
			<!--東西-->
				<xsl:text>　　　　　</xsl:text>
				<xsl:value-of select="Meta/Title" />
				
				<!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>

			<!--新位置-->
				<xsl:text>新位置</xsl:text>

			<!--新再-->
				<xsl:text>　</xsl:text>
				
			<!--力士名-->
				<xsl:text>力士名</xsl:text>
				
          <!--力士名の後を、空白で埋める-->
          <xsl:choose>
            <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
            <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">		 
              <!--力士名の後を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$PlayerNameFormalMaxLength - 3 "/> 
              </xsl:call-template>
            </xsl:when>
              <!--フルネームフラグがそれ以外の場合は、１字分空白で埋める-->
            <xsl:otherwise>  	
              <xsl:text>　</xsl:text>        
             </xsl:otherwise>
          </xsl:choose>

			<!--年齢-->
				<xsl:text>　</xsl:text>
				
			<!--部屋-->
				<xsl:text>　</xsl:text>
				<xsl:text>部　屋</xsl:text>			
			
          <!--部　屋の後を、空白で埋める-->
          <xsl:choose>
            <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
            <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">		 
              <!--部屋-の後を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$BelongFormalMaxLength - 3 "/> 
              </xsl:call-template>
            </xsl:when>
              <!--フルネームフラグがそれ以外の場合は、１字分空白で埋める-->
            <xsl:otherwise>  	
              <xsl:text></xsl:text>        
             </xsl:otherwise>
          </xsl:choose>			
				
			<!--出身地-->
			<!--Ｂタイプの場合に表示-->
			<xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">
				<xsl:text>　</xsl:text>
				<xsl:text>出身地</xsl:text>
				
          <!--出身地の後を、空白で埋める-->
          <xsl:choose>
            <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
            <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">		 
              <!--部屋-の後を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$NativeCountryAreaFormalMaxLength - 3 "/> 
              </xsl:call-template>
            </xsl:when>
              <!--フルネームフラグがそれ以外の場合は、１字分空白で埋める-->
            <xsl:otherwise>  	
              <xsl:text></xsl:text>        
             </xsl:otherwise>
          </xsl:choose>			
      </xsl:if>
      
			<!--旧位置-->
				<xsl:text>　</xsl:text>
				<xsl:text>旧位置</xsl:text>

			<!--昇降情報-->
			<!--Ｂタイプの場合に表示-->
			<xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">
				<xsl:text>　</xsl:text>
				<xsl:text>昇降</xsl:text>
      </xsl:if>
      
			<!--先場所成績-->
				<xsl:text>　</xsl:text>
				<xsl:text>先場所成績</xsl:text>
				
        <!--先場所成績の後を、空白で埋める-->
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$SumoOutcomeTotalWritingMaxLength - 5 "/> 
        </xsl:call-template>
              
			<!--初土俵-->
			<!--Ｂタイプの場合に表示-->
			<xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">
				<xsl:text>初土俵</xsl:text>
      </xsl:if>
      
			<!--身長(cm)-->
			<!--Ｂタイプの場合に表示-->
			<xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">			
				<xsl:text>　</xsl:text>
				<xsl:text>身長</xsl:text>
      </xsl:if>
      
			<!--体重(kg)-->
			<!--Ｂタイプの場合に表示-->
			<xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">						
				<xsl:text>　</xsl:text>
				<xsl:text>体重</xsl:text>
      </xsl:if>
      
			<!--前回体重比-->
			<!--Ｂタイプの場合に表示-->
			<xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">				
				<xsl:text>前比</xsl:text>
      </xsl:if>
      
	</xsl:template>

	<!--=======================================================================================================-->
	<!--新番付選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="sinbanduke_KAKUNIN2">
	
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>		
	
      <!--力士名（改め）-->
      <xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">

				<!--新位置・新再分（間隔をあけるため）-->
				<xsl:text>　　　　</xsl:text>

				<!--力士名（改め）-->
						<xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
						<xsl:text>改め</xsl:text>
						
				<!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
        						
      </xsl:if>
      
			<!--新位置-->
      <xsl:choose>
        <!--新位置の文字数が１つの力士-->      
        <xsl:when test="string-length(PlayerForSumo/SumoGrade[@Kind='新位置']/Writing) = 1">	    
              <xsl:text>　　</xsl:text>	
              <xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" /> 
          </xsl:when> 
          <!--新位置の文字数が２つの力士-->      
          <xsl:otherwise>
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" />		
          </xsl:otherwise>	
        </xsl:choose> 	

			<!--新再-->
      <xsl:choose>
        <!--新再がある場合-->
        <xsl:when test="PlayerForSumo/RankAttribute/Writing">		 
            <xsl:value-of select="PlayerForSumo/RankAttribute/Writing" />
        </xsl:when>
        <!--新再がない場合-->
        <xsl:otherwise>  	
            <xsl:text>　</xsl:text>        
        </xsl:otherwise>
      </xsl:choose>			

			<!--力士名-->
      <xsl:choose>
        <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
        <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">		 
            <xsl:value-of select="PlayerName/Formal[not(@*)]" />
            <!--力士名をフルネーム表示のあと、空白で埋める-->
						<xsl:call-template name="PrintSpaceZenkaku_UTL">
							<xsl:with-param name="count" select="$PlayerNameFormalMaxLength - string-length(PlayerName/Formal[not(@*)])"/>
						</xsl:call-template>            
		      </xsl:when>
          <!--フルネームフラグがそれ以外の場合は、力士名を４字表示-->
          <xsl:otherwise>  	
            <xsl:value-of select="PlayerName/Formal[@Display='4字']" />
          </xsl:otherwise>
        </xsl:choose>  			
			
			<!--年齢-->
					<xsl:call-template name="RensuuHenkan">
						<xsl:with-param name="Sts" select="3"/>
						<xsl:with-param name="Pdata" select="Age"/>
					</xsl:call-template>

			<!--部屋-->
        <xsl:text>　</xsl:text>
            
        <xsl:choose>
          <!--フルネームフラグが１の場合は、部屋名をフルネーム表示-->
          <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">		 
            <xsl:value-of select="Belong/Formal[not(@*)]" />
            <!--力士名をフルネーム表示のあと、空白で埋める-->
						<xsl:call-template name="PrintSpaceZenkaku_UTL">
							<xsl:with-param name="count" select="$BelongFormalMaxLength - string-length(Belong/Formal[not(@*)])"/>
						</xsl:call-template>            
		      </xsl:when>
          <!--フルネームフラグがそれ以外の場合は、部屋名を３字表示-->
          <xsl:otherwise>  			       
						<xsl:value-of select="Belong/Formal[@Display='3字']" />
          </xsl:otherwise>
        </xsl:choose>  	            
			
			<!--出身地-->
      <!--Ｂタイプの場合に表示-->
      <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">						

      <xsl:choose>
        <!--出身国の場合-->
        <xsl:when test="PlayerForSumo/NativeCountry/Formal[not(@*)]">
			  <xsl:text>　</xsl:text>
        <xsl:choose>
          <!--フルネームフラグが１の場合は、出身国をフルネーム表示-->
          <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">		 
            <xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />     
            <!--力士名をフルネーム表示のあと、空白で埋める-->
						<xsl:call-template name="PrintSpaceZenkaku_UTL">
							<xsl:with-param name="count" select="$NativeCountryAreaFormalMaxLength - string-length(PlayerForSumo/NativeCountry/Formal[not(@*)])"/>
						</xsl:call-template>            
		      </xsl:when>
          <!--フルネームフラグがそれ以外の場合は、部屋名を３字表示-->
          <xsl:otherwise>  				      
						<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[@Display='3字']" />
          </xsl:otherwise>
        </xsl:choose>  
        </xsl:when> 							
			
        <!--出身地の場合-->
        <xsl:when test="PlayerForSumo/NativeArea/Formal[not(@*)]">
			  <xsl:text>　</xsl:text>
        <xsl:choose>
          <!--フルネームフラグが１の場合は、部屋名をフルネーム表示-->
          <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">		 
            <xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />            
            <!--力士名をフルネーム表示のあと、空白で埋める-->
						<xsl:call-template name="PrintSpaceZenkaku_UTL">
							<xsl:with-param name="count" select="$NativeCountryAreaFormalMaxLength - string-length(PlayerForSumo/NativeArea/Formal[not(@*)])"/>
						</xsl:call-template>            
		      </xsl:when>
          <!--フルネームフラグがそれ以外の場合は、部屋名を３字表示-->
          <xsl:otherwise>  				      
						<xsl:value-of select="PlayerForSumo/NativeArea/Formal[@Display='3字']" />
          </xsl:otherwise>
        </xsl:choose>  							
        </xsl:when> 			
      </xsl:choose>  		
      </xsl:if>
        
			<!--旧位置-->
            <xsl:text>　</xsl:text>     
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='旧位置']/Writing" />

			<!--昇降-->
        <!--Ｂタイプの場合に表示-->
        <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">					
            <xsl:text>　</xsl:text>     
						<xsl:choose>
						  <!--ShiftCountが０の場合-->
							<xsl:when test="PlayerForSumo/RankShift/ShiftCount = '０'">
								<xsl:text>　―</xsl:text>
							</xsl:when>
							<!--それ以外の場合-->
							<xsl:otherwise>
								<xsl:value-of select="PlayerForSumo/RankShift/UpDown" />
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="PlayerForSumo/RankShift/ShiftCount"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
        </xsl:if>
        
			<!--先場所成績-->
			      <xsl:text>　</xsl:text>     
						<xsl:value-of select="Result[@Period='先場所']/ResultForSumo/SumoOutcomeTotal/Writing" />
        <!--先場所成績の後を、空白で埋める-->
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$SumoOutcomeTotalWritingMaxLength - string-length(Result[@Period='先場所']/ResultForSumo/SumoOutcomeTotal/Writing) "/> 
        </xsl:call-template>						
						
			<!--初土俵-->
        <!--Ｂタイプの場合に表示-->
        <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">					
						<xsl:value-of select="PlayerForSumo/Debut/Writing" />
        </xsl:if>
        
			<!--身長(cm)-->
        <!--Ｂタイプの場合に表示-->
        <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">					
			      <xsl:text>　</xsl:text>     
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Height"/>
						</xsl:call-template>
        </xsl:if>
        
			<!--体重(kg)-->
        <!--Ｂタイプの場合に表示-->
        <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">						
			      <xsl:text>　</xsl:text>
            <xsl:choose>
              <!--体重(kg)が３桁以上の力士-->      
              <xsl:when test="string-length(Weight) &gt;= 3">	    
                <xsl:call-template name="RensuuHenkan">
                  <xsl:with-param name="Sts" select="3"/>
                  <xsl:with-param name="Pdata" select="Weight"/>
                </xsl:call-template>
						  </xsl:when>
						   
              <!--体重(kg)が２桁以下の力士-->      
              <xsl:otherwise>
                <xsl:text>　</xsl:text>   	
                <xsl:call-template name="RensuuHenkan">
                  <xsl:with-param name="Sts" select="3"/>
                  <xsl:with-param name="Pdata" select="Weight"/>
                </xsl:call-template> 				
              </xsl:otherwise>	
            </xsl:choose> 			      
        </xsl:if>
        
			<!--前回体重比-->
        <!--Ｂタイプの場合に表示-->
        <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">						
						<xsl:choose>
              <!--前回体重比が０の場合は、空白を前に入れる-->
							<xsl:when test="PlayerForSumo/WeightDefference = '０'">
                <xsl:text>　</xsl:text>     
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
        </xsl:if>
        
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
			<xsl:for-each select=".//Head/Meta/Title">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//Meta/Title">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/RankAttribute/Writing">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			
      <!-- 力士名 -->
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">
          	<xsl:for-each select=".//PlayerName/Formal[not(@*)]">
              <xsl:call-template name="Gaiji_EDT"/>
            </xsl:for-each>           
		      </xsl:when>
          <!--フルネームフラグがそれ以外の場合は、力士名を４字表示-->
          <xsl:otherwise>  	
            <xsl:for-each select=".//PlayerName/Formal[@Display='4字']">
              <xsl:call-template name="Gaiji_EDT"/>
            </xsl:for-each>
          </xsl:otherwise>
        </xsl:choose> 				
			
      <xsl:choose>
          <!--フルネームフラグが１の場合は、部屋名をフルネーム表示-->
          <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">
          	<xsl:for-each select=".//Belong/Formal[not(@*)]">
              <xsl:call-template name="Gaiji_EDT"/>
            </xsl:for-each>           
		      </xsl:when>
          <!--フルネームフラグがそれ以外の場合は、部屋名を３字表示-->
          <xsl:otherwise>  	
            <xsl:for-each select=".//Belong/Formal[@Display='3字']">
              <xsl:call-template name="Gaiji_EDT"/>
            </xsl:for-each>
          </xsl:otherwise>
      </xsl:choose> 


      <!--Ｂタイプの場合に表示-->
      <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">				
      
      <xsl:choose>
          <!--フルネームフラグが１の場合は、出身国をフルネーム表示-->
          <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">
          	<xsl:for-each select=".//PlayerForSumo/NativeCountry/Formal[not(@*)]">
              <xsl:call-template name="Gaiji_EDT"/>
            </xsl:for-each>           
		      </xsl:when>
          <!--フルネームフラグがそれ以外の場合は、出身国を３字表示-->
          <xsl:otherwise>  	
            <xsl:for-each select=".//PlayerForSumo/NativeCountry/Formal[@Display='3字']">
              <xsl:call-template name="Gaiji_EDT"/>
            </xsl:for-each>
          </xsl:otherwise>
      </xsl:choose> 			
			
      <xsl:choose>
          <!--フルネームフラグが１の場合は、出身地をフルネーム表示-->
          <xsl:when test="$OS03_PLAYERNAME_DISPLAY_SET = 1">
          	<xsl:for-each select=".//PlayerForSumo/NativeArea/Formal[not(@*)]">
              <xsl:call-template name="Gaiji_EDT"/>
            </xsl:for-each>           
		      </xsl:when>
          <!--フルネームフラグがそれ以外の場合は、出身地を３字表示-->
          <xsl:otherwise>  	
            <xsl:for-each select=".//PlayerForSumo/NativeArea/Formal[@Display='3字']">
              <xsl:call-template name="Gaiji_EDT"/>
            </xsl:for-each>
          </xsl:otherwise>
      </xsl:choose>
      	
      </xsl:if>
      
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='旧位置']/Writing">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			
      <!--Ｂタイプの場合に表示-->
      <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">			
			<xsl:for-each select=".//PlayerForSumo/RankShift/UpDown">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
      </xsl:if>
			
      <!--Ｂタイプの場合に表示-->
      <xsl:if test="$OS03_TYPE_DISPLAY_SET = 1">		
			<xsl:for-each select=".//PlayerForSumo/Debut/Writing">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			</xsl:if>
			
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
