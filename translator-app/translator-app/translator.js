async function getSupportedLanguages() {
    const apiKey = "YOUR_GOOGLE_API_KEY"; // Replace with your API key
    const url = `https://translation.googleapis.com/language/translate/v2/languages?key=${apiKey}&target=en`;

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP Error! Status: ${response.status}`);
        }

        const data = await response.json();

        if (!data.data || !data.data.languages) {
            throw new Error("Invalid response from API");
        }

        return data.data.languages;
    } catch (error) {
        console.error("Error fetching languages:", error);
        alert("Failed to load supported languages. Please check your internet connection or API key.");
        return [];
    }
}
