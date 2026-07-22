// Total Sales
fetch("https://retail-intelligence-platform-2un0.onrender.com/total_sales")
.then(response => response.json())
.then(data => {
    document.getElementById("sales").innerHTML =
    "$" + Number(data["Total Sales"]).toLocaleString();
});

// Total Profit
fetch("https://retail-intelligence-platform-2un0.onrender.com/total_profit")
.then(response => response.json())
.then(data => {
    document.getElementById("profit").innerHTML =
    "$" + Number(data["Total Profit"]).toLocaleString();
});

// Total Orders
fetch("https://retail-intelligence-platform-2un0.onrender.com/total_orders")
.then(response => response.json())
.then(data => {
    document.getElementById("orders").innerHTML =
    Number(data["Total Orders"]).toLocaleString();
});
fetch("https://retail-intelligence-platform-2un0.onrender.com/category_summary")
.then(response => response.json())
.then(data => {

    data.forEach(item => {

        if(item.Category === "Furniture"){
            document.getElementById("furnitureSales").innerHTML =
            "$" + Number(item.Total_Sales).toLocaleString();
        }

        if(item.Category === "Technology"){
            document.getElementById("technologySales").innerHTML =
            "$" + Number(item.Total_Sales).toLocaleString();
        }

        if(item.Category === "Office Supplies"){
            document.getElementById("officeSales").innerHTML =
            "$" + Number(item.Total_Sales).toLocaleString();
        }

    });

});


fetch("https://retail-intelligence-platform-2un0.onrender.com/sales_by_category")
.then(response => response.json())
.then(data => {

const labels = data.map(item => item.Category);

const values = data.map(item => item.Total_Sales);

new Chart(document.getElementById("salesChart"), {

type: "bar",

data: {

labels: labels,

datasets: [{

label: "Sales",

data: values

}]

}

});

});
fetch("https://retail-intelligence-platform-2un0.onrender.com/profit_by_category")
.then(response => response.json())
.then(data => {

const labels = data.map(item => item.Category);

const values = data.map(item => item.Total_Profit);

new Chart(document.getElementById("profitChart"), {

type: "pie",

data: {

labels: labels,

datasets: [{

data: values

}]

}

});

});
fetch("https://retail-intelligence-platform-2un0.onrender.com/sales_by_region")
.then(response => response.json())
.then(data => {

    const labels = data.map(item => item.Region);

    const values = data.map(item => item.Total_Sales);

    new Chart(document.getElementById("regionChart"), {

        type: "doughnut",

        data: {

            labels: labels,

            datasets: [{

                data: values

            }]

        }

    });

});
const searchBox = document.getElementById("searchProduct");

searchBox.addEventListener("keyup", function(){

    const filter = this.value.toLowerCase();

    const rows = document.querySelectorAll("#productTable tr");

    rows.forEach(row => {

        const text = row.innerText.toLowerCase();

        if(text.includes(filter)){
            row.style.display = "";
        }
        else{
            row.style.display = "none";
        }

    });

});
async function loadProducts(category = "All") {

    const response = await fetch(
        `https://retail-intelligence-platform-2un0.onrender.com/products_by_category/${category}`
    );

    const data = await response.json();

    const table = document.getElementById("productTable");

    table.innerHTML = "";

    data.forEach(product => {

        table.innerHTML += `
        <tr>
            <td>${product["Product.Name"]}</td>
            <td>${product.Category}</td>
            <td>$${Number(product.Sales).toFixed(2)}</td>
        </tr>
        `;

    });

}
const category = document.getElementById("categoryFilter");

category.addEventListener("change", function () {
    loadProducts(this.value);
});

loadProducts();
fetch("https://retail-intelligence-platform-2un0.onrender.com/top_customers")
.then(response => response.json())
.then(customers => {

    const table = document.getElementById("customerTable");

    table.innerHTML = "";

    customers.forEach(customer => {

        table.innerHTML += `
        <tr>
            <td>${customer["Customer.Name"]}</td>
            <td>$${Number(customer.Sales).toFixed(2)}</td>
        </tr>
        `;

    });

});
fetch("https://retail-intelligence-platform-2un0.onrender.com/monthly_sales")
.then(response => response.json())
.then(data => {

    const labels = data.map(item => item.Month);
    const values = data.map(item => item.Total_Sales);

    new Chart(document.getElementById("monthlyChart"), {

        type: "line",

        data: {
            labels: labels,
            datasets: [{
                label: "Monthly Sales",
                data: values,
                fill: false
            }]
        }

    });

});
fetch("https://retail-intelligence-platform-2un0.onrender.com/monthly_profit")
.then(response => response.json())
.then(data => {

    const labels = data.map(item => item.Month);

    const values = data.map(item => item.Total_Profit);

    new Chart(document.getElementById("monthlyProfitChart"), {

        type: "line",

        data: {

            labels: labels,

            datasets: [{

                label: "Monthly Profit",

                data: values

            }]

        }

    });

});
fetch("https://retail-intelligence-platform-2un0.onrender.com/top_states")
.then(response => response.json())
.then(data => {

    const labels = data.map(item => item.State);

    const values = data.map(item => item.Total_Sales);

    new Chart(document.getElementById("stateChart"), {

        type: "bar",

        data: {

            labels: labels,

            datasets: [{

                label: "Sales",

                data: values

            }]

        }

    });

});
fetch("https://retail-intelligence-platform-2un0.onrender.com/top_customers_profit")
.then(response => response.json())
.then(data => {

    const labels = data.map(item => item["Customer.Name"]);

    const values = data.map(item => item.Total_Profit);

    new Chart(document.getElementById("customerProfitChart"), {

        type: "bar",

        data: {

            labels: labels,

            datasets: [{

                label: "Profit",

                data: values

            }]

        },

        options: {
            indexAxis: "y"
        }

    });

});