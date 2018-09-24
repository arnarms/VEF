% include("vef-midonn/templates/header.tpl")



        <body>

        
            <div class = "menu-wrap">
                        <section> <code>
                                %for r in rows:
                                <ul>
                                    <a href="/{{r}}">
                                        <li>{{r}}</li>
                                    </a>
                                </ul>
                                %end                
                        </section> </code>        
              
                    
                    <table>
                            <tr>
                                <th>Station</th>
                                <th>Cheapest Gas</th>
                                <th>Cheapest diesel</th>
                            </tr>

                % for read in gogn["results"]:
                            <tr>
                        <td>{{read["company"]}} </td>
                        <td>{{read["bensin95"]}} kr</td>
                        <td>{{read["diesel"]}} kr</td>
                            </tr>
                            % end
                    </table>
             </div>
        </body>
% include("vef-midonn/templates/footer.tpl")
