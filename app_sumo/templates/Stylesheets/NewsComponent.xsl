<?xml version="1.0" encoding="UTF-16"?>
<!--<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" version="1.0" encoding="UTF-16" indent="yes"/>
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl" xml:lang="ja">

	<xsl:template match="/">
		<html lang="ja">
			<head>
				<title>NewsComponent</title>
              <style type="text/css">
                   .color1  {color:brown;} 
                   .color2  {color:purple;font-weight:bold}
                   .color3  {color:green;font-size:12pt} 
                   .bgcolor1  {background-color:silver;font-weight:bold;color:black;font-size:10pt}
                   .bgcolor2 {background-color:white}
               </style>


			</head>
			<body>
                    <div style="font-weight:bold;font-size:20pt;color:#483B8D">NewsComponent</div>
                   <xsl:for-each select="NewsML/NewsItem">
                   <div><xsl:apply-templates select="NewsComponent"/></div>
                   <table bgcolor="#000000" cellpadding="0" cellspacing="0">
                         <tr><td>
                   <table border="0" cellpadding="4" cellspacing="1"  width="800">
                    <tr class="bgcolor2"><td class="color1" >項目名</td><td class="color1">内容</td></tr>
				<xsl:apply-templates select="NewsComponent/Comment"/>
				<xsl:apply-templates select="NewsComponent/Catalog"/>
				<xsl:apply-templates select="NewsComponent/NewsLines"/>
				<xsl:apply-templates select="NewsComponent/AdministrativeMetadata"/>
				<xsl:apply-templates select="NewsComponent/RightsMetadata"/>
				<xsl:apply-templates select="NewsComponent/DescriptiveMetadata"/>
				<xsl:apply-templates select="NewsComponent/Metadata"/>
				<xsl:apply-templates select="NewsComponent/NewsItem"/>
				<xsl:apply-templates select="NewsComponent/NewsItemRef"/>
				<xsl:apply-templates select="NewsComponent/NewsComponent"/>
				<xsl:apply-templates select="NewsComponent/ContentItem"/>
                    </table>
                    </td></tr>
                    </table>
                  <p></p>
                   </xsl:for-each>
			</body>
		</html>
	</xsl:template>

     
       <xsl:template match="NewsComponent">
		<xsl:if test="@Essential[not(.='')]">
             <span class="color3">（Essential=<xsl:value-of select="@Essential"/>）</span>
		</xsl:if>
		<xsl:if test="@EquivalentsList[not(.='')]">
             <span class="color3">（EquivalentsList=<xsl:value-of select="@EquivalentsList"/>）</span>
 		</xsl:if>
		<xsl:if test="@Duid[not(.='')]">
               <span class="color3">（Duid=<xsl:value-of select="@Duid"/>）</span>
		</xsl:if>
       </xsl:template>

       <xsl:template match="NewsComponent/Comment">
          <tr class="bgcolor2"><td class="bgcolor1">Comment</td>
         <td>	
          <xsl:for-each select=".">
                <xsl:if test=".[not(.='')]">
                     <span class="color3">／<xsl:value-of select="."/></span>
                 </xsl:if>
          </xsl:for-each>
         </td></tr>
       </xsl:template>

     <xsl:template match="NewsComponent/Catalog">
           <tr class="bgcolor2"><td class="bgcolor1">Catalog</td><td>	
           <xsl:if test="@Href[not(.='')]">
                     <span class="color3">（Href=<xsl:value-of select="@Href"/>）</span>
           </xsl:if>
          </td></tr>
 
         <xsl:for-each select="NewsComponent/Resource">
            <tr class="bgcolor2"><td class="bgcolor1">Catalog/Resouce</td><td>	
                 <xsl:if test="Urn[not(.='')]">
                     <span class="color3">Urn=<xsl:value-of select="Urn"/></span>
                 </xsl:if> 
                 <xsl:for-each select="Url">
                     <span class="color3">／Url=<xsl:value-of select="."/></span>
                 </xsl:for-each>             
                 <xsl:for-each select="DefaultVocabularyFor">
                     <span class="color3">／DefaultVocabularyFor@Context=<xsl:value-of select="@Context"/></span>
                     <xsl:if test="@Scheme[not(.='')]">
                         <span class="color3">／DefaultVocabularyFor@Scheme=<xsl:value-of select="@Scheme"/></span>
                    </xsl:if> 
                 </xsl:for-each> 
                 </td></tr>
         </xsl:for-each>             
     </xsl:template>
 
	<xsl:template match="NewsComponent/NewsLines">
         <tr class="bgcolor2"><td class="bgcolor1">NewsLines</td><td>
          </td></tr>
     </xsl:template>

	<xsl:template match="NewsComponent/AdministrativeMetadata">
         <tr class="bgcolor2"><td class="bgcolor1">AdministrativeMetadata</td><td>
          </td></tr>
     </xsl:template>

	<xsl:template match="NewsComponent/RightsMetadata">
         <tr class="bgcolor2"><td class="bgcolor1">RightsMetadata</td><td>
          </td></tr>
     </xsl:template>

	<xsl:template match="NewsComponent/DescriptiveMetadata">
         <tr class="bgcolor2"><td class="bgcolor1">DescriptiveMetadata</td><td>
          </td></tr>
     </xsl:template>

	<xsl:template match="NewsComponent/Metadata">
         <xsl:for-each select=".">
             <tr class="bgcolor2"><td class="bgcolor1">Metadata</td><td>
             </td></tr>
         </xsl:for-each>
     </xsl:template>

	<xsl:template match="NewsComponent/NewsItem">
         <xsl:for-each select=".">
             <tr class="bgcolor2"><td class="bgcolor1">NewsItem</td><td>
             </td></tr>
         </xsl:for-each>
     </xsl:template>

	<xsl:template match="NewsComponent/NewsItemRef">
         <xsl:for-each select=".">
             <tr class="bgcolor2"><td class="bgcolor1">NewsItemRef</td><td>
             <span class="color3">NewsItem=<xsl:value-of select="@NewsItem"/>
             <xsl:for-each select="Comment">
                <xsl:if test=".[not(.='')]">
                     <span class="color3">（Comment=<xsl:value-of select="."/>）</span>
                 </xsl:if>
             </xsl:for-each>
             </span>
             </td></tr>
         </xsl:for-each>
     </xsl:template>

	<xsl:template match="NewsComponent/NewsComponent">
         <xsl:for-each select=".">
             <tr class="bgcolor2"><td class="bgcolor1">NewsComponent</td><td>
             </td></tr>
         </xsl:for-each>
     </xsl:template>

	<xsl:template match="NewsComponent/ContentItem">
         <xsl:for-each select=".">
             <tr class="bgcolor2"><td class="bgcolor1">ContentItem</td><td>
             </td></tr>
         </xsl:for-each>
     </xsl:template>


</xsl:stylesheet>
