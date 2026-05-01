const API_BASE_URL = "http://127.0.0.1:8000";

const compareButton = document.getElementById("compareButton");

const loading = document.getElementById("loading");
const errorBox = document.getElementById("error");
const comparisonResult = document.getElementById("comparisonResult");

function showLoading(message) {
    loading.textContent = message;
    loading.classList.remove("hidden");
    errorBox.classList.add("hidden");
    comparisonResult.classList.add("hidden");
}

function hideLoading() {
    loading.classList.add("hidden");
}

function showError(message) {
    hideLoading();
    errorBox.textContent = message;
    errorBox.classList.remove("hidden");
}

function formatMetric(value) {
    return (value * 100).toFixed(2) + "%";
}

compareButton.addEventListener("click", async function () {
    showLoading("Training and comparing all models...");

    try {
        const response = await fetch(`${API_BASE_URL}/compare-all`);

        if (!response.ok) {
            throw new Error("Model comparison failed.");
        }

        const data = await response.json();
        const tableBody = document.getElementById("comparisonTableBody");

        tableBody.innerHTML = "";

        data.results.forEach(function (item) {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${item.model_name}</td>
                <td>${formatMetric(item.accuracy)}</td>
                <td>${formatMetric(item.precision)}</td>
                <td>${formatMetric(item.recall)}</td>
                <td>${formatMetric(item.f1_score)}</td>
            `;

            tableBody.appendChild(row);
        });

        hideLoading();
        comparisonResult.classList.remove("hidden");

    } catch (error) {
        showError(error.message);
    }
});