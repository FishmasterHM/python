define("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/drag-scrollbar",function(e,o,t){"use strict";function n(e,o){function t(t){var l=n+t*o.railXRatio,r=Math.max(0,o.scrollbarXRail.getBoundingClientRect().left)+o.railXRatio*(o.railXWidth-o.scrollbarXWidth);o.scrollbarXLeft=0>l?0:l>r?r:l;var a=i.toInt(o.scrollbarXLeft*(o.contentWidth-o.containerWidth)/(o.containerWidth-o.railXRatio*o.scrollbarXWidth))-o.negativeScrollAdjustment;s(e,"left",a)}var n=null,l=null,a=function(o){t(o.pageX-l),c(e),o.stopPropagation(),o.preventDefault()},u=function(){i.stopScrolling(e,"x"),o.event.unbind(o.ownerDocument,"mousemove",a)};o.event.bind(o.scrollbarX,"mousedown",function(t){l=t.pageX,n=i.toInt(r.css(o.scrollbarX,"left"))*o.railXRatio,i.startScrolling(e,"x"),o.event.bind(o.ownerDocument,"mousemove",a),o.event.once(o.ownerDocument,"mouseup",u),t.stopPropagation(),t.preventDefault()})}function l(e,o){function t(t){var l=n+t*o.railYRatio,r=Math.max(0,o.scrollbarYRail.getBoundingClientRect().top)+o.railYRatio*(o.railYHeight-o.scrollbarYHeight);o.scrollbarYTop=0>l?0:l>r?r:l;var a=i.toInt(o.scrollbarYTop*(o.contentHeight-o.containerHeight)/(o.containerHeight-o.railYRatio*o.scrollbarYHeight));s(e,"top",a)}var n=null,l=null,a=function(o){t(o.pageY-l),c(e),o.stopPropagation(),o.preventDefault()},u=function(){i.stopScrolling(e,"y"),o.event.unbind(o.ownerDocument,"mousemove",a)};o.event.bind(o.scrollbarY,"mousedown",function(t){l=t.pageY,n=i.toInt(r.css(o.scrollbarY,"top"))*o.railYRatio,i.startScrolling(e,"y"),o.event.bind(o.ownerDocument,"mousemove",a),o.event.once(o.ownerDocument,"mouseup",u),t.stopPropagation(),t.preventDefault()})}var r=e("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom"),i=e("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper"),a=e("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances"),c=e("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry"),s=e("wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll");t.exports=function(e){var o=a.get(e);n(e,o),l(e,o)}});