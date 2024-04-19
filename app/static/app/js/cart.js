var updateBtns = document.getElementsByClassName("update-cart");


for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var producId = this.dataset.product;
    var action = this.dataset.action;
    console.log("producId: ", producId, "action: ", action);
    console.log("user: ", user);
    if (user === "AnonymousUser") {
      // ng chua dang nhap
      console.log("User not logged in");
    } else {
      updateUserOrder(producId, action);
    }
  });
}

function updateUserOrder(producId, action) {
  console.log("User login success");
  var url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({'productId': producId, 'action': action}),

  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data : ", data);
      location.reload();
    });
}
