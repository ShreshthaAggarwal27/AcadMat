function validateForm() {
    var bookName = document.getElementById("bookName").value;
        var price = document.getElementById("price").value;
        var giverName = document.getElementById("giverName").value;
        var contactInfo = document.getElementById("contactInfo").value;
        var location = document.getElementById("location").value;
        var condition = document.querySelector('input[name="condition"]:checked');

        var isValid = true;

        if (bookName === "") {
            alert("Please enter the name of the book.");
            isValid = false;
        }

        if (price === "") {
            alert("Please enter the price of the book.");
            isValid = false;
        }

        if (giverName === "") {
            alert("Please enter your name.");
            isValid = false;
        }

        if (contactInfo === "") {
            alert("Please enter your contact info.");
            isValid = false;
        }

        if (location === "") {
            alert("Please enter your location.");
            isValid = false;
        }

        if (!condition) {
            alert("Please select the condition of the book.");
            isValid = false;
        }

        return isValid;
    }
function displayImage(input) {
    var imagePreview = document.getElementById("imagePreview");
    imagePreview.innerHTML = "";

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var img = document.createElement("img");
            img.src = e.target.result;
            img.style.maxWidth = "100px";
            imagePreview.appendChild(img);
        };
        reader.readAsDataURL(input.files[0]);
    }
}
document.getElementById("category").addEventListener("change", function () {
    var otherCategory = document.getElementById("otherCategory");
    var category = document.getElementById("category").value;
    
    if (category === "Other") {
        otherCategory.style.display = "block";
    } else {
        otherCategory.style.display = "none";
    }
});