% include("./templates/header.tpl")

    <body>
        <section>

                <h1> Login Homepage </h1>

                <form action="/register" >
                    <input type="submit" value="Register" />
                </form>

                <form action="/login" >
                    <input type="submit" value="Login" />
                </form>

                <form action="/admin" >
                    <input type="submit" disabled value="Admin" />
                </form>
                
        </section>
    </body>
