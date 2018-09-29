% include("header.tpl")

<body>

        </br></br></br></br>
        </br></br>

    <div class = "menu-wrap">
        <table>

            <center><a href="/">Go back</a></center>
            
                    <tr>
                        <th>Station</th>
                        <th>Name</th>
                        <th>Gas Price</th>
                        <th>Diesel Price</th>
                    </tr>

                % for read in data:
                    <tr>
                        <td>{{read["company"]}} </td>
                        <td>{{read["name"]}} </td>
                        <td>{{read["bensin95"]}} kr</td>
                        <td>{{read["diesel"]}} kr</td>
                    </tr>
                % end

                %
                <caption>({{len(data)}}) gas stations are loaded</caption>
                <caption>Last Updated: {{time}}</caption>
                % end
        </table>

        </br></br>
        <center><image src={{url}}></image></center>
    </div>
</body>

% include("footer.tpl")
