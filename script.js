// Конвертация валют
document.getElementById('convert-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const amount = document.getElementById('amount').value;
    const fromCurrency = document.getElementById('from_currency').value;
    const toCurrency = document.getElementById('to_currency').value;

    try {
        const response = await fetch('http://localhost:8000/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                amount: parseFloat(amount),
                from_currency: fromCurrency,
                to_currency: toCurrency
            })
        });

        if (!response.ok) {
            throw new Error('Ошибка при конвертации');
        }

        const data = await response.json();
        document.getElementById('result').innerText = `Результат: ${data.converted_amount} ${data.to_currency}`;

        // Автоматическое обновление истории после конвертации
        loadOperations();
    } catch (error) {
        document.getElementById('result').innerText = 'Произошла ошибка';
    }
});

// Загрузка истории операций
async function loadOperations() {
    try {
        const response = await fetch('http://localhost:8000/operations');
        if (!response.ok) {
            throw new Error('Не удалось загрузить историю операций');
        }

        const operations = await response.json();
        const operationsList = document.getElementById('operations-list');
        operationsList.innerHTML = ''; // Очищаем список

        operations.forEach(op => {
            const li = document.createElement('li');
            li.innerText = `${op.amount} ${op.from_currency} → ${op.result} ${op.to_currency}`;
            operationsList.appendChild(li);
        });
    } catch (error) {
        console.error(error);
    }
}

// Загрузка истории при загрузке страницы
window.addEventListener('load', loadOperations);