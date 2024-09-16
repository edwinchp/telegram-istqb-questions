## Telegram Poll Sender

This project aims to send Telegram polls as a way to challenge your knowledge about whatever certification you are studying or subject you're preparing for.
I believe that taking notes is important when you want to retain information, but wouldn't be great that these notes come back to you at some point?


## 🚀 Getting Started:
Create a bot in Telegram using BotFather.

Create a Telegram Channel or Group.

Clone the repository:
```bash
git clone https://github.com/edwinchp/telegram-poll-sender
```

Enter project folder using:
```bash
cd telegram-poll-sender/
```

Create a .env file and add bot token and channel/group chat id:
```bash
cp .env-example .env
```

Install requirements:
```bash
python -m pip install -r requirements.txt
```

Run script:
```bash
python main.py
```


## 📝 Jenkins usage:

Create a Jenkins job that runs automatically.

Schedule example (10:00AM and 7:00PM):

```bash
0 10,19 * * *
```

Pipeline script example:
```bash
pipeline {
    agent any

    stages {
        stage('Clone and pull') {
            steps {
                git branch: 'istqb-ctfl', url: 'https://github.com/edwinchp/telegram-poll-sender.git'
                sh 'python3.8 main.py'
                sh 'python3.8 main.py'
                sh 'python3.8 main.py'
            }
        }
    }
}
```



👏 Thank you! I hope you find it useful.