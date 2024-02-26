from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    disk_metric = psutil.disk_usage('/').percent
    Message = None
    if cpu_metric > 80 or mem_metric > 80 or disk_metric > 80:
        Message = "High CPU, Memory or Disk Usage Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, disk_metric=disk_metric, message=Message)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')
