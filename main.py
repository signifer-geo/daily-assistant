import schedule
import time
import logging
from tasks.email_tasks import get_unread_email_summaries
from tasks.calendar_tasks import get_todays_events
from tasks.blog_tasks import placeholder_blog_task  # Import blog task
from config import LOG_FILE, LOG_LEVEL

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_daily_tasks():
    logging.info("Running daily tasks...")
    try:
        email_summaries = get_unread_email_summaries()
        print("\nUnread Email Summaries:")
        for summary in email_summaries:
            print(summary)
        logging.info(f"Fetched {len(email_summaries)} email summaries.")

        calendar_events = get_todays_events()
        print("\nToday's Calendar Events:")
        for event in calendar_events:
            print(event)
        logging.info(f"Fetched {len(calendar_events)} calendar events.")

        blog_result = placeholder_blog_task()  # Call the blog task
        print(f"\nBlog Task Result: {blog_result}")
        logging.info(f"Blog task result: {blog_result}")

    except Exception as e:
        logging.exception("An error occurred during task execution:")
        print(f"An error occurred.  See {LOG_FILE} for details.")

# Example scheduling (using 'schedule' library - OPTIONAL)
# schedule.every().day.at("07:00").do(run_daily_tasks)

if __name__ == "__main__":
    run_daily_tasks()  # Run once immediately

    # while True:  # Uncomment for scheduled execution
    #     schedule.run_pending()
    #     time.sleep(60)