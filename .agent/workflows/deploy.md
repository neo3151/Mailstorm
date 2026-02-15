---
description: How to deploy a new episode or site update to production
---

## Deploy Mailstorm to Production

Vercel is connected to GitHub — every push to `main` auto-deploys.

### Steps

// turbo-all

1. Build the site to make sure it compiles cleanly:
```bash
cd /home/neo/.gemini/antigravity/scratch/Mailstorm/web && npm run build
```

2. Stage all changes:
```bash
cd /home/neo/.gemini/antigravity/scratch/Mailstorm && git add -A
```

3. Check what's being committed:
```bash
cd /home/neo/.gemini/antigravity/scratch/Mailstorm && git status
```

4. Commit with a descriptive message (replace the message as appropriate):
```bash
cd /home/neo/.gemini/antigravity/scratch/Mailstorm && git commit -m "Add Episode X panels and update manifest"
```

5. Push to GitHub (auto-triggers Vercel deploy):
```bash
cd /home/neo/.gemini/antigravity/scratch/Mailstorm && git push origin main
```

6. Verify the live site is updated:
- Visit https://web-omega-five-77.vercel.app
- Check that new episode panels load correctly
