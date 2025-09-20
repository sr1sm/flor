import os
from flask import Flask, render_template_string

app = Flask(__name__)

# HTML del ramo de flores amarillas con pétalos centrados
html_page = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Un ramo para ti 🌼</title>
  <style>
    body {
      margin: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background: linear-gradient(to bottom, #fff7d6, #fce68c);
      font-family: Arial, sans-serif;
      overflow: hidden;
      flex-direction: column;
    }

    .ramo {
      display: flex;
      gap: 40px;
      flex-wrap: wrap;
      justify-content: center;
      max-width: 500px;
      animation: aparecer 2s ease-in-out forwards;
      transform: scale(0.5);
      opacity: 0;
    }

    .flor {
      position: relative;
      width: 120px;
      height: 180px;
      animation: abrir 1.5s ease-in-out forwards;
    }

    .petalo {
      position: absolute;
      width: 60px;
      height: 90px;
      background: yellow;
      border-radius: 50% 50% 50% 50%;
      top: -5px;
      left: 30px;
      transform-origin: center 70px;
    }

    .petalo:nth-child(1) { transform: rotate(0deg); }
    .petalo:nth-child(2) { transform: rotate(72deg); }
    .petalo:nth-child(3) { transform: rotate(144deg); }
    .petalo:nth-child(4) { transform: rotate(216deg); }
    .petalo:nth-child(5) { transform: rotate(288deg); }

    .centro {
      width: 50px;
      height: 50px;
      background: orange;
      border-radius: 50%;
      position: absolute;
      top: 40px;
      left: 35px;
      z-index: 2;
    }

    .tallo {
      width: 14px;
      height: 120px;
      background: green;
      position: absolute;
      top: 90px;
      left: 53px;
      border-radius: 5px;
    }

    @keyframes aparecer {
      to { transform: scale(1); opacity: 1; }
    }

    @keyframes abrir {
      from { transform: scale(0); }
      to { transform: scale(1); }
    }

    h1 {
      margin-top: 30px;
      font-size: 26px;
      color: #6b4f00;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="ramo">
    <div class="flor">
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="centro"></div>
      <div class="tallo"></div>
    </div>
    <div class="flor">
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="centro"></div>
      <div class="tallo"></div>
    </div>
    <div class="flor">
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="petalo"></div>
      <div class="centro"></div>
      <div class="tallo"></div>
    </div>
  </div>

  <h1>💛 Un ramo de flores amarillas para ti 💛</h1>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_page)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # si no existe, usa 5000
    app.run(host="0.0.0.0", port=port)


