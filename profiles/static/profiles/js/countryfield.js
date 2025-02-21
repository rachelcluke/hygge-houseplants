let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', 'var(--bluegray)');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', 'var(--bluegray)');
    } else {
        $(this).css('color', 'var(--black)');
    }
});