function previewImage(input, previewId) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        document.getElementById(previewId).src = e.target.result;
      }
      reader.readAsDataURL(input.files[0]);
    }
  }
  function submitForm() {
    // 创建FormData对象
    var formData = new FormData();
  
    // 获取图片预览框的img元素和对应的文件输入框
    var fileInput1 = document.getElementById('file-input1');
    var fileInput2 = document.getElementById('file-input2');
    var fileInput3 = document.getElementById('file-input3');
    var fileInput4 = document.getElementById('file-input4');
  
    // 获取输入框的值
    var itemName = document.querySelector('input[name="item-name"]').value;
    var itemSpecies = document.querySelector('input[name="item-species"]').value;
    var itemStock = document.querySelector('input[name="item-stock"]').value;
    var itemPrice = document.querySelector('input[name="item-price"]').value;
    var itemDescription = document.querySelector('textarea[name="item-description"]').value;
  
    // 判断是否选择了图片并将其添加到FormData对象中
    if (fileInput1.files.length > 0) {
      formData.append('image1', fileInput1.files[0]);
    }
    if (fileInput2.files.length > 0) {
      formData.append('image2', fileInput2.files[0]);
    }
    if (fileInput3.files.length > 0) {
      formData.append('image3', fileInput3.files[0]);
    }
    if (fileInput4.files.length > 0) {
        formData.append('image4', fileInput4.files[0]);
    }
  
    // 添加其他字段到FormData对象中
    formData.append('item-name', itemName);
    formData.append('item-species', itemSpecies);
    formData.append('item-stock', itemStock);
    formData.append('item-price', itemPrice);
    formData.append('item-description', itemDescription);
  
    // 发送POST请求给后端
    fetch('/submit', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(result => {
        // 根据后端返回的结果进行处理
        if (result.message === '添加成功') {
          // 显示成功的弹窗
          Swal.fire({
            icon: 'success',
            title: '添加成功',
            showConfirmButton: false,
            timer: 1000 // 2秒后自动关闭弹窗
          }).then(() => {
            // 2秒后返回到manager_product.html页面
            window.location.href = 'templates/manager_product.html';
          });
        } else {
          // 处理其他情况...
        }
      })
      .catch(error => {
        // 处理请求错误
        console.error('Error:', error);
      });
    
      return false; // 阻止表单默认提交行为
  }