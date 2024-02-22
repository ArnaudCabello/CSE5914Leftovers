// script.js

function addIngredient() {
    var ingredientInput = document.getElementById('ingredients');
    var ingredient = ingredientInput.value.trim();

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
}

function generateRecipes() {
    // You can redirect to the results page here
    window.location.href='/results'
}