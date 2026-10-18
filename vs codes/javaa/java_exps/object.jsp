
<%@ page import="java.util.Date" %>

<html>
<head>
    <title>JSP Objects</title>
</head>
<body>

    <h2>Implicit Objects</h2>

    <p>Request Method: <%= request.getMethod() %></p>
    <p>Client IP: <%= request.getRemoteAddr() %></p>
    <p>Server Name: <%= request.getServerName() %></p>
    <p>Session ID: <%= session.getId() %></p>
    <p>Server Info: <%= application.getServerInfo() %></p>

    <%
        out.println("Hello from JSP");
    %>

    <h2>Explicit Objects</h2>

    <%
        Date today = new Date();
        String message = new String("Welcome to JSP");
    %>

    <p>Date: <%= today %></p>
    <p>Message: <%= message %></p>

</body>
</html>
