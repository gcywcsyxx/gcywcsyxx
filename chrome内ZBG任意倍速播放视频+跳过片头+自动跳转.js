

document.querySelector("video").playbackRate=
"14";
function code(){
 document.querySelector("video").playbackRate=
"3.6";

 }

setTimeout( "code()", "1000" )

 
 setInterval(
function () {
    var aElements=document.getElementsByTagName('div');//所有a标签元素
    var aEle=[];//内容矩阵
    
    for(var i=0;i<aElements.length;i++)
    {

        if(aElements[i].getAttribute('class')=='video-content video-ended')//遍历a标签中linkid为3-368的元素，压入内容矩阵
            {

var ab=document.getElementsByTagName('span');//所有a标签元素
    var abc=[];//内容矩阵

                for(var i=0;i<ab.length;i++)
    {
        if(ab[i].getAttribute('class')=='playVideo-ended-a playVideo-ended-next')//遍历a标签中linkid为3-368的元素，压入内容矩阵
            abc.push( ab[i] );
  

    } 
    

            }
    }  
    abc[0].click() 
     },2000) 
































































