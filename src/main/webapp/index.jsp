<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="com.Recommendation.FlaskAPIClient" %>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>
<head>
    <title>Movie Recommender</title>
</head>
<body>
    <h2>Enter User ID</h2>
    <form action="recommendations.jsp" method="get">
        <label for="user_id">User ID:</label>
        <input type="text" id="user_id" name="user_id" required />
        <input type="submit" value="Get Recommendations" />
    </form>
</body>
</html>
