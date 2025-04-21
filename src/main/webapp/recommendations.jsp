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
    <h2>Enter Movie Title</h2>
    <form action="recommendations.jsp" method="get">
        <label for="movie_title">Movie Title:</label>
        <input type="text" id="movie_title" name="movie_title" required />
        <input type="submit" value="Get Recommendations" />
    </form>

    <%
        String movieTitle = request.getParameter("movie_title");
        if (movieTitle != null && !movieTitle.isEmpty()) {
            // Fetching recommendations based on the movie title
            String[] recommendations = FlaskAPIClient.getRecommendations(movieTitle);
    %>

    <h2>Recommendations for Movie: <%= movieTitle %></h2>
    <ul>
        <% for(String movie : recommendations) { %>
            <li><%= movie %></li>
        <% } %>
    </ul>

    <% } %>

</body>
</html>
