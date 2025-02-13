document.addEventListener('DOMContentLoaded', function() {
    const settingsToggleForm = document.getElementById('settings-toggle-form');
    const daySettingsForm = document.getElementById('day-settings-form');
    const nightSettingsForm = document.getElementById('night-settings-form');
    const saveSettingsBtn = document.getElementById('save-settings');

    // Range input value display
    document.querySelectorAll('input[type="range"]').forEach(range => {
        const valueDisplay = range.nextElementSibling.querySelector('.range-value');
        range.addEventListener('input', () => {
            valueDisplay.textContent = range.value;
        });
    });

    if (settingsToggleForm) {
        settingsToggleForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(settingsToggleForm);
            const enabledSettings = Array.from(formData.keys());

            fetch('/api/camera/enabled-settings', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ enabled_settings: enabledSettings })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Settings preferences saved successfully');
                    location.reload();
                } else {
                    alert('Error saving settings preferences: ' + data.error);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    if (saveSettingsBtn) {
        saveSettingsBtn.addEventListener('click', function() {
            const dayData = Object.fromEntries(new FormData(daySettingsForm));
            const nightData = Object.fromEntries(new FormData(nightSettingsForm));

            fetch('/api/camera/settings', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    day_settings: dayData,
                    night_settings: nightData
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Settings saved successfully');
                } else {
                    alert('Error saving settings: ' + data.error);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }
});