<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl" xml:lang="ja">

	<xsl:template match="/">
		<html lang="ja">
			<head>
				<title>
                 AdministrativeMetadata
              </title>
              <style type="text/css">
                   .color1  {color:brown;} 
                   .color2  {color:purple;font-weight:bold}
                   .color3  {color:green;font-size:12pt} 
                   .bgcolor1  {background-color:silver;font-weight:bold;color:black;font-size:10pt}
                   .bgcolor2 {background-color:white}
               </style>


			</head>
			<body>
                    <div style="font-weight:bold;font-size:20pt;color:#483B8D">AdministrativeMetadata</div>
                   <xsl:for-each select="NewsML/NewsItem/NewsComponent/AdministrativeMetadata">
                   <table bgcolor="#000000" cellpadding="0" cellspacing="0">
                         <tr><td>
                   <table border="0" cellpadding="4" cellspacing="1"  width="800">
                    <tr class="bgcolor2"><td class="color1" >項目名</td><td class="color1">内容</td></tr>
				<xsl:apply-templates select="Catalog"/>
				<xsl:apply-templates select="Provider"/>
                    </table>
                    </td></tr>
                    </table>
				<xsl:apply-templates select="Property"/>
                  <p></p>
                   </xsl:for-each>
			</body>
		</html>
	</xsl:template>

 	<xsl:template match="Catalog">

           <tr class="bgcolor2"><td class="bgcolor1">Catalog</td><td>	
           <xsl:if test="@Href[not(.='')]">
               <span class="color3">（Href=<xsl:value-of select="@Href"/>）</span>
           </xsl:if>
          </td></tr>
 
         <xsl:for-each select="Resource">
            <tr class="bgcolor2"><td class="bgcolor1">Catalog/Resouce</td><td>	
                     <xsl:if test="Urn[not(.='')]">
                        <span class="color3">Urn=<xsl:value-of select="Urn"/></span>
                     </xsl:if> 
                     <xsl:for-each select="Url">
                         <span class="color3">／Url=<xsl:value-of select="."/></span>
                    </xsl:for-each>             
                    <xsl:for-each select="DefaultVocabularyFor">
                        <span class="color3">（DefaultVocabularyFor@Context=<xsl:value-of select="@Context"/>）</span>
                        <xsl:if test="@Scheme[not(.='')]">
                          <span class="color3">（DefaultVocabularyFor@Scheme=<xsl:value-of select="@Scheme"/>）</span>
                       </xsl:if> 
                   </xsl:for-each> 
           </td></tr>
       </xsl:for-each>             
    </xsl:template>      

 	<xsl:template match="Provider">
          <tr class="bgcolor2"><td class="bgcolor1">Provider</td>
         <td>	
          <xsl:for-each select="Party">
                <xsl:if test="@FormalName[not(.='')]">
                    <span class="color3">（Party@FormalName=<xsl:value-of select="@FormalName"/>）</span>
                </xsl:if>
                <xsl:if test="@Topic[not(.='')]">
                    <span class="color3">（Party@Topic=<xsl:value-of select="@Topic"/>）</span>
                </xsl:if>
         </xsl:for-each>
         </td></tr>
     </xsl:template>

	<xsl:template match="Property">
        <xsl:for-each select=".">
           <P></P> 
               <div><span style="color:black;font-size:12pt;font-weight:bold}">Property（FormalName=<xsl:value-of select="@FormalName"/>）
               <xsl:if test="@value[not(.='')]">（Value=<xsl:value-of select="@Value"/>）</xsl:if></span></div> 
               <xsl:for-each select="Property">
                <table border="1" cellpadding="4" cellspacing="1"  width="800">
                 <tr><td rowspan="100" width="200"><span class="bgcolor1"><xsl:value-of select="@FormalName"/></span></td><td><span class="color3"><xsl:value-of select="@Value"/></span></td></tr>
                 <xsl:for-each select="Property" >
                      <tr><td width ="300"><span class="color3"><xsl:value-of select="@FormalName"/></span></td>
                      <td><span class="color3"><xsl:value-of select="@Value"/></span></td></tr>
                 </xsl:for-each>   
               </table>
             </xsl:for-each>
      </xsl:for-each>

   </xsl:template>

    </xsl:stylesheet>    
