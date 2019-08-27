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
<title>Create Course</title>
</head>
<body>

<div class="container">


<!-- Default form -->
<form:form class="text-center border border-light p-5 w-50" method="POST" action="/courses/new" modelAttribute="course">

    <p class="h4 mb-4">Create New Course</p>

    <div class="form-row mb-4">
        <div class="col">
            <!-- First name -->
             <span class="red white-text" style='border-radius:5px;'><form:errors path = "name"/></span>
            <form:input path="name" type="text" id="defaultRegisterFormFirstName" class="form-control" placeholder="Name"/>
        </div>
        <div class="col">
            <!-- instructor -->
             <span class="red white-text" style='border-radius:5px;'><form:errors path = "instructor"/></span>
            <form:input path="instructor" type="text" id="defaultRegisterFormLastName" class="form-control" placeholder="Instructor"/>
        </div>
    </div>

    <!-- cap -->
     <span class="red white-text" style='border-radius:5px;'><form:errors path = "capacity"/></span>
    <form:input path="capacity" type="text" id="defaultRegisterFormEmail" class="form-control mb-4" placeholder="Capacity"/>


    <!-- Sign up button -->
    <button class="btn btn-info my-4 btn-block" type="submit">Add Course!</button>


</form:form>
<!-- Default form register -->
		
				<div>
			<a class="btn btn-primary" href="/courses">Back</a>
		</div>
	</div>

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