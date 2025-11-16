from colorama import Fore, Style, init
from copy_trading_bot import CopyTradingBot
from config.env import Config

# Initialize colorama
init()

def main():
    """Main entry point for the copy trading bot"""
    print(f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗
║                    POLYMARKET COPY TRADING BOT                   ║
║                          Enhanced Python Version                 ║
╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """)
    
    # Validate environment
    try:
        # Test configuration
        print(f"{Fore.BLUE}🔍 Validating configuration...{Style.RESET_ALL}")
        
        if not Config.USER_ADDRESS:
            raise ValueError("❌ USER_ADDRESS not configured")
        if not Config.PROXY_WALLET:
            raise ValueError("❌ PROXY_WALLET not configured")
        if not Config.PRIVATE_KEY:
            raise ValueError("❌ PRIVATE_KEY not configured")
            
        print(f"{Fore.GREEN}✅ Configuration validated{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}{e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Please check your .env file configuration{Style.RESET_ALL}")
        return
    
    # Start the bot
    try:
        bot = CopyTradingBot()
        bot.start()
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to start bot: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
