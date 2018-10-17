% include("./templates/header.tpl")

    <body>
        <section>
                <form action="/send" method="post">
                    <label>Name:</label><br>
                        <input type="text" name="name" required><br>

                    <label>Address:</label><br>
                         <input type="text" name="address" required><br>

                    <label>Email:</label><br>
                        <input type="email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$" name="email" required><br>

                    <label>Phone<font size="2">  (123-4567) :</font-size></label><br>
                         <input type="tel" pattern="^\d{3}-\d{4}"   name="phone" required><br>

                    <label>Day 1:</label><br>
                            <input type="date" name="dateOne" required><br>
                    
                    <label>Course:</label><br>
                                <input type="radio" name="workshopOne" value="python"> Python<br>
                                <input type="radio" name="workshopOne" value="javascript"> JavaScript<br>
                                <input type="radio" name="workshopOne" value="databases"> Databases<br>
                
                    <label>Day 2:</label><br>
                            <input type="date" name="dateTwo" required><br>
                      
                   <label>Course:</label><br>
                                <input type="radio" name="workshopTwo" value="python"> Python<br>
                                <input type="radio" name="workshopTwo" value="javascript"> JavaScript<br>
                                <input type="radio" name="workshopTwo" value="databases"> Databases<br>
                      
                    <label>Day 3:</label><br>
                            <input type="date" name="dateThree" required><br>
                    
                   <label>Course:</label><br>
                                <input type="radio" name="workshopThree" value="python"> Python<br>
                                <input type="radio" name="workshopThree" value="javascript"> JavaScript<br>
                                <input type="radio" name="workshopThree" value="databases"> Databases<br>
                        
    
                    <form action="/send">
                        <input type="submit" class="button_active" value="Register">
                    </form>
        </section>
    </body>
