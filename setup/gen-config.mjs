// Copies business.json into the worker bundle (worker/src/config.js). Run after every edit of business.json.
import fs from "fs"; import path from "path"; import { fileURLToPath } from "url";
const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..");
const cfg = JSON.parse(fs.readFileSync(path.join(root, "business.json"), "utf8"));
fs.writeFileSync(path.join(root, "worker/src/config.js"), "// generated from business.json by setup/gen-config.mjs; do not edit\nexport default " + JSON.stringify(cfg, null, 1) + ";\n");
console.log("worker/src/config.js written");
