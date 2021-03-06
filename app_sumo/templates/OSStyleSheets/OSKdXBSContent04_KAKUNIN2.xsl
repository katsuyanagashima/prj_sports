<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・郷土力士新番付 -->
	<!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
  
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS04_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS04_SET"/>
  </xsl:variable>
  <!-- 力士名・出身地・部屋　表示切替表示切替 -->
  <xsl:variable name="OS04_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS04_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- １行の折り返し個別設定の有効・無効 -->
  <!-- <xsl:variable name="PRINT_MAXTEXT_FLG_OS04_SET"> -->
    <!-- <xsl:call-template name="PRINT_MAXTEXT_FLG_OS04_SET"/> -->
  <!-- </xsl:variable> -->
  <!-- １行の折り返し文字数 -->
  <!-- <xsl:variable name="PRINT_MAXTEXT_OS04_SET"> -->
    <!-- <xsl:call-template name="PRINT_MAXTEXT_OS04_SET"/> -->
  <!-- </xsl:variable> -->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS04_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS04_SET = 0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS04_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS04_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS04_PTEXT_TATEYOKO=1">
            <xsl:value-of select="$PRINT_MAXLINES_TATE_TATE_SET"/>
          </xsl:when>
          <!-- 横書き -->
          <xsl:otherwise>
            <xsl:value-of select="$PRINT_MAXLINES_TATE_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS04_PTEXT_TATEYOKO=1">
            <xsl:value-of select="$PRINT_MAXLINES_YOKO_TATE_SET"/>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXLINES_YOKO_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １行最大折り返し文字数を取得 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS04_MAXLENGTH">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS04_PTEXT_TATEYOKO=1">
            <xsl:choose>
              <!-- 個別設定が有効なら個別設定を使用 -->
              <!-- <xsl:when test="$PRINT_MAXTEXT_FLG_OS04_SET = 1"> -->     
                <!-- <xsl:value-of select="$PRINT_MAXTEXT_OS04_SET"/> -->
              <!-- 力士名４字、出身地３字、部屋３字の場合は、１５文字固定 -->
              <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 0">                  
                <xsl:value-of select="15"/>
              </xsl:when>
              <xsl:otherwise>
                <!-- その他は共通設定を使用 -->
                <!-- $PRINT_MAXTEXT_FLG_OS04_SETに関わらず、縦書きの場合は固定２３文字にした -->            
                <!-- <xsl:value-of select="$PRINT_MAXTEXT_TATE_TATE_SET"/> -->
                <!-- 力士名、出身地、部屋がフルネームの場合は、２３文字固定 -->
                <xsl:value-of select="23"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <!-- 横書き -->
          <xsl:otherwise>
            <xsl:value-of select="$PRINT_MAXTEXT_TATE_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:choose>
          <xsl:when test="$OS04_PTEXT_TATEYOKO=1">
            <!-- 縦書き -->
            <xsl:choose>
              <!-- 個別設定が有効なら個別設定を使用 -->
              <!-- <xsl:when test="$PRINT_MAXTEXT_FLG_OS04_SET = 1"> -->
                <!-- $PRINT_MAXTEXT_FLG_OS04_SETに関わらず、縦書きの場合は固定２３文字にした -->              
                <!-- <xsl:value-of select="$PRINT_MAXTEXT_OS04_SET"/> --> 
              <!-- 力士名４字、出身地３字、部屋３字の場合は、１５文字固定 -->
              <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 0">                  
                <xsl:value-of select="15"/>
              </xsl:when>
              <!-- その他は共通設定を使用 -->
              <xsl:otherwise>
                <!-- $PRINT_MAXTEXT_FLG_OS04_SETに関わらず、縦書きの場合は固定２３文字にした -->        
                <!-- <xsl:value-of select="$PRINT_MAXTEXT_YOKO_TATE_SET"/> -->
                <!-- 力士名、出身地、部屋がフルネームの場合は、２３文字固定 -->                
                <xsl:value-of select="23"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXTEXT_YOKO_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  
  <!--=======================================================================================================-->
	<!-- レイアウト調整用変数 -->
	<!--=======================================================================================================-->
	<!-- 力士名フルネームの最大文字数 -->
	<xsl:variable name="PlayerNameFormalMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/PlayerName/Formal[not(@*)]"/>
		</xsl:call-template>
	</xsl:variable>	
	
	<!-- 出身地の最大文字数 -->
	<xsl:variable name="NativeCityFormalMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/PlayerForSumo/NativeCity/Formal[not(@*)]"/>
		</xsl:call-template>
	</xsl:variable>
  
  <!-- 部屋名の最大文字数 -->
	<xsl:variable name="BelongFormalMaxLength">
		<xsl:call-template name="GetTagsMaxLength_UTL">
			<xsl:with-param name="TargetPath" select="//Standing/Player/Belong/Formal[not(@*)]"/>
		</xsl:call-template>
	</xsl:variable>
  
  
  <!-- ================================================================================= -->
  <!-- 確認テンプレート（起点） -->
  <!-- ================================================================================= -->
  <xsl:template match="SportsData" mode="KAKUNIN2">

  <xsl:choose>
  <!-- 力士名４字、出身地３字、部屋３字の場合 -->
  <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 0"> 
    <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
      <!-- 本文要素 -->
      <xsl:with-param name="HONBUN_DATA">
        <xsl:call-template name="honbun"/>
      </xsl:with-param>
      <!-- 字解 -->
      <xsl:with-param name="JIKAI_DATA">
        <xsl:call-template name="Gaiji_KAKUNIN2"/>
      </xsl:with-param>
      <xsl:with-param name="LINE_MAX_LENGTH" select="$OS04_MAXLENGTH"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$OS04_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$OS04_PTEXT_TATEYOKO"/>
    </xsl:call-template>
  </xsl:when>
  
  <!-- 力士名、出身地、部屋がフルネームの場合 -->    
  <xsl:otherwise> 
    <xsl:call-template name="KAKUNIN2_DIVS_TATELONG_LAYOUT_UTL">
      <!-- 本文要素 -->
      <xsl:with-param name="HONBUN_DATA">
        <xsl:call-template name="honbun"/>
      </xsl:with-param>
      <!-- 字解 -->
      <xsl:with-param name="JIKAI_DATA">
        <xsl:call-template name="Gaiji_KAKUNIN2"/>
      </xsl:with-param>
      <xsl:with-param name="LINE_MAX_LENGTH" select="$OS04_MAXLENGTH"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$OS04_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$OS04_PTEXT_TATEYOKO"/>
    </xsl:call-template>
  </xsl:otherwise>
  </xsl:choose>  
  
  </xsl:template> 
  
              
	<!--=======================================================================================================-->
	<!--【プレーンテキスト版】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
  <xsl:template name="honbun">
      <!--郷土力士新番付編集-->
      <xsl:call-template name="kyoudorikisisinbanduke_KAKUNIN2" />
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
	<!--郷土力士新番付テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="kyoudorikisisinbanduke_KAKUNIN2">

			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--Titleタグ-->
				<xsl:for-each select="Meta/Title">
							<xsl:value-of select="." />
							<!-- 改行 -->
              <xsl:value-of select="$LineFeed_UTL"/>
				</xsl:for-each>

				<!--Paragraphタグ-->
				<xsl:for-each select="Article/Paragraph">
							<xsl:text>　</xsl:text>
							<xsl:value-of select="." />
							<!-- 改行 -->
              <xsl:value-of select="$LineFeed_UTL"/>
				</xsl:for-each>

				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="kyoudorikisisinbanduke_KAKUNIN2" />
			</xsl:for-each>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--郷土力士新番付選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="kyoudorikisisinbanduke_KAKUNIN2">
				<!--力士名-->
					<xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
							<xsl:text>▽</xsl:text>
                <xsl:choose>
                  <!-- OS04_PLAYERNAME_DISPLAY_SET=1の場合は、力士名は正式名、出身地・国は正式名、部屋は正式名 -->
                  <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 1">
                    <xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
                  </xsl:when>
                  <xsl:otherwise>							
                    <xsl:value-of select="PlayerForSumo/PreviousName/Formal[@Display='4字']" />
                  </xsl:otherwise>
                </xsl:choose>
							<xsl:text>改め</xsl:text>
							<!-- 改行 -->
              <xsl:value-of select="$LineFeed_UTL"/>
					</xsl:if>
					
          <xsl:choose>
            <!-- OS04_PLAYERNAME_DISPLAY_SET=1の場合は、力士名は正式名、出身地・国は正式名、部屋は正式名 -->
              <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 1">
                <xsl:value-of select="PlayerName/Formal[not(@*)]" />
                <!--力士名の後を、空白で埋める-->
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="$PlayerNameFormalMaxLength - string-length(PlayerName/Formal[not(@*)])"/> 
                </xsl:call-template>
                <xsl:text>　</xsl:text>
              </xsl:when>
              <xsl:otherwise>							
                <xsl:value-of select="PlayerName/Formal[@Display='4字']" />
              </xsl:otherwise>
          </xsl:choose>	
						
				<!--新位置-->
					<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" />

				<!--出身地（都市）-->
					<xsl:text>（</xsl:text>
					<xsl:choose>
            <!-- OS04_PLAYERNAME_DISPLAY_SET=1の場合は、力士名は正式名、出身地・国は正式名、部屋は正式名 -->
              <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 1">
                <xsl:value-of select="PlayerForSumo/NativeCity/Formal[not(@*)]" />
                <xsl:text>）</xsl:text>
                <!--力士名の後を、空白で埋める-->
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="$NativeCityFormalMaxLength - string-length(PlayerForSumo/NativeCity/Formal[not(@*)])"/> 
                </xsl:call-template>
              </xsl:when>
              <xsl:otherwise>							
                <xsl:value-of select="PlayerForSumo/NativeCity/Formal[@Display='3字']" />
                <xsl:text>）</xsl:text>
              </xsl:otherwise>
          </xsl:choose>						

				<!--部屋-->
					<xsl:choose>
            <!-- OS04_PLAYERNAME_DISPLAY_SET=1の場合は、力士名は正式名、出身地・国は正式名、部屋は正式名 -->
              <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 1">
                <xsl:value-of select="Belong/Formal[not(@*)]" />
                <!--力士名の後を、空白で埋める-->
                <xsl:call-template name="PrintSpaceZenkaku_UTL">
                  <xsl:with-param name="count" select="$BelongFormalMaxLength - string-length(Belong/Formal[not(@*)])"/> 
                </xsl:call-template>
              </xsl:when>
              <xsl:otherwise>							
                <xsl:value-of select="Belong/Formal[@Display='3字']" />
              </xsl:otherwise>
          </xsl:choose>					
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
			<xsl:for-each select=".//Body/Meta/Title">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>	
			<xsl:for-each select=".//Article/Paragraph">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>	
			
      <!--改め名-->
      <xsl:choose>
        <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise>							
          <xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[@Display='4字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:otherwise>
      </xsl:choose>		
      
      <!--力士名-->
      <xsl:choose>
        <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select=".//PlayerName/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise>							
          <xsl:for-each select=".//PlayerName/Formal[@Display='4字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:otherwise>
      </xsl:choose>		
		
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='新位置']/Writing">
				<xsl:call-template name="Gaiji_EDT"/>
			</xsl:for-each>

      <!--出身地-->
      <xsl:choose>
        <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select=".//PlayerForSumo/NativeCity/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise>							
          <xsl:for-each select=".//PlayerForSumo/NativeCity/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:otherwise>
      </xsl:choose>		

      <!--部屋-->
      <xsl:choose>
        <xsl:when test="$OS04_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select=".//Belong/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise>							
          <xsl:for-each select=".//Belong/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:otherwise>
      </xsl:choose>


		</xsl:variable>

    <!--字解が存在した場合-->
    <xsl:if test="($JIKAI_DATA!='')">
      <!--字解見出し-->
      <xsl:text>字解情報</xsl:text>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!--字解-->
      <xsl:value-of select="$JIKAI_DATA"/>
    </xsl:if>

	</xsl:template>
</xsl:stylesheet>
