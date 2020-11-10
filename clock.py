from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from Whatsapp import envia_whats

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(envia_whats, 'interval', seconds=10)

sched.start()