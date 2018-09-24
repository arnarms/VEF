% include("vef-midonn/templates/header.tpl")


<header>
        <h1> Arnar's Gas Price Checker </h1>
		<img src="static/image/lilcat.png" draggable="false">
</header>

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
            </div>
        </body>
% include("vef-midonn/templates/footer.tpl")
