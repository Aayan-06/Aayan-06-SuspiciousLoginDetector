def read_logs(filename):
    with open(filename, 'r') as file:
        logs = file.readlines()
    return [log.strip().split(" | ") for log in logs]

def detect_failed_attempts(logs):
    failed_count = {}
    for log in logs:
        user = log[1]
        status = log[3]
        if status == "FAILED":
            failed_count[user] = failed_count.get(user, 0) + 1

    print("\n[!] Users with multiple failed attempts:")
    for user, count in failed_count.items():
        if count >= 3:
            print(f" - {user} had {count} failed login attempts")

def detect_odd_hour_login(logs):
    print("\n[!] Logins at odd hours (12AM to 5AM):")
    for log in logs:
        time = log[0].split(" ")[1]
        hour = int(time.split(":")[0])
        if hour >= 0 and hour < 5:
            print(f" - {log[1]} logged in at {time}")

def main():
    logs = read_logs("login_logs.txt")
    detect_failed_attempts(logs)
    detect_odd_hour_login(logs)

if __name__ == "__main__":
    main()
