// Total Sales
fetch("http://127.0.0.1:8000/total_sales")
.then(response => response.json())
.then(data => {
    document.getElementById("sales").innerHTML =
    "$" + Number(data["Total Sales"]).toLocaleString();
});

// Total Profit
fetch("http://127.0.0.1:8000/total_profit")
.then(response => response.json())
.then(data => {
    document.getElementById("profit").innerHTML =
    "$" + Number(data["Total Profit"]).toLocaleString();
});

// Total Orders
fetch("http://127.0.0.1:8000/total_orders")
.then(response => response.json())
.then(data => {
    document.getElementById("orders").innerHTML =
    Number(data["Total Orders"]).toLocaleString();
});

// Top Products
fetch("http://127.0.0.1:8000/top_products")
.then(response => response.json())
.then(products => {

    let table = document.getElementById("productTable");

    products.forEach(product => {

        table.innerHTML += `
        <tr>
            <td>${product["Product.Name"]}</td>
            <td>$${Number(product.Sales).toFixed(2)}</td>
        </tr>
        `;
    });

});
fetch("http://127.0.0.1:8000/sales_by_category")
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
fetch("http://127.0.0.1:8000/profit_by_category")
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