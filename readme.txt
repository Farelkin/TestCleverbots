1. Разработать REST API сервер для хранения фотографий. Сервер предлагает наличие двух запросов, с помощью которых можно будет отправлять для хранения фотографии и просматривать все добавленные ранее фотографии. Помимо запросов требуется реализовать панель администратора, в которой можно просматривать добавленные фотографии.

2. Пожелания
2.1 Framework - Django
2.2 Database - Postgres
2.3. nginx:
2.3.1 reverse proxy (все запросы идут через /service, например, GET /service/photos)
2.3.2 фильтр на запросы больше 10 мб
2.3.3 redirect с / на /service
4. Docker = Django + Postgres + nginx
5. Покрытие тестами двух REST запросов
6. Наличие инструкции для деплоя на сервере
7. Панель падминистратора - django admin
8. REST API - django rest framework
9. Выложить на github

3. API описание 
У сервера будет два REST запроса (таб. 1)
1. Добавление фотографий в систему
2. Выгрузка информации по всем загруженным фотографиям

    <table>
        <tr>
            <th>Method</th>
            <th>Request</th>
            <th>Parametrs</th>
            <th>Response</th>
        </tr>
        <tr>
            <td>GET</td>
            <td>photos</td>
            <td>
                Параметры для фильтрации: <br>
                { <br>
                "date" : < string >, <br>
                "size" : < int >, <br>
                }
            </td>
            <td>
                200 <br>
                [{ <br>
                "date" : < string >, <br>
                "place" : < string >, <br>
                "path_to_img" : < string >, <br>
                }]
            </td>
        </tr>
        <tr>
            <td>POST</td>
            <td>photo</td>
            <td>
                Параметры для фильтрации: <br>
                { <br>
                "place" : < string >, <br>
                "img" : < формат по желанию >, <br>
                }
            </td>
            <td>
                200
            </td>
        </tr>
    </table>