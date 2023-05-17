window.onload = function(){
    var username = decodeURI(location.search.split("=")[1]);/* 获取username decodeURI解码，不解会乱码中文*/
    console.log(username) 
    var Words = document.getElementById("words");/* 显示对话 */
    var TalkWords = document.getElementById("talkwords");/* 输入框 */
    var TalkSub = document.getElementById("talksub");/* 发送信息按钮 */
 
    var talksub_img=document.getElementById("talksub_img")/* 发送表情按钮 */
    var image_list = document.getElementById("image_list")/* 获取图片列表 */
    var image_icon=document.getElementById("image_icon")/* 获取表情包图片 */
 
    var title=document.getElementById("title")/* 改变标题 */
    title.innerHTML=username+'私聊房间'
 
    var talk1=document.getElementById("talk1")/* 改变对话 */
    var talk2=document.getElementById("talk2")
    var talk3=document.getElementById("talk3")
    //talk1.innerHTML='12-01 09:53:53 '+username+'说：以后请多关照'
    //talk2.innerHTML='12-01 09:35:06 '+username+'说：大家好'
    talk3.innerHTML='12-01 09:53:53 服务器说：欢迎用户'+username+'光临'
 
    var user=document.getElementById("user")/* 改变用户 */
    user.innerHTML=username
 
    /* 表情包 */
    var image_con=document.getElementsByClassName("image_con")
  /*   console.log(image_con.length) */
  /* 为每个表情包图片绑定点击事件*/
    image_icon.onclick=function(){
        
        for(var i=0;i<image_con.length;i++){
            image_con[i].num=i/* 绑定图片下标，用下标索引图片 */
            image_con[i].onclick=function(){
                x=this.num/* x是下标 1 2 3 */
              /*  console.log(x) */
              /* 点击图片发送显示的 */
               str = '<div class="atalk"><span class="asay">'+username+'说：<img src="static/image/'+(x+1)+'.gif" alt="" class="image_con"></span></div>';
               Words.innerHTML = Words.innerHTML + str;
            }
    
        }
        /* 这里设置表情包框显示余隐藏，一开始我设置隐藏，点击就切换为显示block */
        if(image_list.style.display=="block"){
            image_list.style.display="none"
            console.log(image_con.length)
 
        }else{
            image_list.style.display="block"
        }
 
    }
    
    var talksub_color=document.getElementById("talksub_color")/* 点击切换文字颜色 */
    var talksub_bgcolor=document.getElementById("talksub_bgcolor")/* 点击切换背景颜色 */
    
  
 
 
    talksub_color.onclick=function(){
        var asay=document.getElementsByClassName("asay")
        var txcol=document.getElementById("talksub_color").value
        console.log(asay);
        for(var j=0;j<asay.length;j++){
            asay[j].style.color=txcol
        }
        
 
        
    }
    /* 改变背景颜色 */
   talksub_bgcolor.onclick=function(){
    var bgcol=document.getElementById("talksub_bgcolor").value
    console.log(bgcol)
    Words.style.backgroundColor=bgcol
    } 
 
    
    var back=document.getElementById("back")
    back.onclick=function(){
        window.location.href = ' ./login.html'
    }
    
 
 
    TalkSub.onclick = function(){
        
        //定义空字符串
        var str = "";
        if(TalkWords.value == ""){
             // 消息为空时弹窗
            alert("消息不能为空");
            return;
        }
        
            /* 敏感词过滤 */
            var arr = [/靠/ig,/tmd/ig,/nm/ig,/tm/ig,/他妈的/ig];
            for(var i=0;i<arr.length;i++){
                /*这些if来判断敏感词的个数，i==0就是靠，就一个敏感词，所以就一个*，以此类推*/
                if(i==0){
                    TalkWords.value = TalkWords.value.replace(arr[i],"*");
                }
                if(i==1){
                    TalkWords.value = TalkWords.value.replace(arr[i],"***");
                }
                if(i==2){
                    TalkWords.value = TalkWords.value.replace(arr[i],"**");
                }
                if(i==3){
                    TalkWords.value = TalkWords.value.replace(arr[i],"**");
                }
                if(i==4){
                    TalkWords.value = TalkWords.value.replace(arr[i],"***");
                }
                
            } 
            /* 把输入话语拼接 */
            str = '<div class="atalk"><span class="asay">'+username+'说 :' + TalkWords.value +'</span></div>';
        /* 返回到html显示 */
        Words.innerHTML = Words.innerHTML + str;
        TalkWords.value=""
    }
    
}
 