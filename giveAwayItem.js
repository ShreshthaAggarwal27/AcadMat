function validateForm() {
    var itemName = document.getElementById("itemName").value;
    var itemImage = document.getElementById("itemImage").value;
    var itemCondition = document.getElementById("itemCondition").value;
    var itemAge = document.getElementById("itemAge").value;
    var itemPrice = document.getElementById("itemPrice").value;
    var giverName = document.getElementById("giverName").value;
    var mobileNumber = document.getElementById("mobileNumber").value;
    var email = document.getElementById("email").value;
    var location = document.getElementById("location").value;

    var isValid = true;

    if (itemName === "") {
        alert("Please enter the name of the item.");
        isValid = false;
    }

    if (itemImage === "") {
        alert("Please upload an image of the item.");
        isValid = false;
    }

    if (itemCondition === "") {
        alert("Please select the condition of the item.");
        isValid = false;
    }

    if (itemAge === "") {
        alert("Please enter the age group for the item.");
        isValid = false;
    }

    if (itemPrice === "") {
        alert("Please enter the price of the item.");
        isValid = false;
    }

    if (giverName === "") {
        alert("Please enter your name.");
        isValid = false;
    }

    if (mobileNumber === "") {
        alert("Please enter your mobile number.");
        isValid = false;
    }

    if (email === "") {
        alert("Please enter your email.");
        isValid = false;
    }

    if (location === "") {
        alert("Please enter your location.");
        isValid = false;
    }

    return isValid;
}

function displayImage(input) {
    var itemImagePreview = document.getElementById("itemImagePreview");
    itemImagePreview.innerHTML = "";

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var img = document.createElement("img");
            img.src = e.target.result;
            img.style.maxWidth = "100px";
            itemImagePreview.appendChild(img);
        };
        reader.readAsDataURL(input.files[0]);
    }
}
document.getElementById("itemCategory").addEventListener("change", function () {
    var otherCategory = document.getElementById("otherCategory");
    var category = document.getElementById("itemCategory").value;
    
    if (category === "other") {
        otherCategory.style.display = "block";
    } else {
        otherCategory.style.display = "none";
    }
});