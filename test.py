from selenium import webdriver
from selenium.webdriver.common.by import By

from Database import Databases
from DownloadHTML import DownloadHTML
from AdressCollecting import *
import urllib.request as req
import re
import time
import os
import ssl
text = """
<!doctype html>
<html lang="ko">

                                                                <head>
                
                
                        <!-- BusinessLicenseInfo - START -->
        
            <link href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/plugin/BusinessLicenseInfo/style.css" rel="stylesheet" type="text/css"/>

            <script>function switchFold(entryId) {
    var businessLayer = document.getElementById("businessInfoLayer_" + entryId);

    if (businessLayer) {
        if (businessLayer.className.indexOf("unfold_license") > 0) {
            businessLayer.className = "business_license_layer";
        } else {
            businessLayer.className = "business_license_layer unfold_license";
        }
    }
}
</script>

        
        <!-- BusinessLicenseInfo - END -->
        <!-- DaumShow - START -->
        <style type="text/css">#daumSearchBox {
    height: 21px;
    background-image: url(//i1.daumcdn.net/imgsrc.search/search_all/show/tistory/plugin/bg_search2_2.gif);
    margin: 5px auto;
    padding: 0;
}

#daumSearchBox input {
    background: none;
    margin: 0;
    padding: 0;
    border: 0;
}

#daumSearchBox #daumLogo {
    width: 34px;
    height: 21px;
    float: left;
    margin-right: 5px;
    background-image: url(//i1.daumcdn.net/img-media/tistory/img/bg_search1_2_2010ci.gif);
}

#daumSearchBox #show_q {
    background-color: transparent;
    border: none;
    font: 12px Gulim, Sans-serif;
    color: #555;
    margin-top: 4px;
    margin-right: 15px;
    float: left;
}

#daumSearchBox #show_btn {
    background-image: url(//i1.daumcdn.net/imgsrc.search/search_all/show/tistory/plugin/bt_search_2.gif);
    width: 37px;
    height: 21px;
    float: left;
    margin: 0;
    cursor: pointer;
    text-indent: -1000em;
}
</style>

        <!-- DaumShow - END -->

<!-- System - START -->
<script src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js" async="async" data-ad-host="ca-host-pub-9691043933427338" data-ad-client="ca-pub-7577868474757541"></script>
<!-- System - END -->

        <!-- A_ShareEntryWithSNS - START -->
        <link href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/plugin/A_ShareEntryWithSNS/style.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/plugin/A_ShareEntryWithSNS/script.js"></script>

        <!-- A_ShareEntryWithSNS - END -->

        <!-- TistoryProfileLayer - START -->
        <link href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/plugin/TistoryProfileLayer/style.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/plugin/TistoryProfileLayer/script.js"></script>

        <!-- TistoryProfileLayer - END -->

                
                <meta http-equiv="X-UA-Compatible" content="IE=Edge">
<meta name="format-detection" content="telephone=no">
<script src="//t1.daumcdn.net/tistory_admin/lib/jquery/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
<script src="//t1.daumcdn.net/tistory_admin/lib/lightbox/js/lightbox-v2.10.0.min.js" defer></script>
<script type="text/javascript" src="//t1.daumcdn.net/tiara/js/v1/tiara.min.js"></script><meta name="referrer" content="always"/>
<meta name="google-adsense-platform-account" content="ca-host-pub-9691043933427338"/>
<meta name="google-adsense-platform-domain" content="tistory.com"/>
<meta name="google-adsense-account" content="ca-pub-7577868474757541"/>
<meta name="description" content="안녕 ㅇㄴㅁㅁ 나는 선이에요 블로그는 나랑 안맞다고 생각했는데 요즘 인스타 권태기와서 넘 하기 싫구 -ㅅ - 티스토리 아가로 시작해볼거에요 구독과 댓글 좋아요 (유튭아님) 많이 부탁해요 ! 선이의 인스타 : https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y= Instagram의 류 혜선님 : &quot;@showkingcar_official 🚕&quot; 류 혜선님이 Instagram에 게시물을 공유했습니다:&quot;@showkingcar_official 🚕&quot;. 계정을 팔로우하여 게시물 196개를 확인해보세요. www.instagram.com 선이의 카카오톡 https://open.kakao.com/o/sc4RjOLd 0_0_hs님의 오픈프로필 open.kakao.com"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="https://0-0-hs.tistory.com/2"/>
<meta property="og.article.author" content="선이네 선이"/>
<meta property="og:site_name" content="선이의 선선한"/>
<meta property="og:title" content="티스토리 첫 번째 포스팅 _ 선이의 일상"/>
<meta name="by" content="선이네 선이"/>
<meta property="og:description" content="안녕 ㅇㄴㅁㅁ 나는 선이에요 블로그는 나랑 안맞다고 생각했는데 요즘 인스타 권태기와서 넘 하기 싫구 -ㅅ - 티스토리 아가로 시작해볼거에요 구독과 댓글 좋아요 (유튭아님) 많이 부탁해요 ! 선이의 인스타 : https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y= Instagram의 류 혜선님 : &quot;@showkingcar_official 🚕&quot; 류 혜선님이 Instagram에 게시물을 공유했습니다:&quot;@showkingcar_official 🚕&quot;. 계정을 팔로우하여 게시물 196개를 확인해보세요. www.instagram.com 선이의 카카오톡 https://open.kakao.com/o/sc4RjOLd 0_0_hs님의 오픈프로필 open.kakao.com"/>
<meta property="og:image" content="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fwet1I%2FbtrT8qwzqLU%2FrhasOYqjpWNX2amQ230FgK%2Fimg.jpg"/>
<meta property="article:section" content="'일상다반사'"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:site" content="@TISTORY"/>
<meta name="twitter:title" content="티스토리 첫 번째 포스팅 _ 선이의 일상"/>
<meta name="twitter:description" content="안녕 ㅇㄴㅁㅁ 나는 선이에요 블로그는 나랑 안맞다고 생각했는데 요즘 인스타 권태기와서 넘 하기 싫구 -ㅅ - 티스토리 아가로 시작해볼거에요 구독과 댓글 좋아요 (유튭아님) 많이 부탁해요 ! 선이의 인스타 : https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y= Instagram의 류 혜선님 : &quot;@showkingcar_official 🚕&quot; 류 혜선님이 Instagram에 게시물을 공유했습니다:&quot;@showkingcar_official 🚕&quot;. 계정을 팔로우하여 게시물 196개를 확인해보세요. www.instagram.com 선이의 카카오톡 https://open.kakao.com/o/sc4RjOLd 0_0_hs님의 오픈프로필 open.kakao.com"/>
<meta property="twitter:image" content="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fwet1I%2FbtrT8qwzqLU%2FrhasOYqjpWNX2amQ230FgK%2Fimg.jpg"/>
<meta content="https://0-0-hs.tistory.com/2" property="dg:plink" content="https://0-0-hs.tistory.com/2"/>
<meta name="plink"/>
<meta name="title" content="티스토리 첫 번째 포스팅 _ 선이의 일상"/>
<meta name="article:media_name" content="선이의 선선한"/>
<meta property="article:mobile_url" content="https://0-0-hs.tistory.com/m/2"/>
<meta property="article:pc_url" content="https://0-0-hs.tistory.com/2"/>
<meta property="article:mobile_view_url" content="https://0-0-hs.tistory.com/m/2"/>
<meta property="article:pc_view_url" content="https://0-0-hs.tistory.com/2"/>
<meta property="article:talk_channel_view_url" content="https://0-0-hs.tistory.com/m/2"/>
<meta property="article:pc_service_home" content="https://www.tistory.com"/>
<meta property="article:mobile_service_home" content="https://www.tistory.com/m"/>
<meta property="article:txid" content="5860621_2"/>
<meta property="article:published_time" content="2022-12-20T12:04:47+09:00"/>
<meta property="og:regDate" content="20221220120447"/>
<meta property="article:modified_time" content="2022-12-20T12:04:47+09:00"/>
<link rel="stylesheet" type="text/css" href="https://t1.daumcdn.net/tistory_admin/lib/lightbox/css/lightbox.min.css"/>
<link rel="stylesheet" type="text/css" href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/style/font.css"/>
<link rel="stylesheet" type="text/css" href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/style/content.css"/>
<link rel="stylesheet" type="text/css" href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/style/uselessPMargin.css"/>
<script type="text/javascript">(function() {
    var tjQuery = jQuery.noConflict(true);
    window.tjQuery = tjQuery;
    window.orgjQuery = window.jQuery; window.jQuery = tjQuery;
    window.jQuery = window.orgjQuery; delete window.orgjQuery;
})()</script>
<script type="text/javascript" src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/script/base.js"></script>
<script type="text/javascript">if (!window.T) { window.T = {} }
window.T.config = {"TOP_SSL_URL":"https://www.tistory.com","PREVIEW":false,"ROLE":"user","PREV_PAGE":"","NEXT_PAGE":"","BLOG":{"id":5860621,"name":"0-0-hs","title":"선이의 선선한","isDormancy":false},"NEED_COMMENT_LOGIN":false,"COMMENT_LOGIN_CONFIRM_MESSAGE":"","LOGIN_URL":"https://www.tistory.com/auth/login/?redirectUrl=https%3A%2F%2F0-0-hs.tistory.com%2F2","DEFAULT_URL":"https://0-0-hs.tistory.com","USER":{"name":"SweetDev","homepage":"https://sweetdev.tistory.com"},"SUBSCRIPTION":{"status":"none","isConnected":false,"isPending":false,"isWait":false,"isProcessing":false,"isNone":true},"IS_LOGIN":true,"HAS_BLOG":true,"TOP_URL":"http://www.tistory.com","JOIN_URL":"https://www.tistory.com/member/join","ROLE_GROUP":"visitor"};
window.appInfo = {"domain":"tistory.com","topUrl":"https://www.tistory.com","loginUrl":"https://www.tistory.com/auth/login","logoutUrl":"https://www.tistory.com/auth/logout"};
window.initData = {"user":{"id":3776385,"loginId":"yy991125@naver.com","name":"SweetDev"}};

window.TistoryBlog = {
    basePath: "",
    url: "https://0-0-hs.tistory.com",
    tistoryUrl: "https://0-0-hs.tistory.com",
    manageUrl: "https://0-0-hs.tistory.com/manage",
    token: "nr382ADmL3KbFipcnU23McChxWA+308ESZUCRA/uy96raEhXL2BJSDe95sGozv0C"
};
var servicePath = "";
var blogURL = "";</script>
<script type="text/javascript" src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

                
<meta name="google-site-verification" content="ukG0iUuu7-0n7cPePkkYTSK4nSmeTidb2z1_qXebJTA" />
<meta name="google-site-verification" content="ukG0iUuu7-0n7cPePkkYTSK4nSmeTidb2z1_qXebJTA" />
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7577868474757541"
     crossorigin="anonymous"></script>
		 
	<meta charset="UTF-8">
	<meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, width=device-width">
	<title>티스토리 첫 번째 포스팅 _ 선이의 일상</title>
	<link rel="alternate" type="application/rss+xml" title="선이의 선선한" href="https://0-0-hs.tistory.com/rss" />
<meta name="naver-site-verification" content="e57cc858fa816f3ca06c3d33bc9b9ab165ff06e1" />

	<link rel="stylesheet" href="https://tistory1.daumcdn.net/tistory/5860621/skin/style.css?_version_=1675125350">
	<link rel="stylesheet" href="https://tistory1.daumcdn.net/tistory/5860621/skin/images/font.css?_version_=1675125350">
	<style>
		
		.wrap_sub {
			background-image: url('https://tistory3.daumcdn.net/tistory/5860621/skinSetting/4b0b3394e3e041f2884fe2795b512d38');
		}
		
	</style>

	<!--[if lt IE 9]>
	<script src="//t1.daumcdn.net/tistory_admin/lib/jquery/jquery-1.12.4.min.js"></script>
	<![endif]-->
	<!--[if gte IE 9]><!-->
	<script src="//t1.daumcdn.net/tistory_admin/lib/jquery/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
	<!--<![endif]-->
	<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7577868474757541"
     crossorigin="anonymous"></script>
		 

                
                
                <style type="text/css">.another_category {
    border: 1px solid #E5E5E5;
    padding: 10px 10px 5px;
    margin: 10px 0;
    clear: both;
}

.another_category h4 {
    font-size: 12px !important;
    margin: 0 !important;
    border-bottom: 1px solid #E5E5E5 !important;
    padding: 2px 0 6px !important;
}

.another_category h4 a {
    font-weight: bold !important;
}

.another_category table {
    table-layout: fixed;
    border-collapse: collapse;
    width: 100% !important;
    margin-top: 10px !important;
}

* html .another_category table {
    width: auto !important;
}

*:first-child + html .another_category table {
    width: auto !important;
}

.another_category th, .another_category td {
    padding: 0 0 4px !important;
}

.another_category th {
    text-align: left;
    font-size: 12px !important;
    font-weight: normal;
    word-break: break-all;
    overflow: hidden;
    line-height: 1.5;
}

.another_category td {
    text-align: right;
    width: 80px;
    font-size: 11px;
}

.another_category th a {
    font-weight: normal;
    text-decoration: none;
    border: none !important;
}

.another_category th a.current {
    font-weight: bold;
    text-decoration: none !important;
    border-bottom: 1px solid !important;
}

.another_category th span {
    font-weight: normal;
    text-decoration: none;
    font: 10px Tahoma, Sans-serif;
    border: none !important;
}

.another_category_color_gray, .another_category_color_gray h4 {
    border-color: #E5E5E5 !important;
}

.another_category_color_gray * {
    color: #909090 !important;
}

.another_category_color_gray th a.current {
    border-color: #909090 !important;
}

.another_category_color_gray h4, .another_category_color_gray h4 a {
    color: #737373 !important;
}

.another_category_color_red, .another_category_color_red h4 {
    border-color: #F6D4D3 !important;
}

.another_category_color_red * {
    color: #E86869 !important;
}

.another_category_color_red th a.current {
    border-color: #E86869 !important;
}

.another_category_color_red h4, .another_category_color_red h4 a {
    color: #ED0908 !important;
}

.another_category_color_green, .another_category_color_green h4 {
    border-color: #CCE7C8 !important;
}

.another_category_color_green * {
    color: #64C05B !important;
}

.another_category_color_green th a.current {
    border-color: #64C05B !important;
}

.another_category_color_green h4, .another_category_color_green h4 a {
    color: #3EA731 !important;
}

.another_category_color_blue, .another_category_color_blue h4 {
    border-color: #C8DAF2 !important;
}

.another_category_color_blue * {
    color: #477FD6 !important;
}

.another_category_color_blue th a.current {
    border-color: #477FD6 !important;
}

.another_category_color_blue h4, .another_category_color_blue h4 a {
    color: #1960CA !important;
}

.another_category_color_violet, .another_category_color_violet h4 {
    border-color: #E1CEEC !important;
}

.another_category_color_violet * {
    color: #9D64C5 !important;
}

.another_category_color_violet th a.current {
    border-color: #9D64C5 !important;
}

.another_category_color_violet h4, .another_category_color_violet h4 a {
    color: #7E2CB5 !important;
}
</style>

                
                <link rel="stylesheet" type="text/css" href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/style/dialog.css"/>
<link rel="stylesheet" type="text/css" href="//t1.daumcdn.net/tistory_admin/www/style/top/font.css"/>
<link rel="stylesheet" type="text/css" href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/style/postBtn.css"/>
<link rel="stylesheet" type="text/css" href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/style/tistory.css"/>
<link rel="stylesheet" type="text/css" href="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/style/revenue.css"/>
<link rel="canonical" href="https://0-0-hs.tistory.com/2"/>

<!-- BEGIN STRUCTURED_DATA -->
<script type="application/ld+json">
    {"@context":"http://schema.org","@type":"BlogPosting","mainEntityOfPage":{"@id":"https://0-0-hs.tistory.com/2","name":null},"url":"https://0-0-hs.tistory.com/2","headline":"티스토리 첫 번째 포스팅 _ 선이의 일상","description":"안녕 ㅇㄴㅁㅁ 나는 선이에요 블로그는 나랑 안맞다고 생각했는데 요즘 인스타 권태기와서 넘 하기 싫구 -ㅅ - 티스토리 아가로 시작해볼거에요 구독과 댓글 좋아요 (유튭아님) 많이 부탁해요 ! 선이의 인스타 : https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y= Instagram의 류 혜선님 : &quot;@showkingcar_official 🚕&quot; 류 혜선님이 Instagram에 게시물을 공유했습니다:&quot;@showkingcar_official 🚕&quot;. 계정을 팔로우하여 게시물 196개를 확인해보세요. www.instagram.com 선이의 카카오톡 https://open.kakao.com/o/sc4RjOLd 0_0_hs님의 오픈프로필 open.kakao.com","author":{"@type":"Person","name":"선이네 선이","logo":null},"image":{"@type":"ImageObject","url":"https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fwet1I%2FbtrT8qwzqLU%2FrhasOYqjpWNX2amQ230FgK%2Fimg.jpg","width":"800px","height":"800px"},"datePublished":"20221220T12:04:47","dateModified":"20221220T12:04:47","publisher":{"@type":"Organization","name":"TISTORY","logo":{"@type":"ImageObject","url":"https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png","width":"800px","height":"800px"}}}
</script>
<!-- END STRUCTURED_DATA -->
<script type="text/javascript" src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/script/common.js"></script>

                </head>

                                <body id="tt-body-page">
                
                


	<div id="dkIndex">
		<!--웹접근성용 바로가기 링크 모음-->
		<a href="#dkBody">본문 바로가기</a>
	</div>
	<div id="dkWrap" class="wrap_skin">
		<!-- 카테고리버튼 클릭시 'navi_on' 클래스 부여 -->
		<div id="dkHead" role="banner" class="area_head">
			<h1 class="screen_out">선이의 선선한</h1>
			<button type="button" class="btn_cate">
				<span class="ico_skin ico_cate">카테고리</span>
			</button>
			<div class="area_search ">
				<button type="button" class="btn_search">
					<span class="ico_skin ico_search">검색하기</span>
				</button>
				
					<form action="#" method="get" class="frm_search box_search" onsubmit="try {
    window.location.href = '/search' + '/' + looseURIEncode(document.getElementsByName('search')[0].value);
    document.getElementsByName('search')[0].value = '';
    return false;
} catch (e) {}">
						<fieldset>
							<legend class="screen_out">검색하기</legend>
							<label for="search" class="lab_search screen_out">블로그 내 검색</label>
							<input type="text" name="search" id="search" class="tf_search" placeholder="Search" value="" data-value="">
							<span class="ico_skin ico_search"></span>
						</fieldset>
					</form>
				
			</div>
			<div class="area_profile">
				<div class="tit_post">
					<a href="/" class="link_post">선이의 선선한</a>
				</div>
				<span class="thumb_profile">
                <img src="https://tistory1.daumcdn.net/tistory/5860621/attach/be5dbdc914fc499a92496608a88c022d" class="img_profile" alt="프로필사진">
            </span>
				<span class="txt_profile">선이네 선이</span>
			</div>
		</div>
		<hr class="hide">
		<div id="dkContent" class="cont_skin" role="main">
			<div id="cMain">
				<div id="mFeature" class="wrap_sub">
					<div class="cont_sub">
						<div class="inner_sub">
							<div class="area_sub">
								<div role="navigation" class="area_navi">
									<ul class="tt_category"><li class=""><a href="/category" class="link_tit"> 분류 전체보기 <span class="c_cnt">(72)</span> <img alt="N" src="https://tistory1.daumcdn.net/tistory_admin/blogs/image/category/new_ico_5.gif" style="vertical-align:middle;padding-left:2px;"/></a>
  <ul class="category_list"><li class=""><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%9D%BC%EC%83%81" class="link_item"> 선이의 일상 <span class="c_cnt">(10)</span> <img alt="N" src="https://tistory1.daumcdn.net/tistory_admin/blogs/image/category/new_ico_5.gif" style="vertical-align:middle;padding-left:2px;"/></a></li>
<li class=""><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%97%AC%ED%96%89" class="link_item"> 선이의 여행 <span class="c_cnt">(11)</span> </a></li>
<li class=""><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%9E%90%EB%8F%99%EC%B0%A8" class="link_item"> 선이의 자동차 <span class="c_cnt">(6)</span> </a></li>
<li class=""><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%82%AC%EB%9E%91" class="link_item"> 선이의 사랑 <span class="c_cnt">(3)</span> </a></li>
<li class=""><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%9A%B4%EB%8F%99" class="link_item"> 선이의 운동 <span class="c_cnt">(0)</span> </a></li>
<li class=""><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%A3%BC%EC%9D%B8" class="link_item"> 선이의 주인 <span class="c_cnt">(5)</span> </a></li>
<li class=""><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EB%A8%B9%EB%B0%A9" class="link_item"> 선이의 먹방 <span class="c_cnt">(26)</span> <img alt="N" src="https://tistory1.daumcdn.net/tistory_admin/blogs/image/category/new_ico_5.gif" style="vertical-align:middle;padding-left:2px;"/></a></li>
<li class=""><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%A0%95%EB%B3%B4" class="link_item"> 선이의 정보 <span class="c_cnt">(11)</span> </a></li>
</ul>
</li>
</ul>

									<a href="https://0-0-hs.tistory.com/guestbook" class="link_guestbook">Guestbook</a>
								</div>
								<div class="wrap_etc">
									<div class="col_aside left_side">
										            
												<!-- 최근에 올라온 글 -->
												<div class="box_aside">
													<strong class="tit_aside">Recent Posts</strong>
													<ul class="list_board">
														
															<li><a href="/73" class="link_board">평소에 뭐하고 지내요? 저는 먹기 바쁩니다.</a></li>
														
															<li><a href="/72" class="link_board">머슬카 동호회에서 유명한 돈가스집! 운정 맛집 '⋯</a></li>
														
															<li><a href="/71" class="link_board">파주 문산 5일장에서 먹기만 하고 왔어요.</a></li>
														
															<li><a href="/70" class="link_board">파주 임진각 바로 앞 기차가 지나다니는 카페 ::⋯</a></li>
														
													</ul>
												</div>
											
												<!-- 최근에 달린 댓글 -->
												<div class="box_aside">
													<strong class="tit_aside">Recent Comments</strong>
													<ul class="list_board">
														
															<li><a href="/73#comment14178059" class="link_board">글 잘 읽고 갑니다. 즐거운 저녁 되세요.</a></li>
														
															<li><a href="/73#comment14177823" class="link_board">ㅎㅎㅎ 저도 먹기바쁩니다 인생은 먹는거죠</a></li>
														
															<li><a href="/73#comment14177667" class="link_board">포스팅 잘 보고 하트 남기고 가요~^^</a></li>
														
															<li><a href="/73#comment14177524" class="link_board">저도가끔 배달하면 여기가깨끗한곳인지 의문을가지긴하지만 ⋯</a></li>
														
													</ul>
												</div>
											
												<!-- 공지사항 -->
												
													<div class="box_aside">
														<strong class="tit_aside">Notice</strong>
														<ul class="list_board">
															
														</ul>
													</div>
												
											
												<!-- 링크 -->
												<div class="box_aside">
													<strong class="tit_aside">Link</strong>
													<ul class="list_board">
														
															<li><a href="https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y=" class="link_board" target="_blank">선이의 인스타</a></li>
														
													</ul>
												</div>
											<div class="module module_plugin">        <!-- DaumShow - START -->
        <form action="https://search.daum.net/search" method="get" id="daumSearchBox" target="_blank" style="width:190px"><input type="hidden" name="w" value="tot"/>
  <div id="daumLogo"></div>
<input type="text" name="q" id="show_q" value="검색어" onfocus="this.value=''" style="width:99px"/><input type="submit" id="show_btn" value="검색"/></form>

        <!-- DaumShow - END -->
</div>

									</div>


									<div class="col_aside right_side">
										
												<!-- 달력 -->
												<div class="box_aside box_calendar">
													<table class="tt-calendar" cellpadding="0" cellspacing="1" style="width: 100%; table-layout: fixed">
  <caption class="cal_month"><a href="/archive/202302" title="1개월 앞의 달력을 보여줍니다.">«</a> &nbsp; <a href="/archive/202303" title="현재 달의 달력을 보여줍니다.">2023/03</a> &nbsp; <a href="/archive/202304" title="1개월 뒤의 달력을 보여줍니다.">»</a></caption>
  <thead>
    <tr>
      <th class="cal_week2">일</th>
      <th class="cal_week1">월</th>
      <th class="cal_week1">화</th>
      <th class="cal_week1">수</th>
      <th class="cal_week1">목</th>
      <th class="cal_week1">금</th>
      <th class="cal_week1">토</th>
    </tr>
  </thead>
  <tbody>
    <tr class="cal_week cal_current_week">
      <td class="cal_day1 cal_day2"> </td>
      <td class="cal_day1 cal_day2"> </td>
      <td class="cal_day1 cal_day2"> </td>
      <td class="cal_day cal_day3">1</td>
      <td class="cal_day cal_day3">2</td>
      <td class="cal_day cal_day3">3</td>
      <td class="cal_day cal_day3">4</td>
    </tr>
    <tr class="cal_week">
      <td class="cal_day cal_day3 cal_day_sunday">5</td>
      <td class="cal_day cal_day3"><a href="/archive/20230306" class="cal_click">6</a></td>
      <td class="cal_day cal_day3"><a href="/archive/20230307" class="cal_click">7</a></td>
      <td class="cal_day cal_day3"><a href="/archive/20230308" class="cal_click">8</a></td>
      <td class="cal_day cal_day3"><a href="/archive/20230309" class="cal_click">9</a></td>
      <td class="cal_day cal_day3"><a href="/archive/20230310" class="cal_click">10</a></td>
      <td class="cal_day cal_day3"><a href="/archive/20230311" class="cal_click">11</a></td>
    </tr>
    <tr class="cal_week">
      <td class="cal_day cal_day3 cal_day_sunday"><a href="/archive/20230312" class="cal_click">12</a></td>
      <td class="cal_day cal_day3"><a href="/archive/20230313" class="cal_click">13</a></td>
      <td class="cal_day cal_day3"><a href="/archive/20230314" class="cal_click">14</a></td>
      <td class="cal_day cal_day3"><a href="/archive/20230315" class="cal_click">15</a></td>
      <td class="cal_day cal_day4"><a href="/archive/20230316" class="cal_click">16</a></td>
      <td class="cal_day cal_day3">17</td>
      <td class="cal_day cal_day3">18</td>
    </tr>
    <tr class="cal_week">
      <td class="cal_day cal_day3 cal_day_sunday">19</td>
      <td class="cal_day cal_day3">20</td>
      <td class="cal_day cal_day3">21</td>
      <td class="cal_day cal_day3">22</td>
      <td class="cal_day cal_day3">23</td>
      <td class="cal_day cal_day3">24</td>
      <td class="cal_day cal_day3">25</td>
    </tr>
    <tr class="cal_week">
      <td class="cal_day cal_day3 cal_day_sunday">26</td>
      <td class="cal_day cal_day3">27</td>
      <td class="cal_day cal_day3">28</td>
      <td class="cal_day cal_day3">29</td>
      <td class="cal_day cal_day3">30</td>
      <td class="cal_day cal_day3">31</td>
      <td class="cal_day1 cal_day2"> </td>
    </tr>
  </tbody>
</table>
												</div>
											
												<!-- 태그 클라우드 -->
												<div class="box_aside box_tag">
													<strong class="tit_aside">Tags</strong>
													<ul class="list_tag">
														
															<li><a href="/tag/%EC%9D%BC%EC%82%B0%EB%8D%B0%EC%9D%B4%ED%8A%B8%EC%BD%94%EC%8A%A4" class="link_tag cloud4">일산데이트코스</a></li>
														
															<li><a href="/tag/%EC%9D%BC%EB%B3%B8%EC%97%AC%ED%96%89" class="link_tag cloud3">일본여행</a></li>
														
															<li><a href="/tag/%EC%B9%98%ED%82%A8%EC%B6%94%EC%B2%9C" class="link_tag cloud3">치킨추천</a></li>
														
															<li><a href="/tag/%EA%B9%80%ED%8F%AC%ED%8A%9C%EB%8B%9D%EC%83%B5" class="link_tag cloud4">김포튜닝샵</a></li>
														
															<li><a href="/tag/%EC%97%AC%ED%96%89%EC%97%90%EB%AF%B8%EC%B9%98%EB%8B%A4" class="link_tag cloud4">여행에미치다</a></li>
														
															<li><a href="/tag/%EC%95%BC%EB%8B%B9%EC%97%AD%EC%B9%B4%ED%8E%98" class="link_tag cloud4">야당역카페</a></li>
														
															<li><a href="/tag/%EA%B9%80%ED%8F%AC%EB%9E%A9%ED%95%91" class="link_tag cloud4">김포랩핑</a></li>
														
															<li><a href="/tag/%EC%8A%88%ED%94%84%EB%9D%BC%EC%9D%B4%EC%A6%88" class="link_tag cloud4">슈프라이즈</a></li>
														
															<li><a href="/tag/%EC%9A%B4%EC%A0%95%EC%B9%B4%ED%8E%98%EA%B1%B0%EB%A6%AC" class="link_tag cloud4">운정카페거리</a></li>
														
															<li><a href="/tag/%EC%9A%B4%EC%A0%95%EC%B9%B4%ED%8E%98" class="link_tag cloud2">운정카페</a></li>
														
															<li><a href="/tag/%EC%9A%B4%EC%A0%95%EB%8D%B0%EC%9D%B4%ED%8A%B8" class="link_tag cloud4">운정데이트</a></li>
														
															<li><a href="/tag/%EC%9D%BC%EC%82%B0%EB%A7%9B%EC%A7%91" class="link_tag cloud4">일산맛집</a></li>
														
															<li><a href="/tag/%EC%9A%B4%EC%A0%95%EB%8D%B0%EC%9D%B4%ED%8A%B8%EC%BD%94%EC%8A%A4" class="link_tag cloud4">운정데이트코스</a></li>
														
															<li><a href="/tag/%EA%B9%80%ED%8F%AC%EC%B9%B4%ED%8E%98" class="link_tag cloud3">김포카페</a></li>
														
															<li><a href="/tag/%ED%99%8D%EB%8C%80%EB%82%98%EB%B4%89%EB%A7%9D%EA%B3%A0" class="link_tag cloud3">홍대나봉망고</a></li>
														
															<li><a href="/tag/%EA%B9%80%ED%8F%AC%EB%AC%B4%EC%9D%B8%EC%B9%B4%ED%8E%98" class="link_tag cloud4">김포무인카페</a></li>
														
															<li><a href="/tag/%ED%8C%8C%EC%A3%BC%EB%A7%9B%EC%A7%91" class="link_tag cloud2">파주맛집</a></li>
														
															<li><a href="/tag/%EA%B3%A0%EC%96%91%EC%9D%B4" class="link_tag cloud4">고양이</a></li>
														
															<li><a href="/tag/%EC%9A%B4%EC%A0%95%EB%A7%9B%EC%A7%91" class="link_tag cloud2">운정맛집</a></li>
														
															<li><a href="/tag/%EB%82%98%EC%9D%B4%ED%82%A4" class="link_tag cloud4">나이키</a></li>
														
															<li><a href="/tag/%ED%8C%8C%EC%A3%BC%EC%B9%B4%ED%8E%98" class="link_tag cloud1">파주카페</a></li>
														
															<li><a href="/tag/%EC%9A%B4%EC%A0%95%ED%8C%8C%EC%8A%A4%ED%83%80%EB%A7%9B%EC%A7%91" class="link_tag cloud4">운정파스타맛집</a></li>
														
															<li><a href="/tag/%EC%95%BC%EB%8B%B9%EC%97%AD" class="link_tag cloud3">야당역</a></li>
														
															<li><a href="/tag/%EB%8D%94%EB%B8%94%EB%9E%99%EC%89%BD" class="link_tag cloud4">더블랙쉽</a></li>
														
															<li><a href="/tag/%EB%8F%84%EC%BF%84%EC%97%AC%ED%96%89" class="link_tag cloud3">도쿄여행</a></li>
														
															<li><a href="/tag/%EC%9D%B4%EA%B0%80%EB%9E%A9" class="link_tag cloud4">이가랩</a></li>
														
															<li><a href="/tag/%EC%8B%A0%EC%A3%BC%EC%BF%A0" class="link_tag cloud3">신주쿠</a></li>
														
															<li><a href="/tag/%EA%B9%80%ED%8F%AC%EB%8D%B0%EC%9D%B4%ED%8A%B8" class="link_tag cloud4">김포데이트</a></li>
														
															<li><a href="/tag/%EA%B9%80%ED%8F%AC%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C" class="link_tag cloud3">김포드라이브</a></li>
														
															<li><a href="/tag/%ED%9B%84%EC%A7%80%EC%99%80%EB%9D%BC%EB%91%90%EB%B6%80%EA%B0%80%EA%B2%8C" class="link_tag cloud3">후지와라두부가게</a></li>
														
													</ul>
													<a href="https://0-0-hs.tistory.com/tag" class="link_more">more</a>
												</div>
											
												<!-- 글 보관함 -->
												<div class="box_aside box_archive">
													<strong class="tit_aside">Archives</strong>
													<ul class="list_keep">
														
															<li><a href="/archive/202303" class="link_keep">2023/03</a> (12)</li>
														
															<li><a href="/archive/202302" class="link_keep">2023/02</a> (27)</li>
														
															<li><a href="/archive/202301" class="link_keep">2023/01</a> (20)</li>
														
															<li><a href="/archive/202212" class="link_keep">2022/12</a> (13)</li>
														
													</ul>
												</div>
											
												<!-- 방문자수 -->
												<div class="box_aside box_visitor">
													<dl class="list_visitor">
														<dt>Today</dt>
														<dd>156</dd>
													</dl>
													<dl class="list_total">
														<dt>Total</dt>
														<dd>20,903</dd>
													</dl>
												</div>
											
									</div>
								</div>
							</div>
						</div>
						<button type="button" class="ico_skin btn_close">닫기</button>

						<strong class="screen_out">관리 메뉴</strong>
						<ul class="list_control">
							<li><a href="https://0-0-hs.tistory.com/manage/entry/post" class="ico_skin link_write" title="글쓰기">글쓰기</a></li>
							<li><a href="https://0-0-hs.tistory.com/guestbook" class="ico_skin link_memo" title="방명록">방명록</a></li>
							<li><a href="https://0-0-hs.tistory.com/rss" class="ico_skin link_rss" title="RSS">RSS</a></li>
							<li><a href="https://0-0-hs.tistory.com/manage" class="ico_skin link_manage" title="관리">관리</a></li>
						</ul>
					</div>
				</div>

				<div id="mArticle" class="article_skin">

					

					<div class="index_title">
						<h2 class="tit_skin"><span class="txt_title">선이의 선선한</span></h2>
					</div>

					           
               
	


	
		<h2 id="dkBody" class="screen_out">티스토리 첫 번째 포스팅 _ 선이의 일상 본문</h2>
		<div class="area_title">
			<strong class="tit_category"><a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%9D%BC%EC%83%81">선이의 일상</a></strong>
			<h3 class="tit_post">티스토리 첫 번째 포스팅 _ 선이의 일상</h3>
			<span class="info_post">선이네 선이
                           <span class="txt_bar"></span>2022. 12. 20. 12:04
			
		</span>
		</div>

		<div class="area_view">
			                    <!-- System - START -->
        <div class="revenue_unit_wrap">
  <div class="revenue_unit_item adfit">
    <div class="revenue_unit_info">728x90</div>
    <ins class="kakao_ad_area" style="display: none;" data-ad-unit="DAN-nPubw11jpVXC9WB5" data-ad-width="728px" data-ad-height="90px"></ins>
    <script type="text/javascript" src="//t1.daumcdn.net/kas/static/ba.min.js" async="async"></script>
  </div>
</div>
        <!-- System - END -->

            <div class="tt_article_useless_p_margin contents_style"><p data-ke-size="size16">&nbsp;안녕 ㅇㄴㅁㅁ 나는 선이에요 블로그는 나랑 안맞다고 생각했는데 요즘 인스타 권태기와서 넘 하기 싫구 -ㅅ -&nbsp; &nbsp;</p>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16">티스토리 아가로 시작해볼거에요 구독과 댓글 좋아요 (유튭아님) 많이 부탁해요 !&nbsp;</p>
<figure contenteditable="false" data-ke-type="emoticon" data-ke-align="alignCenter" data-emoticon-type="friends1" data-emoticon-name="010" data-emoticon-isanimation="false" data-emoticon-src="https://t1.daumcdn.net/keditor/emoticon/friends1/large/010.gif"><img src="https://t1.daumcdn.net/keditor/emoticon/friends1/large/010.gif" width="150" /></figure>
<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style3" />
<p data-ke-size="size16"><a title="선이의 인스타" href="https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y=" target="_blank" rel="noopener">선이의 인스타 : https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y=</a></p>
<figure id="og_1671505175835" contenteditable="false" data-ke-type="opengraph" data-ke-align="alignCenter" data-og-type="instapp:photo" data-og-title="Instagram의 류 혜선님 : &quot;@showkingcar_official 🚕&quot;" data-og-description="류 혜선님이 Instagram에 게시물을 공유했습니다:&quot;@showkingcar_official 🚕&quot;. 계정을 팔로우하여 게시물 196개를 확인해보세요." data-og-host="www.instagram.com" data-og-source-url="https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y=" data-og-url="https://www.instagram.com/p/CiUq5mTL189/" data-og-image="https://scrap.kakaocdn.net/dn/LphWE/hyQWsEVymW/qYZ5QZ1Mrd6YaKHnzz0KJk/img.jpg?width=623&amp;height=640&amp;face=0_0_623_640,https://scrap.kakaocdn.net/dn/iRhkO/hyQWskDfry/0vzTEVnacPkJPFyC4SpNh1/img.jpg?width=623&amp;height=640&amp;face=0_0_623_640"><a href="https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y=" target="_blank" rel="noopener" data-source-url="https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y=">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/LphWE/hyQWsEVymW/qYZ5QZ1Mrd6YaKHnzz0KJk/img.jpg?width=623&amp;height=640&amp;face=0_0_623_640,https://scrap.kakaocdn.net/dn/iRhkO/hyQWskDfry/0vzTEVnacPkJPFyC4SpNh1/img.jpg?width=623&amp;height=640&amp;face=0_0_623_640');">&nbsp;</div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">Instagram의 류 혜선님 : "@showkingcar_official 🚕"</p>
<p class="og-desc" data-ke-size="size16">류 혜선님이 Instagram에 게시물을 공유했습니다:"@showkingcar_official 🚕". 계정을 팔로우하여 게시물 196개를 확인해보세요.</p>
<p class="og-host" data-ke-size="size16">www.instagram.com</p>
</div>
</a></figure>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16"><a title="선이의 카카오톡" href="https://open.kakao.com/o/sc4RjOLd" target="_blank" rel="noopener">선이의 카카오톡 https://open.kakao.com/o/sc4RjOLd</a></p>
<figure id="og_1671505195920" contenteditable="false" data-ke-type="opengraph" data-ke-align="alignCenter" data-og-type="website" data-og-title="0_0_hs님의 오픈프로필" data-og-description="" data-og-host="open.kakao.com" data-og-source-url="https://open.kakao.com/o/sc4RjOLd" data-og-url="https://open.kakao.com/o/sc4RjOLd" data-og-image="https://scrap.kakaocdn.net/dn/naMOb/hyQWInttna/0Ovu1v9NhRbmoSbUcUHw81/img.jpg?width=1200&amp;height=628&amp;face=0_0_1200_628"><a href="https://open.kakao.com/o/sc4RjOLd" target="_blank" rel="noopener" data-source-url="https://open.kakao.com/o/sc4RjOLd">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/naMOb/hyQWInttna/0Ovu1v9NhRbmoSbUcUHw81/img.jpg?width=1200&amp;height=628&amp;face=0_0_1200_628');">&nbsp;</div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">0_0_hs님의 오픈프로필</p>
<p class="og-desc" data-ke-size="size16">&nbsp;</p>
<p class="og-host" data-ke-size="size16">open.kakao.com</p>
</div>
</a></figure>
<p data-ke-size="size16">&nbsp;</p></div>
                    <!-- System - START -->
        <div class="revenue_unit_wrap">
  <div class="revenue_unit_item adfit">
    <div class="revenue_unit_info">728x90</div>
    <ins class="kakao_ad_area" style="display: none;" data-ad-unit="DAN-2fwvsVChfh9hZPyo" data-ad-width="728px" data-ad-height="90px"></ins>
    <script type="text/javascript" src="//t1.daumcdn.net/kas/static/ba.min.js" async="async"></script>
  </div>
</div>
        <!-- System - END -->

                                        <div class="container_postbtn #post_button_group">
  <div class="postbtn_like"><script>window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//0-0-hs.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 2
}</script>
<div class="wrap_btn" id="reaction-2"></div>
<script src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/script/reaction-button-container.min.js"></script><div class="wrap_btn wrap_btn_share"><button type="button" class="btn_post sns_btn btn_share" aria-expanded="false" data-thumbnail-url="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fwet1I%2FbtrT8qwzqLU%2FrhasOYqjpWNX2amQ230FgK%2Fimg.jpg" data-title="티스토리 첫 번째 포스팅 _ 선이의 일상" data-description="안녕 ㅇㄴㅁㅁ 나는 선이에요 블로그는 나랑 안맞다고 생각했는데 요즘 인스타 권태기와서 넘 하기 싫구 -ㅅ - 티스토리 아가로 시작해볼거에요 구독과 댓글 좋아요 (유튭아님) 많이 부탁해요 ! 선이의 인스타 : https://www.instagram.com/p/CiUq5mTL189/?igshid=YmMyMTA2M2Y= Instagram의 류 혜선님 : &quot;@showkingcar_official 🚕&quot; 류 혜선님이 Instagram에 게시물을 공유했습니다:&quot;@showkingcar_official 🚕&quot;. 계정을 팔로우하여 게시물 196개를 확인해보세요. www.instagram.com 선이의 카카오톡 https://open.kakao.com/o/sc4RjOLd 0_0_hs님의 오픈프로필 open.kakao.com" data-profile-image="https://tistory1.daumcdn.net/tistory/5860621/attach/be5dbdc914fc499a92496608a88c022d" data-profile-name="선이네 선이" data-pc-url="https://0-0-hs.tistory.com/2" data-relative-pc-url="/2" data-blog-title="선이의 선선한"><span class="ico_postbtn ico_share">공유하기</span></button>
  <div class="layer_post" id="tistorySnsLayer"></div>
</div><div class="wrap_btn wrap_btn_etc" data-entry-id="2" data-entry-visibility="public" data-category-visibility="public"><button type="button" class="btn_post btn_etc2" aria-expanded="false"><span class="ico_postbtn ico_etc">게시글 관리</span></button>
  <div class="layer_post" id="tistoryEtcLayer"></div>
</div></div>
<button type="button" class="btn_menu_toolbar btn_subscription  #subscribe" data-blog-id="5860621" data-url="https://0-0-hs.tistory.com/2" data-device="web_pc"><em class="txt_state">구독하기</em><strong class="txt_tool_id">선이의 선선한</strong><span class="img_common_tistory ico_check_type1"></span></button></div>

                            <!-- A_ShareEntryWithSNS - START -->
        <div class="tt-plugin tt-share-entry-with-sns tt-sns-icon-alignment-center tt-sns-icon-size-big">
  <div class="tt-sns-wrap" id="ttSnsWrap-2">
    <ul class="tt-sns-service-default">
      <li class="tt-sns-service-kakaostory"><a href="javascript:;" onclick="ShareEntryWithSNS.share(`kakaostory`, `2`, `티스토리 첫 번째 포스팅 _ 선이의 일상`, `https://0-0-hs.tistory.com/2`, false);">카카오스토리</a></li>
      <li class="tt-sns-service-twitter"><a href="javascript:;" onclick="ShareEntryWithSNS.share(`twitter`, `2`, `티스토리 첫 번째 포스팅 _ 선이의 일상`, `https://0-0-hs.tistory.com/2`, false);">트위터</a></li>
      <li class="tt-sns-service-facebook"><a href="javascript:;" onclick="ShareEntryWithSNS.share(`facebook`, `2`, `티스토리 첫 번째 포스팅 _ 선이의 일상`, `https://0-0-hs.tistory.com/2`, false);">페이스북</a></li>
    </ul>
  </div>
  <div class="tt-sns-clear"></div>
</div>

        <!-- A_ShareEntryWithSNS - END -->

                    <!-- PostListinCategory - START -->
<div class="another_category another_category_color_gray">
  <h4>'<a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%9D%BC%EC%83%81">선이의 일상</a>' 카테고리의 다른 글</h4>
  <table>
    <tr>
      <th><a href="/26">동생 생일 트렁크 이벤트 그리고 디올 스니커즈 선물</a>&nbsp;&nbsp;<span>(9)</span></th>
      <td>2023.01.14</td>
    </tr>
    <tr>
      <th><a href="/12">크리스마스파티 2탄 내 사랑들과 연말파티 _ 선이의 일상</a>&nbsp;&nbsp;<span>(7)</span></th>
      <td>2022.12.28</td>
    </tr>
    <tr>
      <th><a href="/11">크리스마스파티 1탄 공.연.파 (공주들의 연말 파티)_ 선이의 일상</a>&nbsp;&nbsp;<span>(9)</span></th>
      <td>2022.12.27</td>
    </tr>
    <tr>
      <th><a href="/10">[일상] 잔망스러운 선이의 일상 12월23일 퇴근 - 12월24일 크리스마스 이브</a>&nbsp;&nbsp;<span>(14)</span></th>
      <td>2022.12.27</td>
    </tr>
    <tr>
      <th><a href="/4">[일상] 12월20일 퇴근 그리고 12월21일 출근 _ 선이의 일상</a>&nbsp;&nbsp;<span>(12)</span></th>
      <td>2022.12.21</td>
    </tr>
  </table>
</div>

<!-- PostListinCategory - END -->

		</div>
		<div class="area_etc">
			
				<dl class="list_tag">
					<dt>Tag</dt>
					<dd><a href="/tag/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C" rel="tag">드라이브</a>, <a href="/tag/%EC%97%AC%ED%96%89" rel="tag">여행</a>, <a href="/tag/%EC%9D%B8%EC%8A%A4%ED%83%80" rel="tag">인스타</a>, <a href="/tag/%EC%9D%BC%EC%83%81" rel="tag">일상</a>, <a href="/tag/%EC%9E%90%EB%8F%99%EC%B0%A8" rel="tag">자동차</a>, <a href="/tag/%EC%A2%8B%EC%95%84%EC%9A%94" rel="tag">좋아요</a>, <a href="/tag/%EC%A3%BC%EB%A7%90" rel="tag">주말</a>, <a href="/tag/%EC%B6%9C%EA%B7%BC" rel="tag">출근</a>, <a href="/tag/%ED%8A%9C%EB%8B%9D%EC%B9%B4" rel="tag">튜닝카</a>, <a href="/tag/%ED%8B%B0%EC%8A%A4%ED%86%A0%EB%A6%AC" rel="tag">티스토리</a></dd>
				</dl>
			
		</div>

		
			<div class="area_related">
				<strong class="tit_related">'선이의 일상' Related Articles</strong>
				<ul class="list_related">
					
						<li class="thumb_type">
							<a href="/12?category=1068876" class="link_related">
								
								<span class="thumb_related">
									<img src="//i1.daumcdn.net/thumb/C185x200/?fname=https://img1.daumcdn.net/thumb/R750x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F1Vvl7%2FbtrUM5FxIg1%2FgJyRXnMAfbPpoSheXdfKak%2Fimg.jpg" class="img_related" alt="">
								</span>
								
								<span class="txt_related">크리스마스파티 2탄 내 사랑들과 연말파티 _ 선이의 일상</span>
								<span class="date_related">2022.12.28</span>
								<span class="frame_related"></span>
							</a>
						</li>
					
						<li class="thumb_type">
							<a href="/11?category=1068876" class="link_related">
								
								<span class="thumb_related">
									<img src="//i1.daumcdn.net/thumb/C185x200/?fname=https://img1.daumcdn.net/thumb/R750x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb36lWc%2FbtrUNqvRoYS%2FBPZWHFKO1Oo8XczgLVRigk%2Fimg.jpg" class="img_related" alt="">
								</span>
								
								<span class="txt_related">크리스마스파티 1탄 공.연.파 (공주들의 연말 파티)_ 선이의 일상</span>
								<span class="date_related">2022.12.27</span>
								<span class="frame_related"></span>
							</a>
						</li>
					
						<li class="thumb_type">
							<a href="/10?category=1068876" class="link_related">
								
								<span class="thumb_related">
									<img src="//i1.daumcdn.net/thumb/C185x200/?fname=https://img1.daumcdn.net/thumb/R750x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Flvvk6%2FbtrUDhnC4Le%2FF9BaiqPrlCKcq70q3ikSj1%2Fimg.jpg" class="img_related" alt="">
								</span>
								
								<span class="txt_related">[일상] 잔망스러운 선이의 일상 12월23일 퇴근 - 12월24일 크리스마스 이브</span>
								<span class="date_related">2022.12.27</span>
								<span class="frame_related"></span>
							</a>
						</li>
					
						<li class="thumb_type">
							<a href="/4?category=1068876" class="link_related">
								
								<span class="thumb_related">
									<img src="//i1.daumcdn.net/thumb/C185x200/?fname=https://img1.daumcdn.net/thumb/R750x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAN17N%2FbtrT80zMaHJ%2FEQYXiX8vNNKTucKhaGdMVK%2Fimg.jpg" class="img_related" alt="">
								</span>
								
								<span class="txt_related">[일상] 12월20일 퇴근 그리고 12월21일 출근 _ 선이의 일상</span>
								<span class="date_related">2022.12.21</span>
								<span class="frame_related"></span>
							</a>
						</li>
					
				</ul>
				<a href="/category/%EC%84%A0%EC%9D%B4%EC%9D%98%20%EC%9D%BC%EC%83%81" class="link_more">more</a>
			</div>
		

		<div class="area_reply">
			<strong class="tit_reply" onclick=""><span id="commentCount2_0">4</span>  Comments</strong>
			<div id="entry2Comment">
				
					<ul class="list_reply">
						            

            <li id="none_display_division_for_comment_list_2" style="display: none;"></li>
<script type="text/javascript">
    setInitialEntryComments(2, 1678959714)
</script>

					</ul>
				

				       <form method="post" action="/comment/add/2" onsubmit="return false" style="margin: 0">
           
<fieldset class="fld_reply">
	<legend class="screen_out">댓글쓰기 폼</legend>
	
		
		<div class="writer_check">
                                      <span class="check_secret ">
                                          <input type="checkbox" name="secret" id="secret" class="inp_secret" tabindex="4">
                                          <label for="secret" class="lab_secret">
                                              <span class="ico_skin ico_check"></span>
                                              Secret
                                          </label>
                                      </span>
		</div>
	

	<div class="reply_write ">
		<label for="comment" class="lab_write screen_out">댓글</label>
		<textarea name="comment" id="comment" class="tf_reply" placeholder="여러분의 소중한 댓글을 입력해주세요" tabindex="3"></textarea>
	</div>

	<div class="writer_btn">
		<button type="submit" class="btn_enter" onclick="addComment(this, 2); return false;" tabindex="5">Send</button>
	</div>
</fieldset>

       </form>
			</div>
<script type="text/javascript">loadedComments[2]=true;
findFragmentAndHighlight(2);</script>

		</div>


	

               
           

					

					

					

					

					

					
				</div>
			</div>
		</div>
		<hr class="hide">
		<div id="dkFoot" role="contentinfo" class="area_foot">
			<small class="info_copyright">
				Blog is powered by
				<a href="http://www.kakaocorp.com" class="emph_t" target="_blank">kakao</a> / Designed by
				<a href="http://www.tistory.com" class="emph_t" target="_blank">Tistory</a>
			</small>
		</div>
	</div>



<script src="https://tistory1.daumcdn.net/tistory/5860621/skin/images/script.js?_version_=1675125350"></script>
<div class="#menubar menu_toolbar ">
  <h2 class="screen_out">티스토리툴바</h2>
<div class="btn_tool btn_tool_type1" id="menubar_wrapper"></div><div class="btn_tool"><button class="btn_menu_toolbar btn_subscription  #subscribe" data-blog-id="5860621" data-url="https://0-0-hs.tistory.com" data-device="web_pc"><strong class="txt_tool_id">선이의 선선한</strong><em class="txt_state">구독하기</em><span class="img_common_tistory ico_check_type1"></span></button></div></div>
<iframe id="editEntry" style="position:absolute;width:1px;height:1px;left:-100px;top:-100px" src="//0-0-hs.tistory.com/api"></iframe>

                        <!-- CallBack - START -->
        <script>                (function () { 
                    var blogTitle = '선이의 선선한';
                    
                    (function () {
    function isShortContents () {
        return window.getSelection().toString().length &lt; 30;
    }

    function copyWithSource (event) {
        if (isShortContents()) {
            return;
        }
        var range = window.getSelection().getRangeAt(0);
        var contents = range.cloneContents();
        var temp = document.createElement('div');

        temp.appendChild(contents);

        var url = document.location.href;
        var decodedUrl = decodeURI(url);
        var postfix = ' [' + blogTitle + ':티스토리]';

        event.clipboardData.setData('text/plain', temp.innerText + '\n출처: ' + decodedUrl + postfix);
        event.clipboardData.setData('text/html', '&lt;pre data-ke-type=&quot;codeblock&quot;&gt;' + temp.innerHTML + '&lt;/pre&gt;' + '출처: &lt;a href=&quot;' + url + '&quot;&gt;' + decodedUrl + '&lt;/a&gt;' + postfix);
        event.preventDefault();
    }

    document.addEventListener('copy', copyWithSource);
})()

                })()</script>

        <!-- CallBack - END -->

<!-- DragSearchHandler - START -->
<script src="//search1.daumcdn.net/search/statics/common/js/g/search_dragselection.min.js"></script>

<!-- DragSearchHandler - END -->

<!-- RainbowLink - START -->
<script type="text/javascript" src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/plugin/RainbowLink/script.js"></script>

<!-- RainbowLink - END -->

                
                <script>window.tiara = {"svcDomain":"user.tistory.com","section":"글뷰","trackPage":"글뷰_보기","page":"글뷰","key":"5860621-2","customProps":{"userId":"3776385","blogId":"5860621","entryId":"2","role":"user","trackPage":"글뷰_보기","filterTarget":false},"entry":{"entryId":"2","categoryName":"선이의 일상","categoryId":"1068876","author":"5789717","image":"kage@wet1I/btrT8qwzqLU/rhasOYqjpWNX2amQ230FgK","plink":"/2","tags":["드라이브","여행","인스타","일상","자동차","좋아요","주말","출근","튜닝카","티스토리"]},"kakaoAppKey":"3e6ddd834b023f24221217e370daed18","appUserId":"1546050300"}</script>
<script type="text/javascript" src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/script/tiara.min.js"></script>
<script type="text/javascript">(function($) {
    $(document).ready(function() {
        lightbox.options.fadeDuration = 200;
        lightbox.options.resizeDuration = 200;
        lightbox.options.wrapAround = false;
        lightbox.options.albumLabel = "%1 / %2";
    })
})(tjQuery);</script>
<div style="{margin:0; padding:0; border:none; background:none; float:none; clear:none; z-index:0}"></div>
<script type="text/javascript" src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/script/common.js"></script>
<script type="text/javascript">window.roosevelt_params_queue = window.roosevelt_params_queue || [{channel_id: 'dk', channel_label: '{tistory}'}]</script>
<script type="text/javascript" src="//t1.daumcdn.net/midas/rt/dk_bt/roosevelt_dk_bt.js" async="async"></script>
<script type="text/javascript" src="https://tistory1.daumcdn.net/tistory_admin/userblog/userblog-f7981cefc8bf21c73c6955f1339717f674670b63/static/script/menubar.min.js"></script>
<script>            (function (win, doc, src) {
    win.Wpm = win.Wpm || function (name, param) {
        win.Wpm.queue = win.Wpm.queue || [];
        const { queue } = win.Wpm;
        queue.push([name, param]);
    };
    const script = doc.createElement('script');
    script.src = src;
    script.async = 1;
    const [elem] = doc.getElementsByTagName('script');
    elem.parentNode.insertBefore(script, elem);
})(window, document, 'https://t1.kakaocdn.net/malibu_prod/wpm.js');
            const APP_KEY = 'd3cda7e82e6e4144bdc998b8e25f125d';
            Wpm('appKey', APP_KEY);</script>

                </body>

</html>
"""

db= Databases()
db.insertTistoryBlogBody("s", "s", text.replace("%", '')) # 5200은 되고 5500은 안됨

# print(text[5200:5500])
print("done")
