// Отримання списку країн з зовнішнього API та додавання їх до випадаючого списку
fetch('https://restcountries.com/v3.1/all')
  .then(response => response.json())
  .then(data => {
    // Сортуємо країни за алфавітним порядком
    data.sort((a, b) => a.name.common.localeCompare(b.name.common));

    const countrySelect = document.getElementById('country');
    data.forEach(country => {
      const option = document.createElement('option');
      option.text = country.name.common;
      option.value = country.name.common;
      countrySelect.appendChild(option);
    });
  })
  .catch(error => console.error('Error fetching countries:', error));


document.getElementById("registrationForm").addEventListener("submit", function(event) {
    var age = document.getElementById("age").value;
    if (age < 3 || age > 100) {
        alert("Ви повинні бути віком від 18 до 100 років для реєстрації.");
        event.preventDefault();
    }

    var phoneNumber = document.getElementById("phoneNumber").value;
    if (!/^\+?3?8?(0\d{9})$/.test(phoneNumber)) {
        alert("Недійсний номер телефону.");
        event.preventDefault();
    }

    var email = document.getElementById("email").value;
    if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {
        alert("Недійсна адреса електронної пошти.");
        event.preventDefault();
    }

    var password = document.getElementById("password").value;
    if (password.length < 8 || !/[A-Z]/.test(password) || !/[a-z]/.test(password) || !/\d/.test(password) || !/[!@#$%^&*]/.test(password)) {
        alert("Недійсний пароль. Пароль повинен містити принаймні 8 символів, включаючи принаймні одну велику літеру, одну малу літеру, одну цифру і один спеціальний символ (!@#$%^&*).");
        event.preventDefault();
    }
});

function togglePassword() {
    var passwordInput = document.getElementById("password");
    var eyeIcon = document.getElementById("showPassword");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.src = "/IMG/ОкоПеречеркнуте.png";
    } else {
        passwordInput.type = "password";
        eyeIcon.src = "/IMG/Око.png";
    }
}


function updateFileName(input) {
   let fileName = input.files[0].name;
   let fileSpan = input.parentElement.querySelector('.file-name');
   fileSpan.textContent = fileName;
}
