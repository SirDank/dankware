from datetime import datetime

def get_duration(then: datetime, now: datetime = None, interval: str = "default") -> int | str:

    """
    Returns a duration as specified by the 'interval' variable
    
    __________________________________________________________
    
    valid intervals:
    - year -> int
    - month -> int
    - week -> int
    - day -> int
    - hour -> int
    - minute -> int
    - second -> int
    - dynamic -> str
    - dynamic-mini -> str
    - default -> str
    - default-mini -> str
    """

    if not now: now = datetime.now()
    interval = interval.lower()
    duration = now - then

    if "year" in interval: return int(duration.days / 365)
    if "month" in interval: return int(duration.days / 30)
    if "week" in interval: return int(duration.days / 7)
    if "day" in interval: return duration.days
    if "hour" in interval: return int(duration.total_seconds() / 3600)
    if "minute" in interval: return int(duration.total_seconds() / 60)
    if "second" in interval: return int(duration.total_seconds())
    if "dynamic" in interval:

        mini = bool(interval == "dynamic-mini")
        seconds = duration.total_seconds()

        if seconds < 60:
            if mini: return f"{int(seconds)}s"
            return f"{int(seconds)} second{'s' if seconds > 1 else ''}"

        if seconds < 3600:
            minutes = int(seconds / 60)
            if mini: return f"{minutes}m"
            return f"{minutes} minute{'s' if minutes > 1 else ''}"

        if seconds < 86400:
            hours = int(seconds / 3600)
            if mini: return f"{hours}h"
            return f"{hours} hour{'s' if hours > 1 else ''}"

        if seconds < 604800:
            days = int(seconds / 86400)
            if mini: return f"{days}d"
            return f"{days} day{'s' if days > 1 else ''}"

        if seconds < 2592000:
            weeks = int(seconds / 604800)
            if mini: return f"{weeks}w"
            return f"{weeks} week{'s' if weeks > 1 else ''}"

        if seconds < 31536000:
            months = int(seconds / 2592000)
            if mini: return f"{months}mo"
            return f"{months} month{'s' if months > 1 else ''}"

        years = int(seconds / 31536000)
        if mini: return f"{years}y"
        return f"{years} year{'s' if years > 1 else ''}"

    if "default" in interval:

        seconds = duration.total_seconds()
        years = int(seconds / 31536000)
        months = int((seconds % 31536000) / 2592000)
        weeks = int((seconds % 2592000) / 604800)
        days = int((seconds % 604800) / 86400)
        hours = int((seconds % 86400) / 3600)
        minutes = int((seconds % 3600) / 60)
        seconds = int(seconds % 60)

        parts = []
        if interval == "default":
            if years: parts.append(f"{years} year{'s' if years > 1 else ''}")
            if months: parts.append(f"{months} month{'s' if months > 1 else ''}")
            if weeks: parts.append(f"{weeks} week{'s' if weeks > 1 else ''}")
            if days: parts.append(f"{days} day{'s' if days > 1 else ''}")
            if hours: parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
            if minutes: parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
            if seconds: parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")

        elif interval == "default-mini":
            if years: parts.append(f"{years}y")
            if months: parts.append(f"{months}mo")
            if weeks: parts.append(f"{weeks}w")
            if days: parts.append(f"{days}d")
            if hours: parts.append(f"{hours}h")
            if minutes: parts.append(f"{minutes}m")
            if seconds: parts.append(f"{seconds}s")

        return ", ".join(parts)

    raise ValueError(f"Invalid Interval: {interval} | Valid Intervals: year, month, week, day, hour, minute, second, dynamic, dynamic-mini, default, default-mini")
