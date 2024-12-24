let expenses = [];

function loadApp() {
    setTimeout(() => {
        document.querySelector("p").style.display = 'none';
        document.getElementById("expenseApp").style.display = 'block';
    }, 1000); 
}

function addExpense() {
    const description = document.getElementById("description").value;
    const amount = parseFloat(document.getElementById("amount").value);
    const category = document.getElementById("category").value;

    if (description && amount && category) {
        const expense = { description, amount, category };
        expenses.push(expense);
        alert(`Expense '${description}' added successfully!`);
        clearInputs();
    } else {
        alert("Please fill in all fields.");
    }
}

function clearInputs() {
    document.getElementById("description").value = '';
    document.getElementById("amount").value = '';
    document.getElementById("category").value = '';
}

function viewExpenses() {
    const expenseList = document.getElementById("expenseList");
    expenseList.innerHTML = '';

    if (expenses.length === 0) {
        expenseList.innerHTML = "<p>No expenses recorded.</p>";
    } else {
        expenses.forEach(expense => {
            const div = document.createElement("div");
            div.innerHTML = `${expense.description} | ${expense.amount} | ${expense.category}`;
            expenseList.appendChild(div);
        });
    }
}

function viewCategorySummary() {
    const categorySummary = document.getElementById("categorySummary");
    categorySummary.innerHTML = '';
    
    const categoryTotals = {};
    expenses.forEach(expense => {
        if (!categoryTotals[expense.category]) {
            categoryTotals[expense.category] = 0;
        }
        categoryTotals[expense.category] += expense.amount;
    });

    if (Object.keys(categoryTotals).length === 0) {
        categorySummary.innerHTML = "<p>No expenses to categorize.</p>";
    } else {
        for (const [category, total] of Object.entries(categoryTotals)) {
            const div = document.createElement("div");
            div.innerHTML = `${category}: ${total}`;
            categorySummary.appendChild(div);
        }
    }
}

function viewTotalExpenses() {
    const totalExpenses = document.getElementById("totalExpenses");
    totalExpenses.innerHTML = '';

    const total = expenses.reduce((sum, expense) => sum + expense.amount, 0);
    totalExpenses.innerHTML = `<p>Total Expenses: ${total}</p>`;
}

function clearAllExpenses() {
    expenses = [];
    alert("All expenses have been deleted.");
    viewExpenses(); // Refresh the list to show empty
}


window.onload = loadApp;
