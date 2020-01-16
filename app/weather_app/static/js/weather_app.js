
$(() => {

    let renderButton = $('.check_weather')
    let weatherCell = $('#weather-table')

    renderButton.on('click', () => {

        let city_name = $('#city-selector').val()
        extendedTableWeather(city_name)

    })

     function extendedTableWeather(city_name) {
            console.log('refreshing page...')
            $.ajax({
                url: "/city_weather/" + city_name + "/",
                dataType: "HTML",
                beforeSend: function () {
                    $("#overlay").fadeIn(300);
                },
                complete: function () {
                    $("#overlay").fadeOut(300);
                },
                error: function (msg) {
                    alert(msg.statusText);
                    return msg;
                },
                success: function (html) {
                    $(weatherCell).html(html);
                }
            });
        }

})