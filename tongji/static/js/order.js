var selectedOrderId;
function examine() {
    // 获取按钮的ID
    var orderId = event.target.getAttribute('data-order-id');
    selectedOrderId=event.target.getAttribute('data-order-id');
    // 发送AJAX请求到后端，获取订单信息
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/order-details?id=' + orderId, true);
    xhr.onreadystatechange = function() {
       if (xhr.readyState === 4 && xhr.status === 200) {
          var orderDetails = JSON.parse(xhr.responseText);
          var selectedItemsContainer = document.getElementById('selected-items');
          selectedItemsContainer.innerHTML = ''; // 清空内容

          // 解析图片列表
        var imgList = JSON.parse(orderDetails.img);
   
        for (var i = 0; i < imgList.length; i++) {

            var listItem = document.createElement('div');
            listItem.classList.add('item-row');            

            var imageElement = document.createElement('img');
            imageElement.src = "/static/image/" + imgList[i];
            listItem.appendChild(imageElement);

            var idElement = document.createElement('span');
            idElement.textContent = orderDetails.items[i];
            listItem.appendChild(idElement);
            //输出占位符
            var blankElement = document.createElement('span');
            blankElement.textContent = '    x';
            listItem.appendChild(blankElement);

            var numElement = document.createElement('num');
            numElement.textContent = orderDetails.num[i];
            listItem.appendChild(numElement);
            
            selectedItemsContainer.appendChild(listItem);
            
        }

          // 填充订单信息到弹窗中
         //document.getElementById('selected-items').innerHTML = orderDetails.items;
          document.getElementById('total-amount').innerHTML = orderDetails.totalAmount;
          document.getElementById('creatime').innerHTML = orderDetails.times;

          // 显示弹窗
          document.getElementById('overlay').style.display = 'block';
       }
    };
    xhr.send();
 }

 function closeP() {
   // 关闭弹窗

   // 发送AJAX请求到后端
   
   var xhr = new XMLHttpRequest();
   xhr.open('POST', '/define', true);
   xhr.setRequestHeader('Content-Type', 'application/json');

   xhr.onreadystatechange = function() {
       if (xhr.readyState === 4 && xhr.status === 200) {
           // 请求成功,刷新界面
           window.location.reload();
       }
   };

   var data = {
       orderId: selectedOrderId
   };

   xhr.send(JSON.stringify(data));

   document.getElementById('overlay').style.display = 'none';
}
function closeP1() { 
    document.getElementById('overlay').style.display = 'none';
 }