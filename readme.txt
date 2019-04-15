1. ����������� REST API ������ ��� �������� ����������. ������ ���������� ������� ���� ��������, � ������� ������� ����� ����� ���������� ��� �������� ���������� � ������������� ��� ����������� ����� ����������. ������ �������� ��������� ����������� ������ ��������������, � ������� ����� ������������� ����������� ����������.

2. ���������
2.1 Framework - Django
2.2 Database - Postgres
2.3. nginx:
2.3.1 reverse proxy (��� ������� ���� ����� /service, ��������, GET /service/photos)
2.3.2 ������ �� ������� ������ 10 ��
2.3.3 redirect � / �� /service
4. Docker = Django + Postgres + nginx
5. �������� ������� ���� REST ��������
6. ������� ���������� ��� ������ �� �������
7. ������ ��������������� - django admin
8. REST API - django rest framework
9. �������� �� github

3. API �������� 
� ������� ����� ��� REST ������� (���. 1)
1. ���������� ���������� � �������
2. �������� ���������� �� ���� ����������� �����������

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
                ��������� ��� ����������: <br>
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
                ��������� ��� ����������: <br>
                { <br>
                "place" : < string >, <br>
                "img" : < ������ �� ������� >, <br>
                }
            </td>
            <td>
                200
            </td>
        </tr>
    </table>