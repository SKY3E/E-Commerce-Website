var item_mode = "all";
console.log("Connected...")
console.log(item_mode)

// Main Get Element for All items
document.getElementById("All_Items").onclick = function() {All_Items_func()};

// Sub Get Elements for Specific items
document.getElementById("Meat_Seafood").onclick = function() {Meat_Seafood_func()};
document.getElementById("Bakery").onclick = function() {Bakery_func()};
document.getElementById("Fruits").onclick = function() {Fruits_func()};
document.getElementById("Vegetables").onclick = function() {Vegetables_func()};
document.getElementById("Dairy").onclick = function() {Dairy_func()};

function All_Items_func() {
  item_mode = "all";
  console.log(item_mode);
  Send_Python_Info();
}

function Meat_Seafood_func() {
  item_mode = "meat&seafood";
  console.log(item_mode);
  Send_Python_Info();
}

function Bakery_func() {
  item_mode = "bakery";
  console.log(item_mode);
  Send_Python_Info();
}

function Fruits_func() {
  item_mode = "fruits";
  console.log(item_mode);
  Send_Python_Info();
}

function Vegetables_func() {
  item_mode = "vegetables";
  console.log(item_mode);
  Send_Python_Info();
}

function Dairy_func() {
  item_mode = "dairy";
  console.log(item_mode);
  Send_Python_Info();
}

// Send info to Python File
function Send_Python_Info() {
  ToSend = JSON.stringify(item_mode)
  console.log(ToSend)
  window.alert(ToSend)
  $.ajax({
    url:"/test",
    type:"POST",
    contentType: "application/json",
    data: JSON.stringify(ToSend),
    success: function () {
      alert("Saved!");
    }
  });
}