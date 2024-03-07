// script.js
var ingredients = new Array();

function addIngredient() {
    var ingredientInput = document.getElementById('ingredients');
    var ingredient = ingredientInput.value.trim();
    ingredients.push(ingredient);
    if (ingredient !== "") {
        var ingredientList = document.getElementById('ingredientList');
        var ingredientItem = document.createElement('div');
        ingredientItem.className = 'ingredient-item';
        ingredientItem.textContent = ingredient;
        ingredientList.appendChild(ingredientItem);
        ingredientInput.value = ''; // Clear the input field
    }

    // Return false to prevent the form from submitting
    return false;
}

function clearIngredients() {
    document.getElementById('ingredients').value = '';
    document.getElementById('ingredientList').innerHTML = '';
    ingredients = new Array();
}

function generateRecipes() {
    // You can redirect to the results page here
    var rootPath = '/results';
    var query = '?q=';
    var ingredientsList = ingredients.join("_");
    window.location.href=rootPath.concat(query).concat(ingredientsList)
}