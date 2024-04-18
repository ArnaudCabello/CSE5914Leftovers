// script.js
var ingredients = new Array();

function addIngredient(event) {
    if (event.key === 'Enter') {
        var input = document.getElementById('ingredients');
        var ingredient = input.value.trim();
        ingredients.push(ingredient);
        if (ingredient !== '') {
            var list = document.getElementById('ingredients-list');
            var listItem = document.createElement('li');
            listItem.textContent = ingredient;
            listItem.classList.add('list-group-item'); // Add a class to newly created list item
            listItem.classList.add('list-group-item-action');
            list.appendChild(listItem);
            input.value = ''; // Clear input field
            attachRemoveEventListener(listItem); // Attach event listener to the newly created list item
        }
    }
}

function attachRemoveEventListener(item) {
    item.addEventListener('click', function() {
        this.parentNode.removeChild(this); // Remove the clicked item from HTML
        // Find the index of the clicked item in the ingredients array
        const index = ingredients.indexOf(item.textContent);
        // If the item is found, remove it from the array
        if (index !== -1) {
            ingredients.splice(index, 1);

        }
    });
}


function clearIngredients() {
    var list = document.getElementById('ingredients-list');
    list.innerHTML = ''; // Remove all list items
    ingredients = new Array();
}

function generateRecipes() {
    // You can redirect to the results page here
    var filters = new Array();
    if(document.getElementById('glutenFreeCheckbox').checked){
        filters.push("gluten-free")
    }
    if(document.getElementById('dairyFreeCheckbox').checked){
        filters.push("dairy-free")
    }

    var rootPath = '/results';
    var query = '?q=';
    var ingredientsList = ingredients.join("_");
    if(filters.length > 0){
        var filter = "&filter="
        var filterList = filters.join("_")
        window.location.href=rootPath.concat(query).concat(ingredientsList).concat(filter).concat(filterList)
    } else{
        window.location.href=rootPath.concat(query).concat(ingredientsList)
    }
}

function incPage(page){
    return page + 1
 }