from flask import Flask, redirect, render_template, request, url_for
import jobs
import rq

app = Flask(__name__)
jobs.rq.init_app(app)


# For sake of simplicty, we keep track of the jobs we've launched
# in memory. This will only work as long there is only one python
# process (web server context) and it must not get restarted.
# In advanced use cases you want to keep track of jobs by their ids
# and utilize sessions and redis.
joblist = []


@app.route('/')
def index():
   return "It works"
