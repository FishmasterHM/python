var Monkey=Monkey||{};void function(P){var b=window,D=document,x=encodeURIComponent,r=Math,L=parseInt;if(!document.body.getBoundingClientRect){return}var p=[{getPage:function(){var i;String(D.location).replace(/http:\/\/baike\.baidu\.com\/view\/(\d+)\.htm/i,function(Z,aa){i="view-"+aa});return i},postUrl:"http://nsclick.baidu.com/u.gif",product:103,hid:2254,reports:{click:1,refer:1,staytime:1,pv:1}}],F,V=0;while(F=p[V++]){if(F.page=F.getPage()){break}}if(!F){return}var K=[["mousedown","d"],["scroll","s",b],["resize","e",b],["beforeunload","z",b],["unload","z",b],["focusout","o"],["blur","o",b],["focusin","i"],["focus","i",b]],T,f=(b.ALog&&ALog.t&&ALog.t.st)||new Date,s=(b.ALog&&ALog.sid)||(+new Date).toString(36)+(+Math.random().toFixed(8).substr(2)).toString(36),R=0,g=0,d=0,h=0,l,Q=false,N=0,C=0;var J,q={},I={},A="alog-alias",E="alog-action",k="alog-group",a="alog-param";function t(){if(J){return}J={};"AdivBliCaDulEdlFddGspanHtableIbodyJtrKsectionLtdMolNpOarticlePdtQformRimgSh3TinputUasideViWbXthYemZfont".replace(/([A-Z])([a-z]+)/g,function(aa,i,Z){J[J[i]=Z]=i})}function y(ab,aa,ac,Z){if(!ab){return""}var i=(/^[^u]/.test(typeof ab.getAttribute)&&ab.getAttribute(aa))||"";if("#"==i){i="[id]"}else{if("."==i){i="[class]"}}i.replace(/\[([\w-_]+)\]/,function(ae,ad){i=ab.getAttribute(ad)});Z&&(Z.target=ab);return i||(ac&&y(ab.parentNode,aa,1,Z))||""}function m(ab,i,ae){ae&&t();i=i||D.body;if(!ab||ab==i){return""}if(ab.nodeType!=1||/html/i.test(ab.tagName)){return ab.tagName||""}var aa=y(ab,A),ad=1,ac=ab.previousSibling,Z=ab.nodeName.toLowerCase();while(ac){ad+=ac.nodeName==ab.nodeName;ac=ac.previousSibling}aa=(ae&&J[Z]||Z)+(ad<2?"":ad)+(aa&&"("+aa+")");return ab.parentNode==i?aa:m(ab.parentNode,i,ae)+(/^[A-Z]/.test(aa)?"":"-")+aa}function H(Z,i){return m(Z,i,1)}function B(Z,i){return y(Z,E,true,i)}function o(i){return y(i,k,true)}function e(i){return y(i,a)}function U(ab){if(!ab){return}var i=["ts="+X().toString(36)],aa,ac=new Image,Z="alog_img_"+s+(+new Date).toString(36);for(aa in q){if(q[aa]){i.push(aa+"="+x(q[aa]))}}for(aa in ab){if(ab[aa]){i.push(aa+"="+x(ab[aa]))}}v("report",{const_data:q,event_data:ab});i=F.postUrl+"?"+i.join("&");b[Z]=ac;ac.onload=ac.onerror=ac.onabort=function(){b[Z]=ac=ac.onload=ac.onerror=ac.onabort=null};ac.src=i}function M(i,Z){if(!i){return}v("action",{cmd:"action",ac:i,param:Z});U({cmd:"action",ac:i,param:Z})}function w(i,Z){i&&(q[i]=Z)}function z(i,Z){if(!i||typeof Z!="function"){return}I[i]=I[i]||[];I[i].unshift(Z)}function v(ac,ab){var aa=I[ac];if(!aa){return}var Z=aa.length;while(Z--){aa[Z](ab,ac)}}function O(Z,ac){var ab=Z.getBoundingClientRect(),i=S(Z);function aa(ae,ad){return String(+Math.min(r.max(ae/ad,0),1).toFixed(ad<36?1:(ad<351?2:3))).replace(/^0\./g,".")}return[aa(ac[0]-ab.left,i[0]),aa(ac[1]-ab.top,i[1])]}function S(i){var Z=i.getBoundingClientRect();return[L(Z.right-Z.left),L(Z.bottom-Z.top)]}function u(){var Z=S(D.documentElement),i=S(D.body);return[r.max(Z[0],i[0],b.innerWidth||0,D.documentElement.scrollWidth||0),r.max(Z[1],i[1],b.innerHeight||0,D.documentElement.scrollHeight||0)]}function c(){return[r.max(D.documentElement.scrollLeft||0,D.body.scrollLeft||0,(D.defaultView&&D.defaultView.pageXOffset)||0),r.max(D.documentElement.scrollTop||0,D.body.scrollTop||0,(D.defaultView&&D.defaultView.pageYOffset)||0),b.innerWidth||D.documentElement.clientWidth||D.body.clientWidth||0,b.innerHeight||D.documentElement.clientHeight||D.body.clientHeight||0]}function Y(i,Z,aa){if(!i){return}if(i.addEventListener){i.addEventListener(Z,aa,false)}else{if(i.attachEvent){i.attachEvent("on"+Z,aa)}}}function X(){return new Date-f}function W(i){while(i){if(/^(a|button)$/i.test(i.tagName)){return i}i=i.parentNode}}function j(){switch(F.reports.refer){case 1:case true:return D.referrer;case 2:var i=D.referrer;if(!i){return}var Z="";i.replace(/(^\w+:\/\/)?([^\/]+)/,function(ab,aa){Z=aa});if(D.location.host==Z){return D.referrer}return Z}}q={pid:F.pid||241,sid:s,hid:F.hid,page:F.page,ver:5,p:F.product,px:b.screen.width+"*"+b.screen.height,ref:j()};function G(ah,ae){var af=ae.target||ae.srcElement;switch(ah){case"d":if(!af){return}R++;var ag={},Z=W(af),ac=B(af,ag),i="",aj="";if(Z){if(/^a$/i.test(Z.tagName)){if(F.reports.click){i=Z.getAttribute("href",2);if(/^javascript|#/i.test(i)){i=""}}g++}else{d++}if(F.reports.click){aj=Z.innerHTML.replace(/<[^>]*>/g,"")}}else{if(/input/i.test(af.tagName)&&/button|radio|checkbox|submit/i.test(af.type)){Z=af;d++;aj=af.value}}if(/img/i.test(af.tagName)){h++;aj=af.alt||af.title||af.src}if(!Z&&!ac){break}var ad=H(af),ai=o(af),ab=e(ag.target),aa=O(af,[ae.clientX,ae.clientY]);if(F.reports.click){U({xp:ad,g:ai,ac:ac,ep:aa,param:ab,u:String(i).substr(0,200),txt:String(aj).substr(0,30)})}break;case"o":l=X();Q=true;break;case"i":N+=X()-l;l=X();Q=false;break;case"s":case"e":n=c();C=r.max(n[1]+n[3],C);break;case"z":v("close");Q&&(N+=X()-l);F.reports.staytime&&U({cmd:"close",tc:R,lc:g,bc:d,pc:h,pd:C,ft:(X()-N).toString(36),ps:u().join("*")});break}}for(V=0;T=K[V++];){Y(T[2]||D,T[0],(function(i){return function(aa){if(!f){return}G(i,aa);if(i=="z"){f=0;var Z=new Date;while(new Date-Z<100){}return}}})(T[1]))}l=X();var n=c();C=r.max(n[1]+n[3],C);F.reports.pv&&U({cmd:"open",ps:u().join("*")});(function(){var af=35,aa=0,Z=0,ad=0,ac=[["mousedown","d"]];z("close",function(){w("spd",r.ceil(C/af));w("tac",aa);w("inc",Z);w("cic",ad)});for(var ab=0;T=ac[ab++];){Y(T[2]||D,T[0],(function(i){return function(ah){ag(i,ah)}})(T[1]))}function ag(am,al){var ai=al.target||al.srcElement;switch(am){case"d":if(!ai){return}var an=W(ai),ak=ae(ai);if(!ak){return}if(an||/input/i.test(ai.tagName)&&/button|radio|checkbox|submit/i.test(ai.type)||/img/i.test(ai.tagName)){H(ai).indexOf(J.table)!=-1&&aa++;if(an){var i=an.href||"",aq=b.location.pathname,aj=aq.match(/\/view\/(\d+)\.htm/i),ao=aj&&aj[1],ap=i.match(/\/view\/(\d+)\.htm/i),ah=ap&&ap[1];ah&&ao&&ao!=ah&&Z++}if(/img/i.test(ai.tagName)){ad++}}break}}function ae(ah){while(ah){var i=ah.className;if(i&&i.indexOf("main-body")!=-1){return true}ah=ah.parentNode}return false}})()}(Monkey);var Hunter=Hunter||{};Hunter.userConfig = Hunter.userConfig || [];Hunter.userConfig.push({hid:(function(){var c,d,e,a={qq:[16413,16414],"%u767E%u5EA6%u5F71%u97F3":[16416,16418],"%u795E%u5E99%u9003%u4EA12":[16417,16420],"%u9177%u72D7%u97F3%u4E50":[16415,16419]},b=document.getElementById("word");return b&&(c=escape(b.value.toLowerCase()),d=a[c]||null,d&&(e=d[0],document.getElementById("appDownloadLemmaWrap")&&(e=d[1]))),e})()});Hunter.userConfig.push({hid:(function(){var c,d,e,a={"%u5BD2%u6218":[null,16445,16444],"%u5931%u604B33%u5929":[null,16442,16449],"x%u5973%u7279%u5DE5":[null,16446,16447],"%u767E%u5E74%u9057%u4EA7":[null,16443,16448]},b=document.getElementById("word");return b&&(c=escape(b.value.toLowerCase()),d=a[c]||null,d&&(e=d[0],document.getElementById("shipinLemmaInContent")&&(e=d[1]),document.getElementById("shipinLemmaWrap")&&(e=d[2]))),e})()});Hunter.userConfig.push({hid:(function(){var g,h,i,a={"baike\\.baidu\\.com\\/edit\\/\\d+\\?isnew=1":16454},b=document.location,c=b.hostname,d=b.port,e=b.pathname,f=b.search;if(""!==d&&(d=":"+d),h=c+d+e+f,"baike.baidu.com"===c){for(var j in a)i=RegExp(j),i.test(h)&&(g=a[j]);return g}})()});