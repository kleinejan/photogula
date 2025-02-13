document.addEventListener('DOMContentLoaded', function() {
    // Initialize Feather icons
    feather.replace();

    // Toggle capture button
    const toggleButton = document.getElementById('toggle-capture');
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            fetch('/api/camera/toggle', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                const status = document.getElementById('capture-status');
                if (data.status) {
                    status.textContent = 'Active';
                    status.className = 'badge bg-success';
                    toggleButton.textContent = 'Stop Capture';
                } else {
                    status.textContent = 'Inactive';
                    status.className = 'badge bg-secondary';
                    toggleButton.textContent = 'Start Capture';
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    // System actions
    const systemButtons = {
        'reload-config': 'Are you sure you want to reload the camera configuration?',
        'format-disk': 'Are you sure you want to format the USB disk? All data will be lost!',
        'reboot-system': 'Are you sure you want to reboot the system?'
    };

    Object.keys(systemButtons).forEach(id => {
        const button = document.getElementById(id);
        if (button) {
            button.addEventListener('click', function() {
                if (confirm(systemButtons[id])) {
                    // Implement system action
                    console.log(`Executing ${id}`);
                }
            });
        }
    });

    // Save settings forms
    const forms = [
        'day-settings-form',
        'night-settings-form',
        'system-settings-form',
        'upload-settings-form'
    ];

    forms.forEach(formId => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries());
                
                fetch('/api/camera/settings', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
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
});
