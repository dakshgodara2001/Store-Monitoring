from datetime import datetime
import pytz

def convertTimeStringIntoSeconds(time):
    """
    Convert a time string in the format HH:MM:SS into seconds.

    Parameters:
        time (str): The time string to convert.

    Returns:
        int: The time converted into seconds.
    """
    time = time.split(':')
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

def getOffSet(timezone_str):
    """
    Get the offset in seconds for a given timezone.

    Parameters:
        timezone_str (str): The timezone string (e.g., 'America/New_York').

    Returns:
        int: The offset in seconds.
    """
    return pytz.timezone(timezone_str).utcoffset(datetime.now()).total_seconds()

def getDateObject(timestring):
    """
    Split the timestamp string into date and time components.

    Parameters:
        timestring (str): The timestamp string.

    Returns:
        tuple: A tuple containing the date and time components.
    """
    timestring = timestring.split(' ')
    date = timestring[0].split('-')
    time = timestring[1].split(':')
    time[2] = int(float(time[2]))  # Handle fractional seconds
    return date, time

def getTimeOnly(time):
    """
    Convert the time component into seconds.

    Parameters:
        time (list): A list containing the time components.

    Returns:
        int: The time converted into seconds.
    """
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

def getTimeStamp(timestring):
    """
    Convert the timestamp string into a Unix timestamp.

    Parameters:
        timestring (str): The timestamp string.

    Returns:
        float: The Unix timestamp.
    """
    date, time = getDateObject(timestring)
    stamp = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2])).timestamp()
    return stamp

def getWeekDay(timestring):
    """
    Get the weekday (0-6) for a given timestamp.

    Parameters:
        timestring (str): The timestamp string.

    Returns:
        int: The weekday (0-6, where Monday is 0).
    """
    date, _ = getDateObject(timestring)
    return datetime(int(date[0]), int(date[1]), int(date[2])).weekday()
