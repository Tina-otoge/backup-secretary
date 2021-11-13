# backup-secretary
Backup your files with ease

## Example config

```json
{
	"paths": [
		"~/.local/opt/MechaDon2/app.db"
	],
	"frequency": "weekly",
	"handler": {
		"delay": 5,
		"url": "https://discord.com/api/webhooks/XXX/XXX",
		"data": {
			"avatar_url": "https://cdn.discordapp.com/attachments/439208223673810944/908892929823760384/backup_secretary.png",
			"username": "Backup Secretary"
		}
	}
}
```
