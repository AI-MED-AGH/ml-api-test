document.querySelector('#mod2-form').addEventListener('submit', (event) => {
    event.preventDefault()

    console.log("Submit!")

    const numberInput = document.querySelector('#numberInput');
    const number = parseInt(numberInput.value) || 0;

    console.log("Number:", number)
    
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            data: [number]
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        if (data.prediction) {
            const prediction = data.prediction[0]
            const predictionElement = document.querySelector('#prediction')
            predictionElement.textContent = `${prediction}`
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
})