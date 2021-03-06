<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・新番付資料（補正）　DTD=KdCMNameListv1.0.dtd -->
	<!--  4.0版 2015.06.● プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
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
      <xsl:with-param name="LINE_MAX_LENGTH" select="$PRINT_MAXYOKOTEXT_FontSizeSmall_UTIL"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$PRINT_MAXYOKOLINES_FontSizeSmall_UTIL"/>
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
  <xsl:variable name="OS02_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS02_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>	

	<!-- 休場数の最大文字数 -->
	<xsl:variable name="AbsenceCountMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount"/>
		</xsl:call-template>
	</xsl:variable>	

	<!--=======================================================================================================-->
	<!--新番付資料（補正）テンプレート　本文要素　テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="KAKUNIN2_TEXT">

          <!--新番付資料編集-->
          <xsl:call-template name="sinbandukesiryou_KAKUNIN2" />
      
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
	<!--新番付資料（補正）テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="sinbandukesiryou_KAKUNIN2">

		<!--Title-->
					<xsl:value-of select="./Head/Meta/Title" />

		<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
	
        <!--２回目以降のTableMidashiの前で改ページする-->
        <xsl:if test="position() &gt;= 2">
          <!-- 改ページ -->
          <xsl:value-of select="$PageBreak_UTL"/>	
        </xsl:if>
      
				<!--テーブル見出し-->
				<xsl:call-template name="TableMidashi_sinbandukesiryou_KAKUNIN2" />
				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="sinbandukesiryou_KAKUNIN2" /> 
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
			</xsl:for-each>
  </xsl:template>
	

	<!--=======================================================================================================-->
	<!--新番付資料テーブル見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="TableMidashi_sinbandukesiryou_KAKUNIN2">
	
	  <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>	

	  <!-- ########## テーブル見出し１行目 ########## -->
			<!--新位置-->
          <xsl:text>　</xsl:text>	
          <xsl:text>　</xsl:text>  
          
			<!--力士名-->
          <xsl:choose>
            <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
            <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
              <!--力士名の前を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="format-number(($PlayerNameFormalMaxLength div 2),'#') -1 "/> 
              </xsl:call-template>
              <xsl:text>力</xsl:text>
              <!--力士名の後を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$PlayerNameFormalMaxLength - format-number(($PlayerNameFormalMaxLength div 2),'#')"/> 
              </xsl:call-template>
            </xsl:when>
              <!--フルネームフラグがそれ以外の場合は、力士名を４字表示-->
            <xsl:otherwise>  	
              <xsl:text>　</xsl:text>        
              <xsl:text>力</xsl:text>
              <xsl:text>　　</xsl:text>    
             </xsl:otherwise>
          </xsl:choose>
          	
 			<!--年齢-->   
          <xsl:text>年</xsl:text>	

			<!--部屋-->
        <xsl:text>　</xsl:text> 
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
            <!--部屋名の前を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="format-number(($BelongFormalMaxLength div 2),'#') -1 "/> 
            </xsl:call-template>
            <xsl:text>部</xsl:text>
            <!--部屋名の後を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$BelongFormalMaxLength - format-number(($BelongFormalMaxLength div 2),'#')"/> 
            </xsl:call-template>
          </xsl:when>
            <!--フルネームフラグがそれ以外の場合は、部屋名を４字表示-->
          <xsl:otherwise>  			
            <xsl:text>　</xsl:text>        
            <xsl:text>部</xsl:text>
            <xsl:text>　</xsl:text> 					 
          </xsl:otherwise>
        </xsl:choose>  	

			<!--出身地-->
        <xsl:text>　</xsl:text> 
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
            <!--出身地の前を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="format-number(($NativeCountryAreaFormalMaxLength div 2),'#') -1 "/> 
            </xsl:call-template>
            <xsl:text>出</xsl:text>
            <!--出身地の後を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$NativeCountryAreaFormalMaxLength - format-number(($NativeCountryAreaFormalMaxLength div 2),'#') "/> 
            </xsl:call-template>
          </xsl:when>
            <!--フルネームフラグがそれ以外の場合は、部屋名を４字表示-->
          <xsl:otherwise>  			
            <xsl:text>　</xsl:text>   
            <xsl:text>出</xsl:text>
            <xsl:text>　</xsl:text>   				 
          </xsl:otherwise>
        </xsl:choose> 
			    
			<!--最高位-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>最</xsl:text>  
			    <xsl:text>　</xsl:text>

			<!--場所数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>場</xsl:text>  

      <!--勝ち数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>勝</xsl:text>  

			<!--負け数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>負</xsl:text>  

			<!--分け数-->
      <xsl:choose>
        <xsl:when test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/DrawCount != '０'">
          <xsl:text>分</xsl:text>
        </xsl:when>
        <xsl:otherwise>  	
          <xsl:text>　</xsl:text>        
        </xsl:otherwise>
      </xsl:choose> 

			<!--休場数-->
      <xsl:choose>
        <!--休場数の最大文字数が２桁以下の場合-->
        <xsl:when test="$AbsenceCountMaxLength &lt;= 2">			
		      <xsl:text>休</xsl:text>
		    </xsl:when>
        <!--休場数の最大文字数が３桁以上の場合-->
        <xsl:otherwise>  	
          <xsl:text>　</xsl:text>        
		      <xsl:text>休</xsl:text>
        </xsl:otherwise>
      </xsl:choose> 

			<!--勝率-->
          <xsl:text>　</xsl:text>        
          <xsl:text>勝</xsl:text>	

			<!--休を負とした勝率-->
          <xsl:text>　</xsl:text>        
          <xsl:text>休と勝</xsl:text>	
			
			<!--優勝-->
          <xsl:text>　</xsl:text>        
          <xsl:text>優</xsl:text>	
			
			<!--殊勲賞-->
          <xsl:text>　</xsl:text>        
          <xsl:text>殊</xsl:text>		

			<!--敢闘賞-->
          <xsl:text>　</xsl:text>        
          <xsl:text>敢</xsl:text>	

			<!--技能賞-->
          <xsl:text>　</xsl:text>        
          <xsl:text>技</xsl:text>		

			<!--与金星--> 
          <xsl:text>与</xsl:text>	
			
			<!--奪金星-->
          <xsl:text>奪</xsl:text>		

			<!--身長-->
          <xsl:text>　</xsl:text>   
          <xsl:text>身</xsl:text>	

			<!--体重-->
        <xsl:text>　</xsl:text>   
        <xsl:text>体</xsl:text>	

			<!--前回体重比-->
        <xsl:text>前</xsl:text>   
        <xsl:text>重</xsl:text>	

      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>		

    <!-- ########## テーブル見出し２行目 ########## -->
			<!--新位置-->
          <xsl:text>　</xsl:text>	
					<xsl:value-of select="Meta/Title" />

			<!--力士名-->
          <xsl:choose>
            <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
            <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
              <!--力士名の前を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="format-number(($PlayerNameFormalMaxLength div 2),'#') -1 "/> 
              </xsl:call-template>
              <xsl:text>士</xsl:text>
              <!--力士名の後を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$PlayerNameFormalMaxLength - format-number(($PlayerNameFormalMaxLength div 2),'#')"/> 
              </xsl:call-template>
            </xsl:when>
              <!--フルネームフラグがそれ以外の場合は、力士名を４字表示-->
            <xsl:otherwise>  	
              <xsl:text>　</xsl:text>        
              <xsl:text>士</xsl:text>
              <xsl:text>　　</xsl:text>    
             </xsl:otherwise>
          </xsl:choose>
          	
 			<!--年齢-->   
          <xsl:text>　</xsl:text>	

			<!--部屋-->
        <xsl:text>　</xsl:text> 
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
            <!--部屋名の前を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="format-number(($BelongFormalMaxLength div 2),'#') -1 "/> 
            </xsl:call-template>
            <xsl:text>　</xsl:text>
            <!--力士名の後を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$BelongFormalMaxLength - format-number(($BelongFormalMaxLength div 2),'#')"/> 
            </xsl:call-template>
          </xsl:when>
            <!--フルネームフラグがそれ以外の場合は、部屋名を４字表示-->
          <xsl:otherwise>  			
            <xsl:text>　</xsl:text>        
            <xsl:text>　</xsl:text>
            <xsl:text>　</xsl:text> 					 
          </xsl:otherwise>
        </xsl:choose>  	

			<!--出身地-->
        <xsl:text>　</xsl:text> 
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
            <!--部屋名の前を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="format-number(($NativeCountryAreaFormalMaxLength div 2),'#') -1 "/> 
            </xsl:call-template>
            <xsl:text>身</xsl:text>
            <!--力士名の後を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$NativeCountryAreaFormalMaxLength - format-number(($NativeCountryAreaFormalMaxLength div 2),'#') "/> 
            </xsl:call-template>
          </xsl:when>
            <!--フルネームフラグがそれ以外の場合は、部屋名を４字表示-->
          <xsl:otherwise>  			
            <xsl:text>　</xsl:text>   
            <xsl:text>身</xsl:text>
            <xsl:text>　</xsl:text>   				 
          </xsl:otherwise>
        </xsl:choose> 
			    
			<!--最高位-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>高</xsl:text>  
			    <xsl:text>　</xsl:text>

			<!--場所数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>所</xsl:text>
			    
      <!--勝ち数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>ち</xsl:text>
			    
			<!--負け数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>け</xsl:text> 

			<!--分け数-->
      <xsl:choose>
        <xsl:when test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/DrawCount != '０'">
          <xsl:text>け</xsl:text>
        </xsl:when>
        <xsl:otherwise>  	
          <xsl:text>　</xsl:text>        
        </xsl:otherwise>
      </xsl:choose> 

			<!--休場数-->
      <xsl:choose>
        <!--休場数の最大文字数が２桁以下の場合-->
        <xsl:when test="$AbsenceCountMaxLength &lt;= 2">			
		      <xsl:text>場</xsl:text>
		    </xsl:when>
        <!--休場数の最大文字数が３桁以上の場合-->
        <xsl:otherwise>  	
          <xsl:text>　</xsl:text>        
		      <xsl:text>場</xsl:text>
        </xsl:otherwise>
      </xsl:choose> 

			<!--勝率-->
        <xsl:text>　</xsl:text>        
        <xsl:text>　</xsl:text>	

			<!--休を負とした勝率-->
        <xsl:text>　</xsl:text>        
        <xsl:text>をし率</xsl:text>	
			
			<!--優勝-->
        <xsl:text>　</xsl:text>        
        <xsl:text>　</xsl:text>	
			
			<!--殊勲賞-->
        <xsl:text>　</xsl:text>        
        <xsl:text>勲</xsl:text>	

			<!--敢闘賞-->
        <xsl:text>　</xsl:text>        
        <xsl:text>闘</xsl:text>		

			<!--技能賞-->
        <xsl:text>　</xsl:text>        
        <xsl:text>能</xsl:text>	

			<!--与金星-->
        <xsl:text>金</xsl:text>	
			
			<!--奪金星-->
        <xsl:text>金</xsl:text>	

			<!--身長-->
        <xsl:text>　</xsl:text>   
        <xsl:text>　</xsl:text>	

			<!--体重-->
        <xsl:text>　</xsl:text>   
        <xsl:text>　</xsl:text>	

			<!--前回体重比-->
        <xsl:text>回</xsl:text>   
        <xsl:text>比</xsl:text>	

      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>		
    
    <!-- ########## テーブル見出し３行目 ########## -->  
			<!--新位置-->
          <xsl:text>　</xsl:text>	
          <xsl:text>　</xsl:text>	

			<!--力士名-->
          <xsl:choose>
            <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
            <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
              <!--力士名の前を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="format-number(($PlayerNameFormalMaxLength div 2),'#') -1 "/> 
              </xsl:call-template>
              <xsl:text>名</xsl:text>
              <!--力士名の後を、空白で埋める-->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$PlayerNameFormalMaxLength - format-number(($PlayerNameFormalMaxLength div 2),'#')"/> 
              </xsl:call-template>
            </xsl:when>
              <!--フルネームフラグがそれ以外の場合は、力士名を４字表示-->
            <xsl:otherwise>  	
              <xsl:text>　</xsl:text>        
              <xsl:text>名</xsl:text>
              <xsl:text>　　</xsl:text>    
             </xsl:otherwise>
          </xsl:choose>
          	
 			<!--年齢-->   
          <xsl:text>齢</xsl:text>	

			<!--部屋-->
        <xsl:text>　</xsl:text> 
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
            <!--部屋名の前を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="format-number(($BelongFormalMaxLength div 2),'#') -1 "/> 
            </xsl:call-template>
            <xsl:text>屋</xsl:text>
            <!--力士名の後を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$BelongFormalMaxLength - format-number(($BelongFormalMaxLength div 2),'#')"/> 
            </xsl:call-template>
          </xsl:when>
            <!--フルネームフラグがそれ以外の場合は、部屋名を４字表示-->
          <xsl:otherwise>  			
            <xsl:text>　</xsl:text>        
            <xsl:text>屋</xsl:text>
            <xsl:text>　</xsl:text> 					 
          </xsl:otherwise>
        </xsl:choose>  	

			<!--出身地-->
        <xsl:text>　</xsl:text> 
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
            <!--部屋名の前を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="format-number(($NativeCountryAreaFormalMaxLength div 2),'#') -1 "/> 
            </xsl:call-template>
            <xsl:text>地</xsl:text>
            <!--力士名の後を、空白で埋める-->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$NativeCountryAreaFormalMaxLength - format-number(($NativeCountryAreaFormalMaxLength div 2),'#') "/> 
            </xsl:call-template>
          </xsl:when>
            <!--フルネームフラグがそれ以外の場合は、部屋名を４字表示-->
          <xsl:otherwise>  			
            <xsl:text>　</xsl:text>   
            <xsl:text>地</xsl:text>
            <xsl:text>　</xsl:text>   				 
          </xsl:otherwise>
        </xsl:choose> 
			    
			<!--最高位-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>位</xsl:text>  
			    <xsl:text>　</xsl:text>

			<!--場所数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>数</xsl:text> 

      <!--勝ち数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>数</xsl:text>

			<!--負け数-->
			    <xsl:text>　</xsl:text>			
			    <xsl:text>数</xsl:text>
			    
			<!--分け数-->
      <xsl:choose>
        <xsl:when test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/DrawCount != '０'">
          <xsl:text>数</xsl:text>
        </xsl:when>
        <xsl:otherwise>  	
          <xsl:text>　</xsl:text>        
        </xsl:otherwise>
      </xsl:choose> 

			<!--休場数-->
      <xsl:choose>
        <!--休場数の最大文字数が２桁以下の場合-->
        <xsl:when test="$AbsenceCountMaxLength &lt;= 2">			
		      <xsl:text>数</xsl:text>
		    </xsl:when>
        <!--休場数の最大文字数が３桁以上の場合-->
        <xsl:otherwise>  	
          <xsl:text>　</xsl:text>        
		      <xsl:text>数</xsl:text>
        </xsl:otherwise>
      </xsl:choose> 

			<!--勝率-->
        <xsl:text>　</xsl:text>        
        <xsl:text>率</xsl:text>	
        
			<!--休を負とした勝率-->
        <xsl:text>　</xsl:text>        
        <xsl:text>負た　</xsl:text>	
			
			<!--優勝-->
        <xsl:text>　</xsl:text>        
        <xsl:text>勝</xsl:text>	
			
			<!--殊勲賞-->
        <xsl:text>　</xsl:text>        
        <xsl:text>賞</xsl:text>	

			<!--敢闘賞-->
        <xsl:text>　</xsl:text>        
        <xsl:text>賞</xsl:text>	

			<!--技能賞-->
        <xsl:text>　</xsl:text>        
        <xsl:text>賞</xsl:text>	
        
			<!--与金星-->
        <xsl:text>星</xsl:text>	
			
			<!--奪金星-->
        <xsl:text>星</xsl:text>	

			<!--身長-->
        <xsl:text>　</xsl:text>   
        <xsl:text>長</xsl:text>	

			<!--体重-->
        <xsl:text>　</xsl:text>   
        <xsl:text>重</xsl:text>	

			<!--前回体重比-->
        <xsl:text>体</xsl:text>   
        <xsl:text>　</xsl:text>	

	</xsl:template>

	<!--=======================================================================================================-->
	<!--新番付資料選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="sinbandukesiryou_KAKUNIN2">
	
	    <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>

	    <!--力士名（改め）-->
      <xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
        <xsl:text>　　</xsl:text>	
				<xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
				<xsl:text>改め</xsl:text>
				<!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>	
      </xsl:if>
         
			<!--新位置-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">			
        <xsl:choose>
          <!--新位置の文字数が１つの力士-->      
          <xsl:when test="string-length(PlayerForSumo/SumoGrade[@Kind='新位置']/Writing) = 1">	    
              <xsl:text>　</xsl:text>	
              <xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" /> 
          </xsl:when> 
          <!--新位置の文字数が２つの力士-->      
          <xsl:otherwise>
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" />		
          </xsl:otherwise>	
        </xsl:choose> 	
			</xsl:if>

      <!--力士名-->
      <xsl:if test="//Standing/Player/PlayerName/Formal[not(@*)]">
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
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
      </xsl:if>

      <!--年齢-->
			<xsl:if test="//Standing/Player/Age">
					<xsl:call-template name="RensuuHenkan">
						<xsl:with-param name="Sts" select="3"/>
						<xsl:with-param name="Pdata" select="Age"/>
					</xsl:call-template>
			</xsl:if>
			
			<!--部屋-->
			<xsl:if test="//Standing/Player/Belong/Formal[not(@*)]">
			  <xsl:text>　</xsl:text>
        <xsl:choose>
          <!--フルネームフラグが１の場合は、部屋名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
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
			</xsl:if>
			
			<!--出身国・出身地-->
      <xsl:choose>
        <!--出身国の場合-->
        <xsl:when test="PlayerForSumo/NativeCountry/Formal[not(@*)]">
			  <xsl:text>　</xsl:text>
        <xsl:choose>
          <!--フルネームフラグが１の場合は、出身国をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
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
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">		 
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


			<!--最高位-->
			<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='最高位']/Writing">
						<xsl:text>　</xsl:text>   
						<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='最高位']/Writing" />
			</xsl:if>
			
			<!--場所数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/BashoCount">
            <!--場所数が２桁以下の場合は、空白を入れる-->
            <xsl:if test="string-length(Result/ResultForSumo/SumoOutcomeTotal/BashoCount) &lt;=  2">
              <xsl:text>　</xsl:text>   
            </xsl:if>
            
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/BashoCount"/>
						</xsl:call-template>
			</xsl:if>
			
			<!--勝ち数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/WinCount">
            <!--勝ち数が２桁以下の場合は、空白を入れる-->
            <xsl:if test="string-length(Result/ResultForSumo/SumoOutcomeTotal/WinCount) &lt;=  2">
              <xsl:text>　</xsl:text>   
            </xsl:if>

						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/WinCount"/>
						</xsl:call-template>
			</xsl:if>
			
			<!--負け数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/LossCount">
            <!--負け数が２桁以下の場合は、空白を入れる-->
            <xsl:if test="string-length(Result/ResultForSumo/SumoOutcomeTotal/LossCount) &lt;=  2">
              <xsl:text>　</xsl:text>   
            </xsl:if>
            
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/LossCount"/>
						</xsl:call-template>
			</xsl:if>
			
			<!--分け数-->
      <xsl:choose>
        <!--分け数が０でない力士がいる場合-->
        <xsl:when test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/DrawCount != '０'">
          <xsl:choose>
            <!--分け数が０でない力士は、連数字処理を行う-->
            <xsl:when test="Result/ResultForSumo/SumoOutcomeTotal/DrawCount != '０'">
              <xsl:call-template name="RensuuHenkan">
                <xsl:with-param name="Sts" select="7"/>
                <xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/DrawCount"/>
              </xsl:call-template>
            </xsl:when>
            <!--分け数が０の力士は、空白を入れる-->
            <xsl:otherwise>
              <xsl:text>　</xsl:text>   				
            </xsl:otherwise>
          </xsl:choose>          
        </xsl:when>
        
        <!--力士全員の分け数が０の場合は、空白を入れる-->
        <xsl:otherwise>
           <xsl:text>　</xsl:text>   				
        </xsl:otherwise>          
      </xsl:choose>
			
			<!--休場数-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount">
        <xsl:choose>
        
          <!--休場数の最大文字数が２桁以下の場合-->
          <xsl:when test="$AbsenceCountMaxLength &lt;= 2">			
            <xsl:choose>			
              <!--休場数が２桁以下の力士-->
              <xsl:when test="Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount">			
                <xsl:call-template name="RensuuHenkan">
                  <xsl:with-param name="Sts" select="3"/>
                  <xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount"/>
                </xsl:call-template>
              </xsl:when>
              <!--休場数がない力士は、空白を入れる-->
              <xsl:otherwise>
                <xsl:text>　</xsl:text>   				
              </xsl:otherwise>	
            </xsl:choose>  
		      </xsl:when>        

          <!--それ以外（休場数の最大文字数が３桁以上）の場合-->     
          <xsl:otherwise>	              
            <xsl:choose>
              <!--休場数が３桁以上の力士-->      
              <xsl:when test="string-length(Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount) &gt;= 3">	    
                <xsl:call-template name="RensuuHenkan">
                  <xsl:with-param name="Sts" select="3"/>
                  <xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount"/>
                </xsl:call-template>
              </xsl:when> 
              <!--休場数が２桁以下の力士-->      
              <xsl:when test="string-length(Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount) &lt;= 2">
                <xsl:text>　</xsl:text>   	
                <xsl:call-template name="RensuuHenkan">
                  <xsl:with-param name="Sts" select="3"/>
                  <xsl:with-param name="Pdata" select="Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount"/>
                </xsl:call-template>
              </xsl:when> 
              <!--休場数がない力士は、空白を入れる-->
              <xsl:otherwise>
                <xsl:text>　　</xsl:text>   				
              </xsl:otherwise>	
            </xsl:choose>  
          </xsl:otherwise>
        </xsl:choose>  
			</xsl:if>
			
			<!--勝率-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/WinningPercentage[not(@*)]">
						<xsl:text>　</xsl:text>
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="1"/>
							<xsl:with-param name="Pdata" select="Result/ResultForSumo/WinningPercentage[not(@*)]"/>
						</xsl:call-template>
			</xsl:if>
			
			<!--休を負とした勝率-->
			<xsl:if test="//Standing/Player/Result/ResultForSumo/WinningPercentage[@Kind='休みを負とした']">
        <xsl:choose>			
          <!--休を負とした勝率がある力士の場合-->
          <xsl:when  test="Result/ResultForSumo/WinningPercentage[@Kind='休みを負とした']">
							<xsl:text>（</xsl:text>
							<xsl:call-template name="RensuuHenkan">
								<xsl:with-param name="Sts" select="1"/>
								<xsl:with-param name="Pdata" select="Result/ResultForSumo/WinningPercentage[@Kind='休みを負とした']"/>
							</xsl:call-template>
							<xsl:text>）</xsl:text>
					</xsl:when>
					
          <!--休を負とした勝率がない力士の場合、空白を入れる-->
          <xsl:otherwise>
            <xsl:text>　　　　</xsl:text>   				
          </xsl:otherwise>	
        </xsl:choose>  
			</xsl:if>
			
			<!--優勝-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='優勝']/Count/CountValue">
						<xsl:choose>
					    <!--優勝が０の力士の場合、―を入れる-->						
							<xsl:when test="Result/Award[@Kind='優勝']/Count/CountValue = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							
					    <!--優勝が０でない力士の場合-->			
							<xsl:otherwise>
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="Result/Award[@Kind='優勝']/Count/CountValue"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
			</xsl:if>
			
			<!--殊勲賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='殊勲賞']/Count/CountValue">
					<xsl:text>　</xsl:text>
						<xsl:choose>
					    <!--殊勲賞が０の力士の場合、―を入れる-->								
							<xsl:when test="Result/Award[@Kind='殊勲賞']/Count/CountValue = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							
					    <!--殊勲賞が０でない力士の場合-->		
							<xsl:otherwise>
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="Result/Award[@Kind='殊勲賞']/Count/CountValue"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
			</xsl:if>
			
			<!--敢闘賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='敢闘賞']/Count/CountValue">
          <xsl:text>　</xsl:text>
						<xsl:choose>
					    <!---敢闘賞が０の力士の場合、―を入れる-->								
							<xsl:when test="Result/Award[@Kind='敢闘賞']/Count/CountValue = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							
					    <!--敢闘賞が０でない力士の場合-->		
							<xsl:otherwise>
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="Result/Award[@Kind='敢闘賞']/Count/CountValue"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
			</xsl:if>
			
			<!--技能賞-->
			<xsl:if test="//Standing/Player/Result/Award[@Kind='技能賞']/Count/CountValue">
          <xsl:text>　</xsl:text>
						<xsl:choose>
							<!---技能賞が０の力士の場合、―を入れる-->	
							<xsl:when test="Result/Award[@Kind='技能賞']/Count/CountValue = '０'">
								<xsl:text>―</xsl:text>
							</xsl:when>
							
					    <!--技能賞が０でない力士の場合-->		
							<xsl:otherwise>
								<xsl:call-template name="RensuuHenkan">
									<xsl:with-param name="Sts" select="3"/>
									<xsl:with-param name="Pdata" select="Result/Award[@Kind='技能賞']/Count/CountValue"/>
								</xsl:call-template>
							</xsl:otherwise>
						</xsl:choose>
			</xsl:if>
			
			<!--与金星-->
			<xsl:if test="//Standing/Player/Result/Record[@Kind='与金星']/IntegerPart">
        <xsl:choose>
          <!--与金星がある力士の場合-->
					<xsl:when test="Result/Record[@Kind='与金星']/IntegerPart != '０'">
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="6"/>
							<xsl:with-param name="Pdata" select="Result/Record[@Kind='与金星']/IntegerPart"/>
						</xsl:call-template>
					</xsl:when>

					<!--与金星がない力士の場合、空白を入れる-->
          <xsl:otherwise>
            <xsl:text>　</xsl:text>   				
          </xsl:otherwise>	
				</xsl:choose>
			</xsl:if>
			
			<!--奪金星-->
			<xsl:if test="//Standing/Player/Result/Record[@Kind='奪金星']/IntegerPart">
			  <xsl:choose>
          <!--奪金星がある力士の場合-->
					<xsl:when test="Result/Record[@Kind='奪金星']/IntegerPart != '０'">
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="7"/>
							<xsl:with-param name="Pdata" select="Result/Record[@Kind='奪金星']/IntegerPart"/>
						</xsl:call-template>
					</xsl:when>

					<!--奪金星がない力士の場合、空白を入れる-->
          <xsl:otherwise>
            <xsl:text>　</xsl:text>   				
          </xsl:otherwise>	
				</xsl:choose>
			</xsl:if>
			
			<!--身長-->
			<xsl:if test="//Standing/Player/Height">
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Height"/>
						</xsl:call-template>
			</xsl:if>

			<!--体重-->
			<xsl:if test="//Standing/Player/Weight">
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Weight"/>
						</xsl:call-template>
			</xsl:if>

			<!--前回体重比-->
			<xsl:if test="//Standing/Player/PlayerForSumo/WeightDefference">
						<xsl:choose>
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
			<xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>
			
      <!-- 力士名 -->
        <xsl:choose>
          <!--フルネームフラグが１の場合は、力士名をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">
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
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">
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
			
      <xsl:choose>
          <!--フルネームフラグが１の場合は、出身国をフルネーム表示-->
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">
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
          <xsl:when test="$OS02_PLAYERNAME_DISPLAY_SET = 1">
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

			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='最高位']/Writing">
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
