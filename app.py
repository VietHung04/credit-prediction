from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Lấy dữ liệu từ form
        age = int(request.form.get("age", 0))
        income = int(request.form.get("income", 0))
        late_30 = int(request.form.get("late_30", 0))
        late_90 = int(request.form.get("late_90", 0))
        debt_ratio = float(request.form.get("debt_ratio", 0))
        dependents = int(request.form.get("dependents", 0))

        # Logic đơn giản đánh giá rủi ro
        risk = "low"
        if (
            age < 21
            or income < 5000000
            or late_30 > 2
            or late_90 > 0
            or debt_ratio > 0.6
            or dependents > 3
        ):
            risk = "high"

        if risk == "high":
            result = "Rủi ro cao: Có nguy cơ vỡ nợ"
        else:
            result = "Rủi ro thấp: Ít nguy cơ vỡ nợ"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
