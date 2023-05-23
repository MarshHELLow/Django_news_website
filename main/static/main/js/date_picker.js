// Установка текущей даты и времени по умолчанию
var currentDate = new Date();
var currentDateString = currentDate.toISOString().split('T')[0];
var currentTimeString = currentDate.toTimeString().split(' ')[0];
document.getElementById("id_date").value = currentDateString;
document.getElementById("id_time").value = currentTimeString.substring(0, 5) + ":00";