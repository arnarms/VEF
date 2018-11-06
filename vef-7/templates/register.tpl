% include("./templates/header.tpl")

    <body>
        <section>
                <form action="/send" method="post">
                    <label>Name:</label><br>
                        <input type="text" name="name" required><br>

                    <label>Username:</label><br>
                        <input type="text" name="username" required><br>

                    <label>Password:</label><br>
                         <input type="text" name="address" required><br>
    
                    <form action="/send">
                        <input type="submit" class="button_active" value="Register">
                    </form>
        </section>
    </body>
