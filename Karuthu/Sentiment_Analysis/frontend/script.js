const API_URL = "http://localhost:9000/sentiment/predict";

const btn = document.getElementById("analyzeBtn");

btn.onclick = async () => {

    const feedback = document
        .getElementById("feedback")
        .value
        .trim();

    if (!feedback) {
        alert("Enter feedback");
        return;
    }

    const response = await fetch(API_URL, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            feedback: feedback
        })

    });

    const data = await response.json();

    document
        .getElementById("resultSection")
        .style.display = "block";


    //-------------------------
    // Overall Sentiment
    //-------------------------

    const badge = document.getElementById("overallSentiment");

    badge.innerHTML = data.overall_sentiment.toUpperCase();

    badge.className = "badge fs-5";

    if (data.overall_sentiment === "positive")
        badge.classList.add("bg-success");

    else if (data.overall_sentiment === "negative")
        badge.classList.add("bg-danger");

    else
        badge.classList.add("bg-warning");


    //-------------------------
    // Progress Bars
    //-------------------------

    // setBar("positiveBar", data.positive);

    // setBar("neutralBar", data.neutral);

    // setBar("negativeBar", data.negative);


    //-------------------------
    // Sentence Table
    //-------------------------

    const tbody = document.getElementById("sentenceTable");

    tbody.innerHTML = "";

    data.sentences.forEach(item => {

        let color = "";

        if (item.sentiment === "positive")
            color = "success";

        else if (item.sentiment === "negative")
            color = "danger";

        else
            color = "warning";

        tbody.innerHTML += `

        <tr>

            <td>${item.text}</td>

            <td>${(item.positive*100).toFixed(1)}%</td>

            <td>${(item.neutral*100).toFixed(1)}%</td>

            <td>${(item.negative*100).toFixed(1)}%</td>

            <td>

                <span class="badge bg-${color}">
                    ${item.sentiment}
                </span>

            </td>

        </tr>

        `;

    });

};



function setBar(id, value){

    const bar = document.getElementById(id);

    bar.style.width = (value*100) + "%";

    bar.innerHTML = (value*100).toFixed(1)+"%";

}