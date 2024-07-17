document.getElementById('healthForm').addEventListener('static', function(e) {
    e.preventDefault();

    const formData = {
        prediction: document.getElementById('pred').value,
        age: document.getElementById('age').value,
        gender: document.getElementById('gender').value,
        chestPain: document.getElementById('chestPain').value,
        restingBP: document.getElementById('restingBP').value,
        cholesterol: document.getElementById('cholesterol').value,
        fastingBS: document.getElementById('fastingBS').value,
        restingECG: document.getElementById('restingECG').value,
        maxHR: document.getElementById('maxHR').value,
        exerciseInducedAngina: document.getElementById('exerciseInducedAngina').value,
        previousPeak: document.getElementById('previousPeak').value,
    };

    console.log('Form Data Submitted:', formData);

    // Store form data in session storage
    sessionStorage.setItem('formData', JSON.stringify(formData));

    // Redirect to result page
    window.location.href = 'result.html';
});
