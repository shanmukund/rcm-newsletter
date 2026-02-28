# Custom Domain Setup: www.vaqyaweekly.com

## Overview
This guide will help you connect your custom domain **www.vaqyaweekly.com** to your GitHub Pages newsletter site.

---

## Step 1: Purchase the Domain

### Recommended Registrars (Cheapest to Most Expensive)

1. **Porkbun** (~$8/year)
   - Visit: https://porkbun.com
   - Search: `vaqyaweekly.com`
   - Great value, simple interface

2. **Namecheap** (~$9/year)
   - Visit: https://www.namecheap.com
   - Search: `vaqyaweekly.com`
   - Excellent support, free WHOIS privacy

3. **Cloudflare** (~$9/year at-cost)
   - Visit: https://www.cloudflare.com/products/registrar/
   - At-cost pricing (no markup)
   - Includes free CDN and SSL

4. **Google Domains** (~$12/year)
   - Visit: https://domains.google.com
   - Easy integration with Google services
   - Clean interface

### What to Buy
- **Domain:** `vaqyaweekly.com` (this automatically includes www.vaqyaweekly.com)
- **WHOIS Privacy:** YES (usually free, protects your personal info)
- **Auto-renew:** YES (so you don't lose your domain)

**Cost:** Approximately $8-15 per year

---

## Step 2: Configure DNS Settings

After purchasing, log into your domain registrar and add these DNS records:

### DNS Records to Add

| Type | Name/Host | Value/Points To | TTL |
|------|-----------|-----------------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |
| CNAME | www | shanmukund.github.io | 3600 |

### What These Mean:
- **A records** - Point the root domain (vaqyaweekly.com) to GitHub's servers
- **CNAME record** - Points www.vaqyaweekly.com to your GitHub Pages site
- **TTL** - Time to live (3600 = 1 hour)

### Platform-Specific Instructions

#### Namecheap
1. Go to Dashboard → Domain List → Manage
2. Advanced DNS tab
3. Click "Add New Record"
4. Add each record from the table above
5. Save changes

#### Porkbun
1. Go to Domain Management
2. DNS tab
3. Click "Add" for each record
4. Save when done

#### Cloudflare
1. Go to DNS → Records
2. Click "Add record"
3. Add each record from table
4. Orange cloud = ON for CNAME (proxy enabled)
5. Save

#### Google Domains
1. Go to DNS settings
2. Custom records section
3. Add each record from table
4. Save

---

## Step 3: Configure GitHub Pages

### Push CNAME File
The CNAME file has already been created. Let's push it:

```bash
cd "c:/Users/shanm/OneDrive/Desktop/RCM newsletter blog"
git add CNAME
git commit -m "Add custom domain: www.vaqyaweekly.com"
git push
```

### Update GitHub Settings
1. Go to: https://github.com/shanmukund/rcm-newsletter/settings/pages
2. Under "Custom domain", enter: `www.vaqyaweekly.com`
3. Click "Save"
4. Wait 24-48 hours for DNS to propagate
5. Once DNS is verified, check "Enforce HTTPS"

---

## Step 4: Verify Setup

### Check DNS Propagation (15 min - 48 hours)
```bash
# Check if DNS is configured
nslookup www.vaqyaweekly.com

# Should show:
# Address: 185.199.108.153 (or one of the other GitHub IPs)
```

### Online Tools
- https://dnschecker.org - Check DNS propagation globally
- Enter: `www.vaqyaweekly.com`
- Look for GitHub's IP addresses

### Test Your Site
After DNS propagates (usually 1-24 hours):
- http://www.vaqyaweekly.com → Should redirect to HTTPS and show your newsletter
- https://www.vaqyaweekly.com → Should show your newsletter
- http://vaqyaweekly.com → Should redirect to www version
- https://vaqyaweekly.com → Should redirect to www version

---

## Step 5: Update Links (Optional)

### Update Newsletter References
After domain is working, you may want to update:

1. **Social media profiles** - Update your website link
2. **Email signatures** - Use your new domain
3. **Business cards** - Add www.vaqyaweekly.com
4. **Newsletter footer** - Update "Visit our website" links

### Update Index.html (Optional)
You can add your domain to the index page:
```html
<p>Visit us at <a href="https://www.vaqyaweekly.com">www.vaqyaweekly.com</a></p>
```

---

## Timeline

| Step | Duration |
|------|----------|
| Domain purchase | 5 minutes |
| DNS configuration | 10 minutes |
| GitHub setup | 5 minutes |
| DNS propagation | 1-48 hours (usually 1-6 hours) |
| HTTPS certificate | Auto after DNS verified |

**Total active time:** ~20 minutes
**Total wait time:** 1-48 hours for DNS

---

## Troubleshooting

### "Domain not yet verified" on GitHub
- Wait longer - DNS can take up to 48 hours
- Check DNS records are correct
- Try removing and re-adding custom domain in GitHub

### "Certificate error" or "Not Secure"
- Don't check "Enforce HTTPS" until DNS is fully verified
- Wait 24 hours after DNS verification
- GitHub auto-generates SSL certificate

### Site shows 404
- CNAME file must be in repository root
- Custom domain must be set in GitHub Pages settings
- Wait for DNS propagation

### www doesn't work but root does (or vice versa)
- Check CNAME record points to `shanmukund.github.io`
- GitHub Pages CNAME file should have `www.vaqyaweekly.com`
- Set up redirect at domain registrar if needed

---

## Cost Summary

**One-time:**
- Domain purchase: $8-15 (first year)

**Annual:**
- Domain renewal: $8-15/year
- GitHub Pages hosting: FREE ✅
- SSL certificate: FREE ✅
- Bandwidth: FREE ✅

**Total annual cost: ~$8-15** (just the domain renewal)

---

## Domain Alternatives (If vaqyaweekly.com is Taken)

If `vaqyaweekly.com` is not available, try:
- `rcmpulse.com`
- `revcycle-rx.com`
- `revcyclerx.io`
- `rcmweekly.com`
- `pulseweekly.com`
- `revcyclereport.com`

---

## Quick Start Checklist

- [ ] Purchase domain at Namecheap/Porkbun/Cloudflare
- [ ] Add 4 A records pointing to GitHub IPs
- [ ] Add CNAME record: www → shanmukund.github.io
- [ ] Push CNAME file to GitHub (already created)
- [ ] Add custom domain in GitHub Pages settings
- [ ] Wait 1-24 hours for DNS propagation
- [ ] Enable "Enforce HTTPS" in GitHub after verification
- [ ] Test www.vaqyaweekly.com in browser
- [ ] Update social media and marketing materials

---

**Ready to get started? Let me know once you've purchased the domain and I'll help you with the DNS configuration!**
