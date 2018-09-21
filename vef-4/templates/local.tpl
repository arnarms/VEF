% include("vef-4/templates/header.tpl")

<body>
    <section>
        <a href="/">Go back</a>
        <table>
                <tr>
                    <th>Long name</th>
                    <th>Short name</th>
                    <th>Value</th>
                </tr>
                <%
                    import json
                    with open("vef-4/gengi.json","r") as skra:
                        gogn = json.load(skra)
                %>

                % for lesa in gogn["results"]:
                    <tr>
                        <td>{{lesa["longName"]}}</td>
                        <td>{{lesa["shortName"]}}</td>
                        <td>{{lesa["value"]}}</td>
                    </tr>
                % end
        </table>
    </section>

% include("vef-4/templates/footer.tpl")
