from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
import datetime

# Initialize Rich console
console = Console()

# ───────────────────────────────
# 1. Stylized Banner Header
# ───────────────────────────────
def print_header():
    header = """
                                                                                                                      
     #####    ##                       /                                     ##### ##                                 
  ######  /  #### /                  #/                                   /#####  /##                                 
 /#   /  /   ####/                   ##                                 //    /  / ###                                
/    /  /    # #                     ##                                /     /  /   ###                               
    /  /     #                       ##                                     /  /     ###                              
   ## ##     #      /###     /###    ##  /##      /##  ###  /###           ## ##      ##    /###     /###      /##    
   ## ##     #     / ###  / / ###  / ## / ###    / ###  ###/ #### /        ## ##      ##   / ###  / / #### /  / ###   
   ## ########    /   ###/ /   ###/  ##/   /    /   ###  ##   ###/         ## ##      ##  /   ###/ ##  ###/  /   ###  
   ## ##     #   ##    ## ##         ##   /    ##    ### ##                ## ##      ## ##    ## ####      ##    ### 
   ## ##     ##  ##    ## ##         ##  /     ########  ##                ## ##      ## ##    ##   ###     ########  
   #  ##     ##  ##    ## ##         ## ##     #######   ##                #  ##      ## ##    ##     ###   #######   
      /       ## ##    ## ##         ######    ##        ##                   /       /  ##    ##       ### ##        
  /##/        ## ##    /# ###     /  ##  ###   ####    / ##              /###/       /   ##    ##  /###  ## ####    / 
 /  #####      ## ####/ ## ######/   ##   ### / ######/  ###            /   ########/     ######  / #### /   ######/  
/     ##           ###   ## #####     ##   ##/   #####    ###          /       ####        ####      ###/     #####   
#                                                                      #                                              
 ##                                                                     ##                                            
                                                                                                                      
                                                                                                                      HACKER DAILY DOSE NEWS — by Aditya Bhosale 
"""
    console.print(Text(header, style="bold red"))


# ───────────────────────────────
# 2. Dummy News Data (for demo)
# ───────────────────────────────
def fetch_news_sources():
    return {
        "Global Cybersecurity (The Hacker News)": [
            {"title": "Critical RCE flaw found in OpenSSH", "link": "https://thehackernews.com/2024/07/openssh-rce-flaw.html"},
            {"title": "Massive data leak from AI training firm", "link": "https://thehackernews.com/2024/07/ai-training-data-leak.html"}
        ],
        "Trending Threats (Cyware)": [
            {"title": "New phishing scam targets banks", "link": "https://cyware.com/news/phishing-scam-banks"},
        ],
        "Government Alerts (CISA)": [
            {"title": "CISA issues urgent warning on VPN vulnerabilities", "link": "https://www.cisa.gov/news-events/news/vpn-vulnerabilities"},
            {"title": "Joint advisory from CISA and NSA", "link": "https://www.cisa.gov/news-events/news/nsa-joint-advisory"}
        ],
        "PIB Cybersecurity": [],
        "MHA India (Cyber)": [],
        "NCIIPC India": [],
        "Data Security Council of India (DSCI)": [],
        "NASSCOM Cybersecurity": [],
        "Economic Times – Cybersecurity": [],
        "The Hindu – Tech": [],
        "Times of India – Cyber": [],
        "Hindustan Times – Cyber": [],
        "DarkReading (Asia)": [],
        "BleepingComputer – India": []
    }

# ───────────────────────────────
# 3. Render News in Tables
# ───────────────────────────────
def render_news(sources):
    for source, articles in sources.items():
        table = Table(title=f"[bold magenta]{source}", header_style="bold white")
        table.add_column("No.", style="cyan", width=4)
        table.add_column("Title", style="green", overflow="fold")
        table.add_column("Link", style="blue", overflow="fold")

        if articles:
            for i, item in enumerate(articles, start=1):
                table.add_row(str(i), item["title"], item["link"])
        else:
            table.add_row("❌", "No News Available", "-")

        console.print(table)

# ───────────────────────────────
# 4. Footer Timestamp
# ───────────────────────────────
def print_footer():
    timestamp = datetime.datetime.now().strftime("%A, %d %B %Y | %I:%M %p")
    console.print(Panel(f"[bold yellow]Last Updated:[/] {timestamp}", expand=False, style="bold green"))

# ───────────────────────────────
# 5. Main Function
# ───────────────────────────────
def main():
    print_header()
    news_data = fetch_news_sources()
    render_news(news_data)
    print_footer()

# ───────────────────────────────
# 6. Entry Point
# ───────────────────────────────
if __name__ == "__main__":
    main()
