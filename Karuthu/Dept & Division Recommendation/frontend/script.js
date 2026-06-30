const API_URL = "http://localhost:2000/questions/predict";

async function predictDepartment() {

    const feedback =
        document.getElementById("feedback").value.trim();

    const messageBox =
        document.getElementById("feedbackMessage");

    messageBox.style.display = "none";
    messageBox.innerHTML = "";

    if (!feedback) {
        messageBox.innerHTML =
            "Please enter feedback";
        messageBox.style.display = "block";
        return;
    }

    try {

        const response = await fetch(
            "http://localhost:2000/questions/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: feedback
                })
            }
        );

        const data = await response.json();

        if (!data.success) {

            document.getElementById("department").value = "";
            document.getElementById("division").value = "";

            messageBox.innerHTML =
                `${data.message} (Similarity: ${data.score ?? "N/A"})`;

            messageBox.style.display = "block";

            return;
        }

        document.getElementById("department").value =
            data.department;

        document.getElementById("division").value =
            data.division;

    } catch (error) {

        messageBox.innerHTML =
            "Unable to connect to prediction service";

        messageBox.style.display = "block";

        console.error(error);
    }
}

async function saveEscalation() {

    const feedback =
        document.getElementById("feedback").value.trim();

    const department =
        document.getElementById("department").value.trim();

    const division =
        document.getElementById("division").value.trim();

    if (!feedback || !department || !division) {

        alert(
            "Feedback, Department and Division are required"
        );

        return;
    }

    try {

        const response = await fetch(
            "http://localhost:2000/questions/add",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: feedback,
                    department: department,
                    division: division
                })
            }
        );

        const data = await response.json();
        console.log(data);
        alert(data.message);

    } catch (error) {

        console.error(error);

        alert("Save Failed");
    }
}