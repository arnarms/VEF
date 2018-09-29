% include("header.tpl")

<body>

        <section> 
            %for r in rows:
            <ul>
                <a href="/{{r}}">
                    <li>{{r}}</li>
                </a>
            </ul>
            %end
   

    <table>
        <tr>
            <th>Station</th>
            <th>Name</th>
            <th>Cheapest Gas</th>
            <th>Cheapest diesel</th>
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

        % end
    </table><center><caption>Last Updated: {{time}}</caption> </center> </section> 

  
</body>
% include("footer.tpl")
