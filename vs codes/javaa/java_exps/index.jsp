<%@ page import="java.util.Date" %>

<html>
<head>
    <title>JSP Implicit and Explicit Objects</title>
</head>
<body>

    <h2>JSP Implicit Objects</h2>

    <p>Request Method: <%= request.getMethod() %></p>

    <p>Client IP: <%= request.getRemoteAddr() %></p>

    <p>Server Name: <%= request.getServerName() %></p>

    <p>Session ID: <%= session.getId() %></p>

    <p>Server Information: <%= application.getServerInfo() %></p>

    <p>
        Output using out:
        <% out.println("Hello from JSP out object"); %>
    </p>

    <h2>JSP Explicit Objects</h2>

    <%
        Date today = new Date();
        String message = new String("Welcome to JSP Programming");
    %>

    <p>Explicit Date Object: <%= today %></p>

    <p>Explicit String Object: <%= message %></p>

</body>
</html>