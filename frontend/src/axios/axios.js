import axios from 'axios';

axios.get('/api/data')
  .then(response => {
    // Обработка успешного ответа
    console.log(response.data);
  })
  .catch(error => {
    // Обработка ошибки
    console.error(error);
  });
