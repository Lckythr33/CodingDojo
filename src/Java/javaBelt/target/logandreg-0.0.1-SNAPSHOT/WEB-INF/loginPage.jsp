<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
	<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
<!DOCTYPE html>
<html>
<head>
<!-- Font Awesome -->
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
<!-- Bootstrap core CSS -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
<!-- Material Design Bootstrap -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.7/css/mdb.min.css" rel="stylesheet">

<meta charset="ISO-8859-1">
<title>Login Page</title>
</head>
<body>

<form class="border border-light p-5 w-25" method="post" action="/login">

    <p class="h4 mb-4 text-center">Log In</p>

    <input type="email" name="email" id="defaultLoginFormEmail" class="form-control mb-4" placeholder="E-mail"/>

    <input type="password" name="password" id="defaultLoginFormPassword" class="form-control mb-4" placeholder="Password"/>
	
	 <span class="red white-text" style='border-radius:5px;'><c:out value="${error}" /></span>
	

<!--       <p>Not a member? -->
<!--         <a href=/registration>Register</a> -->
<!--       </p> -->

    <button class="btn btn-info btn-block my-4" type="submit">Log In</button>


</form>


<!-- JQuery -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<!-- Bootstrap tooltips -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script>
<!-- Bootstrap core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
<!-- MDB core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.7/js/mdb.min.js"></script>
</body>
</html>