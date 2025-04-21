package com.Recommendation;

import java.io.*;
import java.net.*;
import org.json.JSONObject;
import org.json.JSONArray;

public class FlaskAPIClient {

    // Updated to take movie title as input
    public static String[] getRecommendations(String title) {
        try {
            URL url = new URL("http://127.0.0.1:5000/recommend");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json; utf-8");
            conn.setDoOutput(true);

            JSONObject jsonInput = new JSONObject();
            jsonInput.put("title", title);  // Sending the title input

            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInput.toString().getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"));
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) {
                response.append(line.trim());
            }

            JSONArray recs = new JSONArray(response.toString());

            String[] results = new String[recs.length()];
            for (int i = 0; i < recs.length(); i++) {
                results[i] = recs.getJSONObject(i).getString("title"); // Getting the movie title from recommendations
            }

            return results;

        } catch (Exception e) {
            e.printStackTrace();
            return new String[]{"Error fetching recommendations"};
        }
    }
}
