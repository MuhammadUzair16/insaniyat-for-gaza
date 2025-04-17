document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', function(e) {
        let isValid = true;

        // Clear previous errors
        document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
        document.querySelectorAll('.help-block').forEach(el => el.textContent = '');

        // Validate each field
        ['name', 'email', 'subject', 'message'].forEach(field => {
            const input = document.getElementById(`id_${field}`);
            if (!input.value.trim()) {
                input.classList.add('is-invalid');
                document.querySelector(`.help-block`).textContent = 'This field is required';
                isValid = false;
            }
        });

        // Validate email format
        const email = document.getElementById('id_email');
        if (email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
            email.classList.add('is-invalid');
            document.querySelector(`.help-block`).textContent = 'Please enter a valid email';
            isValid = false;
        }

        if (!isValid) {
            e.preventDefault();
        }
    });
});