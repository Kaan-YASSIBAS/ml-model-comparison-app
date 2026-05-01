const API_BASE_URL = "http://127.0.0.1:8000";

const modelSelect = document.getElementById("modelSelect");
const evaluateButton = document.getElementById("evaluateButton");

const loading = document.getElementById("loading");
const errorBox = document.getElementById("error");
const singleResult = document.getElementById("singleResult");

function showLoading(message) {
    loading.textContent = message;
    loading.classList.remove("hidden");
    errorBox.classList.add("hidden");
    singleResult.classList.add("hidden");
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

evaluateButton.addEventListener("click", async function () {
    const selectedModel = modelSelect.value;

    showLoading("Training and evaluating selected model...");

    try {
        const response = await fetch(`${API_BASE_URL}/evaluate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                model_name: selectedModel
            })
        });

        if (!response.ok) {
            throw new Error("Model evaluation failed.");
        }

        const data = await response.json();

        document.getElementById("modelName").textContent = data.model_name;
        document.getElementById("accuracy").textContent = formatMetric(data.accuracy);
        document.getElementById("precision").textContent = formatMetric(data.precision);
        document.getElementById("recall").textContent = formatMetric(data.recall);
        document.getElementById("f1Score").textContent = formatMetric(data.f1_score);

        document.getElementById("cm00").textContent = data.confusion_matrix[0][0];
        document.getElementById("cm01").textContent = data.confusion_matrix[0][1];
        document.getElementById("cm10").textContent = data.confusion_matrix[1][0];
        document.getElementById("cm11").textContent = data.confusion_matrix[1][1];

        hideLoading();
        singleResult.classList.remove("hidden");

    } catch (error) {
        showError(error.message);
    }
});