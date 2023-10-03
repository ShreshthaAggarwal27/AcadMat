function validateForm() {
    var itemName = document.getElementById("company").value;
    var itemImage = document.getElementById("images").value;
    var itemCondition = document.getElementById("condition").value;
    var itemAge = document.getElementById("age").value;
    var itemPrice = document.getElementById("price").value;


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
document.getElementById("id_category").addEventListener("change", function(){
    var otherCategory = document.getElementById("otherCategory");
    var category = document.getElementById("id_category").value;
    
    if (category === "Other") {
        otherCategory.style.display = "block";
    } else {
        otherCategory.style.display = "none";
    }
});
    