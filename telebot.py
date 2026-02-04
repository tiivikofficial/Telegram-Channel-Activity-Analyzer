import io
import logging
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from telethon import TelegramClient, events

# Developer: @tiivik
# Set backend to Agg to avoid GUI errors on servers
matplotlib.use('Agg')

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
API_ID = 123456          # REPLACE WITH YOUR API ID
API_HASH = 'your_hash'    # REPLACE WITH YOUR API HASH
SESSION_NAME = 'analyser_session'
# ---------------------------------------------------------

# Initialize the client (Userbot)
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    """Handles the /start command."""
    await event.respond(
        "**Channel Activity Analyzer (Userbot Mode)** 📊\n\n"
        "Send command in this format:\n"
        "`@username YYYY-MM-DD YYYY-MM-DD`\n\n"
        "Example:\n"
        "`@telegram 2025-01-01 2025-02-01`\n\n"
        "Developer: @tiivik"
    )

@client.on(events.NewMessage(pattern=r'(@\w+)\s+(\d{4}-\d{2}-\d{2})\s+(\d{4}-\d{2}-\d{2})'))
async def analyze_handler(event):
    """Handles the analysis request fetching history as a user."""
    msg = await event.reply("🔄 **Fetching data...** This might take a moment depending on the range.")
    
    try:
        # Parse arguments
        channel_username = event.pattern_match.group(1)
        start_date_str = event.pattern_match.group(2)
        end_date_str = event.pattern_match.group(3)

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        # Adjust end_date to end of day
        end_date = end_date.replace(hour=23, minute=59, second=59)

        dates = []
        
        # Developer: @tiivik
        # Fetching history using user account credentials
        async for message in client.iter_messages(channel_username, offset_date=end_date, reverse=False):
            if message.date.replace(tzinfo=None) < start_date:
                break
            if message.date:
                dates.append(message.date.date())

        if not dates:
            await msg.edit(f"❌ No activity found for {channel_username} in this period.")
            return

        # Prepare Data
        df = pd.DataFrame(dates, columns=['Date'])
        activity_counts = df['Date'].value_counts().sort_index()

        # -----------------------------------------------------
        # PLOTTING CHART
        # -----------------------------------------------------
        plt.style.use('dark_background')
        plt.figure(figsize=(12, 6))
        
        # Seaborn styling
        sns.set_context("notebook", font_scale=1.0)
        
        # Draw Line Chart
        ax = sns.lineplot(
            x=activity_counts.index, 
            y=activity_counts.values, 
            marker='o', 
            color='#00ff9d', 
            linewidth=2.5
        )
        
        # Fill area
        plt.fill_between(activity_counts.index, activity_counts.values, color='#00ff9d', alpha=0.1)
        
        # Labels and Title
        plt.title(f'Activity Chart: {channel_username}', fontsize=16, color='white', pad=20)
        plt.xlabel('Date', fontsize=12, color='gray')
        plt.ylabel('Messages', fontsize=12, color='gray')
        plt.grid(color='#333333', linestyle='--', linewidth=0.5)
        plt.xticks(rotation=45)
        sns.despine()

        # Save to buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=300, facecolor='#121212')
        buf.seek(0)
        plt.close()

        # Send File
        await client.send_file(
            event.chat_id,
            buf,
            caption=f"📊 **Analysis Result**\n\n"
                    f"TARGET: {channel_username}\n"
                    f"FROM: {start_date_str}\n"
                    f"TO: {end_date_str}\n"
                    f"TOTAL: {len(dates)} posts\n\n"
                    f"By Developer: @tiivik",
            reply_to=event.id
        )
        await msg.delete()

    except Exception as e:
        await msg.edit(f"⚠️ **Error:** {str(e)}")

if __name__ == '__main__':
    print("Userbot Started... Login required on first run.")
    print("Developer: @tiivik")
    client.start()
    client.run_until_disconnected()
