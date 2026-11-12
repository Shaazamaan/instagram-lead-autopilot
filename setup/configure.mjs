// One-time wiring after the repo is created and the Instagram account id is known.
// Usage: node setup/configure.mjs <github-owner>/<repo> <instagram-user-id> <worker-subdomain>
//   worker-subdomain: the <name>.workers.dev account subdomain shown in the Cloudflare dashboard (Workers & Pages).
// Fills worker/wrangler.toml, writes the ops key to ~/.autopilot_ops_key (never commit or print it), and prints the
// GitHub repository variables to set (WORKER_URL, IG_USER_ID).
import fs from "fs"; import os from "os"; import path from "path"; import crypto from "crypto"; import { fileURLToPath } from "url";
const [repo, igId, sub] = process.argv.slice(2);
if (!repo || !igId || !sub) { console.error("usage: node setup/configure.mjs owner/repo IG_USER_ID workers-subdomain"); process.exit(1); }
const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..");
const [owner, name] = repo.split("/");
const keyFile = path.join(os.homedir(), ".autopilot_ops_key");
const opsKey = fs.existsSync(keyFile) ? fs.readFileSync(keyFile, "utf8").trim() : crypto.randomBytes(24).toString("hex");
fs.writeFileSync(keyFile, opsKey, { mode: 0o600 });
const t = path.join(root, "worker/wrangler.toml");
const w = fs.readFileSync(t, "utf8")
  .replace("__IG_USER_ID__", igId)
  .replace("__VERIFY_TOKEN__", "verify-" + crypto.randomBytes(9).toString("hex"))
  .replace("__OPS_KEY_SHA256__", crypto.createHash("sha256").update(opsKey).digest("hex"))
  .replace("__LIB_BASE__", `https://${owner.toLowerCase()}.github.io/${name}`);
fs.writeFileSync(t, w);
const workerUrl = `https://ig-autopilot.${sub}.workers.dev`;
console.log(`wrangler.toml filled. Ops key saved to ${keyFile}.
Set these GitHub repository variables (gh variable set NAME --body VALUE):
  WORKER_URL=${workerUrl}
  IG_USER_ID=${igId}
Webhook callback URL for Meta: ${workerUrl}/webhook   verify token: see VERIFY_TOKEN in worker/wrangler.toml`);
