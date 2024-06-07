document.addEventListener('DOMContentLoaded', function () {
    const snacksRadio = document.querySelector('input[name="snacks"]:checked');
    if (snacksRadio && snacksRadio.value === '기타') {
        document.getElementById('id_snacks_other').style.display = 'block';
    }

    const healthGoalsRadio = document.querySelector('input[name="health_goals"]:checked');
    if (healthGoalsRadio && healthGoalsRadio.value === '기타') {
        document.getElementById('id_health_goals_other').style.display = 'block';
    }

    const supplementsRadio = document.querySelector('input[name="interested_supplements"]:checked');
    if (supplementsRadio && supplementsRadio.value === '기타') {
        document.getElementById('id_interested_supplements_other').style.display = 'block';
    }

    const radios = document.querySelectorAll('input[type="radio"][name="snacks"], input[type="radio"][name="health_goals"], input[type="radio"][name="interested_supplements"]');
    radios.forEach(function (radio) {
        radio.addEventListener('change', function () {
            const otherFieldId = 'id_' + this.name + '_other';
            const otherField = document.getElementById(otherFieldId);
            if (this.value === '기타') {
                otherField.style.display = 'block';
            } else {
                otherField.style.display = 'none';
            }
        });
    });
});