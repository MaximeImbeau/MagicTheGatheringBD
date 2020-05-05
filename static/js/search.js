function toggleSearchParameters() {
    let checkbox = document.getElementById("advanced-params-checkbox");
    let params = document.getElementById("advanced-params");

    if (checkbox.checked == false) {
        params.style.display = "none";
    } else {
        params.style.display = "flex";
    }
}

function toggleColorCheckboxes() {
    let checkboxes = document.getElementsByClassName("color-checkbox");

    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = false;
    }
}

function toggleColorlessCheckbox() {
    let checkbox = document.getElementById("colorless-checkbox");

    if (checkbox.checked) {
        checkbox.checked = false;
    }
}

function addRarityParameter(selectedRarity) {
    let value = selectedRarity.value;
    let input = document.getElementById("rarity")

    input.value = value;
}

function addTypeParameter(selectedType) {
    let value = selectedType.value;
    let input = document.getElementById("type")

    input.value = value;
}

function addColorParameter(color) {
    let colorInputs = document.getElementsByClassName('color-inputs');

    for (var i = 0; i < colorInputs.length; i++) {
        if (colorInputs[i].value === color) {
            return colorInputs[i].disabled = true;
        }
    }

    let form = document.getElementById("search-form");

    addElementToForm(form, 'color', color);
}

function addElementToForm(form, name, value) {
    let element = document.createElement('input');

    element.className = 'color-inputs';
    element.type = 'hidden';
    element.name = name;
    element.value= value;

    form.appendChild(element);
}