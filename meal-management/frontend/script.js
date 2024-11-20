document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');

    // Login handler
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // API call to login (example endpoint)
            // fetch('/api/login', {...})
            console.log('Logging in with:', username, password);
        });
    }
});

// Admin Function
async function addFunds() {
    const userId = document.getElementById('userId').value;
    const amount = document.getElementById('fundAmount').value;

    // API call to add funds
    console.log(`Adding ${amount} to user ${userId}`);
}

async function setMealPrices() {
    const breakfastPrice = document.getElementById('breakfastPrice').value;
    const lunchPrice = document.getElementById('lunchPrice').value;
    const dinnerPrice = document.getElementById('dinnerPrice').value;

    // API call to set meal prices
    console.log(`Setting prices: Breakfast ${breakfastPrice}, Lunch ${lunchPrice}, Dinner ${dinnerPrice}`);
}

// User Functions
async function submitMealPreferences() {
    const breakfast = document.getElementById('breakfast').checked;
    const lunch = document.getElementById('lunch').checked;
    const dinner = document.getElementById('dinner').checked;

    // API call to submit preferences
    console.log('Saving preferences:', { breakfast, lunch, dinner });
}
async function loginUser(username, password) {
    const response = await fetch("https://meal-management-209x.onrender.com/users/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });
    if (response.ok) {
        const data = await response.json();
        // Redirect or store token
    } else {
        alert("Login failed");
    }
}

async function submitMealPreferences(userId, breakfast, lunch, dinner) {
    const response = await fetch(`https://meal-management-209x.onrender.com/meals/?user_id=${userId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ breakfast, lunch, dinner }),
    });
    if (response.ok) {
        alert("Meal preferences saved");
    } else {
        alert("Failed to save preferences");
    }
}
async function getMealStatement(userId, month = null) {
    const url = month 
        ? `https://https://meal-management-209x.onrender.com/users/${userId}/meal_statement?month=${month}`
        : `https://https://meal-management-209x.onrender.com/users/${userId}/meal_statement`;
    
    const response = await fetch(url);
    if (response.ok) {
        const data = await response.json();
        console.log("Meal Statement:", data);
        printStatement(data);  // Function to display statement in a printable format
    } else {
        alert("Could not fetch statement");
    }
}

async function checkUserBalance(userId) {
    const response = await fetch(`https://https://meal-management-209x.onrender.com/users/${userId}/balance`);
    if (response.ok) {
        const { balance } = await response.json();
        alert(`Your balance is: $${balance}`);
    } else {
        alert("Could not check balance");
    }
}

function printStatement(data) {
    let printContent = `<h2>Meal Statement</h2><table><tr><th>Date</th><th>Breakfast</th><th>Lunch</th><th>Dinner</th><th>Cost</th></tr>`;
    data.forEach(meal => {
        printContent += `<tr><td>${meal.date}</td><td>${meal.breakfast ? 'Yes' : 'No'}</td><td>${meal.lunch ? 'Yes' : 'No'}</td><td>${meal.dinner ? 'Yes' : 'No'}</td><td>${meal.cost}</td></tr>`;
    });
    printContent += `</table>`;
    const newWin = window.open();
    newWin.document.write(printContent);
    newWin.print();
    newWin.close();
}

