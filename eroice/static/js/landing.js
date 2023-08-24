function setInputAttributesAndClasses(inputElement, refName) {
    inputElement.setAttribute('x-ref', refName);
    inputElement.classList.add('outline-none', 'cursor-default', 'w-full', 'dark:bg-gray-800');
    inputElement.setAttribute('x-bind:value', 'value');
}

const inputElements = document.querySelectorAll('input');

setInputAttributesAndClasses(inputElements[2], 'usernameInput');
setInputAttributesAndClasses(inputElements[3], 'emailInput');
setInputAttributesAndClasses(inputElements[4], 'password1Input');
setInputAttributesAndClasses(inputElements[5], 'password2Input');
