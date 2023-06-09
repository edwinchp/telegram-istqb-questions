## Telegram Poll Sender

This project aims to send Telegram polls as a way to challenge your knowledge about whatever certification you are studying or subject you're preparing for.
I believe that taking notes is important when you want to retain information, but wouldn't be great that these notes come back to you at some point?


## 🚀 Getting Started:
Clone the repository
`git clone https://github.com/edwinchp/telegram-poll-sender`

Enter project folder using `cd telegram-poll-sender/`

Create a bot in Telegram using BotFather.

Create a setup.json file and add your token and chat_id there. (See setup-example.json)

Run the script using `python3 main.py`.


## 📝 Usage:
Create a new Telegram channel or group and add the bot you created there.

Create a Jenkins job that runs automatically.

Schedule example (10:00AM and 7:00PM):

```bash
0 10,19 * * *
```

Pipeline script:
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