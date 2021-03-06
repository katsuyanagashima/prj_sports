<?xml version="1.0" encoding="UTF-16"?>
<!--<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" version="1.0" encoding="UTF-16" indent="yes"/>
-->
<!-- 2002.08.30  大分類InBClass、中分類①InBClass1、中分類②InBClass2、小分類InSClass -->
<!-- 2002.08.30  画像電説情報部追加            　　　　　　　　　　　　　　　　　　　 -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl" xml:lang="ja">

	<xsl:template match="/">
		<html lang="ja">
			<head>
				<title>内容情報部</title>
               <style type="text/css">
                   .color1  {color:brown;} 
                   .color2  {color:purple;font-weight:bold}
                   .color3  {color:green;font-size:12pt} 
                   .bgcolor1  {background-color:silver;font-weight:bold;color:black;font-size:10pt}
                   .bgcolor2 {background-color:white}
               </style>
			</head>
			<body>
                   <div style="font-weight:bold;font-size:20pt;color:#483B8D">内容情報部リスト</div>
                   <xsl:for-each select="NewsML/NewsItem/NewsComponent/ContentItem/DataContent/InContent/InMetadata">
                   <table bgcolor="#000000" cellpadding="0" cellspacing="0">
                         <tr><td>
                   <table border="0" cellpadding="4" cellspacing="1"  width="800">
                    <tr class="bgcolor2"><td class="color1" >項目名</td><td class="color1">内容</td></tr>
				<xsl:apply-templates select="InAdminInfo"/>
				<xsl:apply-templates select="InCategoryInfo/InNewsCategory"/>
				<xsl:apply-templates select="InCategoryInfo/InNewsLine"/>
				<xsl:apply-templates select="InCategoryInfo/InClasses"/>
				<xsl:apply-templates select="InCategoryInfo/InAreaInfo"/>
				<xsl:apply-templates select="InCategoryInfo/InCorpInfo"/>
				<xsl:apply-templates select="InNewsInfo/InNewsKindInfo"/>
				<xsl:apply-templates select="InNewsInfo/InSupportControl"/>
				<xsl:apply-templates select="InNewsInfo/InMainHeader"/>
				<xsl:apply-templates select="InNewsInfo/InEditInfo/InNewsRefType"/>
				<xsl:apply-templates select="InNewsInfo/InEditInfo/InLimitations"/>
				<xsl:apply-templates select="InNewsInfo/InEditInfo/InPostInfo"/>
                    <xsl:apply-templates select="InNewsInfo/InEditInfo/InDispatch"/>
                    <xsl:apply-templates select="InNewsInfo/InEditInfo/InAuthor"/>
                    <xsl:apply-templates select="InNewsInfo/InEditInfo/InEditLines/InEditLine"/>
				<xsl:apply-templates select="InNewsInfo/InEndInfo"/>
				<xsl:apply-templates select="InNewsInfo/InSubHeader"/>
                    <xsl:apply-templates select="InNewsInfo/InImageInfo/InBasicInfo"/>
                    <xsl:apply-templates select="InNewsInfo/InImageInfo/InAddInfo"/>
                    </table>
                    </td></tr>
                    </table>
                  <p></p>
                   </xsl:for-each>
			</body>
		</html>
	</xsl:template>

     


	<xsl:template match="InAdminInfo">

          <tr class="bgcolor2"><td class="bgcolor1">運用日付／区分</td>
          <td>	
		<xsl:if test="InDateTime[not(.='')]">
              <span class="color3"><xsl:value-of select="InDateTime"/></span>
		</xsl:if>
		<xsl:if test="InTestClass[not(.='')]">
               <span class="color3">／<xsl:value-of select="InTestClass"/></span>
		</xsl:if>
		<xsl:if test="InReSendClass[not(.='')]">
               <span class="color3">／<xsl:value-of select="InReSendClass"/></span>
		</xsl:if>
		<xsl:if test="InModifyInfo[not(.='')]">
               <span class="color3">／<xsl:value-of select="InModifyInfo"/></span>
		</xsl:if>
          </td></tr>
          <tr class="bgcolor2"><td class="bgcolor1">製品ＩＤ</td>
          <td><span class="color3"><xsl:value-of select="InProductId"/></span></td></tr>
          <tr class="bgcolor2"><td class="bgcolor1">データ形式</td><td>
          <span class="color3"><xsl:value-of select="InFormat/InFormatType"/></span>
		<xsl:if test="InFormat/InFormatComment[not(.='')]">
               <span class="color3">（<xsl:value-of select="InFormat/InFormatComment"/>）</span>
		</xsl:if>
          </td></tr>

			<xsl:for-each select="InRelatedInfo/InRelatedTo">
                    <tr class="bgcolor2"><td class="bgcolor1">関連リンク</td>
				 <td><span class="color3">（<xsl:value-of select="@InRelatedID"/>）（<xsl:value-of select="@InRelatedKind"/>）</span>
				 <xsl:if test="@InInstruction[not(.='')]">
							<span class="color3">（<xsl:value-of select="@InInstruction"/>）</span>
                     </xsl:if>
                     <xsl:if test="InRelatedTitle[not(.='')]">
                               <span class="color3"><xsl:value-of select="InRelatedTitle"/></span>
                            </xsl:if> 
                  </td></tr>
			</xsl:for-each>

       </xsl:template>

     <xsl:template match="InCategoryInfo/InNewsCategory">

		<xsl:if test=".[not(.='')]">
                    <tr class="bgcolor2"><td class="bgcolor1">記事種別情報</td><td>
                       <span class="color3"><xsl:value-of select="InNewsGenre"/></span>
                       <span class="color3"><xsl:value-of select="InNewsNo"/></span>
                    </td></tr>
          </xsl:if>
     </xsl:template>
 
	<xsl:template match="InCategoryInfo/InNewsLine">
         <xsl:apply-templates/>
     </xsl:template>
 
     <xsl:template match="InHeadLine">
         <tr class="bgcolor2"><td class="bgcolor1">見出し</td><td>
          <span class="color3"><xsl:apply-templates/></span>
          </td></tr>
     </xsl:template>

     <xsl:template match="InSubHeadLines">
      <xsl:if test="InSubHeadLine[not(.='')]">
         <xsl:for-each select="InSubHeadLine">
             <tr class="bgcolor2"><td class="bgcolor1">脇見出し</td><td>
             <span class="color3"><xsl:apply-templates/></span>
             </td></tr>
         </xsl:for-each>
      </xsl:if>
     </xsl:template>
    
     <xsl:template match="InKeywords">
         <xsl:if test="InKeyword[not(.='')]">
            <xsl:for-each select="InKeyword">
                 <tr class="bgcolor2"><td class="bgcolor1">キーワード</td><td>
                 <span class="color3"><xsl:apply-templates/></span>
                 </td></tr>
            </xsl:for-each>
         </xsl:if>
     </xsl:template>

	<xsl:template match="InCategoryInfo/InClasses">

		<xsl:if test=".[not(.='')]">
			<xsl:for-each select="InClass">
                    <tr class="bgcolor2"><td class="bgcolor1">内容分類</td><td>
				<xsl:if test="InBClass[not(.='')]">
                        <xsl:for-each select="InBClass">
                         <span class="color3">／大分類＝<xsl:apply-templates/></span>
                        </xsl:for-each>   
				</xsl:if>
				<xsl:if test="InMClass1[not(.='')]">
                       <xsl:for-each select="InMClass">
                        <span class="color3">／中分類１＝<xsl:apply-templates/></span>
                       </xsl:for-each>
				</xsl:if>
				<xsl:if test="InMClass2[not(.='')]">
                       <xsl:for-each select="InMClass2">
                          <span class="color3">／中分類２＝<xsl:apply-templates/></span>
                       </xsl:for-each>
 				</xsl:if>
				<xsl:if test="InSClass[not(.='')]">
                       <xsl:for-each select="InSClass">
                         <span class="color3">／小分類＝<xsl:apply-templates/></span>
                       </xsl:for-each>
				</xsl:if>
                   </td></tr>
			</xsl:for-each>
		</xsl:if>
     </xsl:template>

	<xsl:template match="InCategoryInfo/InAreaInfo">
       <xsl:for-each select="InAreas">
            <tr class="bgcolor2"><td class="bgcolor1">地域分類</td><td>
            <xsl:if test="@InPlace[not(.='')]">   
                 <span class="color3"><span>（<xsl:value-of select="@InPlace"/>）</span></span>  
            </xsl:if >  
            <xsl:apply-templates/>
            </td></tr>
        </xsl:for-each>   
     </xsl:template>

     <xsl:template match="InCountry">
          <span class="color3">／国名＝</span>
          <span class="color3"><xsl:value-of select="."/></span>
     </xsl:template>

     <xsl:template match="InJpnAreaName">
          <span class="color3">／地域コード＝</span>
          <span class="color3"><xsl:value-of select="."/></span>
     </xsl:template> 

     <xsl:template match="InLocation">
          <span class="color3"><xsl:apply-templates/></span>
     </xsl:template>
 
   <xsl:template match="InCategoryInfo/InCorpInfo">
       <xsl:for-each select="InCorps">
           <tr class="bgcolor2"><td class="bgcolor1">企業情報</td><td>
           <xsl:if test="@InTsecode[not(.='')]">   
                <span class="color3">（企業コード＝</span>  
                <span class="color3"><xsl:value-of select="@InTsecode"/>）</span>
           </xsl:if >  
           <xsl:apply-templates/>
           </td></tr>
       </xsl:for-each>   
     </xsl:template>

     <xsl:template match="InOfficial">
         <span class="color3">／正式名称＝</span>
         <span class="color3"><xsl:apply-templates/></span>
     </xsl:template>  

     <xsl:template match="InCorporation">
          <span class="color3">／企業名＝</span>
          <span class="color3"><xsl:apply-templates/></span>
     </xsl:template> 

   <xsl:template match="InNewsInfo/InNewsKindInfo">

      <xsl:if test=".[not(.='')]">
          <tr class="bgcolor2"><td class="bgcolor1">記事種目</td><td>
          <xsl:if test="InNewsKind[not(.='')]">
              <xsl:if test="InNewsKind/@InSubtype[not(.='')]">
                  <span class="color3"><xsl:value-of select="InNewsKind"/>（<xsl:value-of select="InNewsKind/@InSubtype"/>）</span>
              </xsl:if>
                  <span class="color3"><xsl:value-of select="InNewsKind"/></span>
		</xsl:if>
		<xsl:if test="InNewsKindDetail[not(.='')]">
              <span class="color3">／<xsl:value-of select="InNewsKindDetail"/></span>
		</xsl:if>
		<xsl:if test="InNewsType[not(.='')]">
              <span class="color3">／<xsl:value-of select="InNewsType"/></span>
		</xsl:if>
           </td></tr>
	</xsl:if>
  </xsl:template>

  <xsl:template match="InNewsInfo/InSupportControl">
       <tr class="bgcolor2"><td class="bgcolor1">サポート情報</td><td> 
       <xsl:apply-templates/>
       </td></tr>
  </xsl:template>

    <xsl:template match="RespInfo">
         <xsl:if test="InRespInfo/InRespDate[not(.='')]">
              <span class="color3"><xsl:value-of select="InRespInfo/InRespDate"/></span>
         </xsl:if>
         <xsl:if test="InRespInfo/InSendTo[not(.='')]">
              <span class="color3">／<xsl:value-of select="InRespInfo/InSendTo"/></span>
         </xsl:if>
         <xsl:if test="InRespInfo/InSendFrom[not(.='')]">
              <span class="color3">／<xsl:value-of select="InRespInfo/InSendFrom"/></span>
         </xsl:if>
    </xsl:template>

    <xsl:template match="InComment">
           <span class="color3">（<xsl:apply-templates/>）</span>
    </xsl:template>

   <xsl:template match="InNewsInfo/InMainHeader">
      <xsl:if test=".[not(.='')]">
         <tr class="bgcolor2"><td class="bgcolor1">主ヘッダ</td><td>
         <xsl:if test="InMainRank[not(.='')]">
             <span class="color3"><xsl:value-of select="InMainRank"/></span>
         </xsl:if>
         <xsl:if test="InSubRank[not(.='')]">
             <span class="color3"><xsl:value-of select="InSubRank"/></span>
         </xsl:if>
         <xsl:if test="InPriority[not(.='')]">
             <span class="color3"><xsl:value-of select="InPriority"/></span>
         </xsl:if>
         <xsl:if test="InOfficeId[not(.='')]">
             <span class="color3"><xsl:value-of select="InOfficeId"/></span>
         </xsl:if>
         <xsl:if test="InTotalNo[not(.='')]">
             <span class="color3"><xsl:value-of select="InTotalNo"/></span>
         </xsl:if>
         <xsl:if test="InSendSeq[not(.='')]">
              <xsl:if test="InSendSeq/InSendSeqTotal[not(.='')]">
                   <span class="color3">（<xsl:value-of select="InSendSeq/InSendSeqTotal"/>）完</span>
		    </xsl:if>
	         <xsl:if test="InSendSeq/InSendSeqNo[not(.='')]">
                    <span class="color3">（<xsl:value-of select="InSendSeq/InSendSeqNo"/>）</span>
		    </xsl:if>
         </xsl:if>
         </td></tr>
	</xsl:if>
  </xsl:template>


  <xsl:template match="InNewsInfo/InEditInfo/InNewsRefType">
    <tr class="bgcolor2"><td class="bgcolor1">記事タイプ</td><td>
    <span class="color3">／<xsl:value-of select="."/></span></td></tr>
  </xsl:template>

  <xsl:template match="InNewsInfo/InEditInfo/InLimitations">
       <xsl:for-each select="InLimitation" >
           <tr class="bgcolor2"><td class="bgcolor1">解禁情報</td><td>
           <xsl:if test="@InLimitDateAndTime[not(.='')]">
               <span class="color3">（<xsl:value-of select="@InLimitDateAndTime"/>）</span>
           </xsl:if>
           <xsl:if test="@InLimitType[not(.='')]">
               <span class="color3">（<xsl:value-of select="@InLimitType"/>）</span>
           </xsl:if>
           <span class="color3"><xsl:value-of select="."/></span>
           </td></tr> 
       </xsl:for-each>   
  </xsl:template>

  <xsl:template match="InNewsInfo/InEditInfo/InPostInfo">
      <tr class="bgcolor2"><td class="bgcolor1">注意喚起部署</td><td>
      <xsl:for-each select="InPostName">
           <span class="color3"><xsl:value-of select="."/></span>
      </xsl:for-each>
      </td></tr> 
  </xsl:template>

  <xsl:template match="InNewsInfo/InEditInfo/InDispatch">
      <tr class="bgcolor2"><td class="bgcolor1">発信地</td><td>
      <span class="color3"><xsl:apply-templates/></span>
     </td></tr>
  </xsl:template>

  <xsl:template match="InNewsInfo/InEditInfo/InAuthor">
      <tr class="bgcolor2"><td class="bgcolor1">作成者</td><td>
      <span class="color3"><xsl:apply-templates/></span>
      </td></tr>
  </xsl:template>

  <xsl:template match="InNewsInfo/InEditInfo/InEditLines/InEditLine">
     <tr class="bgcolor2"><td class="bgcolor1">編注記述</td><td>
     <xsl:if test="@InEditType[not(.='')]">   
        <span class="color3">（<xsl:value-of select="@InEditType"/>）</span>
     </xsl:if >  
     <span class="color3"><xsl:apply-templates/></span>
     </td></tr>
  </xsl:template>



  <xsl:template match="InNewsInfo/InEndInfo">
     <tr class="bgcolor2"><td class="bgcolor1">末尾編注</td><td>
     <xsl:apply-templates/> 
     </td></tr>
  </xsl:template>

  <xsl:template match="InHomeTown">
      <span class="color3">／<xsl:apply-templates/></span>
  </xsl:template>

  <xsl:template match="InEndLines">
       <xsl:for-each select="InEndLine">
           <span class="color3">／<xsl:apply-templates/></span>
       </xsl:for-each>
  </xsl:template>

  <xsl:template match="InNewsInfo/InSubHeader">
       <xsl:if test=".[not(.='')]">
            <xsl:if test="InSendControl[not(.='')]">
                  <tr class="bgcolor2"><td class="bgcolor1">副ヘッダ</td><td>
                  <xsl:if test="InSendControl/InSendBlkInfo[not(.='')]">
                      <xsl:if test="InSendControl/InSendBlkInfo/InSendBlk[not(.='')]">
                           <xsl:for-each select="InSendControl/InSendBlkInfo/InSendBlk">
                                 <span class="color3">／<xsl:value-of select="."/></span>
                           </xsl:for-each>
                      </xsl:if>                                
                   </xsl:if>
                   <xsl:if test="InSendControl/InSendIndInfo[not(.='')]">
                        <xsl:if test="InSendControl/InSendIndInfo/InSendInd[not(.='')]">
                            <xsl:for-each select="InSendControl/InSendIndInfo/InSendInd">
                                 <span class="color3">／<xsl:value-of select="."/></span>
                            </xsl:for-each>
                        </xsl:if>                                
                   </xsl:if>
                   </td></tr>
                   <xsl:if test="InSendControl/InSendRestrict[not(.='')]">
                        <tr class="bgcolor2"><td class="bgcolor1">縛り情報</td><td>
                        <span class="color3"><xsl:value-of select="InSendControl/InSendRestrict"/></span>
                        </td></tr>
                   </xsl:if>
           </xsl:if>
      </xsl:if>
  </xsl:template>

 <xsl:template match="InNewsInfo/InImageInfo/InBasicInfo">
     <tr class="bgcolor2"><td class="bgcolor1">電説編注</td><td>
     <xsl:if test="InView[not(.='')]">
          <xsl:for-each select="InView">
             <span class="color3">／<xsl:apply-templates/></span>
          </xsl:for-each>      
       </xsl:if>
     <xsl:if test="InRef[not(.='')]">
          <xsl:for-each select="InRef">
             <span class="color3">／<xsl:apply-templates/></span>
           </xsl:for-each>
      </xsl:if>
     <xsl:if test="InStyle[not(.='')]">
         <xsl:for-each select="InStyle">
             <span class="color3">／<xsl:apply-templates/></span>
           </xsl:for-each>
      </xsl:if>
      <xsl:if test="InDeviceInfo[not(.='')]">
           <xsl:for-each select="InDeviceInfo">
                <xsl:for-each select="InDevice">
                     <span class="color3">／<xsl:apply-templates/></span>
                 </xsl:for-each>
            </xsl:for-each>
       </xsl:if>
     <xsl:if test="InImageRightsInfo[not(.='')]">
        <xsl:for-each select="InImageRightsInfo/InImageRights">
           <span class="color3">／<xsl:apply-templates/></span>
        </xsl:for-each>
     </xsl:if>
  </td></tr>
 </xsl:template>

<xsl:template match="InNewsInfo/InImageInfo/InAddInfo">
  <tr class="bgcolor2"><td class="bgcolo1">画像情報</td><td>
     <xsl:if test="InImageFormat[not(.='')]">
          <xsl:for-each select="InImageFormat">
             <span class="color3">データ種別＝<xsl:apply-templates/></span>
          </xsl:for-each>      
       </xsl:if>
     <xsl:if test="InImageSize[not(.='')]">
          <xsl:for-each select="InImageSize">
             <span class="color3">／データサイズ＝<xsl:apply-templates/></span>
           </xsl:for-each>
      </xsl:if>
     <xsl:if test="InDateCreated[not(.='')]">
         <xsl:for-each select="InDateCreated">
             <span class="color3">／生成日時＝<xsl:apply-templates/></span>
           </xsl:for-each>
      </xsl:if>
     <xsl:if test="InImageCredit[not(.='')]">
         <xsl:for-each select="InImageCredit">
             <span class="color3">／外電種別＝<xsl:apply-templates/></span>
           </xsl:for-each>
      </xsl:if>
  </td></tr>
  <xsl:if test="InAddEditLines[not(.='')]">
    <tr class="bgcolor2"><td class="bgcolor1">画像追加情報</td><td>
    <xsl:apply-templates/>
    </td></tr>
  </xsl:if>
</xsl:template>

<xsl:template match="InAddEditLines">
   <xsl:for-each select="InAddEditLine">
       <span class="color3">／<xsl:apply-templates/></span>
   </xsl:for-each>
</xsl:template>

<xsl:template match="KdRuby">
  <RUBY style="ruby-align:left">
  <xsl:value-of select="KdRb"/>
  <xsl:if test="KdRb/KdGaiji[not(.='')]">
     （<xsl:value-of select="KdRb/KdGaiji/@KdJikai"/>）
  </xsl:if>
  <RT style="font-size:6pt">
  <xsl:value-of select="KdRt"/>
  </RT>
  </RUBY>
</xsl:template>

<xsl:template match="KdGaiji">
   <xsl:value-of select="." />
   （<xsl:value-of select="@KdJikai"/>）
</xsl:template>

<xsl:template match="text()">
  <xsl:value-of  />
</xsl:template>	

</xsl:stylesheet>
