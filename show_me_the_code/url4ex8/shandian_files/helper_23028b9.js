define("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper",function(t,e){"use strict";var n=t("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/class"),o=t("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom");e.toInt=function(t){return parseInt(t,10)||0},e.clone=function(t){if(null===t)return null;if("object"==typeof t){var e={};for(var n in t)e[n]=this.clone(t[n]);return e}return t},e.extend=function(t,e){var n=this.clone(t);for(var o in e)n[o]=this.clone(e[o]);return n},e.isEditable=function(t){return o.matches(t,"input,[contenteditable]")||o.matches(t,"select,[contenteditable]")||o.matches(t,"textarea,[contenteditable]")||o.matches(t,"button,[contenteditable]")},e.removePsClasses=function(t){for(var e=n.list(t),o=0;o<e.length;o++){var i=e[o];0===i.indexOf("ps-")&&n.remove(t,i)}},e.outerWidth=function(t){return this.toInt(o.css(t,"width"))+this.toInt(o.css(t,"paddingLeft"))+this.toInt(o.css(t,"paddingRight"))+this.toInt(o.css(t,"borderLeftWidth"))+this.toInt(o.css(t,"borderRightWidth"))},e.startScrolling=function(t,e){n.add(t,"ps-in-scrolling"),"undefined"!=typeof e?n.add(t,"ps-"+e):(n.add(t,"ps-x"),n.add(t,"ps-y"))},e.stopScrolling=function(t,e){n.remove(t,"ps-in-scrolling"),"undefined"!=typeof e?n.remove(t,"ps-"+e):(n.remove(t,"ps-x"),n.remove(t,"ps-y"))},e.env={isWebKit:"WebkitAppearance"in document.documentElement.style,supportsTouch:"ontouchstart"in window||window.DocumentTouch&&document instanceof window.DocumentTouch,supportsIePointer:null!==window.navigator.msMaxTouchPoints}});