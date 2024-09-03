document.getElementById('action-button').addEventListener('click', async () => {
    const task = document.getElementById('task').value;
    const inputText = document.getElementById('input-text').value;
    const targetLang = document.getElementById('target-lang').value;

    let apiUrl = '';
    let payload = {};

    if (task === 'generate') {
        apiUrl = '/generate';
        payload = { prompt: inputText };
    } else if (task === 'convert') {
        apiUrl = '/convert';
        payload = { code: inputText, targetLang: targetLang };
    }

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (data.result) {
            document.getElementById('output').textContent = data.result;
        } else if (data.error) {
            document.getElementById('output').textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        document.getElementById('output').textContent = `Request failed: ${error}`;
    }
});
