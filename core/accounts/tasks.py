from celery import shared_task

import time
@shared_task
def Send_email():
    time.sleep(10)
    print("Done Sending")